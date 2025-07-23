# AWS Cloud Security & Compliance Reference Implementation

A ready-to-deploy, open-source reference for implementing robust security, compliance, and monitoring in AWS cloud environments.

## Features

- High-level cloud security architecture
- Infrastructure as Code (Terraform) for AWS security services
- IAM policies and roles for least-privilege access
- Lambda automation for remediation and reporting
- Best practices and compliance checklist
- Open source (MIT License)

## Hybrid Architecture & Monitoring Stack

This diagram shows both AWS native observability and our open‑source Docker‑based monitoring stack feeding into a unified Grafana UI:

```mermaid
flowchart LR
  subgraph AWS Native
    CW[CloudWatch Metrics & Alarms]
    CT[CloudTrail Logs]
    XR[AWS X-Ray Traces]
    CW --> GrafanaDocker[Grafana]
    CT --> CWLogs[CloudWatch Logs] --> Promtail
    XR --> TempoDocker[Grafana Tempo]
  end

  subgraph Docker Stack
    Prom[Prometheus]
    Loki[Grafana Loki]
    TempoDocker
    GrafanaDocker
    AlertM[Alertmanager]
    Prom --> GrafanaDocker
    Loki --> GrafanaDocker
    TempoDocker --> GrafanaDocker
    Prom --> AlertM
    Loki --> AlertM
  end

  CWLogs --> Loki
  CW --> CloudwatchExporter[cloudwatch-exporter] --> Prom

  subgraph Users & Actions
    User[Users & Services]
    User --> CW
    User --> Promtail
    User --> Prom
    AlertM --> PagerDuty[PagerDuty / Slack]
  end

  classDef aws fill:#f3f4f6,stroke:#999;
  classDef docker fill:#edf2f7,stroke:#555;

  class CW,CT,XR,CloudwatchExporter,CWLogs aws;
  class Prom,Loki,TempoDocker,GrafanaDocker,AlertM docker;
