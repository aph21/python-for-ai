# Learning Journal

## Day 1 - 2026-02-23
- Set up repo and virtual environment
- First `print()` statements
- **Variables** — named references to objects in memory
- Python is dynamically typed; values determine types
- `=` is assignment, `==` is equality
- **Indentation** is syntax, not style — wrong indentation crashes the program
- Used `requests` library to call the GitHub API

## Day 2 - 2026-02-24
- **Comments** — `#` for single-line; triple quotes for multiline string literals
- **Mutation vs Rebinding** — `lst.append()` mutates the original; `lst = [...]` rebinds the local name only
- **Mutable shared references** — two names pointing to the same list see each other's mutations
- **Passing mutables to functions** — function receives a reference; mutation affects caller, rebinding does not
- **Everything is an object** — each value has a type, methods, and immutability rules
- **`type()` and `isinstance()`** — `type()` returns exact class; `isinstance()` checks inheritance chain
- **Immutability** — `int`, `float`, `str`, `bool` can't be mutated; operations create new objects
- **Falsy values** — `0`, `""`, `[]`, `None` → `False`; everything else → `True`
- **`bool` is a subclass of `int`** — `True + 1 = 2`; `bool("False")` is `True` (non-empty string)
- **First functions** using `def`

## Day 3 - 2026-02-25
- **`None`** — a singleton representing the absence of a value (`NoneType`); not the same as `False` or `0`
- **`None` in production** — critical in API responses (missing fields) and optional parameters in LLM/backend systems
- **`None == False` is `False`** — None means "no value", False means falsehood; they are distinct concepts
- **`is` vs `==`** — `is` checks identity (same object in memory); `==` checks value equality
- **Integer interning** — Python caches integers −5 to 256; `a is b` is `True` for cached range, unreliable outside it
- **String interning** — Python interns short strings and identifiers; unreliable for longer or dynamic strings
- **When to use `is`** — only for `None`, `True`/`False`, or intentional identity checks
- **Never use `is` for numeric/string comparison** — interning behavior is implementation-dependent; always use `==` for values
- **Reassignment vs Mutation** — `a = [4,5,6]` rebinds `a` to a new list (old reference `b` is unaffected); `a.append(4)` mutates the shared object (both `a` and `b` see the change)
- **List (mutable sequence)** — supports `append`, `insert`, `remove`; designed for dynamic resizing with extra space pre-allocated
- **Tuple (immutable sequence)** — no mutation methods; fixed size, more memory-efficient, and faster than lists
- **Why tuples matter in Backend/AI systems** — immutable config = safety; hashable so usable as dictionary keys (lists are not); functions return multiple values as tuples; better performance for large datasets
- **Shallow immutability** — a tuple's structure is immutable, but mutable objects inside it (e.g. a list) can still be modified: `(1, 2, [3, 4])` → appending to the inner list works, but reassigning the slot (`t[2] = ...`) raises `TypeError`
- **Tuple identity & interning** — CPython may intern small tuple literals in the same code block, so `a is b` might be `True`; never rely on this — always use `==` for value comparison

## Day 4 - 2026-02-27
- **Hashing** — a hash is a number Python makes from an object to store and find it fast
- **Hashable** — an object is hashable if its hash never changes; simple test: can it be a dict key?
- **Mutability breaks hashing** — if a key changes, its hash changes, and the dict can't find it anymore
- **Lists can't be keys** — `{[1,2]: "val"}` raises `TypeError` because lists are mutable
- **Tuples can be keys** — they're immutable so the hash stays the same
- **Tuple caveat** — a tuple is hashable only if everything inside it is too; `(1, 2, [3])` crashes

## Day 5 - 2026-03-04
- **Sets** — a collection of unique elements; unordered and mutable; uses hashing internally for storage
- **Creating sets** — `set()` for empty set (not `{}`), `{1, 2, 3}` with literals, or `set([1, 2, 3])` from a list
- **No duplicates** — `{1, 1, 2, 6, 6}` becomes `{1, 2, 6}`; duplicates are silently ignored on add
- **Unordered** — elements have no guaranteed order; sets optimize for fast lookup, not sequence
- **Only hashable elements** — ints, strings, tuples work; lists inside a set raise `TypeError`
- **`add()` and `remove()`** — `add()` inserts an element (no-op if duplicate); `remove()` deletes or raises `KeyError` if missing
- **Membership check (`in`)** — `2 in s` is O(1) on average because sets use hash-table lookup, not linear scan
- **Tuples in sets** — `(1, 2)` is hashable so it can be added; `(1, 2, [3])` is not because the inner list is unhashable
- **Duplicate detection via hashing** — adding `(1, 2)` twice keeps `len(s)` at 1; Python compares hash first, then checks equality
- **`True` vs `1` in sets** — `bool` is a subclass of `int`; `True == 1` so `{1, 2, 3}.add(True)` changes nothing — `True` is already "present" as `1`

## Day 6 - 2026-03-05
- Learnt what a **dictionary** is — stores key-value pairs, like a hash map
- Created my first dict: `{"name": "Anjana", "age": 24, "role": "AI Engineer"}`
- Dict keys must be **hashable** and **unique**; values can be anything
- Dicts are **mutable** and give **fast lookups**
- Discovered that `True` and `1` collide as dict keys — `d[1]` and `d[True]` point to the same slot because `True == 1` and `hash(True) == hash(1)`
- Same thing with `False` and `0` — the first key name sticks, but the value gets overwritten
- Lists can't be dict keys (`TypeError: unhashable type: 'list'`), but tuples can
- Reviewed the hashability table — `int`, `float`, `str`, `bool`, `tuple` are hashable; `list`, `set`, `dict` are not
- Started **control flow** (`if` / `elif` / `else`)
- `0` is falsy, so `if 0:` goes straight to `else`
- An empty list `[]` is falsy too, but `x == []` is `True` — the `elif` catches it
- `None` is falsy; `x == None` matches before `x is None` even gets checked — first matching branch wins

## Day 7 - 2026-03-06
- **Filtering falsy values** — looping with `if v:` naturally skips `0`, `""`, and `None`; useful for cleaning lists
- **`range()` function** — generates a sequence of numbers; returns a lazy range object, not a list
- `range(stop)` — numbers from `0` to `stop-1`; e.g. `range(5)` → `0, 1, 2, 3, 4`
- `range(start, stop)` — numbers from `start` to `stop-1`; e.g. `range(2, 5)` → `2, 3, 4`
- `range(start, stop, step)` — numbers with a custom step; e.g. `range(0, 10, 2)` → `0, 2, 4, 6, 8`
- **`range()` in for loops** — the most common pattern to repeat something N times: `for i in range(5):`
- Wrap `range()` in `list()` to see all values at once — `list(range(5))` → `[0, 1, 2, 3, 4]`

## Day 8 - 2026-03-06
- **`range()` returns a range object, not a list** — use `list(range(2,6))` to see `[2, 3, 4, 5]`; stop value is exclusive
- **`break` vs `continue`** — `break` exits the loop permanently; `continue` skips the current iteration and moves to the next
- **`break`** is for stopping early (task done); **`continue`** is for skipping bad data
- Combined example — `continue` at `i==2` skips printing 2; `break` at `i==4` stops the loop; output: `0, 1, 3`
- **Nested loops** — a loop inside another loop; outer loop controls rows, inner loop runs completely for each outer iteration
- **Multiplication table** with nested `range(1,4)` — prints a 3x3 grid of products
- **Grid traversal** — nested loops over rows and columns; used in 2D arrays, pathfinding, image processing
- **`break` in nested loops** — `break` only stops the **inner** loop, not the outer one
- Inner loop runs fully for each outer iteration **unless** interrupted by `break`, `return`, or an exception
- **Total prints calculation** — outer iterations × inner iterations (minus skips/breaks) gives the count

## Day 9 - 2026-03-07
- **Functions** — named, reusable blocks of code that take input, do something, and optionally return output
- **First-class objects** — functions in Python are values; can be stored in lists, assigned to variables, passed as arguments, and returned from other functions
- **Parameters** — variables that only exist inside the function; arguments get assigned to them on call
- **Multiple parameters** — order matters; `intro("Anjana", 25)` vs `intro(25, "Anjana")` gives different results
- **`return` vs `print`** — `print` shows output on screen and it's gone; `return` sends the value back to the caller so it can be stored and reused
- **In AI pipelines, always use `return`** — output of one function feeds into the next; `print` returns `None`
- **Mutable default arguments trap** — `def f(item, cart=[])` shares the same list across calls; fix by using `None` as default and creating a new list inside
- **Default parameter values** — provide fallback values; must come after non-default params; e.g. `def greet(name, language="English")`
- **Type hints** — `: int`, `: float`, `-> float` annotate expected types; not enforced at runtime but help readability, IDEs, and static checkers like mypy
- **Returning multiple values** — `return name, age, role` packs into a tuple; unpack with `name, age, role = get_info()`
- **Variable scope** — local variables exist only inside their function; global variables are accessible but modifying them inside a function needs the `global` keyword
- **Avoid global variables** in professional/AI code — pass values in, return values out

## Day 10 - Closures
- **Closure** — happens when a nested function references a variable from the enclosing scope, is returned, and remembers that variable even after the outer function finishes
- The inner function "closes over" the variable and keeps it alive in memory — that's why it's called a closure
- **The Famous Loop Bug** — all functions created inside a `for` loop share the same loop variable reference; they all print the final value, not their iteration's value
- **Fix** — capture the current value using a default argument: `def f(x=i):`; defaults are evaluated at function creation time, not call time
- **`nonlocal` keyword** — needed when you want to reassign (not just read) a variable from the enclosing scope inside a nested function
- Without `nonlocal`, reassignment makes Python treat it as a new local variable, causing `UnboundLocalError`
- `nonlocal` only works with enclosing function scope (use `global` for module-level); the variable must already exist in the enclosing function

## Day 11 - *args, **kwargs & String Immutability
- **String immutability** — `food.replace("z", "s")` returns a new string; it does NOT modify the original. Must reassign: `food = food.replace("z", "s")`
- **Positional arguments** — matched by order: `greet("Anjana", 24)`
- **Keyword arguments** — matched by name: `greet(age=30, name="Prabha")`; order doesn't matter
- **`*args`** — collects any number of positional arguments into a **tuple**; `*` tells Python to pack them
- **`**kwargs`** — collects any number of keyword arguments into a **dictionary**; `**` tells Python to pack key=value pairs
- **Parameter order rule** — regular params first, then `*args`, then `**kwargs`
- **Unpacking with `*` and `**`** — also works when calling functions: `add(*[1,2,3])` unpacks a list; `intro(**info)` unpacks a dict into keyword arguments
- **`**` in dicts** — `{"model": model, **kwargs}` merges a dict into another dict
- **AI connection** — `build_request("gpt-4", temperature=0.7, max_tokens=500)` using `**kwargs` is exactly how real AI libraries (OpenAI SDK, LangChain) handle flexible API configurations

## Day 12 - Lambda Functions, filter() & sorted() with key - 2026-03-24
- **Lambda function** — a small, one-line anonymous function with no name; written as `lambda arguments: expression`
- The expression after `:` is automatically returned — no need to write `return`
- **Two ways to use a lambda** — assign it to a variable: `square = lambda x: x ** 2`, or use it directly inline: `(lambda x: x ** 2)(5)`
- **Lambda is just a shorter function** — `lambda x: x ** 2` does the exact same thing as `def square(x): return x ** 2`
- **Lambda limitations** — can only have one expression; no loops, no multiple lines, no `return`, no variable assignments
- **`filter()`** — goes through every item in a list and keeps only the items where the lambda returns `True`; think of it as a bouncer — only items that pass the test get through
- **Why wrap `filter()` with `list()`** — `filter()` returns a lazy filter object, not a list; wrapping it with `list()` forces it to run and collect all results (same reason we use `list(range(5))`)
- **`sorted()` with `key`** — the `key` parameter takes a function (usually a lambda) that tells Python *what value to sort by*; like putting a sticky note on each item and sorting by the sticky note
- **`reverse=True`** — after sorting, flips the result so the largest comes first
- **`[0]` after `sorted()`** — picks just the first (best) item from the sorted list
- **Real AI use case** — `filter()` to remove models outside budget → `sorted()` by quality → `[0]` to pick the best one; this is a real pattern used in production AI systems to select models dynamically

