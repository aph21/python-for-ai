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
1. Filters only "pending" tasks # keep taks only where status == "pending"
2. Filters only tasks with priority >= 2 #keeps only tasks where priority >=  2
3. Sorts by priority — highest first #sorts the tasks based on priority in descending order
4. Prints each task in this format:
    [HIGH] Task: <title> → Agent: <assigned>
    [MEDIUM] Task: <title> → Agent: <assigned>

Use your own sample data.
Minimum 6 tasks in your list.
Use functions for every step.
Use the 5-Step Framework before coding.
Plan on paper first.

"""
def filter_pending(tasks):
    pending_tasks = []
    for task in tasks:
        if task["status"] == "pending":
            pending_tasks.append(task)
    return pending_tasks
#this above pattern for filter_pending(tasks) is known as "accumulator pattern" -> means most common / natural way to think about it.ascii
#but in python we have a shorter way to write the exact same logic that is called as list comprehension


def filter_priority(tasks):
    priority_tasks = []
    for task in tasks:
        if task["priority"] >= 2:
            priority_tasks.append(task)
    return priority_tasks

def sort_priority(tasks):
    sorted_tasks = sorted(tasks, key = lambda x:x["priority"], reverse = True)
    return sorted_tasks

def format_task(task):
    priority_map = {
        1 : "LOW",
        2 : "MEDIUM",
        3 : "HIGH"
    }
    priority_label = priority_map.get(task["priority"], "UNKNOWN")
    return f"[{priority_label}] Task: {task['title']} → Agent: {task['assigned']}"

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

# Run the pipeline
step1 = filter_pending(tasks)
step2 = filter_priority(step1)
step3 = sort_priority(step2)

for task in step3:
    print(format_task(task))

