# HoARD: Heads on Applied Research and Development

Notebooks and notes from the books and papers I am studying.

## Objective

Become an expert AI researcher and applied researcher.

1. **Close my ML/DL gaps:** work through foundational books chapter by chapter, implementing
   everything myself.
2. **Read and reproduce research:** read papers critically and reimplement their core ideas.
3. **Apply it:** turn what I learn into experiments and projects of my own.

## How to use the notebooks

A book's official notebooks usually contain all the code and the exercise solutions, so running
them teaches very little. Use them only to check your work or get unstuck:

1. Read the chapter in the book.
2. Copy `notebooks/sample.ipynb` into a folder for that chapter and type the code yourself.
3. Do the exercises before looking at any solution (30–60 minutes of real effort each).
4. Only then open `books/` (set `"books": false` under `files.exclude` in `.vscode/settings.json`)
   to compare, and log what you missed in section 5 of your notebook.

### Example: starting Chapter 3 of a book

```sh
mkdir notebooks/<author>_<book>/ch03_<chapter_slug>
cp notebooks/sample.ipynb notebooks/<author>_<book>/ch03_<chapter_slug>/ch03.ipynb
```

Open `ch03.ipynb`, pick the kernel **Python (HoARD)**, change the title to
`# Chapter 3: <Chapter title>`, fill in **Book:** and **Started:**, and work through the sections as you read.

### Starting a new book

Create `notebooks/<author>_<book>/` (e.g. `notebooks/bishop_deep_learning/`) with a short
`README.md` giving the title and author. If the book has official code, add it under the same name:

```sh
git submodule add <repo url> books/<author>_<book>
```

## Setup (first time on a new machine)

**Requirements:** [uv](https://docs.astral.sh/uv/), git and `make`, plus:

- **macOS:** [Homebrew](https://brew.sh).
- **Linux:** nothing extra. `make setup` uses `apt-get`, `dnf` or `pacman` (it asks for `sudo`).
  On Fedora, `ffmpeg` needs [RPM Fusion](https://rpmfusion.org/Configuration) enabled first.
- **Windows:** use [WSL 2](https://learn.microsoft.com/windows/wsl/install) with Ubuntu, clone
  the repo inside WSL and follow the Linux steps. NVIDIA GPUs work there through CUDA.

`make setup` installs the system packages (`graphviz swig ffmpeg imagemagick`) for your OS, then
the Python environment. On any other system, install those four yourself and run the remaining
lines of the `setup` target by hand.

```sh
git clone --recurse-submodules <this repo> && cd hoard
make setup
```

## Daily use

- **VS Code:** open a notebook, pick the kernel **Python (HoARD)**.
- **JupyterLab:** `make lab`
- **Add a package:** `uv add <pkg>`
- **Pull book updates:** `make update-books`. If a book's official code lists its own dependencies,
  compare them with `pyproject.toml` and run `make lock`.

## Tracking progress

Each book's progress is tracked in its own `notebooks/<author>_<book>/README.md`, in a table with
one row per chapter:

| # | Chapter | Started | Finished |
|---|---|---|---|
| 1 | <Chapter title> | 2026-11-02 | 2026-11-09 |

- **Started:** fill it in when you copy `sample.ipynb` for the chapter.
- **Finished:** fill it in only once you've done the exercises, logged what you missed, and passed
  the "Rebuild from scratch" section of the chapter notebook.

The same dates go at the top of each chapter notebook, so the table and the notebooks always match.

## GPU (CUDA, Apple MPS, or CPU)

```python
from hoard import get_device
device = get_device()  # cuda > mps > cpu
```

`PYTORCH_ENABLE_MPS_FALLBACK=1` is set in the Jupyter kernel and in `make lab`, so ops MPS lacks
run on CPU instead of crashing. MPS has no float64: use float32. For LLM-scale work (or
CUDA-only code) use Colab or a cloud GPU; `get_device()` picks CUDA there automatically.

## Layout

| Path | What |
|---|---|
| `books/<author>_<book>/` | Official code for each book (git submodules, hidden in VS Code). Answer keys, not textbooks |
| `notebooks/sample.ipynb` | Template to copy for each chapter, for any book |
| `notebooks/<author>_<book>/` | One folder per book, with a `README.md` (title, author, where its official notebooks are) |
| `notebooks/<author>_<book>/chXX_<slug>/` | My notebook for a chapter I'm reading |
| `papers/README.md` | How papers are organized, and how we respect authors' work |
| `papers/sample.md` | Reading-notes template to copy for each paper |
| `papers/<year>_<short_title>/` | `notes.md`, optional `implementation.ipynb`, local `paper.pdf` (git-ignored) |
| `src/hoard/` | Reusable code (`from hoard import get_device, seed_everything`) |
| `advice.md` | How to learn effectively (see the Learning section) |
| `tests/` | Tests for `src/hoard/` (`uv run pytest`) |

## License

[MIT](LICENSE). Book code under `books/` and the papers linked from `papers/` belong to their
authors and keep their own licenses.
