# 📘 Architecture Skeleton Library  
*A reusable blueprint system for designing tools, agents, engines, and full software architectures.*

This repository defines a **unified architectural schema** that every system can follow — whether it’s a tool ecosystem, an agent, an event bus, an evaluator engine, or a cognitive cycle.

The goal is simple:

> **Make architecture reusable.  
Make system design consistent.  
Make new repos trivial to create.**

This library provides **10 core artifacts** that every architecture should expose, plus example skeletons and diagram templates you can copy into new projects.

---

# 🧱 1. The 10‑Artifact Architecture Schema

Every architecture skeleton in this repo follows the same structure.  
These artifacts form the **minimum viable ontology** for describing any system.

---

## 1. Architecture  
The structural blueprint — the *city map*.

Defines:
- Major subsystems  
- Boundaries  
- Data flow  
- Control flow  
- High‑level diagrams  

This is the heart of the system.

---

## 2. Flows  
The behavioral blueprint — the *movie*.

Defines:
- Request flow  
- Event flow  
- Execution flow  
- Error flow  
- State update flow  

These patterns are the most reusable part of any architecture.

---

## 3. Contracts  
The constitution.

Defines:
- Guarantees  
- Assumptions  
- Invariants  
- Pre/post conditions  

Contracts prevent architectural drift.

---

## 4. Types  
The vocabulary.

Defines:
- Core domain types  
- Shared primitives  
- Enums  
- Identifiers  
- Structural schemas  

This is the dictionary the architecture speaks.

---

## 5. Schemas  
The conceptual ontology.

Defines:
- Entity → State → Event → Evaluation → Decision → Action  
- Cognitive schemas  
- Information schemas  
- Transformation schemas  

This is where architectures become generalizable.

---

## 6. Interfaces  
The plug points.

Defines:
- Tool interface  
- Evaluator interface  
- Router interface  
- State store interface  
- Execution interface  

Interfaces make modules interchangeable.

---

## 7. Dependencies  
The dependency graph.

Defines:
- Allowed dependency directions  
- Forbidden dependency directions  
- Module hierarchy  
- Import rules  

This prevents entropy.

---

## 8. Modules  
The organizational chart.

Defines:
- Module list  
- Ownership  
- Responsibilities  
- Boundaries  

This is the decomposition layer.

---

## 9. DecisionLog  
The architectural memory.

Defines:
- Decisions  
- Alternatives  
- Reasons  
- Dates  

This prevents future confusion.

---

## 10. README  
The elevator pitch.

Defines:
- What is this?  
- Why does it exist?  
- What problem does it solve?  
- What are the major components?  

This is the front door to the repo.

---

# 🗂️ 2. Repository Structure

```
architecture-skeletons/
│
├── README.md
│
├── diagrams/
│   ├── architecture_overview.md
│   ├── artifact_relationships.md
│   └── skeleton_example.png
│
├── skeletons/
│   ├── tool-ecosystem/
│   ├── agent-architecture/
│   ├── event-bus/
│   ├── evaluator-engine/
│   └── cognitive-cycle/
│
└── templates/
    ├── file_tree_template.md
    ├── flow_diagram_template.md
    ├── contract_template.md
    └── schema_template.md
```

Each folder under `skeletons/` contains a **complete empty architecture**, ready to clone.

---

# 🧭 3. How to Use This Repo

### **1. Choose a skeleton**
Pick the architecture pattern closest to what you’re building:
- Tool ecosystem  
- Agent  
- Event bus  
- Evaluator engine  
- Cognitive cycle  

### **2. Copy the folder into your new repo**
This gives you the full 10‑artifact structure instantly.

### **3. Fill in the artifacts**
Start with:
- Architecture.md  
- Flows.md  
- Contracts.md  

Then fill in the rest as the design solidifies.

### **4. Add diagrams**
Use the templates in `/templates` or `/diagrams`.

---

# 🧩 4. Diagram: The Architecture Artifact Stack

```
          ┌──────────────────────┐
          │     Architecture     │
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │        Flows         │
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │       Contracts      │
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │         Types        │
          └──────────┬───────────┘
                     ↓
          ┌──────────────────────┐
          │        Schemas       │
          └──────────────────────┘
```

This shows the **hierarchy of meaning** inside an architecture.

---

# 🧠 5. Philosophy

Architecture is not code.  
Architecture is **information**.

This repo exists to:

- Standardize how architectures are described  
- Make system design reusable  
- Create a shared cognitive language  
- Reduce the cost of starting new systems  
- Preserve architectural intent over time  

This is a **meta‑architecture** — a blueprint for blueprints.

---

# 🧭 6. Next Steps

Which skeleton do you want generated next?

- Tool Ecosystem Skeleton  
- Agent Architecture Skeleton  
- Event Bus Skeleton  
- Evaluator Engine Skeleton  
- Cognitive Cycle Skeleton
