# Verification — Finding 010

## Verify the finding is present

Inspect the source:

```bash
cd /home/schaden637/naser-audit-clean
sed -n '9,15p' lib/cms-origins.ts
```

Line 14 must read:

```ts
return [...new Set([...productionOrigins, configuredURL.origin])]
```

and there must be no host validation between lines 10 and 14.

Run the local PoC (see `poc.md`) and confirm a hostile `serverURL` is appended.

## Verify a fix

After applying `remediation.md`:

```bash
cd /home/schaden637/naser-audit-clean
# 1. Hostile origins must now be rejected
npx tsx -e "import {cmsOrigins} from './lib/cms-origins.ts'; \
try { cmsOrigins('https://attacker.example'); console.log('FAIL: accepted'); } \
catch { console.log('PASS: rejected'); }"

# 2. Existing behavior preserved for trusted origins
npx tsx -e "import {cmsOrigins} from './lib/cms-origins.ts'; \
console.log(cmsOrigins('https://www.naser.solutions'))"

# 3. Run the project's origin tests
npx tsx --test tests/cms-origins.test.ts
```

Expected:

1. `PASS: rejected`
2. All four production origins present; `https://www.naser.solutions` not duplicated.
3. All tests pass, including the new negative assertions.

## Regression checks

- Confirm `payload.config.ts:100-101` still receives a valid array (no throw at
  startup for legitimate values).
- Confirm local development (`http://localhost:3000`) still works if localhost is on
  the host allowlist.
