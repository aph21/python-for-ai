Step 1 — What is my input?
A list of models. Each model has name, cost, quality.
→ List of dictionaries

Step 2 — What is my output?
The single best model within budget.
→ One dictionary

Step 3 — What data structure do I need?
Input is already a list of dicts.
No new structure needed.
Just need to filter and sort.

Step 4 — What are the steps?
Step A: Filter models within budget → filter()
Step B: Sort by quality descending → sorted()
Step C: Pick the first one → [0]

Step 5 — Build one step at a time:
First build and test the filter.
Then add the sort.
Then add the [0] pick.


You are building an AI pipeline.
You have a list of raw user messages.

Each message needs to go through these steps:
1. Clean it — strip spaces, lowercase
2. Validate it — reject messages under 3 words
3. Format it — add "User said: " prefix

At the end you should have only
the valid, cleaned, formatted messages.

1) for cleaning -> strip() and lower()
2) for validating -> len(message.split()) >= 3
3) for formatting -> "User said: " + message
