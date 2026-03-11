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
