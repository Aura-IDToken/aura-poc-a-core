# Aura Protocol: Iron Core (Sandbox Minimal)
Deterministic Proof-of-Consistent-Agency (PoCA) for the 2026 AI Regulatory Sandbox.

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
- Policy enforcement
- Consistency score calculation (PoCA)

Output:
- Numeric consistency score ∈ [0.0 – 1.0]
- Drift signal
- Deterministic metadata

---

### `/compliance`
Cryptographic audit layer.

Responsibilities:
- Merkle tree construction
- Immutable event anchoring
- Proof-of-existence generation
- Non-repudiation support

Output:
- Merkle root
- Per-event Merkle proofs
- Verifiable audit artifacts

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
- AI Act (Art. 13 – transparency & traceability)
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
