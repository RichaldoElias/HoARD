import torch

from hoard import get_device


def test_returns_a_usable_device():
    device = get_device()
    assert device.type in {"cuda", "mps", "cpu"}
    assert (torch.ones(2, device=device) * 2).sum().item() == 4


def test_prefers_cuda_then_mps(monkeypatch):
    monkeypatch.setattr(torch.cuda, "is_available", lambda: True)
    assert get_device().type == "cuda"
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)
    monkeypatch.setattr(torch.backends.mps, "is_available", lambda: True)
    assert get_device().type == "mps"
    monkeypatch.setattr(torch.backends.mps, "is_available", lambda: False)
    assert get_device().type == "cpu"


def test_prefer_overrides_detection():
    assert get_device(prefer="cpu").type == "cpu"
