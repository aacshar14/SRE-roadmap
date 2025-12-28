# Infrastructure as Code (Terraform)

This module demonstrates SRE best practices for managing infrastructure using Terraform.

## 1. Local Demo (Docker)
Located in `iac/terraform/docker/`. This is for learning concepts without cloud costs.

### Concepts
*   **Providers:** `kreuzwerker/docker`
*   **State:** Local `terraform.tfstate`
*   **Modules:** Best practice separation (`main.tf`, `vars.tf`, `outputs.tf`).

### Usage
1.  Navigate to the folder:
    ```bash
    cd iac/terraform/docker
    ```
2.  Init:
    ```bash
    terraform init
    ```
3.  Plan (See what will change):
    ```bash
    terraform plan
    ```
4.  Apply (Create infrastructure):
    ```bash
    terraform apply
    ```
5.  Access App: `http://localhost:8080`
6.  Cleanup: `terraform destroy`

---

## 2. Cloud Production (Azure)
Located in `iac/terraform/azure/`. This is a production-ready template for deploying an AKS Cluster.

### Prerequisites
*   Azure CLI installed (`az login`).
*   Active Subscription.

### Usage
1.  Navigate to `iac/terraform/azure`.
2.  `terraform init`
3.  `terraform apply` (Will create a Resource Group and AKS Cluster).
