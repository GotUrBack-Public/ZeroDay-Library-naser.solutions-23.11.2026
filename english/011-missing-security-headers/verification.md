# Verification — Finding 011

## Verify the finding is present

```bash
cd /home/schaden637/naser-audit-clean
# 1. Only one scoped header rule should exist
sed -n '5,7p' next.config.mjs
# 2. Confirm no security headers are configured
grep -nE "Content-Security-Policy|Strict-Transport-Security|X-Frame-Options|X-Content-Type-Options|Referrer-Policy|Permissions-Policy" next.config.mjs || echo "NONE (finding present)"
```

Expected: the grep prints `NONE (finding present)`.

## Runtime confirmation (local)

```bash
curl -sD - -o /dev/null http://localhost:3000/ | grep -iE "content-security-policy|strict-transport-security|x-frame-options|x-content-type-options|referrer-policy|permissions-policy" || echo "NO SECURITY HEADERS"
```

Expected: `NO SECURITY HEADERS`.

## Verify a fix

After applying `remediation.md`:

```bash
# Headers must now be present
curl -sD - -o /dev/null http://localhost:3000/ | grep -iE "content-security-policy|strict-transport-security|x-frame-options|x-content-type-options|referrer-policy|permissions-policy"

# PDF route keeps its SEO directive
curl -sD - -o /dev/null http://localhost:3000/zertifikate/hexagon-cyber-security.pdf | grep -i "x-robots-tag"
```

Expected: all listed security headers appear, and the PDF route still returns
`x-robots-tag: noindex`.

## Regression checks

- Confirm the application still renders and functions (CSP in report-only first).
- Confirm the favicon rewrite (`next.config.mjs:8-10`) is unaffected.
