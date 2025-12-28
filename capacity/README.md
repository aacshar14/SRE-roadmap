# Capacity Planning

Capacity planning is the process of determining the resources needed to meet future demand.

## Core Concepts
1.  **Organic Growth:** Natural increase in usage (e.g., more users signing up).
2.  **Inorganic Growth:** Spikes due to events (e.g., Marketing launch, Black Friday).
3.  **Headroom:** The safety buffer (usually +20-30%) kept available.

## The Formula
A basic formula for estimation:
`Required Cores = (Requests Per Second * Latency per Request) + Headroom`

## Resources
*   [Worksheet Template](./worksheet.md) - Use this to calculate your needs.
