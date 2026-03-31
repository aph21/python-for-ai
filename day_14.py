#LOGIC BUILDING

"""
You are building an AI agent task manager.

You have a list of tasks.
Each task is a dictionary with:
- "title"     : string
- "priority"  : number (1=low, 2=medium, 3=high)
- "status"    : string ("pending" or "done")
- "assigned"  : string (agent name)

Build a pipeline that:
1. Filters only "pending" tasks
2. Filters only tasks with priority >= 2
3. Sorts by priority — highest first
4. Prints each task in this format:
    [HIGH] Task: <title> → Agent: <assigned>
    [MEDIUM] Task: <title> → Agent: <assigned>

Use your own sample data.
Minimum 6 tasks in your list.
Use functions for every step.
Use the 5-Step Framework before coding.
Plan on paper first.

"""


tasks = [
    {
        "title" : "To write up the landing page",
        "priority" : 3,
        "status" : "pending",
        "assigned" : "Claude Sonnet 4.5"
    },
    {
        "title" : "To obtain the API key",
        "priority" : 1,
        "status" : "pending",
        "assigned" : "Gemini 3 Pro"
    },
    {
        "title" : "To set up the database",
        "priority" : 2,
        "status" : "pending",
        "assigned" : "Claude Sonnet 4.5"
    },
    {
        "title" : "To complete the assignment",
        "priority" : 2,
        "status" : "done",
        "assigned" : "Gemini 3 Pro"
    },
    {
        "title" : "To prepare the presentation",
        "priority" : 1,
        "status" : "pending",
        "assigned" : "Ollama"
    },
    {
        "title" : "To set up meeting through Teams",
        "priority" : 3,
        "status" : "pending",
        "assigned" : "OpenAI GPT 5"
    },
    {
        "title" : "To study DSA",
        "priority" : 2,
        "status" : "done",
        "assigned" : "Claude Sonnet 4.5"
    },
    {
        "title" : "To contact the Client through email",
        "priority" : 1,
        "status" : "pending",
        "assigned" : "Claude Opus 4.5"
    },
]

