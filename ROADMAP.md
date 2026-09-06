# Roadmap – Bokföringsagenten

AI-driven bokföringsassistent för svenska frilansare och konsulter.
Projektet är under aktiv utveckling som en del av min LIA-förberedelse.

## Fas 1 – Grundstruktur (Klar)

 Projektstruktur skapad (src/, tests/, .env)
 Anthropic API-integration uppsatt
 Git-repo med SSH-nyckel kopplat till GitHub
 README med projektbeskrivning

## Fas 2 – Kvittotolkning (Pågår)

Kärnan i demot: ta emot en kvittotext och returnera strukturerad bokföringsinformation.

 Färdigställa analyze_receipt() i src/agent.py
 Returnera BAS-kontokod, momssats och kostnadstyp
 Hantera vanliga kvittokategorier (resor, mat, utrustning m.m.)
 Enkel felhantering vid otydliga kvitton

## Fas 3 – Demo-gränssnitt (Planerad)

Göra agenten körbar utan terminalkännedom.

 CLI-gränssnitt: klistra in kvittotext, få svar direkt
 Alternativ: enkel webbsida med FastAPI + HTML-formulär
 Visa resultat strukturerat (konto, moms, kategori)

## Fas 4 – Utökad funktionalitet (Framtid)

 Stöd för bildkvitton (OCR)
 Bankintegration via Open Banking (Tink / Nordigen)
 Generera VAT-sammanställningar och F-skatt-underlag
 Exportera till SIE-format (kompatibelt med Skatteverket)

## Fas 5 – Driftsättning (Framtid)

 Docker-container
 Kubernetes-deployment (AKS på Azure)
 Stöd för flera användare

### Teknisk stack

Komponent - Val
Språk - Python 3.12
AI-API - Anthropic Claude
Backend - FastAPI (planerad)
Infra - Docker, Kubernetes, Azure AKS
Målmarknad - Svenska frilansare & konsulter
