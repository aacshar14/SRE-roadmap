# SRE Culture: Blameless Postmortems

> "You cannot fire your way to reliability."

## The Core Principle
When systems fail, we do **not** look for a person to blame. We assume that:
1.  Everyone had good intentions.
2.  Everyone did the best they could with the information they had.
3.  If a human made a mistake, it is a **system failure** for allowing that mistake to have a catastrophic impact.

## Rules of Engagement
*   **Don't say:** "Engineer X forgot to check the logs."
*   **Do say:** "The deployment pipeline did not enforce a log check."
*   **Don't say:** "Why did you do that?"
*   **Do say:** "What information led to that decision?"

This culture encourages transparency. If people fear punishment, they hide incidents. If they feel safe, they share knowledge, and the system improves.
