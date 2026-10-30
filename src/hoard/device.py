"""Pick the best available accelerator so the same code runs on a Mac, a CUDA box, or a CPU."""

import os
import random

# Let ops that MPS doesn't implement fall back to CPU instead of raising.
# Must be set before torch is imported to take effect.
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")

import numpy as np
import torch


def get_device(prefer: str | None = None) -> torch.device:
    """Return CUDA, then MPS (Apple GPU), then CPU. Pass `prefer="cpu"` to force one."""
    if prefer is not None:
        return torch.device(prefer)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def seed_everything(seed: int = 42) -> None:
    """Seed Python, NumPy and PyTorch (all devices) for reproducible runs."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)  # also seeds CUDA and MPS
