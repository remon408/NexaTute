# First-visit language prompt — all products (owner standing order, 31 Oct 2026)

Applies to: NexaTute (web, admin, Nexa Speak app), Remon Motion Studio, NexaLogicDev, RemonLogic company site, every landing page and every future site/app. Build it in by default; the owner should never have to ask again.

## Behaviour
1. First visit: detect the visitor's country (IP country lookup only; the IP address is not stored) and the browser/device language.
2. If that country's language is one of our 10 (bn, en, hi, ur, ar, fr, ja, de, zh, ko) and is not English, show one small prompt in BOTH languages: "View in বাংলা / or in English?" (two buttons, equal size, ≥ 44 px).
3. The choice is saved: in the account Settings (logged in) and in the browser (guest, first-party preference cookie/localStorage, no tracking). Never asked again; changeable any time from Settings and the header language switcher.
4. Country language not supported → site opens in English with no prompt.
5. English-speaking countries → English, no prompt.

## Approved defaults (owner 31 Oct 2026; admin-editable)
- Countries with more than one of our languages: India → Hindi or English (browser language decides which is offered); Pakistan → Urdu or English; Switzerland/Belgium/Canada → French or German/English by browser language; Bangladesh → বাংলা or English. Arabic-speaking countries → Arabic (RTL) or English.
- Browser language beats IP country when they differ (e.g. a Bangladeshi in Japan with a Bangla browser is offered বাংলা).
- Not a full-screen popup: a small top banner/bottom sheet that does not block reading (Google treats blocking pop-ups as intrusive and lowers search ranking; also WCAG). Search-engine bots never see it; every language has its own URL with hreflang.
- Mobile apps (Nexa Speak etc.): use the phone's language on first launch, same prompt, same English fallback.
- Under-18 accounts: guardian's chosen language is used for guardian screens; child screens follow the child's class/course language.
- Country lookup from the Cloudflare CF-IPCountry header (owner chose Cloudflare CDN, 31 Oct 2026); DB-IP Lite (CC BY 4.0) only as fallback for apps/servers not behind Cloudflare.
- Each new language goes live only after native-speaker review (existing rule).

## Admin panel (each product)
On/off switch; country → language map; prompt text in all 10 languages; default fallback language (English); report: prompt shown / chosen language / changed later (counts only, cells < 20 hidden). Changes need two-person approval and are logged.
