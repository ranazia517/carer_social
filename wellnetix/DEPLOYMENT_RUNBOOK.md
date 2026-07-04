# Wellnetix Ltd Website — Deployment & Operations Runbook

Everything needed to understand, edit, deploy, and troubleshoot **https://wellnetixltd.com**.
Last updated: 2026-07-04.

---

## 1. What this is

The Wellnetix Ltd company landing page — the parent-company site that sits **above** NiMind and CARER.

- **One self-contained static page**: `index.html` (inline CSS + JS, no build step, no framework).
- Plus `contact.php` (form handler) and `assets/og-card.png` (link-preview image).
- **Dark-premium brand**: near-black bg `#0B0B14`, gradient indigo `#6D5FF6` → violet `#9B6BF2` → pink `#E879C7`, Inter (page) / Poppins (og card).
- **Sections**: nav → hero ("Advancing Human Wellbeing / Through Intelligent Technologies") → About (Who We Are / Mission) → Focus Areas (4) → **Products & Ventures (NiMind card, then CARER card → carer.wellnetixltd.com)** → Collaboration & Research → Contact **form** → footer.
- It was **designed in Fable 5** (claude.ai/design project `d445832c`, file "Wellnetix Landing") but the live site is **hand-built to match** (the Fable Standalone-HTML export wouldn't land in a reachable download path, and a hand-built single file is instantly editable with no credits). The Fable design still exists in that project if the literal export is ever wanted.

---

## 2. Key facts (memorise / grep these)

| Thing | Value |
|---|---|
| Live URLs | https://wellnetixltd.com , https://www.wellnetixltd.com |
| Host | Hostinger — Business Web Hosting |
| Hostinger username | `u629956930` |
| Hosting order_id | `1007956796` |
| **Origin server IP** | **`89.116.147.54`** (LiteSpeed) |
| Server docroot | `/home/u629956930/domains/wellnetixltd.com/public_html` |
| Contact email | `nimind@wellnetixltd.com` |
| Repo | `github.com/ranazia517/carer_social` |
| Branch | **`wellnetix-site`** |
| Folder in repo | `wellnetix/` (index.html, contact.php, assets/og-card.png, tools/make_og.py, README.md, this runbook) |
| Local git clone | `~/Developer/carer/carer_social` — **note:** `~/Developer/carer` itself is *not* a git repo |
| GitHub auth | `source ~/Developer/nimind/.secrets/github-tokens.env` → `$GITHUB_TOKEN_CLASSIC` |
| Design source | claude.ai/design project `d445832c`, file "Wellnetix Landing" (Fable 5) |

Interface tooling: the **Hostinger MCP connector** does hosting + DNS. Deploys read a **Mac-filesystem** zip path.

---

## 3. ⚠️ THE BIG GOTCHA — apex was CDN-fronted, deploys looked "stale"

**Symptom:** you deploy a change, curl/verify shows it live, but the browser (and some locations) still show the **old** page.

**Root cause:** the apex `wellnetixltd.com` was a Hostinger **CDN** record —
`@ ALIAS → wellnetixltd.com.cdn.hstgr.net.` and `www CNAME → …cdn.hstgr.net.`.
The CDN (`server: hcdn`) caches HTML at each edge POP with `cache-control: public, s-maxage=604800` (**7 days**), and **`hosting_deployStaticWebsite` does NOT purge the edge**. So some POPs kept serving the pre-deploy page for up to a week. Meanwhile the **origin was always correct**.

**How to diagnose (do this first if a change "won't show"):**
```bash
# What the public/CDN path serves + cache headers:
curl -sSI https://wellnetixltd.com/ | grep -iE '^(server|x-hcdn|age|cache-control|last-modified)'
#   server: hcdn  +  x-hcdn-cache-status: HIT  +  a big age  ==> CDN is serving stale.

# What the ORIGIN actually has (bypass DNS/CDN, force the origin IP):
curl -sSI --resolve wellnetixltd.com:443:89.116.147.54 https://wellnetixltd.com/ | grep -iE '^(server|last-modified)'
#   server: LiteSpeed  ==> origin, always fresh. If this is right, it's purely a cache/DNS issue.
```

**THE FIX WE APPLIED (2026-07-04) — bypass the CDN by pointing DNS at the origin:**
Repointed the apex + www to the origin IP, exactly like `carer.wellnetixltd.com` already is.
- `@ ALIAS → ftp.wellnetixltd.com.` (which is an A record → `89.116.147.54`)
- `www CNAME → ftp.wellnetixltd.com.`
- **Left untouched:** `@ MX → SMTP.GOOGLE.COM` (email lives on Google), `@ TXT` google-site-verification (×2), `carer A → 89.116.147.54`, `ftp A → 89.116.147.54`.

Result: apex now resolves to `89.116.147.54` → served **direct from LiteSpeed, no CDN, always fresh**. Propagated in <1 min (apex TTL 300 + ALIAS flattening). **Future deploys now show instantly.**

**How to do that DNS change via the MCP (reproducible):**
```
DNS_updateDNSRecordsV1(
  domain="wellnetixltd.com",
  overwrite=true,                       # same name+type => clean content swap, no delete needed
  zone=[
    {name:"@",   type:"ALIAS", ttl:300, records:[{content:"ftp.wellnetixltd.com."}]},
    {name:"www", type:"CNAME", ttl:300, records:[{content:"ftp.wellnetixltd.com."}]}
  ]
)
```

**Tooling limits found (so future-me doesn't waste time):**
- There is **NO cache-purge tool** in the Hostinger MCP.
- **`DNS_deleteDNSRecordsV1` is unusable here** — its MCP schema omits the required `filters` field, so the arg is stripped and it returns `"The filters field is required."`. **Do not try to delete records; change them in place with `DNS_updateDNSRecordsV1(overwrite:true)`.**
- To re-enable the CDN later (if ever wanted for performance/DDoS), point `@ ALIAS` / `www CNAME` back to `wellnetixltd.com.cdn.hstgr.net.` / `www.wellnetixltd.com.cdn.hstgr.net.` via hPanel, and expect edge staleness again.

**Note:** any staleness a visitor sees *now* is just their own **browser cache** → hard-refresh (Cmd+Shift+R / Ctrl+Shift+R).

---

## 4. Deploy an edit (now ~30 seconds, shows immediately)

1. **Edit the source** in the repo working copy: `~/Developer/carer/carer_social/wellnetix/index.html` (and/or `contact.php`, `assets/*`).
2. **Build a FLAT zip** — `index.html`, `contact.php`, `assets/` must be at the **ROOT** of the zip (not under `wellnetix/`). The `hosting_deployStaticWebsite` extract becomes `public_html`.
   - **`zip` binary fails** in the Cowork sandbox mounts (`Operation not permitted` — temp-file+rename blocked). **Build with Python instead:**
     ```bash
     python3 -c "import zipfile; z=zipfile.ZipFile('site.zip','w',zipfile.ZIP_DEFLATED); \
       z.write('index.html','index.html'); z.write('contact.php','contact.php'); \
       z.write('assets/og-card.png','assets/og-card.png'); z.close()"
     ```
   - The `archivePath` you pass must be a **Mac filesystem path** (the Hostinger MCP runs locally and reads Mac paths). A zip built in a Cowork mount that maps to the Mac (e.g. the outputs dir, or `~/Documents`) works.
3. **Deploy:**
   ```
   hosting_deployStaticWebsite(domain="wellnetixltd.com", archivePath="/abs/mac/path/site.zip")
   ```
   (A static deploy **replaces** the whole `public_html`, so the zip must contain the *entire* site — currently just those 3 files.)
4. **Verify (cache-busted):**
   ```bash
   curl -sS "https://wellnetixltd.com/?v=$(date +%s)" | grep -oE '<title>[^<]*</title>'
   curl -sSI https://wellnetixltd.com/ | grep -i '^server'   # expect: LiteSpeed  (NOT hcdn)
   ```
5. **Commit** the source change to `carer_social@wellnetix-site` (`$GITHUB_TOKEN_CLASSIC`).

---

## 5. Contact form (`index.html` form + `contact.php`)

- The form (name / email / message) submits via `fetch()` to `contact.php`, shows inline success/error, and has a **direct-email fallback link** beneath it.
- **CRITICAL — the fetch URL is `contact.php?t=' + Date.now()`.** Hostinger's edge forces `s-maxage` on `contact.php` and **ignores** PHP's `Cache-Control: no-store`; without a unique query it serves a **stale cached response** (this is why the first form test looked broken/422). Keep the `?t=` (belt-and-braces even now that apex is origin-direct).
- `contact.php`: validates, **honeypot** (hidden `company` field — bots fill it → silently accepted, nothing sent), header-injection guard (strips CR/LF), sends via PHP `mail()` to `nimind@wellnetixltd.com` with `Reply-To` = the submitter. Server is **PHP 8.3, `mail()` available**.
- **⚠️ DELIVERABILITY CAVEAT (unverified):** the domain's email is on **Google (MX→Google)** but the form sends from **Hostinger's server** as `noreply@wellnetixltd.com` → likely **SPF-misaligned → may land in SPAM**. `mail()` returns true (handed to the MTA) but inbox delivery isn't guaranteed, and we can't see the inbox to confirm.
  - **To harden if it lands in spam:** (a) add Hostinger's sending include to the domain **SPF TXT** via `DNS_updateDNSRecordsV1` (careful — the domain's SPF is Google's; append, don't clobber); or (b) route through **Google SMTP** (needs an app password from the owner); or (c) use a form service. The mailto fallback works regardless.

---

## 6. OG link-preview card (`assets/og-card.png`)

- 1200×630 PNG referenced by `og:image` + `twitter:card` in `index.html`; makes shares (LinkedIn/WhatsApp/Slack/iMessage/X) show a branded thumbnail.
- Generated by **`tools/make_og.py`** (Pillow + numpy): dark bg, additive indigo/pink radial glow, **gradient wordmark** (white text mask composited over a horizontal gradient), NiMind + CARER gradient-border pills, "wellnetixltd.com". Rendered at 2× and LANCZOS-downsampled for crispness.
- **FONT GOTCHA:** the nimind repo's `Inter-*.ttf` files are **Git-LFS pointer files** (they contain `<!DOCTYPE html>` → Pillow throws `OSError: unknown file format`). Use **Poppins** from `/usr/share/fonts/truetype/google-fonts/` instead (that's what `make_og.py` does). If running outside the Cowork sandbox, update `FDIR` in the script to a real Poppins/Inter path.
- To change it: edit `make_og.py`, run `python3 make_og.py`, then redeploy with the new `assets/og-card.png` (§4). Social platforms cache previews — re-share or use a platform's link-preview debugger to force a refresh.

---

## 7. Quick reference — "I just want to…"

- **Change wording/colour** → edit `wellnetix/index.html`, deploy (§4). Shows instantly.
- **Change the contact email** → edit `$to` in `contact.php` **and** the fallback `mailto:` in `index.html`, deploy.
- **New link-preview image** → edit/run `tools/make_og.py`, deploy the new `assets/og-card.png`.
- **"It still shows the old page"** → §3 diagnose; almost always browser cache now (hard-refresh) — confirm with the two curl commands.
- **Re-enable the CDN** → repoint `@`/`www` back to the `*.cdn.hstgr.net.` hostnames (hPanel), accept edge staleness.
