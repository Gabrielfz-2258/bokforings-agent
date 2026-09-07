# Bokforings-agent

An AI-powered bookkeeping assistant for Swedish freelancer and consultant

## About

A demo project that uses the Claude API to interpret receipts, extract key data, and categorize expenses according to Swedish accounting standards (BAS codes and Skatteverket rules).

## Tech Stack

- Python 3.12
- Claude API (Anthropic)
- python-dotenv

## Features

- Receipt interpretation via AI
- Expense categorization using Swedish BAS account codes
- VAT (moms) extraction
- Conversational bookkeeping using Swedish BAS account codes
- Clean web interface

## Run with docker

```bash
docker run -p 8000:000 --env-file .env gabrielfernandez2258/bokforingsagent

## Roadmap

- Bank integration via Open Banking (Tink/Nordigen)
- Multi-user support
- FastAPI backend
- Docker + Kubernetes deployment
