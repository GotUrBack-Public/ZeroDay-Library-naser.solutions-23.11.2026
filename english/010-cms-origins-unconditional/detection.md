# Detection & Monitoring — Finding 010

This document describes how to detect the presence of the weakness and how to monitor
for the dangerous misconfiguration that would make it exploitable. It applies equally
to confirming a fix.

## Static detection

### Confirm the unconditional append

```bash
cd /home/schaden637/naser-audit-clean
grep -n "configuredURL.origin" lib/cms-origins.ts
```

Expected vulnerable form: line 14 appends `configuredURL.origin` with no host check
between the scheme check (`lib/cms-origins.ts:11-13`) and the return.

### Confirm the consumers

```bash
grep -n "cmsOrigins(serverURL)" payload.config.ts
```

Both `cors` (line 100) and `csrf` (line 101) must reference the function.

## Configuration monitoring (the real risk signal)

The weakness is only dangerous when `serverURL` is attacker-influenced. Monitor:

1. **Environment variable provenance.** Alert on changes to
   `NEXT_PUBLIC_SERVER_URL`, `VERCEL_PROJECT_PRODUCTION_URL`, and `VERCEL_URL`
   outside approved deployment pipelines.
2. **Deployment origin drift.** On startup, log the resolved `serverURL` origin and
   compare it against the four production origins. Alert on any unknown host.
3. **Fork / preview leakage.** In CI, fail a build if a preview deployment's resolved
   origin is not in an explicit allowlist.

## Runtime detection

If Payload logs or a reverse proxy logs CORS decisions, alert on any `Origin` header
value that is not one of the four production origins while a valid CMS session cookie
is present. Such events indicate a widened allowlist is being exercised.

## Post-fix verification

After remediation, the static check should show a host validation before the return,
and the negative tests in `verification.md` should pass (hostile origins rejected).
