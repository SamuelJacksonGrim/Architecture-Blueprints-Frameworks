# SECURITY — controls by exposure and feature

SELECTOR Step D says when to read this. Take:
- **always**, whenever the system stores data;
- your exposure row and every exposure row before it (local-shared →
  networked → multi-tenant);
- every feature row that applies.

Write them into Contracts as guarantees. A control you skip goes in DecisionLog
with the reason. This is a floor for you, not a menu for the human. Do not ask
them to pick algorithms.

## Exposure

| Row | Controls |
|---|---|
| **always** | Parameterized queries, never string-built. Validate input at the boundary. Secrets from env or a secret store, never in code or logs. Private data never in logs or error messages. Files holding private data created owner-only. |
| **local-shared** | Per-user access checks in the one component that owns the data. No world-readable files. |
| **networked** | Bind 127.0.0.1 during the pass. Public binding and TLS are go-live items for the human (PIPELINE). Check Origin and use CSRF protection on every state-changing request. CSP. CORS closed by default, opened per origin. A single-user local UI uses a random per-launch token, not accounts. |
| **multi-tenant** | Tenant id on every row and every query. Row-level security where the store supports it. Tests proving tenant A cannot read tenant B. Audit log of cross-tenant access. |

## Features

| Row (when it applies) | Controls |
|---|---|
| **accounts** (people log in) | Passwords hashed with Argon2id (bcrypt if unavailable). Server-side sessions in `HttpOnly; Secure; SameSite` cookies (short-lived JWTs only between services). Rate limits on login and reset. MFA offered to any account that controls money or other people's data. |
| **uploads** (accepts files) | Detect type from content, not extension. Size and pixel limits. Random stored names. Store outside the web root and serve through an access check. Anything shown to other people is re-encoded and stripped of location and device metadata. An owner's original that is itself the product (a sold photo, a document) is kept intact apart from location data, and the owner's authorship fields are kept. |
| **protected downloads** (paid or private files) | Random, expiring, revocable links, checked on every request. |
| **money** | Never store card data. Use the processor's hosted flow. "Paid" changes only from signature-verified webhooks, handled idempotently. The amount comes from the server, never the client. One authority owns "paid". The system reacts to money movement and never starts a new kind of it unless the human named it. |
| **encryption at rest** (when asked, or when a law or contract requires it; if unsure, list it for the human) | AES-256-GCM. Key from a passphrase via Argon2id (PBKDF2-SHA256 ≥ 600k iterations if unavailable). A fresh nonce per write. The README says a forgotten passphrase means lost data. |
