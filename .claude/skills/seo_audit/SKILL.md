# SEO Audit Skill

> Reference for the Sell mode when auditing a live site's SEO or generating SEO-ready meta tags.

---

## Running an SEO Audit

### 1. Fetch the Page

```bash
curl -sL -o /tmp/page.html "[live_url]"
```

### 2. Check Meta Tags

```bash
# Title tag
grep -oP '<title>(.*?)</title>' /tmp/page.html

# Meta description
grep -oP '<meta name="description" content="(.*?)"' /tmp/page.html

# OG tags
grep -oP '<meta property="og:(.*?)" content="(.*?)"' /tmp/page.html

# Canonical
grep -oP '<link rel="canonical" href="(.*?)"' /tmp/page.html
```

### 3. Check Heading Structure

```bash
# H1 tags (should be exactly 1)
grep -oP '<h1[^>]*>(.*?)</h1>' /tmp/page.html

# All headings
grep -oP '<h[1-6][^>]*>(.*?)</h[1-6]>' /tmp/page.html
```

### 4. Check Images

```bash
# Images missing alt text
grep -oP '<img[^>]*>' /tmp/page.html | grep -v 'alt='
```

### 5. Check Performance Signals

```bash
# Page size
wc -c < /tmp/page.html

# Check for render-blocking resources
grep -c '<link.*stylesheet' /tmp/page.html
grep -c '<script(?!.*defer|async)' /tmp/page.html
```

## Meta Tag Templates

### Standard Meta Tags
```html
<title>[Primary Keyword] — [Brand Name] | [Value Prop]</title>
<meta name="description" content="[Action verb] [benefit]. [Product] helps [target user] [outcome]. [CTA or differentiator]." />
<meta name="robots" content="index, follow" />
<link rel="canonical" href="[live_url]" />
```

### Open Graph Tags
```html
<meta property="og:type" content="website" />
<meta property="og:title" content="[Same as title or shorter]" />
<meta property="og:description" content="[Same as meta description or shorter]" />
<meta property="og:image" content="[1200x630 image URL]" />
<meta property="og:url" content="[live_url]" />
<meta property="og:site_name" content="[Brand Name]" />
```

### Twitter Card Tags
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="[Title]" />
<meta name="twitter:description" content="[Description]" />
<meta name="twitter:image" content="[1200x630 image URL]" />
```

## Keyword Targeting

### Process
1. Extract the positioning statement from marketing-strategy.md
2. Identify 3-5 primary keywords from the product's core value prop
3. Map keywords to pages:
   - Homepage: brand + primary keyword
   - Feature pages: long-tail keywords
   - Blog/content: informational keywords

### Keyword Placement
- Title tag: primary keyword near the front
- H1: primary keyword (natural language, not stuffed)
- First paragraph: primary keyword within first 100 words
- URL slug: keyword-rich, hyphenated
- Image alt text: descriptive, keyword where natural
- Meta description: primary keyword + CTA

## robots.txt Template

```
User-agent: *
Allow: /
Disallow: /api/
Disallow: /admin/
Disallow: /_next/

Sitemap: [live_url]/sitemap.xml
```

## sitemap.xml Template

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>[live_url]/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>[live_url]/features</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

## SEO Audit Report Structure

Output to `.onemillion/seo-audit.md`:

```markdown
# SEO Audit — [Product Name]

## Score: [X/10]

## Meta Tags
| Tag | Status | Current Value | Recommendation |
|-----|--------|---------------|----------------|

## Heading Structure
| Level | Count | Content | Issue |
|-------|-------|---------|-------|

## Images
| Image | Alt Text | Issue |
|-------|----------|-------|

## Keywords
| Keyword | Volume Signal | Page | Placement |
|---------|--------------|------|-----------|

## Technical
- Page size: [X KB]
- Render-blocking resources: [N]
- robots.txt: [exists/missing]
- sitemap.xml: [exists/missing]
- Canonical: [set/missing]
- HTTPS: [yes/no]

## Recommendations (priority order)
1. ...
2. ...
```

## Best Practices

- Title tags: 50-60 characters max
- Meta descriptions: 150-160 characters max
- One H1 per page, keyword-rich
- All images need descriptive alt text
- Canonical URL on every page
- robots.txt at site root
- sitemap.xml submitted to Google Search Console
- HTTPS everywhere (no mixed content)
