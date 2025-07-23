# AWS Cloud Security & Compliance Reference Implementation

A ready-to-deploy, open-source reference for implementing robust security, compliance, and monitoring in AWS cloud environments.

## Features

- High-level cloud security architecture
- Infrastructure as Code (Terraform) for AWS security services
- IAM policies and roles for least-privilege access
- Lambda automation for remediation and reporting
- Best practices and compliance checklist
- Open source (MIT License)

## High-Level Architecture

```mermaid
graph TD
    subgraph User Access Layer
        A1[User Devices]
        A2[Admin Console]
        A3[SSO/Identity Provider]
    end

    subgraph Network Layer
        B1[AWS VPC]
        B2[AWS Security Groups / NACLs]
        B3[AWS Network Firewall]
    end

    subgraph Security Services
        C1[Amazon GuardDuty (IDS)]
        C2[AWS CloudTrail (Audit Logs)]
        C3[AWS Config (Compliance Monitoring)]
        C4[AWS Security Hub (Aggregation)]
        C5[Third-Party IDS/IPS (Optional)]
    end

    subgraph Compute & Data Layer
        D1[EC2 Instances]
        D2[RDS / Databases]
        D3[S3 Buckets]
        D4[Lambda Functions]
    end

    subgraph Management & Monitoring
        E1[AWS IAM]
        E2[AWS KMS (Encryption)]
        E3[CloudWatch (Monitoring/Alarms)]
        E4[AWS Systems Manager]
        E5[SNS (Alerting)]
    end

    %% User access flows
    A1 --> A3
    A2 --> A3
    A3 --> E1
    E1 --> B1

    %% Traffic flow through network
    A1 --> B2
    B2 --> B3
    B3 --> D1
    B3 --> D2
    B3 --> D3
    B3 --> D4

    %% Security services connections
    B1 --> C1
    B1 --> C5
    B1 --> C2
    B1 --> C3
    B1 --> C4

    %% Compute/data monitored and protected
    D1 --> E3
    D2 --> E3
    D3 --> E3
    D4 --> E3

    D1 --> E2
    D2 --> E2
    D3 --> E2

    %% Compliance and auditing
    C2 --> C4
    C3 --> C4

    %% Alerting and management
    C1 --> E5
    C4 --> E5
    E3 --> E5

    %% Automation and remediation
    C4 --> E4
    E4 --> D1
    E4 --> D2
    E4 --> D3
    E4 --> D4
```
## CI/CD with GitHub Actions

This project includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) to automate Terraform deployment:
- **validate**: Checks Terraform format and validates configuration.
- **plan**: Generates and uploads a plan artifact.
- **apply**: Applies the plan on `main` branch after manual `/apply` approval.

Configure AWS credentials in your repository **Settings → Secrets** (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
