# Detection & Monitoring — Finding 011

This document describes how to detect the missing-header condition and how to monitor
for regressions after a fix.

## Static detection

```bash
cd /home/schaden637/naser-audit-clean
grep -nE "Content-Security-Policy|Strict-Transport-Security|X-Frame-Options|X-Content-Type-Options|Referrer-Policy|Permissions-Policy" next.config.mjs || echo "NO GLOBAL SECURITY HEADERS CONFIGURED"
```

If the command prints `NO GLOBAL SECURITY HEADERS CONFIGURED`, the finding is present.

## Runtime detection (local)

```bash
curl -sD - -o /dev/null http://localhost:3000/ \
  | grep -iE "content-security-policy|strict-transport-security|x-frame-options|x-content-type-options|referrer-policy|permissions-policy" \
  || echo "MISSING SECURITY HEADERS"
```

## Continuous monitoring

1. **Response-header assertions in CI.** Add a smoke test that requests `/` and asserts
   the presence of the required headers; fail the build if any are missing.
2. **CSP report monitoring.** Once CSP is deployed (even report-only), collect
   `report-uri`/`report-to` violations and alert on spikes, which may indicate injection
   attempts.
3. **Edge-header reconciliation.** If a CDN or reverse proxy injects headers, add a
   synthetic check that compares edge headers against the application's intended set to
   catch drift.

## Post-fix verification

After applying `remediation.md`, the static grep should list the configured header
keys, and the runtime check should print the header names rather than the
`MISSING SECURITY HEADERS` sentinel. See `verification.md` for the full procedure.
