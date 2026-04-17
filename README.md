# python-for-ai

Python from the ground up — built for anyone who wants to learn Python with a focus on AI, Machine Learning, and Agentic AI development.

Each file covers one day of learning, with real code, comments, and exercises. No fluff, just the stuff that matters.

---

## Folder Structure

```
python-for-ai/
├── day_1.py        # Day 1  — print, variables, data types, indentation
├── day_2.py        # Day 2  — mutation vs rebinding, immutability, falsy values, None, is vs ==
├── day_3.py        # Day 3  — lists vs tuples, shallow immutability, interning
├── day_4.py        # Day 4  — hashing, hashable types, why mutables can't be dict keys
├── day_5.py        # Day 5  — sets, no duplicates, membership checks, hashability
├── day_6.py        # Day 6  — dictionaries, control flow (if/elif/else), loops
├── day_7.py        # Day 7  — filtering falsy values, range() basics
├── day_8.py        # Day 8  — break vs continue, nested loops, grid traversal
├── day_9.py        # Day 9  — functions, return vs print, scope, type hints, LEGB rule
├── day_10.py       # Day 10 — closures, the famous loop bug, nonlocal keyword
├── day_11.py       # Day 11 — *args, **kwargs, unpacking with * and **, string immutability
├── day_12.py       # Day 12 — lambda functions, filter(), sorted() with key
├── day_13.py       # Day 13 — first-class functions, HOF practice, message pipelines
├── day_14.py       # Day 14 — logic building, AI agent task manager pipeline
├── day_15.py       # Day 15 — higher-order functions, map, filter, sorted, run_pipeline
├── Day_16/         # Day 16 — list & dictionary comprehensions
│   ├── day_16.py   #          comprehension syntax, filter, transform, nested, dict comp
│   └── practice.py #          Agentic AI pipeline practice, interview questions
├── JOURNAL.md      # Daily notes on what was learned each day
└── README.md       # This file
```

---

## Topics Covered

| Day | Topic | Key Ideas | File |
|-----|-------|-----------|------|
| 1 | Print, Variables, Data Types | `print()`, `int`, `str`, `bool`, indentation, `=` vs `==` | `hello.py` |
| 1 | External Libraries | Using `requests` to call the GitHub API | `hello.py` |
| 2 | Mutation vs Rebinding | `lst.append()` mutates; `lst = [...]` rebinds | `day_2.py` |
| 2 | Immutability | `int`, `float`, `str`, `bool` cannot be changed in-place | `day_2.py` |
| 2 | Falsy Values | `0`, `""`, `[]`, `None` → `False` in boolean context | `day_2.py` |
| 2 | `bool` as a subclass of `int` | `True + 1 == 2`; `bool("False")` is `True` | `day_2.py` |
| 2 | `None` | Represents absence of a value; critical in APIs and AI systems | `day_2.py` |
| 2 | `is` vs `==` | `is` checks identity (same object); `==` checks value | `day_2.py` |
| 2 | Integer & String Interning | Python caches `-5` to `256`; don't rely on `is` for comparisons | `day_2.py` |
| 3 | Lists vs Tuples | Lists are mutable; tuples are immutable and faster | `day_3.py` |
| 3 | Shallow Immutability | Tuple structure is fixed, but mutable items inside it can still change | `day_3.py` |
| 3 | Why Tuples Matter in AI | Hashable, safe as dict keys, good for returning multiple values | `day_3.py` |
| 4 | Hashing | A hash is a fixed number Python uses to find objects quickly | `day_4.py` |
| 4 | Hashable vs Unhashable | `int`, `str`, `tuple` → hashable; `list`, `dict`, `set` → not hashable | `day_4.py` |
| 4 | Dict Keys Must Be Hashable | Using a list as a key raises `TypeError` | `day_4.py` |
| 5 | Sets | Unordered collection of unique, hashable elements | `day_5.py` |
| 5 | Set Methods | `add()`, `remove()`, `in` for fast O(1) membership check | `day_5.py` |
| 5 | `True` vs `1` in Sets | `bool` is a subclass of `int`, so `True` and `1` are the same in a set | `day_5.py` |
| 6 | Dictionaries | Key-value store with fast lookups; keys must be hashable | `day_6.py` |
| 6 | `True`/`1` and `False`/`0` collision | `True == 1` and `False == 0` — they share the same dict slot | `day_6.py` |
| 6 | Control Flow | `if`, `elif`, `else`; falsy values affect which branch runs | `day_6.py` |
| 6 | Loops | `for` loops for known iterations; `while` loops for conditions | `day_6.py` |
| 6 | Infinite Loops | `while True:` used intentionally in backend systems and AI agents | `day_6.py` |
| 6 | `break` and `continue` | `break` exits the loop; `continue` skips the current step | `day_6.py` |
| 7 | Filtering Falsy Values | `if v:` inside a loop skips `0`, `""`, `None` naturally | `day_7.py` |
| 7 | `range()` | `range(stop)`, `range(start, stop)`, `range(start, stop, step)` | `day_7.py` |
| 8 | `break` in Nested Loops | `break` only exits the **inner** loop, not the outer one | `day_8.py` |
| 8 | Grid Traversal | Nested loops for 2D arrays — used in image processing, pathfinding | `day_8.py` |
| 9 | Functions | Named, reusable blocks of code; functions are first-class objects | `day_9.py` |
| 9 | `return` vs `print` | `print` shows output and discards it; `return` sends it back to the caller | `day_9.py` |
| 9 | Default Parameters | `def greet(name, language="English")` — fallback when not provided | `day_9.py` |
| 9 | Mutable Default Argument Bug | `def f(cart=[])` shares the same list across all calls — use `None` instead | `day_9.py` |
| 9 | Type Hints | `: int`, `-> float` for readability; not enforced at runtime | `day_9.py` |
| 9 | Returning Multiple Values | `return name, age` packs a tuple; unpack with `a, b = fn()` | `day_9.py` |
| 9 | Variable Scope & LEGB Rule | Local → Enclosing → Global → Built-in | `day_9.py` |
| 10 | Closures | A nested function that remembers variables from its outer function | `day_10.py` |
| 10 | The Loop Bug | All functions in a loop share the same `i`; fix using default args `def f(x=i)` | `day_10.py` |
| 10 | `nonlocal` keyword | Lets an inner function modify a variable from its enclosing function | `day_10.py` |
| 11 | String Immutability | `str.replace()` returns a new string; you must reassign to keep the change | `day_11.py` |
| 11 | `*args` | Collects any number of positional arguments into a **tuple** | `day_11.py` |
| 11 | `**kwargs` | Collects any number of keyword arguments into a **dictionary** | `day_11.py` |
| 11 | Unpacking with `*` and `**` | `add(*[1,2,3])` unpacks a list; `intro(**info)` unpacks a dict | `day_11.py` |
| 11 | AI Connection | `build_request("gpt-4", temperature=0.7)` — this is exactly how OpenAI/LangChain work | `day_11.py` |
| 12 | Lambda Functions | Small, one-line anonymous functions: `lambda x: x ** 2` | `day_12.py` |
| 12 | Lambda Limitations | Can only have one expression; no loops, no multiple lines, no `return` | `day_12.py` |
| 13 | First-Class Functions | Assign to variables, store in lists, pass as args, return from functions | `day_13.py` |
| 13 | `apply_operation` HOF | One HOF, many behaviors by swapping the function passed in | `day_13.py` |
| 13 | Function Factory | `make_greet(language)` returns a customized greeting function (closure) | `day_13.py` |
| 13 | Message Pipeline | `clean` → `validate` → `add_prefix` using `map()` and `filter()` | `day_13.py` |
| 14 | Logic Building | AI agent task manager — filter, sort, and format a list of task dicts | `day_14.py` |
| 14 | Accumulator Pattern | Loop → append matching items → return new list; precursor to comprehensions | `day_14.py` |
| 14 | `dict.get()` Safe Lookup | `priority_map.get(key, "UNKNOWN")` — returns default instead of `KeyError` | `day_14.py` |
| 15 | Higher-Order Functions | Functions that take or return other functions; foundation of FP | `day_15.py` |
| 15 | Built-in HOFs | `map()`, `filter()`, `sorted()` — all accept functions as arguments | `day_15.py` |
| 15 | `run_pipeline` | HOFs composing HOFs — each stage transforms the output of the previous one | `day_15.py` |
| 16 | List Comprehension | `[expr for item in iterable]` — single-line list building, no `.append()` | `Day_16/day_16.py` |
| 16 | Comprehension Filter | `if` after `for` = filter; `if` before `for` = transform (ternary) | `Day_16/day_16.py` |
| 16 | Nested Comprehension | `[n for row in matrix for n in row]` — flatten nested structures | `Day_16/day_16.py` |
| 16 | Dict Comprehension | `{key: val for item in iterable}` — same idea, builds a dictionary | `Day_16/day_16.py` |
| 16 | Grouping with `.get()` | Running totals per group — can't be replaced by a simple comprehension | `Day_16/practice.py` |

---

## How to Run

Make sure you have Python installed. Then run any file like this:

```bash
python hello.py
python day_12.py
```

To use a virtual environment (already set up in this repo):

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

---

## Goal

Learn Python the right way — not just syntax, but the **why** behind how things work in memory, with a focus on patterns used in real AI systems like LangChain, OpenAI SDK, FastAPI, and Pydantic.

> New topics and files will be added as the learning continues.
