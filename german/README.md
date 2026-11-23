# Security Research — Naser Solutions Webanwendung

[![Audit Status](https://img.shields.io/badge/audit-complete-brightgreen)](EXECUTIVE-SUMMARY.md)
[![Findings](https://img.shields.io/badge/findings-13-blue)](RISK-MATRIX.md)
[![CVSS](https://img.shields.io/badge/CVSS-4.0-orange)](RISK-MATRIX.md)
[![Language](https://img.shields.io/badge/language-German-blue)](README.md)
[![Scope](https://img.shields.io/badge/scope-Next.js%2016%20%2B%20Payload%20CMS%203-informational)](TEST-ENVIRONMENT.md)

Unabhängige Sicherheitsforschung und Dokumentation zur verantwortungsvollen Offenlegung für die **Naser Solutions**-Webplattform: eine **Next.js 16**-Anwendung (App Router) mit **Payload CMS 3**, PostgreSQL, Vercel Blob Storage und Nodemailer-basiertem Kontaktversand.

Dieses Repository dokumentiert eine mehrstufige Sicherheitsüberprüfung des Anwendungscodes. Es enthält einen konsolidierten Satz von **13 Feststellungen** — **11 validiert** und **2 False Positives** — jede klassifiziert, bewertet und mit Handlungsempfehlungen zur Behebung versehen. Sämtliche Tests wurden lokal durchgeführt; es wurde kein Produktivsystem anvisiert (siehe [DISCLOSURE.md](DISCLOSURE.md)).

---

## Inhaltsverzeichnis

- [Sprachversionen](#sprachversionen)
- [Repository-Aufbau](#repository-aufbau)
- [Prüfungsumfang](#prüfungsumfang)
- [Feststellungen auf einen Blick](#feststellungen-auf-einen-blick)
- [Schweregrad-Zusammenfassung](#schweregrad-zusammenfassung)
- [Dokumentationsindex](#dokumentationsindex)
- [Offenlegungserklärung (Zusammenfassung)](#offenlegungserklärung-zusammenfassung)
- [Test & Reproduktion](#test--reproduktion)
- [Mitwirken & Korrekturen](#mitwirken--korrekturen)

---

## Sprachversionen

Dieses Dokument ist die **deutsche Version**. Lokalisierte Feststellungs-Sets werden pro Sprache gepflegt:

| Sprache | Einstiegspunkt | Feststellungen |
|----------|-------------|----------|
| English | [README.md](../README.md) (englisches Original) | [en/findings/](../en/findings/) |
| Deutsch | [de/README.md](README.md) (diese Datei) | [de/findings/](findings/) |
| Русский | [ru/README.md](../ru/README.md) | [ru/findings/](../ru/findings/) |

Die englischen Ausführungen der Top-Level-Dokumente in diesem Verzeichnis (`README.md`, `EXECUTIVE-SUMMARY.md`, `RISK-MATRIX.md`, `TEST-ENVIRONMENT.md`, `DISCLOSURE.md`, `DOCUMENTATION-QA.md`) bilden das Referenzset.

---

## Repository-Aufbau

```
security-research/
├── README.md                 # Englische Übersicht (Original)
├── EXECUTIVE-SUMMARY.md      # Umfang, Summen, Klassifizierung, Top-Prioritäten
├── RISK-MATRIX.md            # CVSS 4.0 Matrix, Schweregradverteilung, Heatmap
├── TEST-ENVIRONMENT.md       # Umgebung, Reproduktion, Einschränkungen
├── DISCLOSURE.md             # Richtlinie und Zeitplan zur verantwortungsvollen Offenlegung
├── DOCUMENTATION-QA.md       # Qualitäts-Checkliste und bekannte Einschränkungen
├── en/findings/              # Englische Detailbeschreibung je Feststellung (13 Feststellungen)
├── de/findings/              # Deutsche Detailbeschreibung je Feststellung (13 Feststellungen)
└── ru/findings/              # Russische Detailbeschreibung je Feststellung (13 Feststellungen)
```

Jedes Feststellungsverzeichnis ist nach dem Schema `NNN-kurztitel` benannt und enthält die Feststellungsbeschreibung (Beschreibung, Code Fundstelle, Proof of Concept, Erläuterung und Klassifizierung). Die Nummerierung ist in allen drei Sprachen identisch.

---

## Prüfungsumfang

| Punkt | Wert |
|------|-------|
| Ziel | Naser Solutions Webplattform (`naser-audit-clean`) |
| Framework | Next.js **16.2.6** (App Router, Edge- + Node.js-Runtimes) |
| CMS | Payload CMS **3.86.0** (`@payloadcms/*` 3.86.0) |
| Datenbank | PostgreSQL über `@payloadcms/db-postgres` 3.86.0 |
| Speicher | Vercel Blob 2.3.1 (Client-Uploads) |
| E-Mail | Nodemailer über `smtp.strato.de:465` |
| Geprüfte Komponenten | Öffentliche Website, Payload-Admin/CMS, Kundenportal, API-Routen, Auth/Session, Uploads, Kontakt, Thumbnails |
| Methode | Statische Code-Analyse, Aufrufketten-Review, lokaler Proof of Concept auf `http://localhost:3000` |
| Runden | Runde 1 (erste Feststellungen), Runde 3 (weitere Feststellungen), Runde 4 (tiefe Validierung) |

Vollständige Umgebungdetails und Reproduktionsschritte finden sich in [TEST-ENVIRONMENT.md](TEST-ENVIRONMENT.md).

---

## Feststellungen auf einen Blick

| ID | Feststellung | Schweregrad | Klassifizierung | Primäre Fundstelle |
|----|---------|----------|----------------|------------------|
| 001 | Payload Secret leerer Standardwert | **Kritisch** | BESTÄTIGT | `payload.config.ts:39` |
| 002 | Portal-Login ohne Rate Limiting | **Hoch** | BESTÄTIGT | `app/api/portal/login/route.ts:15` |
| 003 | Ressourcenerschöpfung/Verstärkung bei Thumbnails | **Hoch** | BESTÄTIGT | `app/api/generate-thumbnail/route.ts:66` |
| 004 | Kontaktformular ohne Rate Limiting | Mittel | BESTÄTIGT | `app/api/contact/route.ts:70` |
| 005 | Upload ohne nutzerspezifisches Kontingent | Niedrig | BESTÄTIGT | `app/api/portal/attachments/upload/route.ts:25` |
| 006 | Session-Cookie mit schwachen Attributen | Niedrig | BESTÄTIGT | `lib/portal-session.ts:25` |
| 007 | Preview-CSRF über GET (Entwurfsmodus) | Mittel | BESTÄTIGT | `app/preview/route.ts:6` |
| 008 | Portal-JWT ohne Client-Bindung | Mittel | BESTÄTIGT | `lib/portal-session.ts:5` |
| 009 | Lost Update in `saveClientFeedback` | Niedrig | INFORMATIONAL | `app/portal/actions.ts:43` |
| 010 | `cmsOrigins` bedingungslose Allowlist | Niedrig | INFORMATIONAL | `lib/cms-origins.ts:14` |
| 011 | Fehlende Sicherheitsheader | Informational | INFORMATIONAL | `next.config.mjs:5` |
| 012 | E-Mail-Header-Injection | — | FALSE POSITIVE | `app/api/contact/route.ts:89` |
| 013 | Aufzählung von Entwurfsseiten | — | FALSE POSITIVE | `lib/cms.ts:39` |

CVSS 4.0-Vektoren und Bewertungen für jede Feststellung finden sich in [RISK-MATRIX.md](RISK-MATRIX.md).

---

## Schweregrad-Zusammenfassung

| Schweregrad | Anzahl | Feststellungen |
|----------|-------|----------|
| Kritisch | 1 | 001 |
| Hoch | 2 | 002, 003 |
| Mittel | 3 | 004, 007, 008 |
| Niedrig | 4 | 005, 006, 009, 010 |
| Informational | 1 | 011 |
| False Positive | 2 | 012, 013 |
| **Gesamt** | **13** | **11 validiert + 2 False Positives** |

---

## Dokumentationsindex

| Dokument | Zweck |
|----------|---------|
| [EXECUTIVE-SUMMARY.md](EXECUTIVE-SUMMARY.md) | Umfang, Summen, Klassifizierungsaufschlüsselung, Top-5-Prioritäten, Risikoüberblick |
| [RISK-MATRIX.md](RISK-MATRIX.md) | CVSS 4.0 Matrix für alle 13 Feststellungen, Schweregradverteilung, Heatmap-Beschreibung |
| [TEST-ENVIRONMENT.md](TEST-ENVIRONMENT.md) | Lokale Testerklärung, Umgebungdetails, Reproduktionsanleitung, Einschränkungen |
| [DISCLOSURE.md](DISCLOSURE.md) | Offenlegungsrichtlinie, Kontakt, Zeitplan, Erklärung zu nicht anvisierten Produktivsystemen |
| [DOCUMENTATION-QA.md](DOCUMENTATION-QA.md) | Verifikations-Checkliste zu Anforderung 11, Status je Punkt, bekannte Einschränkungen |

---

## Offenlegungserklärung (Zusammenfassung)

Diese Forschung wurde **lokal und schreibgeschützt** durchgeführt. Es wurde kein Produktivsystem, kein Drittanbieterdienst und kein Live-Endpunkt gescannt, angegriffen oder verändert. Feststellungen werden ausschließlich zur defensiven Behebung berichtet.

- **Keine Produktivsysteme anvisiert** — sämtliche Proof-of-Concept-Arbeiten liefen gegen `http://localhost:3000`.
- **Schreibgeschützt** — es wurden keine Quelldateien geändert und im Rahmen der Überprüfung keine Fixes angewendet.
- **Koordinierte Offenlegung** — der Betreiber wird erwartet, Feststellungen vor einer öffentlichen Veröffentlichung zu beheben.

Die vollständige Richtlinie, der Kontakt-Platzhalter und der Zeitplan finden sich in [DISCLOSURE.md](DISCLOSURE.md).

---

## Test & Reproduktion

Die Reproduktion ist so ausgelegt, dass sie vollständig auf einem lokalen Entwicklungsserver läuft:

```bash
npm ci
# serverseitige Umgebungsvariablen konfigurieren (siehe TEST-ENVIRONMENT.md)
npm run dev
# Anwendung verfügbar unter http://localhost:3000
```

Der Proof of Concept jeder Feststellung nutzt ausschließlich `localhost`. Siehe [TEST-ENVIRONMENT.md](TEST-ENVIRONMENT.md) für die vollständige Umgebungsmatrix, die Reproduktionsschritte je Feststellung und die Einschränkungen.

---

## Mitwirken & Korrekturen

Dies ist eine statische Überprüfung des Quellbaums zum referenzierten Commit im Sinne einer Momentaufnahme. Wenn eine Feststellung nach der Behebung nicht mehr reproduzierbar ist oder eine Klassifizierung falsch erscheint, eröffnen Sie bitte ein Issue, das die betroffene Feststellungs-ID, den geprüften Commit und das beobachtete Verhalten beschreibt. Korrekturen sollten die konkrete Quelldatei und Zeile nennen.

---

*Erstellt als deutsche Version der Dokumentation. Alle Feststellungen wurden gegen den Quellbaum validiert; CVSS 4.0-Bewertungen dienen der Priorisierung (siehe Methodik-Hinweis in [RISK-MATRIX.md](RISK-MATRIX.md)).*
