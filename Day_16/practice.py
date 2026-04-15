'''
The Problem
You are building an Agentic AI pipeline. Your agent has just received a batch of API responses from an LLM. Each response is a dictionary with:

"role" — who sent it ("user" or "assistant")
"content" — the message text
"tokens" — how many tokens the message used
Here is your raw data:
'''

messages = [
    {"role": "user",      "content": "What is RAG?",              "tokens": 12},
    {"role": "assistant", "content": "RAG stands for Retrieval...", "tokens": 85},
    {"role": "user",      "content": "How does it work?",          "tokens": 9},
    {"role": "assistant", "content": "It works by fetching...",    "tokens": 120},
    {"role": "user",      "content": "Give me an example.",        "tokens": 8},
    {"role": "assistant", "content": "Sure! " * 300,               "tokens": 950},
]

'''Your task has two parts:

Part A — Filter the messages: keep only "assistant" messages that used fewer than 200 tokens. Build a list of just their "content" strings.

Part B — Build a summary registry: a dictionary mapping each message's role to its total token count across all messages. Expected output: {"user": 29, "assistant": 1155}'''
# QUE 1: For Part A — what is your input? Describe its type and structure precisely.
#here messages are list of dictionaries
#each individual element inside the list is a dictionary
# each dictionary has 3 key-value pairs
#role, content and token

# QUE 2: For Part A — what is your output? Describe its type and structure precisely.
#ans: we will use list comprehension to filter the messages
# [m["content"]  for m in messages  if m["role"] == "assistant" and m["tokens"] < 200]
#  ─────────────  ────────────────── ──────────────────────────────────────────────────
#  EXTRACT        LOOP OVER          FILTER (both conditions combined)


#QUE 3: What are the two conditions that a message must satisfy to be included in Part A?
#m["role"] == "assistant" and m["tokens"] < 200


#QUE 4: now for Part B:
#look at the expected output:
# {"user": 29, "assistant": 1155}
#You need to build this dictionary. Each key is a role. Each value is the total tokens for that role across all messages.
#What Python tool or technique do you need to compute a running total per group from a list?
#ans: dictionary comprehension with a built one higher order function called sum()