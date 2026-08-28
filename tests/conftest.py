from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless: tests must never open windows or block on plt.show()

import pytest

ROOT = Path(__file__).resolve().parent.parent  # repo root
TEST_DATA = ROOT / "tests" / "files"


@pytest.fixture(scope="session")
def data_path() -> Path:
    return TEST_DATA


@pytest.fixture(autouse=True)
def _close_figures():
    """Close all pyplot figures after each test.

    The plot functions register their figures with pyplot and no longer show
    (and thereby consume) them, so without this the registry fills up over
    the test run.
    """
    yield
    import matplotlib.pyplot as plt

    plt.close("all")
