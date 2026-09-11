# TARA 2026 BLR

Local exercises for ARENA Chapter 0 prerequisites and CNNs/ResNets.

## Setup

```bash
uv sync
```

Use `.venv/bin/python` as the notebook kernel in VS Code.

## Workflow

1. Open this repo as the VS Code workspace.
2. Open the course page and its matching `answers.py` file.
3. Add each exercise under a new `# %%` cell.
4. Run each cell with `Shift+Enter`.

Keep your work in `answers.py`. Do not copy the ARENA directory for each exercise.

### Next exercise

1. Read one exercise on the course page.
2. Copy its function stub and test call into `answers.py`.
3. Add a `# %%` cell before the exercise.
4. Implement it and run the cell with `Shift+Enter`.
5. Use the hints after 10-15 minutes if blocked.
6. Check `solutions.py` only after attempting the exercise.

After cloning this repo, add the ARENA remote once:

```bash
git remote add upstream https://github.com/callummcdougall/ARENA_3.0.git
```

For a new section, fetch it once from that remote:

```bash
git fetch upstream main
git restore --source=upstream/main -- chapter0_fundamentals/exercises/<section>
```

Create `<section>/answers.py` and copy the setup imports from its course page.

## Exercises

- Prerequisites and einops: open `part0_prereqs/answers.py` and follow the [course page](https://learn.arena.education/chapter0_fundamentals/00_prereqs/intro/).
- CNNs and ResNets: open `part2_cnns/answers.py` and follow the [course page](https://learn.arena.education/chapter0_fundamentals/02_cnns/).

Both paths are under `chapter0_fundamentals/exercises`. The notebooks and `solutions.py` files are references.

The ResNet setup selects Apple Metal (`mps`), then CUDA, then CPU.

VS Code can also run the exercise notebooks with the `.venv/bin/python` kernel. Copy a notebook once before editing it. Replace its first setup cell with `%run` for the matching `answers.py`; the upstream cell expects a directory named `ARENA_3.0`.
