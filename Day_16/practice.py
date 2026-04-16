"""
The Problem
You are building an Agentic AI pipeline. Your agent has just received a batch of API responses from an LLM. Each response is a dictionary with:

"role" — who sent it ("user" or "assistant")
"content" — the message text
"tokens" — how many tokens the message used
Here is your raw data:
"""

"""Your task has two parts:

Part A — Filter the messages: keep only "assistant" messages that used fewer than 200 tokens. Build a list of just their "content" strings.

Part B — Build a summary registry: a dictionary mapping each message's role to its total token count across all messages. Expected output: {"user": 29, "assistant": 1155}"""
# QUE 1: For Part A — what is your input? Describe its type and structure precisely.
# here messages are list of dictionaries
# each individual element inside the list is a dictionary
# each dictionary has 3 key-value pairs
# role, content and token

# QUE 2: For Part A — what is your output? Describe its type and structure precisely.
# ans: we will use list comprehension to filter the messages
# [m["content"]  for m in messages  if m["role"] == "assistant" and m["tokens"] < 200]
#  ─────────────  ────────────────── ──────────────────────────────────────────────────
#  EXTRACT        LOOP OVER          FILTER (both conditions combined)


# QUE 3: What are the two conditions that a message must satisfy to be included in Part A?
# m["role"] == "assistant" and m["tokens"] < 200


# QUE 4: now for Part B:
# look at the expected output:
# {"user": 29, "assistant": 1155}
# You need to build this dictionary. Each key is a role. Each value is the total tokens for that role across all messages.
# What Python tool or technique do you need to compute a running total per group from a list?
# ans: dictionary comprehension with a built one higher order function called sum()

messages = [
    {"role": "user", "content": "What is RAG?", "tokens": 12},
    {"role": "assistant", "content": "RAG stands for Retrieval...", "tokens": 85},
    {"role": "user", "content": "How does it work?", "tokens": 9},
    {"role": "assistant", "content": "It works by fetching...", "tokens": 120},
    {"role": "user", "content": "Give me an example.", "tokens": 8},
    {"role": "assistant", "content": "Sure! " * 300, "tokens": 950},
]
#PART A : Filter the messages: keep only "assistant" messages that used fewer than 200 tokens. Build a list of just their "content" strings.
assistant_responses = [
    m["content"] for m in messages if m["role"] == "assistant" and m["tokens"] < 200
] # what is m here? -> m is the variable that represents each individual elemnt in the list 'messages'
# m["content"] -> it is an expression that we want to extract from the list 'messages' if following condition is met
# if m["role"] == "assistant" and m["tokens"] < 200 -> it is a filter that we want to apply to the list 'messages' 
print(assistant_responses)

#Part B — Build a summary registry: a dictionary mapping each message's role to its total token count across all messages. Expected output: {"user": 29, "assistant": 1155}
result = {}
for m in messages:
    result[m["role"]] = result.get(m["role"], 0) + m["tokens"]
print(result)
# output: {'user': 29, 'assistant': 1155}
# How? -> 
# result.get(m["role"], 0) -> it is used to get the value of the key m["role"] from the dictionary result
# if the key is not found then it will return 0
# m["tokens"] -> it is the value that we want to add to the key m["role"]
# result[m["role"]] = ... -> it is used to update the value of the key m["role"] in the dictionary result
#===========================================================




#PRACTICE 2
logs = [
    {"tool": "search",    "status": "success", "latency_ms": 120},
    {"tool": "summarize", "status": "error",   "latency_ms": 340},
    {"tool": "search",    "status": "success", "latency_ms": 95},
    {"tool": "classify",  "status": "success", "latency_ms": 210},
    {"tool": "summarize", "status": "success", "latency_ms": 180},
    {"tool": "search",    "status": "error",   "latency_ms": 500},
]
#Task 1: Using a list comprehension, extract the latency_ms values of all logs where status == "success". Name it successful_latencies.

successful_latencies: list[int] = [log["latency_ms"] for log in logs if log["status"] == "success"] # log is the variable that represents each individual elemnt in the list 'logs'
# log["latency_ms"] -> it is an expression that we want to extract from the list 'logs' if following condition is met
# if log["status"] == "success" -> it is a filter that we want to apply to the list 'logs' 
print(successful_latencies)
# output: [120, 95, 210, 180]

#Task 2: Using a list comprehension, build a list of strings in this format: "search → 120ms" — for every log entry regardless of status. Name it log_labels.
log_labels : list[str] = [f"{log['tool']} → {log['latency_ms']}ms" for log in logs] # log is the variable that represents each individual elemnt in the list 'logs'
# f"{log['tool']} → {log['latency_ms']}ms" -> it is an expression that we want to extract from the list 'logs'
print(log_labels)
# output: ['search → 120ms', 'summarize → 340ms', 'search → 95ms', 'classify → 210ms', 'summarize → 180ms', 'search → 500ms']

#Task 3: Using a loop with .get(), build a dict that maps each tool name to its total latency across all calls. Name it tool_latency_total.
tool_latency_total = {}
for log in logs:
    tool_latency_total[log["tool"]] = tool_latency_total.get(log["tool"], 0) + log["latency_ms"]
print(tool_latency_total)
# output: {'search': 715, 'summarize': 520, 'classify': 210}
# How? -> 
# tool_latency_total.get(log["tool"], 0) -> it is used to get the value of the key log["tool"] from the dictionary tool_latency_total
# if the key is not found then it will return 0
# log["latency_ms"] -> it is the value that we want to add to the key log["tool"]
# tool_latency_total[log["tool"]] = ... -> it is used to update the value of the key log["tool"] in the dictionary tool_latency_total
#===========================================================


#Rules:
#Type hints on every variable
#f-strings where strings are built
#One comment per line explaining what it does
#print() each result