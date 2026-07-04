Wellnetix Ltd company landing page — served at https://wellnetixltd.com. Dark-premium single-file static site (inline CSS/JS, no build). Sections: hero ('Advancing Human Wellbeing Through Intelligent Technologies'), about (Who We Are / Our Mission), focus areas, Products & Ventures (NiMind card + CARER card → https://carer.wellnetixltd.com), collaboration & research, contact, footer.

## Contact form
The "Get in Touch" section is a name/email/message form that POSTs to `contact.php` (self-hosted PHP `mail()` handler → nimind@wellnetixltd.com; honeypot + validation + header-injection guard). The browser appends `?t=<timestamp>` to the request to bypass Hostinger's edge cache.

## Assets
OG link-preview image at `assets/og-card.png`.

## Deploy
Deployed to wellnetixltd.com via Hostinger static hosting — edit the files and redeploy, no build needed. Deploy = a FLAT zip with `index.html` + `contact.php` + `assets/` at the ROOT, pushed via `hosting_deployStaticWebsite`.
