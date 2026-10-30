.PHONY: setup system-deps lab lock update-books

setup: system-deps  ## install everything (first time, or after pulling)
	uv sync --extra box2d
	uv run python -m ipykernel install --user --name=hoard --display-name "Python (HoARD)" --env PYTORCH_ENABLE_MPS_FALLBACK 1
	uv run nbstripout --install

system-deps:    ## system packages: graphviz (diagrams), swig (builds Box2D), ffmpeg + imagemagick (animations)
	@if [ "$$(uname)" = "Darwin" ]; then \
		brew install graphviz swig ffmpeg imagemagick; \
	elif command -v apt-get >/dev/null; then \
		sudo apt-get update && sudo apt-get install -y graphviz swig ffmpeg imagemagick; \
	elif command -v dnf >/dev/null; then \
		sudo dnf install -y graphviz swig ffmpeg ImageMagick; \
	elif command -v pacman >/dev/null; then \
		sudo pacman -S --needed graphviz swig ffmpeg imagemagick; \
	else \
		echo "Unknown system: install graphviz, swig, ffmpeg and imagemagick yourself, then rerun make setup."; \
		exit 1; \
	fi

lab:            ## start JupyterLab
	PYTORCH_ENABLE_MPS_FALLBACK=1 uv run jupyter lab

lock:           ## re-resolve after editing pyproject.toml
	uv lock && uv sync --extra box2d

update-books:   ## pull the latest official code for every book in books/
	git submodule update --remote
