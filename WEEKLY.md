# Week 01 · 2026-10-29 → 2026-11-10 (review: 2026-11-12)
### 3 key lessons
1. **Python compares lists by value, Dart by identity.** `b = a` does not copy a list,
   it only gives the same object a second name. In Python `[1, 2] == [1, 2]` is `True`,
   in Dart it is `false`. Use `.copy()` (shallow) or `copy.deepcopy()` when I need a real copy.
2. **The tooling maps almost 1:1 to Dart.** `pyproject.toml` ↔ `pubspec.yaml`,
   `uv.lock` ↔ `pubspec.lock`, `ruff` ↔ `dart analyze` + `dart format`. Commit the lock file,
   never `.venv/`. The src layout keeps tests honest, like `lib/` vs `test/` in Flutter.
3. **Small CLI apps need the same structure as big ones.** In the todo CLI, `storage.py` knows
   about files and `cli.py` only knows about commands. IDs come from `max(id) + 1`, not
   `len() + 1`, and errors go to `stderr` with exit code 1. Also, `.gitignore` only affects
   untracked files: anything already committed needs `git rm --cached`.
### Summary (EN, 5 sentences)
This week I set up python project with uv. I learned that how to use git, uv, ruff, argparese and subparsers. The hardest part was working with files, argparese and subparsers.
I built python project. Next week I want to closure, decorator, generator
### Open questions
- argparese and subparsers
### Stats
Days done: 6/6 · Commits: 28 · Lab files: N