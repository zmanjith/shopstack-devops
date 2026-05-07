# ShopStack DevOps

DevOps repository for **ShopStack** — an e-commerce platform modernization effort focused on **migrating from a monolithic application to microservices** and delivering a production-grade, cost-aware platform on **AWS + Kubernetes**.

---

## Architecture (Priority)

### High-level overview

- **Platform goal:** Break down a monolith into independently deployable **microservices** with updated service layers and modern delivery practices.
- **Runtime:** **Kubernetes** (on **AWS**)
- **GitOps delivery:** **Argo CD** (sync from Git)
- **CI:** **GitHub Actions**
- **Data layer:** **Amazon DynamoDB**
- **Observability:** **Prometheus**
- **Non-functional priorities:** **Cost optimization** and **autoscaling**

### Component map

- **Microservices (service layer split)**
  - Multiple independently deployable services (migrated from the monolith)
  - Containerized workloads deployed to Kubernetes
- **Kubernetes (AWS)**
  - Deployments/Services/Ingress (as applicable)
  - Autoscaling (HPA / cluster autoscaler depending on setup)
- **Database**
  - **DynamoDB** as the primary datastore for services
- **CI/CD**
  - **GitHub Actions** for build/test/package
  - **Argo CD** for GitOps-based continuous delivery into Kubernetes
- **Observability**
  - **Prometheus** for metrics scraping/alerting foundation

### Delivery flow (CI → GitOps CD)

1. Developer pushes changes to GitHub.
2. **GitHub Actions** runs CI (lint/test/build) and produces deployable artifacts (e.g., container images/manifests).
3. Kubernetes manifests (or Helm/Kustomize overlays, depending on repo structure) are updated in Git.
4. **Argo CD** detects changes and reconciles the desired state into the **AWS-hosted Kubernetes** cluster.
5. **Prometheus** monitors service and cluster metrics; autoscaling policies help meet demand while maintaining cost targets.

---

## Repository scope

This repo is intended to hold DevOps/platform assets for ShopStack, such as:

- Kubernetes manifests / Helm charts / Kustomize overlays (whichever is used)
- GitHub Actions workflows
- Argo CD application definitions
- Observability configuration (Prometheus rules/scrape configs, etc.)
- Platform documentation and runbooks

> If you’d like, I can further tailor this section once the repo structure (folders like `k8s/`, `helm/`, `.github/workflows/`, `argocd/`, etc.) is finalized.

---

## Resume-ready project summary

**ShopStack DevOps (AWS, Kubernetes, GitHub Actions, Argo CD, DynamoDB, Prometheus)**

- Led/implemented the **migration strategy from a monolithic application to microservices**, enabling independent deployments and faster release cycles.
- Built CI pipelines with **GitHub Actions** and implemented **GitOps continuous delivery via Argo CD** to reliably deploy microservices to **Kubernetes on AWS**.
- Established **Prometheus-based observability** to monitor service and cluster health, supporting data-driven operations.
- Implemented **autoscaling** and **cost-focused optimizations** to balance performance and cloud spend in production-like environments.

---

## Next improvements (optional)

- Add an architecture diagram (Mermaid) once service names and traffic paths (Ingress/API Gateway, service-to-service calls) are confirmed.
- Document environments (dev/stage/prod), branching strategy, and promotion flow.
- Add runbooks: deploy/rollback steps, incident checklist, and cost-optimization guidelines.
