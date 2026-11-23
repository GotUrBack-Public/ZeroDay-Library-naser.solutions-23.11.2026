# Responsible Disclosure

Dieses Dokument legt die Offenlegungsrichtlinie, die Kontaktdaten und den Zeitplan für die in diesem Repository veröffentlichte Sicherheitsforschung dar.

---

## 1. Offenlegungsrichtlinie

Diese Forschung folgt der **koordinierten (verantwortungsvollen) Offenlegung**. Ziel ist es, dem Betreiber eine angemessene Gelegenheit zur Behebung von Feststellungen zu geben, bevor eine öffentliche Veröffentlichung erfolgt.

Grundsätze:

- **Keinen Schaden anrichten.** Tests wurden lokal und schreibgeschützt durchgeführt. Es wurde kein Produktivsystem, kein Drittanbieterdienst und kein Live-Endpunkt gescannt, angegriffen oder verändert.
- **Zuerst privat.** Feststellungen werden dem Betreiber privat mitgeteilt und nicht veröffentlicht, bis die Behebung bestätigt ist oder der Offenlegungszeitplan abläuft.
- **Datenminimierung.** Es werden nur die minimal erforderlichen Belege aufbewahrt, die zum Nachweis einer Feststellung nötig sind. Es sind keine Kundendaten, Zugangsdaten oder Secrets enthalten.
- **Defensiver Zweck.** Feststellungen werden dokumentiert, um Behebung und Härtung zu ermöglichen, nicht um Ausnutzung zu ermöglichen.
- **Guter Glaube.** Keine Erpressung, keine Dienstverschlechterung und kein unbefugter Zugriff auf Daten über das hinaus, was zum Nachweis einer Feststellung erforderlich ist.

---

## 2. Keine Produktivsysteme anvisiert

Diese Forschung hat ausdrücklich **nicht** Produktivsysteme anvisiert:

- **Es wurden keine Produktivsysteme abgerufen, gescannt oder angegriffen.** Sämtliche Proof-of-Concept-Arbeiten liefen gegen einen lokalen Entwicklungsserver unter `http://localhost:3000`.
- **Es wurden keine Drittanbieterdienste belastet.** Es wurde kein Last- oder Missbrauchsverkehr an Vercel, Strato SMTP, thum.io, Microlink oder WordPress mshots gesendet.
- **Es wurden keine Daten exfiltriert oder verändert.** Die Analyse war schreibgeschützt gegen den Quellbaum; es wurden keine Fixes angewendet und keine Kundendaten abgerufen.
- **Deployment-abhängige Feststellungen sind bedingt.** Feststellungen wie das leere `PAYLOAD_SECRET` beschreiben eine Schwachstelle auf Code-Ebene, die nur unter einer bestimmten Fehlkonfiguration auftritt; es wurde nicht versucht, die Produktivkonfiguration zu ermitteln.

---

## 3. Kontaktinformationen

Berichte und Fragen zu dieser Forschung richten Sie bitte an den Sicherheitskontakt des Betreibers:

| Zweck | Kontakt |
|---------|---------|
| Sicherheitsberichte | `security@naser-solutions.de` *(Platzhalter — vor Veröffentlichung durch das überwachte Sicherheits-Postfach ersetzen)* |
| Allgemeiner Kontakt | `info@naser-solutions.de` |
| PGP-Schlüssel | *(Platzhalter — hier den Fingerprint veröffentlichen, falls verschlüsselte Berichte angeboten werden)* |

> Die oben genannten Adressen sind Platzhalter bis zur Bestätigung des überwachten Sicherheitskontakts. Wird ein Bericht an eine Platzhalteradresse gesendet, benachrichtigen Sie den Betreiber zusätzlich über einen bekannten Support-Kanal.

Bitte geben Sie bei einem Bericht an:

- Die Feststellungs-ID (z. B. `001`) und den geprüften Commit oder das Datum.
- Eine Beschreibung des Problems und seiner Auswirkung.
- Schritte zur Reproduktion auf einer lokalen Instanz.
- Vorschläge zur Behebung.

---

## 4. Zeitplan

Der folgende Zeitplan gilt ab dem Datum, an dem der Betreiber einen Bericht bestätigt:

| Phase | Ziel | Anmerkungen |
|-------|--------|-------|
| Bestätigung | Innerhalb von 2 Werktagen | Betreiber bestätigt den Eingang und weist eine Referenznummer zu. |
| Ersteinschätzung | Innerhalb von 7 Tagen | Betreiber bestätigt Gültigkeit und Schweregrad. |
| Behebungsplan | Innerhalb von 30 Tagen | Fixes terminiert; Zeitpläne für komplexe Punkte vereinbart. |
| Behebungs-Deployment | Innerhalb von 90 Tagen | Behebung in Produktion ausgerollt; Verifikation geteilt. |
| Öffentliche Offenlegung | Nach Fix oder 90 Tagen | Veröffentlichung erfolgt, falls ungelöst, mit vermerkten Gegenmaßnahmen. |

Beantragt der Betreiber mehr Zeit für einen komplexen Fix, kann das Offenlegungsdatum durch gegenseitiges Einvernehmen verlängert werden. Kritische Feststellungen (z. B. `001`) sollten so schnell wie möglich behoben werden und werden nicht erwartet, das volle Zeitfenster abzuwarten.

---

## 5. Safe Harbor

In gutem Glauben durchgeführte Sicherheitsforschung unter dieser Richtlinie wird nicht rechtlich verfolgt, sofern sie:

- Die obige Regel zu nicht anvisierten Produktivsystemen einhält.
- Keine Daten über das zum Nachweis einer Feststellung Erforderliche hinaus abruft, verändert oder exfiltriert.
- Den Dienst nicht verschlechtert oder den Betrieb stört.
- Privat über die oben genannten Kanäle berichtet wird.

Diese Safe-Harbor-Erklärung spiegelt die Absicht der Forschung wider und stellt keine Rechtsberatung oder einen verbindlichen Vertrag dar.
