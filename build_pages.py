import os
WHOP = 'https://whop.com/akashicwealth/wealth-builder-membership-73/'
DISCORD = 'https://discord.gg/kAXU5p4gTA'
PEEK = '</div><div class="ring-wrap" id="ring-wrap"><div class="ring-scene"><button class="ring-nav prev" type="button" aria-label="Previous post">&larr;</button><div class="ring" id="ring"><figure class="ring-card"><img src="assets/peek/m01.webp" width="514" height="521" alt="Member post in #post-profits: 1 week in the group. I knew @Kevinthechineseguy and @billmsft were the guys to follow which is why I was quick to pay fo" /></figure><figure class="ring-card"><img src="assets/peek/m02.webp" width="438" height="455" alt="Member post in #post-profits: @billmsft the goat!! Still holding 1 runner" /></figure><figure class="ring-card"><img src="assets/peek/m03.webp" width="388" height="455" alt="Member post in #post-profits: Bill back at it once again" /></figure><figure class="ring-card"><img src="assets/peek/m04.webp" width="648" height="353" alt="Member post in #post-profits: @billmsft you’re the man, bringing my port slowly back to life, thank you!" /></figure><figure class="ring-card"><img src="assets/peek/m05.webp" width="543" height="477" alt="Member post in #post-profits: Woke up a little late today and sold later than signaled but I guess it worked in my favor thanks @billmsft !" /></figure><figure class="ring-card"><img src="assets/peek/m06.webp" width="551" height="433" alt="Member post in #post-profits: & late ty to @Queso_Fresco" /></figure><figure class="ring-card"><img src="assets/peek/m07.webp" width="648" height="427" alt="Member post in #post-profits: Thanks @billmsft" /></figure><figure class="ring-card"><img src="assets/peek/m08.webp" width="386" height="455" alt="Member post in #post-profits: thank you @billmsft for the extra" /></figure><figure class="ring-card"><img src="assets/peek/m09.webp" width="391" height="455" alt="Member post in #post-profits: Lets fking go @billmsft" /></figure><figure class="ring-card"><img src="assets/peek/m10.webp" width="648" height="401" alt="Member post in #post-profits: Still on spy swing call from @billmsft" /></figure><figure class="ring-card"><img src="assets/peek/m11.webp" width="503" height="477" alt="Member post in #post-profits: I know he still has this position open but I’m happy with 20% lfg bill! @billmsft" /></figure><figure class="ring-card"><img src="assets/peek/m12.webp" width="503" height="477" alt="Member post in #post-profits: @Queso_Fresco The juicy double dip. Thank you sir, moving up my stop loss" /></figure></div><button class="ring-nav next" type="button" aria-label="Next post">&rarr;</button></div><div class="ring-cap" id="ring-cap">#post-profits</div></div><div class="shell"><div class="desk"><div class="chan recap"><div class="recap-cols"><img src="assets/peek/recap-a.webp" width="679" height="865" loading="lazy" class="tint" alt="A daily recap, first half: sixteen wins including TSLA 365P +514% (Bill), MU 980C +500% (Moose), MU 1110/1100C +100% (Kevin) and PLTR 180P +63% (Queso)" /><img src="assets/peek/recap-b.webp" width="679" height="667" loading="lazy" class="tint" alt="A daily recap, second half: three losses, SPY 775C -60%, NVDA 240C -100% and TSLA 352.5P -12.5%, and the summary: 19 trades, 15W 3L 1BE, +2,017% total, +106.16% average per trade" /></div></div><div class="desk-col"><div class="chan"><div class="chan-body"><img src="assets/peek/bill-entry.webp" width="506" height="55" loading="lazy" class="tint" alt="Bill: [BUY] ORCL 7/31 160 Call at 2.58, swing trade" /><img src="assets/peek/bill-trims.webp" width="427" height="226" loading="lazy" class="tint" alt="Bill the next morning: LETS GO ORCL with six fire reactions, then [TRIM] ORCL for 52% and [TRIM] ORCL for 56%, holding a third" /></div></div><div class="chan"><div class="chan-body"><img src="assets/peek/kevin-rivn.webp" width="498" height="98" loading="lazy" class="tint" alt="Kevin: RIVN BACK FROM THE DEAD TRIM 40% LFGGG, with six fire reactions" /><img src="assets/peek/kevin-runners.webp" width="377" height="164" loading="lazy" class="tint" alt="Kevin: leaving rivn runners, 110%, leaving hood runners as well for next week" /><img src="assets/peek/kevin-uber.webp" width="541" height="120" loading="lazy" alt="Kevin: also getting UBER 10/16 85 CALL, filled at 1.45, with heart and thumbs-up reactions" /></div></div></div></div>'
FONTS = '<link rel="stylesheet" href="assets/fonts.css" />'

def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta name="theme-color" content="#070707" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="Akashic Wealth" />
  <link rel="icon" type="image/png" href="assets/logo-mark.png" />
  {FONTS}
  <link rel="stylesheet" href="akashic.css" />
  <script>if (!window.matchMedia || !matchMedia('(prefers-reduced-motion: reduce)').matches) {{ document.documentElement.classList.add('js-reveal'); }}</script>
</head>
<body id="top">
  <div class="grain" aria-hidden="true"></div>
  <header class="nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-brand">
        <img src="assets/logo-mark.png" alt="" aria-hidden="true" />
        <span class="wordmark">Akashic <span class="brand-accent">Wealth</span></span>
      </a>
      <nav class="nav-links">
        <a href="index.html">Home</a>
        <a href="events.html">Events</a>
        <a href="index.html#faq">FAQ</a>
        <a href="about.html">About</a>
        <a href="support.html">Contact</a>
        <a class="nav-cta" href="{WHOP}" rel="noopener">Join</a>
      </nav>
    </div>
  </header>
'''

FOOT = f'''
  <footer class="foot">
    <div class="shell">
      <div class="foot-inner">
        <div>
          <div class="foot-brand">Akashic <span class="brand-accent">Wealth</span></div>
          <div class="foot-tag">Build Lasting Wealth</div>
        </div>
        <nav class="foot-links">
          <a href="events.html">Events</a>
          <a href="terms.html">Terms</a>
          <a href="privacy.html">Privacy</a>
          <a href="risk.html">Risk Disclosure</a>
          <a href="support.html">Contact</a>
          <a href="https://www.instagram.com/akashicwealth/" rel="noopener">Instagram</a>
        </nav>
      </div>
      <div class="foot-legal">
        &copy; Akashic Wealth · Signals and commentary are educational, not investment advice. Trading involves substantial risk including loss of capital.
      </div>
    </div>
  </footer>
  <script src="akashic.js" defer></script>
</body>
</html>
'''

def legal_page(title, eyebrow, blocks):
    body = ''.join(f'<h2 class="sec-title" style="font-size:28px;margin-top:40px">{h}</h2>' + ''.join(f'<p class="sec-sub" style="max-width:70ch;margin-bottom:14px">{p}</p>' for p in ps) for h, ps in blocks)
    return f'''
  <section class="hairline" style="padding-top:140px">
    <div class="shell" style="max-width:900px">
      <div class="sec-eyebrow">{eyebrow}</div>
      <h1 class="sec-title" style="font-size:clamp(36px,5vw,56px)">{title}</h1>
      {body}
    </div>
  </section>'''

index = head('Akashic Wealth', 'Akashic Wealth is a trading signal group for options, stocks and futures. Four traders, live calls, a daily log and a weekly recap. Seven-day free trial on Whop.') + f'''
  <section class="hero" id="hero">
    <canvas id="hero-canvas" aria-hidden="true"></canvas>
    <div class="shell">
      <div class="hero-grid">
        <div class="hero-copy">
          <h1 class="hero-title">Build Lasting Wealth</h1>
          <p class="hero-sub">A community for ambition and consistency.</p>
          <div class="hero-cta-row">
            <a class="btn btn-gold" href="{WHOP}" rel="noopener">Start 7-day free trial</a>
            <a class="btn btn-ghost" href="{DISCORD}" rel="noopener">Join the Discord</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="features hairline" id="signals">
    <div class="shell">
      <div class="sec-head center">
        <div class="sec-eyebrow">What you get</div>
        <h2 class="sec-title">Signals with the work shown.</h2>
        <p class="sec-sub">Four traders, one Discord, every call logged.</p>
      </div>
      <div class="feat-grid">
        <div class="feat wide">
          <h3 class="feat-title">Live signals from experienced analysts</h3>
          <p class="feat-body">Analysts with proven market experience post entries, trims and exits as they happen.</p>
        </div>
        <div class="feat">
          <h3 class="feat-title">Options, stocks and futures</h3>
          <p class="feat-body">0DTE and lottos on SPX, SPY and the big names, spreads, LEAPs, stock picks, and a futures room with BRUH&#39;s live streams.</p>
        </div>
        <div class="feat">
          <h3 class="feat-title">Transparent by default</h3>
          <p class="feat-body">Every trade is logged with its outcome and recapped weekly, losses included. Nothing is hidden.</p>
        </div>
        <div class="feat">
          <h3 class="feat-title">The $5K Challenge</h3>
          <p class="feat-body">A $5,000 account traded in the open toward $10,000. No deadline, no forced trades.</p>
        </div>
        <div class="feat">
          <h3 class="feat-title">Education and tools</h3>
          <p class="feat-body">Spreads and volatility walkthroughs, stock analysis and the VIX Holistic Adaptive indicator.</p>
        </div>
        <div class="feat wide">
          <h3 class="feat-title">A free tier on Discord</h3>
          <p class="feat-body">Occasional alerts, the news feed and the community. <a href="{DISCORD}" rel="noopener">Join the free Discord</a>.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="record hairline" id="record">
    <div class="shell">
      <div class="sec-head center">
        <div class="sec-eyebrow">A peek inside</div>
        <h2 class="sec-title">What the room looks like.</h2>
        <p class="sec-sub">Members&#39; own posts, two signal channels, and a full daily recap.</p>
      </div>
      {PEEK}
      <p class="sec-sub rec-note">These are real posts by members in the group&#39;s post-profits channel. Members share their wins there, so losing trades do not appear, and we do not track how members do overall. The recap counts each posted alert from its posted entry to its highest trim as a percentage move per contract. It is not the return on any account, it is not net of fees, and it is not what any member made. Your fills, size and timing will differ from the poster&#39;s, and a trade that showed a gain in the room can lose money for you. Many people who trade options and futures lose money, including everything they put into a trade. Nothing here predicts or promises what you will make.</p>
    </div>
  </section>

  <section class="faq hairline" id="faq">
    <div class="shell">
      <div class="sec-head center">
        <div class="sec-eyebrow">Common questions</div>
        <h2 class="sec-title">Frequently asked.</h2>
      </div>
      <div class="faq-list">
        <details class="faq-item">
          <summary>Is this financial advice?</summary>
          <div class="faq-body">No. Signals and commentary are shared for educational purposes. Every decision to trade is yours, and trading involves substantial risk including loss of capital.</div>
        </details>
        <details class="faq-item">
          <summary>How do I join?</summary>
          <div class="faq-body">Through Whop. Membership is $49.99 a month after a 7-day free trial and renews automatically each month until you cancel from your Whop account. Membership admits you to the VIP channels of the Akashic Wealth Discord.</div>
        </details>
        <details class="faq-item">
          <summary>Do you offer annual or lifetime plans?</summary>
          <div class="faq-body">Occasionally. When an annual or lifetime offer opens, it is announced in the group first.</div>
        </details>
        <details class="faq-item">
          <summary>What markets do you cover?</summary>
          <div class="faq-body">US options first: 0DTE and lotto plays on SPX, SPY and large caps, debit spreads, and LEAPs. Alongside that, long-term stock picks, small-cap swings, and a futures room.</div>
        </details>
        <details class="faq-item">
          <summary>How are wins and losses counted?</summary>
          <div class="faq-body">A position opened and closed in the same day counts as one trade, recorded at its highest realized trim. If the remaining contracts later stop out below breakeven, that loss is recorded too. A re-entry on the same strike after a close is a separate trade. The full rules are pinned in the group.</div>
        </details>
        <details class="faq-item">
          <summary>I paid on Whop. How do I get into the VIP channels?</summary>
          <div class="faq-body">In your Whop settings open Connected Accounts, click the plus next to Discord, log in and authorize. The VIP channels appear in the Akashic Wealth Discord automatically.</div>
        </details>
        <details class="faq-item">
          <summary>What does a signal look like?</summary>
          <div class="faq-body">Buy posts carry the ticker, strike, expiration and entry price. Trim or Sell means profits are being taken. Close means the trade is being exited, winner or not. The full guide is in the getting-started channel.</div>
        </details>
        <details class="faq-item">
          <summary>Is there a free way to follow?</summary>
          <div class="faq-body">Yes. The free Discord has a free-trades channel with occasional alerts, the market news feed and the community chat. Full signals are in the VIP channels.</div>
        </details>
      </div>
    </div>
  </section>

  <section class="offer hairline" id="membership">
    <div class="shell">
      <div class="offer-plate">
        <div class="offer-frame"></div>
        <img class="offer-mark" src="assets/logo-mark.png" alt="" width="52" height="52" />
        <div class="sec-eyebrow">Membership</div>
        <h2 class="offer-title">Build Lasting Wealth</h2>
        <div class="offer-price">$49.99 a month<span>Seven days free first</span></div>
        <p class="offer-copy">Everything the group posts, from the day you join. Renews automatically at $49.99 a month after the 7-day trial until you cancel in Whop.</p>
        <div class="hero-cta-row" style="justify-content: center;">
          <a class="btn btn-gold" href="{WHOP}" rel="noopener">Start 7-day free trial</a>
          <a class="btn btn-ghost" href="{DISCORD}" rel="noopener">Free Discord</a>
        </div>
        <div class="offer-facts"><span>Billed through Whop</span><span>Renews monthly until you cancel</span><span>Annual and lifetime open occasionally, announced in the group first</span></div>
      </div>
    </div>
  </section>
''' + FOOT.replace('<script src="akashic.js" defer></script>', '<script src="hero.js" defer></script>\n  <script src="akashic.js" defer></script>')

about = head('About · Akashic Wealth', 'Who is behind Akashic Wealth, why the group exists, and how it works.') + legal_page('About Akashic Wealth', 'About', [
    ('Why the group exists', ['Too often, traders are forced to choose between overpriced services and learning entirely on their own. Akashic Wealth was built to make quality trading education and support accessible: a valuable, affordable community with education, market insights, accountability and support, and no unnecessary barriers. The aim is a room where traders support one another, sharpen their skills and work toward becoming consistently profitable.']),
    ('Who we are', ['Akashic Wealth, formerly The Wealth Project, is a Discord community run by a small team of analysts with years of market experience. The focus is making money short term, in options and futures, and rolling those gains into long-term positions.', 'Bill started investing during the 2020 crash, researching companies and building long-term positions with his brother, then moved to options in 2022. Options are now most of his trading, after more than six years in the markets. Kevin trades futures and 0DTE options and built the VIX Holistic Adaptive indicator the group uses.']),
    ('What we promised when we opened', ['Full transparency: every trade and every bit of analysis laid out for everyone to see. Reachable founders who answer questions. The indicator given away free. Education for new traders, the why behind every play, not just the play. Trades sized for every account, whether you trade with $500 or $50,000. And a focus on profitability, accountability and transparency across options, futures, long-term portfolio building, stock picking and analysis.']),
    ('How a signal reads', ['Buy: the ticker, strike, expiration and entry price. Enter as close to that price as you can, set your own limit rather than chasing, and if you cannot get within 5% of the entry, skip it and wait for the next one. Trim or Sell: profits are being taken, and followers generally start trimming too. Close: the trade is being exited, winner or not, and you can exit with the group or hold to your own plan. There will always be another setup.']),
    ('The $5K Challenge', ['A $5,000 account grown toward $10,000 through disciplined trading, proper risk management and high-conviction setups. There is no set timeline: quality trades take time to develop, and no trade is forced to meet a deadline.']),
    ('Mentorship', ['A limited-availability mentorship program, a bootcamp and one-to-one sessions cover high-probability setups, risk management, options and market analysis for members who want to build their own process. Open a ticket in the Discord to ask.']),
    ('How the record is kept', ['An intraday position counts as one trade at its highest realized trim; a later stop-out below breakeven is recorded as a loss. Re-entries on the same strike are separate trades. The rules have been the same since the start and are pinned in the group.']),
    ('Follow along', [f'Instagram: <a href="https://www.instagram.com/akashicwealth/" rel="noopener">@akashicwealth</a> and <a href="https://www.instagram.com/akashicwealth.kevin/" rel="noopener">@akashicwealth.kevin</a>. Free Discord: <a href="{DISCORD}" rel="noopener">join here</a>.']),
]) + FOOT
support = head('Contact · Akashic Wealth', 'How to reach Akashic Wealth and manage your membership.') + legal_page('Contact', 'Support', [
    ('Membership and billing', [f'Membership, the 7-day trial, billing and cancellations are handled in your Whop account. <a href="{WHOP}" rel="noopener">Open Akashic Wealth on Whop</a>.']),
    ('Talk to us', [f'The team lives in the Discord. <a href="{DISCORD}" rel="noopener">Join the free Discord</a> and post in the community chat, or message a moderator directly.', 'For anything about a VIP subscription or a problem with the Discord itself, open a ticket in the support channel. Tickets are for membership and server issues, not personal portfolio analysis.']),
]) + FOOT
terms_blocks = [
    ('Who these terms cover', [
        'These Terms of Membership are an agreement between you and Akashic Wealth. Akashic Wealth, also we or us, means the team that runs this website, the Akashic Wealth Discord community and the Akashic Wealth store on Whop. You, or a member, means anyone who uses the website, joins the Discord or buys a membership.',
        'You accept these terms when you use the website, join the Discord, start a free trial or buy a membership. If you do not agree with them, do not join.',
        'Your Whop account is governed by Whop\'s own terms, and your Discord account by Discord\'s. Those agreements sit alongside this one and cover payment processing and the Discord platform itself.',
    ]),
    ('What the service is', [
        'Akashic Wealth is a subscription community for people learning to trade. Membership gives you access to the VIP channels of the Discord, where the team posts trade alerts on options, stocks and futures, market commentary, live streams, education, a daily trade log and a weekly recap.',
        'Every post goes to every member at the same time. Nothing is written for your account, your goals or your finances. Treat the service as a live classroom where traders show their own work, not as a plan for you to copy.',
    ]),
    ('What the service is not', [
        'Akashic Wealth does not give investment, financial, tax or legal advice. We are not a registered investment adviser, broker-dealer or commodity trading advisor, we do not manage money and we do not owe you a fiduciary duty.',
        'A Buy, Trim or Close post describes what the person posting is doing with their own position at that moment. It is not an instruction to you and not a recommendation that the trade suits you.',
        'Mentorship, the bootcamp and one-to-one sessions teach process, risk management and market analysis. They do not include telling you what to buy or sell in your own account, and staff will not review your portfolio or size your trades for you. If you need advice about your own situation, talk to a licensed professional.',
        'No one at Akashic Wealth promises profits, and nobody can. You can lose money following any post in the group, including all of the money you put into a trade. The Risk Disclosure page explains this in more detail and is part of these terms.',
    ]),
    ('Who can join', [
        'You must be at least 18 years old, live in the United States and be able to enter a binding contract. If you are under 18, do not start a trial or buy a membership. If we learn that a member is under 18 we will end the membership.',
        'You are responsible for meeting the age and account rules of Whop, Discord and any broker you use, and for following the laws that apply to you. Trading on margin, in options or in futures requires approvals from your broker that are separate from anything we provide.',
    ]),
    ('Your account and how to behave in the group', [
        'One membership admits one person. Keep your Discord and Whop logins to yourself, and tell us if you think someone else is using them. You are responsible for anything posted from your account.',
        'In the Discord, do not harass, threaten or discriminate against anyone. Do not spam, advertise your own paid service, post referral links or recruit members for anything without a moderator\'s permission. Do not impersonate staff, pass off a post as a signal when it is not, or coordinate with others to move a price.',
        'Do not post anything illegal, anything that infringes another person\'s rights, or anything that breaks Discord\'s terms and community guidelines. Moderators can remove content and members at their discretion.',
    ]),
    ('Content, intellectual property and no redistribution', [
        'The signals, trade log, recaps, live streams, lessons, the VIX Holistic Adaptive indicator and everything else the team publishes belong to Akashic Wealth or to the people who created them. Your membership gives you a personal, non-transferable license to read and use that content for your own trading and learning.',
        'You may not copy, screenshot, forward, resell, scrape, mirror or re-post signals or member content outside the group, feed them into another server, channel, chat, bot or automated trading tool, or use them to run your own signal service. Doing so ends your membership without refund and may lead to a legal claim.',
        'Posts you write in the group stay yours. By posting them you allow us to show them inside the community. If you post in a channel marked as public-facing, such as the post-profits channel, you also allow us to show that post on our website and social media, with your username and picture hidden if you ask. Tell a moderator any time you want a post taken down from the website.',
    ]),
    ('Membership, billing and automatic renewal', [
        f'Membership is sold and billed by Whop. The monthly plan costs $49.99 a month and starts with a 7-day free trial. <a href="{WHOP}" rel="noopener">The Akashic Wealth page on Whop</a> shows the current price and any annual or lifetime offer that is open.',
        'Your membership renews automatically. When the free trial ends, Whop charges the payment method on your Whop account for the first month, and it charges you again on each monthly renewal date after that until you cancel. An annual membership renews each year in the same way unless the offer says otherwise. A lifetime membership is a one-time payment and lasts for as long as Akashic Wealth operates the service.',
        'One free trial per person. If you cancel during the trial you are not charged. If you do not cancel before the trial ends, the paid membership begins.',
        'If we change the price of a recurring plan we will tell you in the Discord and through Whop before the change applies to a renewal, and you can cancel before then. Taxes, if any apply, are shown at checkout.',
    ]),
    ('How to cancel and how refunds work', [
        'Cancel in your Whop account: open your memberships, choose Akashic Wealth and select cancel. Cancellation stops the next charge. You keep VIP access until the end of the period you already paid for, and Whop removes the VIP role from your Discord account when that period ends.',
        'Leaving the Discord server does not cancel your billing. Only cancelling in Whop does. If you cannot get into Whop, open a ticket in the Discord before your renewal date and we will help you find the setting.',
        'Refunds follow the refund policy shown on the Akashic Wealth page on Whop at the time you buy. Ask us through a Discord ticket or through Whop before disputing a charge with your card issuer. A chargeback filed without asking us first ends your membership.',
    ]),
    ('Our own trading and outside links', [
        'The team trades the same things it posts, usually before or at the time it posts them, and may add to, trim or exit a position without posting an update. The Risk Disclosure says more about this.',
        'Links or codes for brokers, card issuers or prop trading firms that appear in the Discord may pay the person who posted them a referral bonus or commission if you sign up. Those companies are not part of Akashic Wealth, and their products are governed by their own terms.',
    ]),
    ('No warranties', [
        'The service is provided as it is and as it is available. We do not promise that any post will be accurate, complete, timely or profitable, that the Discord or Whop will be online when you need them, or that any alert will reach you before the price moves.',
        'To the fullest extent the law allows, we disclaim all warranties, express or implied, including any implied warranty of merchantability, fitness for a particular purpose and non-infringement. Some states do not allow the disclaimer of implied warranties, so some of this section may not apply to you.',
    ]),
    ('Limits on our liability', [
        'You decide what to trade, how much to risk and when to enter and exit. Akashic Wealth and the people who run it are not liable for trading losses, lost profits, lost data or any indirect, incidental, special, consequential or punitive damages arising from the service or from anything posted in it, even if we were told such losses were possible.',
        'To the fullest extent the law allows, our total liability to you for all claims relating to the service is limited to the membership fees you paid to us through Whop in the twelve months before the event giving rise to the claim, or one hundred dollars, whichever is greater.',
        'Nothing in these terms limits liability for fraud, for gross negligence or willful misconduct, or for anything that cannot be limited under the law of the state where you live. Some states do not allow the exclusion or limitation of certain damages, so some of the limits above may not apply to you.',
    ]),
    ('Your responsibility to us', [
        'If a third party brings a claim against Akashic Wealth or its team because you broke these terms, redistributed content, broke the law or misused the service, you agree to cover the resulting losses, costs and reasonable legal fees. We will tell you about any such claim and let you take part in defending it.',
    ]),
    ('Ending a membership', [
        'You can cancel at any time in Whop as described above.',
        'We can suspend or end your membership if you break these terms, the Discord rules or Whop\'s terms, if you dispute a charge without contacting us first, or if you act in a way that harms the community. A membership ended for one of these reasons is not refunded for the remainder of the period.',
        'We can also change or shut down parts of the service, or the whole of it. If we close the service while you have paid for a period you have not used, we will arrange a proportionate refund through Whop for that period. Lifetime memberships end when the service ends.',
    ]),
    ('Changes to these terms', [
        'We may update these terms. When we do, we will post the new version on this page and announce the change in the Discord. If the change is significant we will announce it before it takes effect and before your next renewal, so you can cancel if you disagree. Staying a member after that notice means you accept the new terms.',
    ]),
    ('Disputes and governing law', [
        'If you have a problem with the service, open a ticket in the Discord or contact us through Whop first. We will try to resolve it with you informally within thirty days before either of us takes it further.',
        'These terms are governed by the federal law of the United States and the law of the state where Akashic Wealth is based, without regard to rules on conflict of laws, except where the consumer protection law of the state where you live gives you rights that cannot be taken away by agreement.',
        'If any part of these terms is found unenforceable, the rest still applies. If we do not enforce a term on one occasion, we can still enforce it later. You may not transfer your membership to anyone else. These terms, the Risk Disclosure and the Privacy Policy are the whole agreement between you and Akashic Wealth about the service.',
    ]),
    ('Contact', [
        f'Questions about these terms: open a ticket in the support channel of <a href="{DISCORD}" rel="noopener">the Discord</a>, or message us through the Akashic Wealth page on Whop.',
    ]),
]

privacy_blocks = [
    ('The short version', [
        'Akashic Wealth runs this website, a Discord community and a store on Whop. This policy explains what each of them collects about you and what we do with it.',
        'The website collects an email address only if you save a seat for a class. It sets no cookies, runs no advertising trackers and does not store your IP address. We do not sell personal information, and we do not share it for advertising.',
    ]),
    ('What this website collects', [
        'When you save a seat for a class, we store the email address you type, the name of the class, the time you signed up and the country your connection came from, as reported by Cloudflare. The form also contains a hidden field that only automated bots fill in; if it is filled, the entry is discarded.',
        'When you visit a page or follow one of our tagged links, we record the link tag, the time, the country, region and city your connection appears to come from, the page that referred you, and your browser\'s user-agent string. We do not store your IP address and we do not set a cookie or any other identifier, so these records are not tied to you and cannot be used to recognize you on a later visit.',
    ]),
    ('What we use it for', [
        'We use your email address to send you the invitation, the time and the link for the class you saved a seat for, along with any change to those details and a follow-up for that class. If we ever want to email you about anything else, we will ask you first.',
        'We use the visit records to count how many people each link and post brings to the site and where they come from. That tells us where to spend our time. We do not use them for advertising and do not combine them with the signup list.',
    ]),
    ('Who else handles your data', [
        'Cloudflare hosts the website and the database where signups and visit records live. As the host, Cloudflare processes your IP address to deliver the pages and to work out the country and city recorded above, under Cloudflare\'s privacy policy.',
        'Google Sheets holds a copy of the signup list so the team can read it and send invitations. The spreadsheet lives in a Google account controlled by the team.',
        'An email delivery service may send the class emails on our behalf. If we use one, it processes your address, records whether the email was delivered and opened, and provides the unsubscribe link in every email.',
        'We do not sell or rent your personal information and we do not share it with anyone else, unless the law requires it or we need to protect the rights or safety of our members.',
    ]),
    ('What Whop collects', [
        'When you start a trial or buy a membership, Whop collects your name, email address, payment details and billing information, and, when you connect your Discord account, your Discord username and ID. Whop\'s privacy policy governs all of that.',
        'We do not see your card number. From Whop we receive your name or username, your email address, your Discord ID, your membership status and your order history, and we use them to admit you to the VIP channels, to support you, and to send you notices about your membership.',
    ]),
    ('What Discord collects', [
        'Discord collects account and usage information under its own privacy policy. Inside our server we can see your username, your profile picture, when you joined, your roles and anything you post. We use that to run the community and to enforce the membership terms, and we keep moderation notes about rule breaches.',
        'Posts made in channels marked as public-facing, such as the post-profits channel, may be shown on this website or on our social media under the Terms of Membership. Ask a moderator to have a post removed from the website at any time.',
    ]),
    ('How long we keep it', [
        'We keep class signup addresses until the class and its follow-up emails are done, then delete them from the database, the spreadsheet and the email service, unless you have asked to hear from us about future events.',
        'Visit records contain no identifier, and we keep them for as long as we need them to measure the site.',
        'Membership records held by Whop stay for as long as you are a member and for as long as Whop or the law requires after that. Discord messages stay in the server under Discord\'s rules unless you or a moderator deletes them.',
    ]),
    ('Your choices and how to be removed', [
        f'To have your email address removed from the class list, message a moderator or open a ticket in <a href="{DISCORD}" rel="noopener">the Discord</a>. We remove it from the database, the spreadsheet and the email service. Every class email also carries an unsubscribe link.',
        'To change or delete what Whop holds, use your Whop account settings or Whop\'s support. To change or delete what Discord holds, use your Discord settings; leaving the server removes your access, and you can delete your own messages.',
        'Because the site sets no cookies and does not track you across other websites, a Do Not Track signal from your browser changes nothing: there is no tracking to turn off.',
    ]),
    ('Children', [
        'The service is for adults. We do not knowingly collect personal information from anyone under 13, and membership is limited to people 18 and older. If you believe a child has given us an email address or joined the paid community, tell a moderator and we will delete the information and end the membership.',
    ]),
    ('Where your data is processed', [
        'The team and the services above operate in the United States. If you use the site from outside the United States, your information is processed there.',
    ]),
    ('Security', [
        'Access to the signup list is limited to the people who run Akashic Wealth, and exports are protected by a secret key. No method of storage or transmission is completely secure, so we cannot promise absolute security, and we ask you not to send us anything more sensitive than an email address.',
    ]),
    ('Changes to this policy', [
        'When we change this policy we will post the new version here and announce the change in the Discord. If a change affects how we use information we already hold, we will announce it before it takes effect.',
    ]),
    ('Contact', [
        f'Questions about your data: message a moderator or open a ticket in <a href="{DISCORD}" rel="noopener">the Discord</a>.',
    ]),
]

risk_blocks = [
    ('Read this before you trade anything posted in the group', [
        'Trading stocks, options and futures carries a substantial risk of loss and is not suitable for everyone. You can lose the entire amount you put into a trade, and in futures and other leveraged products you can lose more than you deposited. Only trade with money you can afford to lose entirely.',
        'Akashic Wealth is an educational community, not an investment adviser. Nothing in the Discord, on this website, in a live stream or in a mentorship session is a recommendation for you. Every trade you place is your own decision, and its result is yours.',
    ]),
    ('Options', [
        'Most of what the group posts is options, including 0DTE contracts that expire the same day and low-priced lotto contracts. These can lose their whole value in minutes and often expire worthless. Time decay works against you every hour you hold, and wide bid-ask spreads mean you can lose money even when the underlying moves your way.',
        'Debit spreads cap your loss at what you paid but can still go to zero. LEAPs last longer but can also expire worthless. If you sell options, your loss can be far larger than the premium you collect, and you can be assigned at any time. Your broker sets the approvals, margin and rules that apply to you, and your broker can close a position without your consent.',
    ]),
    ('Futures', [
        'Futures are highly leveraged. A small move in the index is a large move in your account, margin calls can arrive quickly, and you can lose more than the money in your account. Futures trade almost around the clock, so a position can move sharply while you are not watching.',
        'Funded or evaluation accounts from prop trading firms have their own rules, fees and payout conditions, and the firm decides whether you are paid. Passing an evaluation is not a guarantee of income. Any referral code the team posts for a prop firm may earn the poster a commission.',
    ]),
    ('Stocks and small caps', [
        'Small-cap and swing trades can be thinly traded, halted, diluted or moved by a single headline. You may not be able to exit at the price you want, or at all, and a stock can gap through your stop.',
    ]),
    ('What a signal is, and what it is not', [
        'A Buy post records that the poster entered a trade at the stated ticker, strike, expiration and price. A Trim or Sell post records that the poster took some profit. A Close post records that the poster exited, whether at a gain or a loss. Each post describes one person\'s own position at one moment. It does not consider your account size, your risk tolerance, your tax situation or anything else about you.',
        'The group\'s guideline is to enter within 5% of the posted price or skip the trade. Even inside that band your entry, your size, your exit and your fees will differ from the poster\'s, so your result will differ too, sometimes by a great deal. A trade the poster closed for a gain can be a loss for you.',
    ]),
    ('Signals may not be timely', [
        'Alerts travel through Discord, and Discord, your phone and your broker can each add delay. Notifications can be missed or silenced. By the time you read a post the price may have moved, the setup may be gone or the trade may already be closed. We do not guarantee that any alert reaches you at all, and we are not liable for a trade you entered late or missed.',
    ]),
    ('The team trades what it posts', [
        'Bill, Kevin and the contributing analysts trade their own money in the positions they post, usually before or as they post them. They may add, trim or exit without posting, hold a position after posting Close, or hold a different position in the same name in another account. Their interests and yours can differ: members buying after a post can, for example, help the poster exit.',
        'Team members may earn referral bonuses or commissions from brokers, card issuers or prop firms whose links or codes they share. If a team member ever has a paid arrangement tied to a specific stock or contract they post about, the post will say so.',
    ]),
    ('Past performance, the trade log and the recaps', [
        'The daily log and weekly recap record the alerts the team posted, not the results of any real account and not the results of any member. A trade is counted from the posted entry to its highest realized trim, and an intraday position that later stops out below breakeven is recorded as a loss. Re-entries count as separate trades. The counting rules are pinned in the group.',
        'Percentages in the log are the move in the option\'s price per contract. They are not account returns, they are not net of commissions or fees, and they do not tell you how much money anyone made. A 500% gain on a $50 contract is $250. A run of large percentage wins can sit alongside a net loss in dollars once size and losses are counted.',
        'Past performance does not predict future results. Markets change, and a strategy that worked in one period can lose in the next.',
    ]),
    ('Member results shown on this website', [
        'Screenshots of member posts on the home page come from the post-profits channel, where members share trades that went well. Losses are not posted there. The screenshots are individual results, chosen by us, and are not typical of members as a group. We do not track how members do overall, and many people who trade options and futures lose money.',
        'Members who trade the group\'s alerts can and do lose money, including the entire amount they risk on a trade. Do not join expecting the results shown in any screenshot.',
    ]),
    ('Statement on hypothetical performance', [
        'The log is a record of posted alerts, not the audited results of one account that took every trade at every posted price. Treat it as hypothetical performance and read it with the following statement in mind:',
        'HYPOTHETICAL PERFORMANCE RESULTS HAVE MANY INHERENT LIMITATIONS, SOME OF WHICH ARE DESCRIBED BELOW. NO REPRESENTATION IS BEING MADE THAT ANY ACCOUNT WILL OR IS LIKELY TO ACHIEVE PROFITS OR LOSSES SIMILAR TO THOSE SHOWN. IN FACT, THERE ARE FREQUENTLY SHARP DIFFERENCES BETWEEN HYPOTHETICAL PERFORMANCE RESULTS AND THE ACTUAL RESULTS SUBSEQUENTLY ACHIEVED BY ANY PARTICULAR TRADING PROGRAM. ONE OF THE LIMITATIONS OF HYPOTHETICAL PERFORMANCE RESULTS IS THAT THEY ARE GENERALLY PREPARED WITH THE BENEFIT OF HINDSIGHT. IN ADDITION, HYPOTHETICAL TRADING DOES NOT INVOLVE FINANCIAL RISK, AND NO HYPOTHETICAL TRADING RECORD CAN COMPLETELY ACCOUNT FOR THE IMPACT OF FINANCIAL RISK IN ACTUAL TRADING. FOR EXAMPLE, THE ABILITY TO WITHSTAND LOSSES OR TO ADHERE TO A PARTICULAR TRADING PROGRAM IN SPITE OF TRADING LOSSES ARE MATERIAL POINTS WHICH CAN ALSO ADVERSELY AFFECT ACTUAL TRADING RESULTS. THERE ARE NUMEROUS OTHER FACTORS RELATED TO THE MARKETS IN GENERAL OR TO THE IMPLEMENTATION OF ANY SPECIFIC TRADING PROGRAM WHICH CANNOT BE FULLY ACCOUNTED FOR IN THE PREPARATION OF HYPOTHETICAL PERFORMANCE RESULTS AND ALL OF WHICH CAN ADVERSELY AFFECT ACTUAL TRADING RESULTS.',
    ]),
    ('The $5K Challenge', [
        'The $5K Challenge is one account, traded by the team, with its own size and risk. Its progress is that account\'s result and nothing else. It has no deadline, and it can lose money as well as make it.',
    ]),
    ('Taxes', [
        'Short-term trading has tax consequences, and options, futures and stocks are taxed differently. Nothing we post is tax advice. Talk to a tax professional about your own situation.',
    ]),
    ('Before you start', [
        'Decide your own position size and maximum loss before you enter any trade, and use a limit order rather than chasing a fill. If you are unsure whether trading options or futures is appropriate for you, talk to a licensed financial adviser before you start, not after a loss.',
    ]),
]

terms = head('Terms · Akashic Wealth', 'Terms of membership for the Akashic Wealth signal group.') + legal_page('Terms of Membership', 'Legal', terms_blocks) + FOOT
privacy = head('Privacy · Akashic Wealth', 'What Akashic Wealth collects and how it is used.') + legal_page('Privacy Policy', 'Legal', privacy_blocks) + FOOT
risk = head('Risk Disclosure · Akashic Wealth', 'Trading risk disclosure for the Akashic Wealth signal group.') + legal_page('Risk Disclosure', 'Legal', risk_blocks) + FOOT

EVENTS = [dict(tag='free-class', kind='Free class', title='How we find and research high&#8209;conviction trades', meta='Sunday, October 4 &middot; Online &middot; time announced soon',
    pitch='The process behind a trade, shown in full, rather than a callout to follow.',
    covers=['Finding 0DTE, swing and LEAPS setups across timeframes', 'Researching a company from the ground up', 'The catalysts that matter, and the hype and red herrings that do not',
            'Building a thesis and knowing what would invalidate it', 'Setups with a strong risk to reward'])]

def event_card(e):
    covers = ''.join(f'<li>{c}</li>' for c in e['covers'])
    return f'''
      <article class="event" id="{e['tag']}">
        <div class="offer-frame"></div>
        <div class="event-kind">{e['kind']}</div>
        <h2 class="event-title">{e['title']}</h2>
        <p class="event-meta">{e['meta']}</p>
        <p class="event-pitch">{e['pitch']}</p>
        <ul class="event-list">{covers}</ul>
        <form class="signup" action="/signup" method="post">
          <input type="hidden" name="event" value="{e['tag']}" />
          <div class="signup-row">
            <input class="support-input" name="email" type="email" required autocomplete="email" inputmode="email" maxlength="254" placeholder="Your email" aria-label="Your email" />
            <input class="signup-hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" />
            <button class="btn btn-gold" type="submit">Save my seat</button>
          </div>
          <p class="signup-status" role="status" aria-live="polite">By saving a seat you agree to receive emails about this class. Unsubscribe any time.</p>
        </form>
      </article>'''

events = head('Events · Akashic Wealth', 'Upcoming events from Akashic Wealth. Save a seat for the free class on how high-conviction trades are found and researched.') + f'''
  <section class="hairline" style="padding-top:140px">
    <div class="shell" style="max-width:900px">
      <h1 class="sec-title" style="font-size:clamp(36px,5vw,56px)">Events</h1>
      {''.join(event_card(e) for e in EVENTS)}
    </div>
  </section>''' + FOOT

for name, html in (('index.html', index), ('events.html', events), ('about.html', about), ('support.html', support), ('terms.html', terms), ('privacy.html', privacy), ('risk.html', risk)):
    open(name, 'w', encoding='utf-8').write(html)
print('pages written:', 7)
import shutil
shutil.rmtree('dist', ignore_errors=True); os.makedirs('dist')
for f in ('index.html', 'events.html', 'about.html', 'support.html', 'terms.html', 'privacy.html', 'risk.html', 'akashic.css', 'akashic.js', 'hero.js'): shutil.copy(f, 'dist')
shutil.copytree('assets', 'dist/assets', ignore=shutil.ignore_patterns('showcase'))
print('dist assembled')
