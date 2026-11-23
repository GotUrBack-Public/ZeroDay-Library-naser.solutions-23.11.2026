# Testumgebung

Dieses Dokument beschreibt die für die Sicherheitsüberprüfung verwendete Umgebung, wie die Feststellungen lokal reproduziert werden können und die Einschränkungen der Bewertung.

---

## 1. Lokale Testerklärung

Alle in diesem Bericht dokumentierten Proofs of Concept und Exploit-Demonstrationen wurden ausschließlich in einer kontrollierten lokalen Testumgebung mit localhost, isolierten Testinstanzen oder Mocks durchgeführt. Es wurden keine Produktionssysteme, Infrastrukturen Dritter oder externen Benutzer angegriffen.

Sämtliche in dieser Forschung beschriebene Sicherheitstests wurden **lokal** gegen eine Entwicklungsinstanz der Anwendung unter `http://localhost:3000` durchgeführt. Es wurde kein Produktivsystem, keine Staging-Deployment und kein Drittanbieter-Live-Dienst gescannt, angegriffen oder verändert.

- Jeder Proof of Concept zielt auf `http://localhost:3000` oder einen lokalen Mock.
- Während des Testens wurden keine Anfragen an Vercel, Strato SMTP, thum.io, Microlink oder WordPress mshots gesendet.
- Die Analyse war **schreibgeschützt**: es wurden keine Quelldateien geändert und im Rahmen der Überprüfung keine Fixes angewendet.
- Feststellungen, die von der Deployment-Konfiguration abhängen (z. B. `PAYLOAD_SECRET`), wurden aus dem Code bewertet und als bedingt dokumentiert.

Diese Erklärung spiegelt sich in [DISCLOSURE.md](DISCLOSURE.md) wider.

---

## 2. Umgebungdetails

### 2.1 Anwendungs-Stack

| Komponente | Version / Detail |
|-----------|------------------|
| Framework | Next.js **16.2.6** (App Router) |
| CMS | Payload CMS **3.86.0** (`@payloadcms/next`, `@payloadcms/ui`, `@payloadcms/richtext-lexical`, `@payloadcms/plugin-cloud-storage`) |
| Datenbankadapter | `@payloadcms/db-postgres` 3.86.0 |
| Datenbanktreiber | `pg` 8.22.0 (PostgreSQL) |
| Objektspeicher | `@vercel/blob` 2.3.1 |
| E-Mail | `nodemailer` (aktuellste Version) über `smtp.strato.de:465` (implicit TLS) |
| Bildverarbeitung | `sharp` 0.34.0 |
| UI-Runtime | React 19, React DOM 19 |
| Styling | Tailwind CSS 4, PostCSS 8 |
| Sprache | TypeScript 5 |
| Paketmanager | npm (`package-lock.json`, `.npmrc`) |

### 2.2 Runtimes

| Runtime | Verwendet von |
|---------|---------|
| Node.js | Portal-Login/Logout, Kontaktformular, Anhang-Upload, Server Actions |
| Edge | Thumbnail-Generierung (`app/api/generate-thumbnail/route.ts`) |

### 2.3 Lokale Konfiguration

- Anwendungs-URL: `http://localhost:3000`
- Datenbank: PostgreSQL, Verbindung über `DATABASE_URL` (Schema `payload`, `push: false`)
- Speicher: Vercel Blob über `BLOB_READ_WRITE_TOKEN`
- E-Mail: `STRATO_SMTP_PASSWORD` (nur serverseitig)
- Secret: `PAYLOAD_SECRET` (nur serverseitig)
- Öffentliche Server-URL: `NEXT_PUBLIC_SERVER_URL`, mit Fallback auf Vercel-URL-Variablen oder `http://localhost:3000`

Es existiert ein lokaler CMS-Preview-Modus (`LOCAL_CMS_PREVIEW=1`), der gebündelte Beispielinhalte ohne Datenbank bereitstellt; er ist auf Vercel deaktiviert und kein Ersatz für authentifiziertes CMS-Testing.

---

## 3. Reproduktionsanleitung

### 3.1 Voraussetzungen

- Node.js und npm installiert.
- Eine lokale PostgreSQL-Instanz (oder der Preview-Modus für DB-freie Prüfungen).
- Serverseitige Umgebungsvariablen gesetzt für die zu testenden Code-Pfade.

### 3.2 Einrichtung

```bash
# 1. Abhängigkeiten installieren
npm ci

# 2. Serverseitige Konfiguration bereitstellen (Werte sind Beispiele)
export DATABASE_URL="postgres://user:pass@localhost:5432/naser"
export PAYLOAD_SECRET="<ein starkes zufälliges Secret von mindestens 32 Bytes>"
export BLOB_READ_WRITE_TOKEN="<vercel blob token>"
export STRATO_SMTP_PASSWORD="<smtp passwort>"

# 3. Entwicklungsserver starten
npm run dev
# -> App verfügbar unter http://localhost:3000
```

Für einen datenbankfreien Smoke-Test:

```bash
LOCAL_CMS_PREVIEW=1 npm run dev
```

### 3.3 Beispielreproduktionen

Die folgenden Beispiele illustrieren das lokal-only Proof-of-Concept-Muster. Die Beschreibung jeder Feststellung unter `de/findings/` enthält die vollständige Reproduktion.

**001 — Payload Secret leerer Standardwert.** Ist `PAYLOAD_SECRET` nicht gesetzt, wird ein JWT mit einem leeren Schlüssel signiert und als Payload-Session-Token präsentiert; der Server akzeptiert es. Der getestete Fix ist eine Startzeit-Validierung, die ein leeres oder zu kurzes Secret ablehnt.

**002 — Portal-Login ohne Rate Limiting.** Wiederholtes POSTen von Zugangsdaten an den Portal-Login-Endpunkt und Beobachten, dass keine Sperre eintritt:

```bash
for i in $(seq 1 100); do
  curl -s -o /dev/null -w "%{http_code}\n" \
    -X POST http://localhost:3000/api/portal/login \
    -H "Content-Type: application/json" \
    -d "{\"email\":\"client@example.com\",\"password\":\"wrong-$i\"}"
done
# Alle Versuche geben 401 zurück; das Konto wird nie gesperrt.
```

**003 — Ressourcenerschöpfung/Verstärkung bei Thumbnails.** Paralleles Senden von Anfragen an den öffentlichen Thumbnail-Endpunkt und Beobachten der Fächerung zu externen Anbietern:

```bash
for i in $(seq 1 25); do
  curl -s "http://localhost:3000/api/generate-thumbnail?url=https://example.com/page$i" &
done
wait
# Jede Anfrage kann bis zu vier ausgehende Fetches auslösen.
```

**004 — Kontaktformular ohne Rate Limiting.** Wiederholtes POSTen an den Kontakt-Endpunkt und Beobachten ausgehender Mail-Versuche ohne Drosselung:

```bash
for i in $(seq 1 25); do
  curl -s -o /dev/null -X POST http://localhost:3000/api/contact \
    -H "Content-Type: application/json" \
    -d "{\"name\":\"Test\",\"email\":\"bot$i@example.com\",\"message\":\"synthetic test\"}"
done
```

> Führen Sie diese nur gegen Ihre eigene lokale Instanz aus. Verwenden Sie synthetische Daten und vermeiden Sie nach Möglichkeit externe Anbieter (z. B. das Kontaktformular auf ein lokales SMTP-Sink zeigen lassen).

---

## 4. Einschränkungen

1. **Nur lokale Tests.** Das gesamte Verhalten wurde auf `http://localhost:3000` beobachtet. Das Produktivverhalten kann abweichen, insbesondere bei plattformverwalteten Headern und TLS.
2. **Statische Analyse.** Das Laufzeitverhalten von Drittanbieterdiensten (Vercel-Header-Standards, Anbieter-Rate-Limits, SMTP-Server-Richtlinie) wurde aus Code und Dokumentation bewertet, nicht aus Live-Interaktion.
3. **Deployment-abhängige Feststellungen.** Die Feststellungen 001 (Secret), 006 (Cookie-`secure`-Flag) und 010 (CMS-Origins) hängen von Umgebungsvariablen und Deployment-Konfiguration ab; die Bewertungen spiegeln den Worst-Case-Zustand des Codes wider.
4. **Keine Fixes angewendet.** Die Überprüfung ist schreibgeschützt; die Behebung ist nicht Gegenstand und wird separat verfolgt.
5. **Momentaufnahme.** Die Ergebnisse spiegeln den Quellbaum zum geprüften Commit wider. Spätere Änderungen können Feststellungen verändern oder beheben.
6. **Externe Dienste nicht belastet.** Es wurden keine Last-, Denial-of-Service- oder Missbrauchstests gegen Vercel, Strato SMTP, thum.io, Microlink oder WordPress mshots durchgeführt.
7. **CVSS-Bewertung.** Bewertungen dienen der Priorisierung; die CVSS 4.0-Werte sind eine äquivalente Neubewertung der ursprünglichen CVSS 3.1-Basisbewertungen (siehe [RISK-MATRIX.md](RISK-MATRIX.md)).
