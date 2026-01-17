# Aura Protocol (Core Engine) — Iron Core

**Sovereign implementation of the Proof of Consistent Agency (PoCA) for the 2026 Polish AI Regulatory Sandbox.**

Deterministic Proof-of-Consistency (PoCA) Core  
with Cryptographic Audit & Compliance Outputs

---

## Compliance Mapping (EU AI Act)

| Requirement | Implementation | Component |
|---|---|---|
| **Art. 5 Safeguard** | Prohibition of human evaluation via hard assertions. | `core/policy.py` |
| **Art. 13 Transparency** | Merkle-hashed audit trails and Event Trust Certificates (ETC). | `audit/merkle.py` |
| **Art. 14 Oversight** | Mandatory manual emergency halt (Kill-Switch). | `core/policy.py` |

---

## Technical Stack

* **Logic**: Python 3.10+ (Type-hinted, Deterministic)
* **Database**: PostgreSQL + pgvector (Local-First)
* **Structure**: Modular Monolith (pnpm/Turborepo)
* **License**: Business Source License 1.1 (BSL 1.1)

---

## Initialization

### Prerequisites

* Ensure **Docker** is running.

### Quick Start

```bash
docker-compose up -d
```

The **ARI Evaluator** is now ready for sterilized algorithmic auditing.

### Verify Setup

```bash
# Check PostgreSQL + pgvector is running
docker-compose ps

# Connect to database (optional)
docker exec -it aura-postgres psql -U aura -d aura_core
```

---

## Overview

**aura-poc-a-core** is a minimal, deterministic core for evaluating and proving
the consistency of autonomous agents (human or AI) against their declared intent
and hard constraints.

This repository implements the *foundational execution layer* only.

No UX.  
No tokens.  
No narratives.

Only verifiable logic.

---

## What This Is

A **Proof-of-Consistent-Agency (PoCA)** engine that:

- deterministically evaluates agent actions
- detects semantic drift from declared intent
- produces cryptographically verifiable audit artifacts
- generates compliance-ready outputs (AI Act–oriented)

---

## What This Is NOT

Out of scope by design:

- ❌ UI / dashboards
- ❌ wallets / tokens / blockchain protocols
- ❌ monetization logic
- ❌ identity issuance
- ❌ orchestration layers
- ❌ hype abstractions

This repo is a **core primitive**, not a product.

---

## Core Components

### `/core`
Deterministic execution layer.

Responsibilities:
- Structural integrity validation
- Semantic alignment scoring
- Policy enforcement (Art. 5: Algorithmic-only evaluation)
- Kill-Switch oversight (Art. 14: Manual emergency halt)
- Consistency score calculation (PoCA)

Output:
- Numeric consistency score ∈ [0.0 – 1.0]
- Drift signal
- Deterministic metadata

---

### `/audit`
Cryptographic audit layer.

Responsibilities:
- Merkle tree construction
- Event Trust Certificate (ETC) generation (Art. 13)
- Immutable event anchoring
- Proof-of-existence generation
- Non-repudiation support

Output:
- Merkle root
- Per-event Merkle proofs
- Event Trust Certificates (ETC)
- Verifiable audit artifacts

---

### `/compliance`
Compliance certification layer.

Responsibilities:
- Certificate generation
- Schema validation
- Regulatory output formatting

Output:
- Aura Event Certificates
- Compliance-ready JSON artifacts

---

### `/docs`
Specification & intent layer.

Responsibilities:
- System assumptions
- Threat model
- Determinism constraints
- Regulatory mapping (e.g. AI Act transparency)

---

## Determinism Guarantee

This system is designed to be:

- deterministic by construction
- reproducible across environments
- auditable without privileged access
- explainable via cryptographic proofs, not narratives

Same input → same output.  
No hidden state.  
No stochastic execution paths.

---

## Compliance Orientation

Designed with:
- **AI Act (Art. 13)** – transparency & traceability via Merkle audit trails
- **AI Act (Art. 5)** – prohibition of human evaluation (algorithmic assertions)
- **AI Act (Art. 14)** – human oversight via mandatory Kill-Switch
- audit-first architecture
- privacy-preserving verification (Merkle proofs)
- regulator-facing evidence generation

This is **Law-as-Code**, not post-hoc reporting.

---

## Project Status

**Status:** Research-backed prototype  
**Phase:** Core implementation  
**Stability:** Interfaces subject to refinement, logic is fixed

---

## License

MIT  
(New codebase. No code continuity with archived repositories.)

---

## Guiding Principle

> Trust is not asserted.  
> Trust is computed — and proven.
