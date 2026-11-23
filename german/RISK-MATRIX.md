# Risikomatrix

CVSS 4.0-Risikomatrix für alle 13 Audit-Feststellungen (11 validiert + 2 False Positives). Bewertungen unterstützen die Priorisierung und die Sequenzierung der Behebung.

> **Methodik-Hinweis.** Die zugrunde liegende Tiefe-Validierungsrunde hat CVSS **3.1**-Basisbewertungen erfasst. Dieses Dokument präsentiert eine äquivalente **CVSS 4.0**-Neubewertung, die zur Priorisierung erstellt wurde; die ursprüngliche 3.1-Bewertung bleibt zur Nachvollziehbarkeit daneben erhalten. CVSS 4.0-Basisbewertungen sollten vor einer externen Veröffentlichung mit einem offiziellen CVSS 4.0-Rechner bestätigt werden. Umgebungs- und zeitliche Metriken sind nicht Gegenstand.

---

## 1. Feststellungsmatrix

| ID | Feststellung | CVSS 4.0-Vektor | Bewertung | Schweregrad | Klasse | CVSS 3.1 (Quelle) |
|----|---------|-----------------|-------|----------|-------|-------------------|
| 001 | Payload Secret leerer Standardwert | `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:N/SC:N/SI:N/SA:N` | **9.3** | Kritisch | BESTÄTIGT | 9.8 |
| 002 | Portal-Login ohne Rate Limiting | `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N` | **8.7** | Hoch | BESTÄTIGT | 7.5 |
| 003 | Ressourcenerschöpfung/Verstärkung bei Thumbnails | `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N` | **8.7** | Hoch | BESTÄTIGT | 7.5 |
| 004 | Kontaktformular ohne Rate Limiting | `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:L/VA:L/SC:N/SI:N/SA:N` | **5.3** | Mittel | BESTÄTIGT | 6.5 |
| 005 | Upload ohne nutzerspezifisches Kontingent | `CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N` | **4.3** | Niedrig | BESTÄTIGT | 4.3 |
| 006 | Session-Cookie mit schwachen Attributen | `CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N` | **2.3** | Niedrig | BESTÄTIGT | 3.7 |
| 007 | Preview-CSRF über GET (Entwurfsmodus) | `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:P/VC:L/VI:L/VA:N/SC:N/SI:N/SA:N` | **5.1** | Mittel | BESTÄTIGT | 5.4 |
| 008 | Portal-JWT ohne Client-Bindung | `CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N` | **5.9** | Mittel | BESTÄTIGT | 5.9 |
| 009 | Lost Update in `saveClientFeedback` | `CVSS:4.0/AV:N/AC:H/AT:P/PR:L/UI:N/VC:N/VI:L/VA:N/SC:N/SI:N/SA:N` | **2.7** | Niedrig | INFORMATIONAL | 2.7 |
| 010 | `cmsOrigins` bedingungslose Allowlist | `CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N` | **3.1** | Niedrig | INFORMATIONAL | 3.1 |
| 011 | Fehlende Sicherheitsheader | `CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:N/VI:N/VA:N/SC:N/SI:N/SA:N` | **0.0** | Informational | INFORMATIONAL | 0.0 |
| 012 | E-Mail-Header-Injection | — (kein Vektor) | **0.0** | False Positive | FALSE POSITIVE | — |
| 013 | Aufzählung von Entwurfsseiten | — (kein Vektor) | **0.0** | False Positive | FALSE POSITIVE | — |

**Legende der CVSS 4.0-Metriken:** `AV` Attack Vector, `AC` Attack Complexity, `AT` Attack Requirements, `PR` Privileges Required, `UI` User Interaction, `VC/VI/VA` Vulnerable Confidentiality/Integrity/Availability, `SC/SI/SA` Subsequent Confidentiality/Integrity/Availability. `N/P` = None/Physical, `L/H` = Low/High, `P` = Passive.

---

## 2. Schweregradverteilung

| Schweregrad | Anzahl | Anteil (von 13) | Feststellungen |
|----------|-------|---------------|----------|
| Kritisch | 1 | 7.7% | 001 |
| Hoch | 2 | 15.4% | 002, 003 |
| Mittel | 3 | 23.1% | 004, 007, 008 |
| Niedrig | 4 | 30.8% | 005, 006, 009, 010 |
| Informational | 1 | 7.7% | 011 |
| False Positive | 2 | 15.4% | 012, 013 |
| **Gesamt** | **13** | **100%** | |

**Validierte Feststellungen nach Schweregrad (11 insgesamt):** Kritisch 1 · Hoch 2 · Mittel 3 · Niedrig 4 · Informational 1.

---

## 3. Risiko-Heatmap

Die Heatmap stellt jede validierte Feststellung nach **Auswirkung** (vertikal) gegen **Wahrscheinlichkeit / Ausnutzbarkeit** (horizontal) dar. False Positives (012, 013) werden ausgeschlossen, da sie kein Restrisiko tragen.

```
AUSWIRKUNG
  Hoch │  006       001
       │             002
       │                    003
       │              008
  Mit  │                    004
       │                    007
       │  009  010
  Nied │  005
       │              011
       └────────────────────────────────────────
          Niedrig     Mittel      Hoch     WAHRSCHEINLICHKEIT
```

| Zone | Feststellungen | Interpretation |
|------|----------|----------------|
| **Kritisch (hohe Auswirkung, hohe Wahrscheinlichkeit)** | 001 | Sofort beheben; trivialer Aufwand, maximale Risikoreduktion. |
| **Hoch (hohe Auswirkung, mittlere/hohe Wahrscheinlichkeit)** | 002, 003 | Öffentlich erreichbar ohne Rate Limiting; als Nächstes priorisieren. |
| **Mittel (mittlere Auswirkung, mittlere Wahrscheinlichkeit)** | 004, 007, 008 | Im aktuellen Behebungszyklus adressieren. |
| **Niedrig / Härtung** | 005, 006, 009, 010, 011 | Als Defense-in-Depth einplanen; geringe Dringlichkeit. |
| **Kein Restrisiko** | 012, 013 | Keine Maßnahme; False Positives. |

**Die Karte lesen:** Feststellung 001 steht allein in der oberen rechten kritischen Zone — hohe Auswirkung (vollständige Authentifizierungsumgehung bei Fehlkonfiguration) und hohe Wahrscheinlichkeit (eine fehlende Umgebungsvariable ist ein realistischer Deployment-Fehler, und der Fix ist trivial). Die Feststellungen 002 und 003 sind wirkungsstark und leicht erreichbar, weil ihre Endpunkte öffentlich und ungedrosselt sind. Der Cluster in der unteren rechten Ecke spiegelt Härtungslücken wider: real, aber eingeschränkt durch Authentifizierung, Origin-Prüfungen oder Konfigurations-Voraussetzungen.

---

## 4. Anmerkungen je Feststellung

- **001 — Payload Secret leerer Standardwert (9.3).** Die Auswirkung setzt voraus, dass `PAYLOAD_SECRET` nicht gesetzt ist; ist die Variable korrekt gesetzt, ist das Restrisiko vernachlässigbar. Die Bewertung spiegelt den Worst-Case-Fehlkonfiguration wider.
- **002 — Portal-Login ohne Rate Limiting (8.7).** Auswirkung nur auf Vertraulichkeit; Integrität und Verfügbarkeit bleiben unberührt. Das praktische Risiko hängt von der Passwortrichtlinie und der Verfügbarkeit von Credential-Stuffing-Listen ab.
- **003 — Ressourcenerschöpfung/Verstärkung bei Thumbnails (8.7).** Verfügbarkeitsgetrieben (Funktionsminuten, Bandbreite, Anbieter-Kontingente) zuzüglich Risiko des Proxy-Missbrauchs/Reputationsschadens.
- **004 — Kontaktformular ohne Rate Limiting (5.3).** Geringe Integritäts-/Verfügbarkeitsauswirkung; realer Schaden ist Postfach-Flutung und SMTP-Konto-Drosselung.
- **005 — Upload ohne nutzerspezifisches Kontingent (4.3).** Eingeschränkt durch Authentifizierung und eine projektbezogene Obergrenze; primäre Auswirkung sind Kosten für verwaiste Blobs.
- **006 — Session-Cookie mit schwachen Attributen (2.3).** Hohe Angriffs-Komplexität (erfordert einen Nicht-Produktions-Kontext oder eine Netzwerkposition); im Produktivbetrieb wird `secure` gesetzt.
- **007 — Preview-CSRF über GET (5.1).** Erfordert ein authentifiziertes Admin-/Editor-Opfer und Benutzerinteraktion; der Angreifer kann Entwurfsinhalte nicht direkt lesen.
- **008 — Portal-JWT ohne Client-Bindung (5.9).** Hohe Vertraulichkeitsauswirkung nach Token-Diebstahl; hohe Komplexität, da der Diebstahl einen zweiten Vektor erfordert (`httpOnly` blockiert direkten XSS-Diebstahl).
- **009 — Lost Update in `saveClientFeedback` (2.7).** Datenintegritätsproblem, kein direkter Sicherheitsverstoß; erfordert präzises Timing.
- **010 — `cmsOrigins` bedingungslose Allowlist (3.1).** Erfordert die Kontrolle über eine Deployment-Umgebungsvariable zuzüglich einer Opfersitzung.
- **011 — Fehlende Sicherheitsheader (0.0).** Kein direkter Exploit-Vektor; Defense-in-Depth-Lücke.
- **012 — E-Mail-Header-Injection (0.0).** Widerlegt: Nodemailer bereinigt Header-Werte.
- **013 — Aufzählung von Entwurfsseiten (0.0).** Widerlegt: Payload-Zugriffskontrolle und Mitarbeiter-Beschränkung der Preview verhindern dies.
