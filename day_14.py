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
