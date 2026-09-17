# Handoff

## State

Finished and live at handoff: home (hero, six feature cards, proof section, FAQ, membership plate), events (the free class on Sunday, October 4 with the signup form), about, contact, terms, privacy, risk disclosure, the tracker, signups, CSV and stats. Mobile verified at 390 px.

The previous deployment ran on the developer's own Cloudflare account and subdomain. Nothing carries over: create your own D1, `STATS_KEY` and domain. The old signup table held only test rows.

## Open

1. Class time: `EVENTS[0]['meta']` in `build_pages.py`, rebuild, deploy.
2. Domain: two lines in `wrangler.toml`, see README.
3. Emails: the form only stores addresses. Sending the invite needs an email service (Loops, Resend, Mailchimp) on your own address with an unsubscribe link and a postal address in the footer. `signup()` in `worker.js` can POST each signup to it once chosen.
4. Google Sheet: formula in README. Share it only with people who should see the list.

## Legal pages

Terms, Privacy and Risk were rewritten after a compliance review of the business as it runs today. No licensed attorney has reviewed them and the site does not say otherwise. They deliberately name no entity, state or address. Do not add those until an LLC exists and an attorney approves the wording.

The copy depends on these staying true:

- Members are US residents, 18 and older.
- Class signup addresses get deleted after the class unless the person asked to hear about future events. Someone has to do that.
- The site sets no cookies, stores no IP and loads nothing from third parties except Cloudflare.
- The results disclaimer under the proof section and the risk sections about member results and hypothetical performance exist because the site shows profit screenshots. Removing the disclaimer while keeping the screenshots is the fastest way to draw a complaint.

## For the owners

1. Form an LLC and have an attorney review the three legal pages. Until then the founders are personally liable.
2. Ask the attorney whether a paid signal group fits the publisher's exclusion from investment adviser registration. What keeps it inside: never discuss a specific member's positions in tickets, DMs, mentorship or one-to-one sessions; never trade anyone else's account; do not exit into member buying after a post; disclose own positions.
3. Written consent from each of the twelve members in the carousel, and confirmation none is staff, family or comped. Swap out anyone who is.
4. Whop: publish a refund policy on the product page; add a checkout question "I am 18 or older and agree to the Terms and Risk Disclosure" linking both pages.
5. Discord: Membership Screening with the same line.
6. Before the first class email: a postal address (PO box is fine) and an email service with unsubscribe. Both are required by CAN-SPAM. No emails to non-US addresses without express consent.
7. Every post with a referral link or code (Robinhood, Amex, prop firm) says the poster is paid if someone signs up.
8. Same profit-claim rules on Instagram as on the site.
9. Confirm Whop's checkout shows the trial end date, the renewal price and the cancel path.

## What an attorney will ask

Entity name, type, state, EIN, owners, mailing address. Who owns the Discord, Whop store, domain, Instagram and the VHAC indicator. Status and agreements of the contributing analysts. Whether anyone discusses member positions or trades member accounts. Paid promotion or referral arrangements. Whether posts are timestamped and archived. The Whop refund policy and checkout screenshots. Annual and lifetime offer terms. Who remits sales tax. Member count, revenue range, share of members outside the US. The twelve consents. The pinned counting rules for the trade log. Performance claims on Instagram. Any known minors. Who holds the stats key and the Sheet. Email service and retention period. Appetite for arbitration. Insurance. Trademark search on "Akashic Wealth" and "The Wealth Project".
