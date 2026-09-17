const TAG = /^[a-z0-9][a-z0-9-]{0,31}$/;
const BOT = /bot|crawl|spider|preview|fetch|curl|wget|facebookexternalhit|slurp|headless/i;
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    const p = url.pathname;
    if (p === '/stats') return stats(url, env);
    if (p === '/signups.csv') return csv(url, env);
    if (p === '/signup') return req.method === 'POST' ? signup(req, env) : new Response('Method not allowed', { status: 405 });
    if (p === '/') { log(req, env, ctx, url.searchParams.get('src') || 'direct'); return env.ASSETS.fetch(req); }
    const tag = p.startsWith('/go/') ? p.slice(4) : p.slice(1);
    if (TAG.test(tag) && !p.startsWith('/go/')) {
      const asset = await env.ASSETS.fetch(req);
      if (asset.status !== 404) return asset;
    }
    if (TAG.test(tag)) { log(req, env, ctx, tag); return Response.redirect(url.origin + '/', 302); }
    return env.ASSETS.fetch(req);
  }
};

function log(req, env, ctx, tag) {
  const ua = req.headers.get('user-agent') || '';
  if (BOT.test(ua)) return;
  const cf = req.cf || {};
  ctx.waitUntil(env.DB.prepare('INSERT INTO hits (ts, tag, country, region, city, ref, ua) VALUES (?, ?, ?, ?, ?, ?, ?)')
    .bind(new Date().toISOString(), tag, cf.country || '', cf.region || '', cf.city || '', (req.headers.get('referer') || '').slice(0, 200), ua.slice(0, 200)).run().catch(() => {}));
}

async function signup(req, env) {
  const html = (req.headers.get('accept') || '').includes('text/html');
  const reply = (ok, msg) => html
    ? new Response(`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${ok ? 'Seat saved' : 'Not saved'}</title><body style="font:16px/1.6 -apple-system,Segoe UI,sans-serif;background:#070707;color:#e9e4d6;padding:48px 24px;text-align:center"><p>${msg}</p><p><a href="/events" style="color:#d4af5a">Back to events</a></p>`, { status: ok ? 200 : 400, headers: { 'content-type': 'text/html; charset=utf-8' } })
    : Response.json({ ok, error: ok ? undefined : msg }, { status: ok ? 200 : 400 });
  if (+(req.headers.get('content-length') || 0) > 4096) return reply(false, 'Request too large.');
  let f;
  try { f = Object.fromEntries((await req.formData()).entries()); } catch { return reply(false, 'That did not go through. Try again.'); }
  if (f.website) return reply(true, 'Seat saved. Watch your inbox for the invite.');
  const email = String(f.email || '').trim().toLowerCase(), event = String(f.event || '');
  if (!TAG.test(event) || email.length > 254 || !EMAIL.test(email)) return reply(false, 'That email address does not look right.');
  await env.DB.prepare('INSERT OR IGNORE INTO signups (ts, event, email, country) VALUES (?, ?, ?, ?)')
    .bind(new Date().toISOString(), event, email, (req.cf || {}).country || '').run();
  return reply(true, 'Seat saved. Watch your inbox for the invite.');
}

async function csv(url, env) {
  if (!env.STATS_KEY || url.searchParams.get('key') !== env.STATS_KEY) return new Response('Not found', { status: 404 });
  const { results } = await env.DB.prepare('SELECT ts, event, email, country FROM signups ORDER BY id').all();
  const q = v => '"' + String(v ?? '').replace(/"/g, '""') + '"';
  const body = 'signed_up_utc,event,email,country\n' + results.map(r => [r.ts, r.event, r.email, r.country].map(q).join(',')).join('\n') + '\n';
  return new Response(body, { headers: { 'content-type': 'text/csv; charset=utf-8', 'content-disposition': 'attachment; filename="akashic-signups.csv"', 'cache-control': 'no-store', 'referrer-policy': 'no-referrer' } });
}

async function stats(url, env) {
  if (!env.STATS_KEY || url.searchParams.get('key') !== env.STATS_KEY) return new Response('Not found', { status: 404 });
  const day = new Date(Date.now() - 864e5).toISOString(), week = new Date(Date.now() - 7 * 864e5).toISOString();
  const [tags, countries, last, events, signups] = await Promise.all([
    env.DB.prepare('SELECT tag, COUNT(*) total, SUM(ts > ?) week, SUM(ts > ?) day FROM hits GROUP BY tag ORDER BY total DESC').bind(week, day).all(),
    env.DB.prepare('SELECT country, COUNT(*) n FROM hits GROUP BY country ORDER BY n DESC LIMIT 15').all(),
    env.DB.prepare('SELECT ts, tag, country, region, city, ref FROM hits ORDER BY id DESC LIMIT 100').all(),
    env.DB.prepare('SELECT event, COUNT(*) total, SUM(ts > ?) week, SUM(ts > ?) day FROM signups GROUP BY event ORDER BY total DESC').bind(week, day).all(),
    env.DB.prepare('SELECT ts, event, email, country FROM signups ORDER BY id DESC LIMIT 200').all(),
  ]);
  const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const rows = (list, cols) => list.map(r => '<tr>' + cols.map(c => '<td>' + esc(r[c]) + '</td>').join('') + '</tr>').join('');
  const html = `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Akashic link stats</title>
<style>body{font:14px/1.5 -apple-system,Segoe UI,sans-serif;background:#0a0a0a;color:#e8e2d6;padding:24px;max-width:1000px;margin:auto}h1,h2{font-weight:500;color:#d4af5a}table{border-collapse:collapse;width:100%;margin:8px 0 28px}td,th{padding:6px 10px;border-bottom:1px solid #222;text-align:left;font-variant-numeric:tabular-nums}th{color:#9a927f;font-weight:500;font-size:12px;text-transform:uppercase;letter-spacing:.1em}</style>
<h1>Akashic link stats</h1><p>Any link of the form ${esc(url.host)}/&lt;tag&gt; counts a hit for that tag and lands on the home page. Plain visits count as direct.</p>
<h2>Event signups</h2><table><tr><th>Event</th><th>All time</th><th>Last 7 days</th><th>Last 24 h</th></tr>${rows(events.results, ['event', 'total', 'week', 'day'])}</table>
<p><a href="/signups.csv?key=${esc(url.searchParams.get('key'))}" style="color:#d4af5a">Download every signup as CSV</a> (for sending the invites)</p>
<h2>Last 200 signups</h2><table><tr><th>Time (UTC)</th><th>Event</th><th>Email</th><th>Country</th></tr>${rows(signups.results, ['ts', 'event', 'email', 'country'])}</table>
<h2>By link</h2><table><tr><th>Tag</th><th>All time</th><th>Last 7 days</th><th>Last 24 h</th></tr>${rows(tags.results, ['tag', 'total', 'week', 'day'])}</table>
<h2>By country</h2><table><tr><th>Country</th><th>Hits</th></tr>${rows(countries.results, ['country', 'n'])}</table>
<h2>Last 100 hits</h2><table><tr><th>Time (UTC)</th><th>Tag</th><th>Country</th><th>Region</th><th>City</th><th>Referrer</th></tr>${rows(last.results, ['ts', 'tag', 'country', 'region', 'city', 'ref'])}</table>`;
  return new Response(html, { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store', 'referrer-policy': 'no-referrer' } });
}
