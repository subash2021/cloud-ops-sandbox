# Local Cloud Ops Sandbox: IaC and Monitoring Demo

This project is a fully-containerized, local sandbox environment designed to demonstrate core Cloud Ops and DevOps principles, including Infrastructure as Code (IaC) and Observability.

It provisions a complete monitoring stack (Prometheus & Grafana) to observe a simple Python web application, all defined and managed through code. It's a perfect miniature of how a modern cloud-native application environment is managed.

# To generate traffic, run bash
while true; do curl http://localhost:5000; echo " - Request sent at $(date)"; sleep 2; done

## Architecture

The entire environment is orchestrated by Docker Compose, creating an internal network where services can communicate.

```mermaid
graph TD
    subgraph Your Laptop
        A[User/Traffic Generator] -- HTTP requests --> B{my-app:5000};
    end

    subgraph Docker Network
        B -- Exposes /metrics --> C[Prometheus:9090];
        C -- Scrapes metrics --> B;
        D[Grafana:3000] -- Queries data --> C;
    end

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#9cf,stroke:#333,stroke-width:2px
    style D fill:#9c9,stroke:#333,stroke-width:2px




