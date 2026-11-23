# Attack Scenario — Finding 011

## Nature

Missing security headers are a **defense-in-depth** weakness, not a directly
exploitable vulnerability. Concrete impact requires a secondary weakness that these
headers would otherwise mitigate. The scenarios below document those conditions.

## Prerequisite (general)

At least one of the following must coexist for meaningful impact:

- A content-injection / XSS sink (for CSP to matter).
- A sensitive state-changing action that a victim can be tricked into performing
  (for framing protection to matter).
- A MIME-confusion surface serving user-influenced content (for `nosniff`).
- A network position allowing protocol downgrade (for HSTS).

## Scenario A — Clickjacking (no framing protection)

1. The site is framed in an attacker-controlled page.
2. A logged-in victim is lured to the attacker page.
3. Transparent overlays align attacker UI with legitimate buttons.
4. The victim's clicks trigger sensitive actions in the framed application.

Because no `X-Frame-Options`/`frame-ancestors` is set, the browser permits the framing.

## Scenario B — Amplified XSS (no CSP)

1. A separate XSS sink exists (out of scope for this finding).
2. Injected script runs with full origin privileges because no CSP restricts it.
3. The script can read authenticated responses and exfiltrate data.

CSP would have constrained or blocked the injected script; its absence removes that
containment.

## Scenario C — Protocol downgrade / SSL strip (no HSTS)

1. A victim is on a hostile network.
2. The attacker intercepts an initial `http://` request.
3. Without HSTS, the browser accepts the downgraded connection and the attacker can
   read/modify traffic before any redirect to HTTPS.

## Scenario D — MIME sniffing (no `nosniff`)

1. The application serves user-influenced content with a declared type.
2. A browser MIME-sniffs the response and interprets it as an executable type.
3. The content executes in the origin context.

## What is not claimed

- No claim that the application currently contains an XSS sink or framing-sensitive
  action; those are separate concerns.
- No claim of direct compromise from header absence alone.
