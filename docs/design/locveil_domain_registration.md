# Locveil — domain registration instructions (owner action)

**Status: MOSTLY EXECUTED 2026-07-11.** `locveil.com` (Porkbun) + `locveil.ru` (REG.RU) registered,
GitHub org `locveil` claimed — all verified same day. **`.io` DROPPED from the required list**
(owner decision — invented word, `.com` is canonical). **`.eu` PENDING**: register via Porkbun once
REG.RU ID verification supplies the EURid-verifiable data — the one open item this doc still tracks.

## What to register

| Domain | Verified free via | Purpose |
|---|---|---|
| `locveil.com` | Verisign RDAP (404) | the brand home; landing page (`site/`, GitHub Pages) |
| ~~`locveil.io`~~ | RDAP (404) | DROPPED 2026-07-11 — not required; .com is canonical |
| `locveil.eu` | EURid whois: `Status: AVAILABLE` | EU presence; defensive |
| `locveil.ru` | TCI whois: no entries | Russian-first audience — register via your usual .ru registrar (not covered here) |

Also claim (free, do the same day): the **`locveil` GitHub org** — it was free at the
sweep and orgs can't be watched via RDAP; whoever claims first wins.
PyPI/npm/crates names cannot be reserved without publishing; they get claimed when the
first `locveil-*` packages ship (never publish a bare `locveil` package before the
umbrella exists — prefix everything, same discipline as planned for Domovoy).

## Registrar recommendation for .com / .io / .eu

**Primary recommendation: [Porkbun](https://porkbun.com)** — one account for all three.

- Supports all three TLDs (900+ TLDs, including .eu; Cloudflare's ~200-TLD list is thinner
  on ccTLDs).
- "Fair-profit" pricing: ~$1–1.5 over wholesale. 2026 ballpark: .com ≈ $9.3/yr,
  .io ≈ $27.8/yr, .eu single-digit €. Total for the three ≈ **$45–50/yr**.
- Free WHOIS privacy, free SSL, no upsell circus, solid reputation among indie devs.
- No lock-in: you can point nameservers anywhere (e.g. free Cloudflare DNS) or transfer out.

**Alternative: [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/)** —
sells at exact wholesale cost (zero markup; .com ≈ $10.4, .io ≈ $27.9), marginally cheaper
than Porkbun on renewals. Two caveats: (1) domains there **must use Cloudflare
nameservers** — fine if the DNS lands on Cloudflare anyway, but it's lock-in; (2) .eu
support/eligibility handling is less battle-tested than Porkbun's. Price difference is
$1–2/yr — choose on workflow, not cost.

Avoid GoDaddy/1&1-style registrars (teaser first-year pricing, expensive renewals, upsells).

## ⚠️ .eu eligibility gate — check before paying

EURid restricts registrants to: **EU citizens (anywhere in the world, since 2021-08),
non-citizens resident in the EU/EEA, or organisations established in the EU/EEA**
(Iceland/Liechtenstein/Norway count). EURid **verifies registrant data** (name, address,
email, phone) and can suspend on mismatch — register with real data that passes the check.
If neither citizenship nor EU residency applies, drop `.eu` from the cart; `.com`+`.io`+`.ru`
cover the brand fine.

Payment note: Porkbun and Cloudflare both need a payment method they accept
(international card / PayPal); Russian-issued cards will not work — use whatever
non-RU payment channel you already use for such services.

## Step-by-step (Porkbun)

1. Create the account → **enable 2FA immediately** (the registrar account is now the
   keys to the brand).
2. Fill the contact profile with verifiable data (matters for the EURid check).
3. Cart all three domains in one checkout: `locveil.com`, `locveil.io`, `locveil.eu`.
   Register for **2+ years** if offered — cheap insurance against a missed renewal
   during the busiest brand-building year.
4. Switch **auto-renew ON** for all three; keep the default WHOIS privacy ON
   (note: .eu publishes registrant data per EURid policy regardless — expected).
5. Verify the registration emails (ICANN verification links — domains get suspended
   if ignored).
6. DNS: nothing needs to resolve yet. Either leave parked, or set all three to redirect
   to `github.com/droman42` until `site/` exists. When the landing page lands
   (GitHub Pages), point `locveil.com` at it (CNAME/A per GitHub docs) and 301 the
   other TLDs to `locveil.com`.
7. Same day: claim the **GitHub org `locveil`** (Settings → Organizations → New).
   Park it with a one-line README; repos move in at BUILD-21.

## After registration

Report back in a commons session → the name lock is then complete and Phase 1 step 2
(`gh repo rename` eval-commons → `locveil-commons` + local dir rename) proceeds, followed
by the BUILD-21 restructuring. This file then moves under `board/`/`process/` housekeeping
or gets deleted as executed.
