# SRE & Platform Engineering RACI Matrix

This matrix defines the roles and responsibilities for SRE, Platform Engineering, DevOps, Development, and Cloud Engineering teams, ensuring clarity on who helps build, maintain, and validate the SRE Platform based on core SRE principles.

## Roles Key

*   **R (Responsible):** Those who do the work to achieve the task.
*   **A (Accountable):** The one ultimately answerable for the correct and thorough completion of the deliverable or task.
*   **C (Consulted):** Those whose opinions are sought; two-way communication.
*   **I (Informed):** Those who are kept up-to-date on progress; one-way communication.

## Teams

1.  **SRE:** Site Reliability Engineering.
2.  **Platform:** Platform Engineering (Internal Developer Platform).
3.  **DevOps:** Automation and CI/CD specialists.
4.  **Cloud:** Cloud Infrastructure Engineering.
5.  **Dev:** Product Development Teams.
6.  **Stakeholders:** Business/Tech Leadership.

## RACI Matrix

| Activity | SRE | Platform | DevOps | Cloud | Dev | Stakeholders |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Strategy & Governance** | | | | | | |
| Define SRE Principles & Standards | **A/R** | C | C | I | I | I |
| **Validate Platform alignment with SRE Principles** | **R** | **A** | I | I | I | **I** |
| Define SLO/SLI Standards | **A/R** | I | C | I | C | I |
| | | | | | | |
| **Platform Implementation** | | | | | | |
| Design Internal Developer Platform (IDP) | C | **A/R** | C | C | I | I |
| Implement Platform Features | C | **R** | R | C | I | I |
| Provision Core Infrastructure | I | C | C | **A/R** | I | I |
| Maintain CI/CD Pipelines | C | C | **A/R** | I | I | I |
| | | | | | | |
| **Operations & Reliability** | | | | | | |
| Incident Management (Platform) | **R** | **A** | R | I | I | I |
| Incident Management (Product) | C | I | I | I | **A/R** | I |
| Chaos Engineering | **A/R** | C | I | I | C | I |

### Validation Note
The **SRE Team** is Responsible (R) for validating that the Platform built by **Platform Engineering** (Accountable) adheres to the defined SRE principles. **Stakeholders** are strictly **Informed (I)** of the outcome of this validation to maintain transparency without adding friction to the technical validation process.
