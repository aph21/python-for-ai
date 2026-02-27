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
