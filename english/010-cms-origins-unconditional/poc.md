# Proof of Concept — Finding 010

> Scope: this proof of concept runs entirely against `http://localhost`. It does not
> target any production host or third-party service. It demonstrates the
> **function behaviour**, not a live cross-origin exploit.

## Objective

Show that `cmsOrigins()` appends an arbitrary, unvalidated origin supplied via
`serverURL`, proving that a hostile value would enter the CORS/CSRF allowlist.

## Environment

- Node.js (the project already uses `node:test`, see `tests/cms-origins.test.ts`).
- The repository checkout at the reviewed revision.

## Local reproduction (unit-level)

Create a temporary script `/tmp/kilo/poc-010.mjs`:

```js
import { cmsOrigins } from '/home/schaden637/naser-audit-clean/lib/cms-origins.ts'

for (const candidate of [
  'https://attacker.example',
  'https://www.naser-solutions.de.attacker.example',
  'http://www.naser-solutions.de',            // scheme-only control
  'https://www.naser-solutions.de:8443',      // arbitrary port
]) {
  const origins = cmsOrigins(candidate)
  console.log(candidate, '=>', origins.includes(new URL(candidate).origin))
}
```

Run it with the project's TypeScript-capable runner (for example `npx tsx`
or `node --experimental-strip-types` depending on the installed Node version):

```bash
cd /home/schaden637/naser-audit-clean
npx tsx /tmp/kilo/poc-010.mjs
```

## Expected output

```
https://attacker.example => true
https://www.naser-solutions.de.attacker.example => true
http://www.naser-solutions.de => true
https://www.naser-solutions.de:8443 => true
```

Each `true` means the candidate origin was appended to the allowlist by
`lib/cms-origins.ts:14`. The function accepts every one of them; only a non-HTTP(S)
scheme (e.g. `file:///tmp/cms`) is rejected, as already asserted by
`tests/cms-origins.test.ts:30`.

## Interpretation

The PoC confirms the root cause: `configuredURL.origin` is trusted unconditionally.
It does **not** demonstrate a reachable cross-origin exploit against a deployed
instance; that additionally requires configuration control as described in
`attack-scenario.md`.

## Cleanup

```bash
rm -f /tmp/kilo/poc-010.mjs
```
