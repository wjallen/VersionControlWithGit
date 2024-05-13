#!/usr/bin/env python3
from pi import compute_pi
from math import pi as PI
import pytest

ATTEMPTS = 1_000_000

def test_compute_pi():
    assert(compute_pi(ATTEMPTS) == pytest.approx(PI, abs=1e-2))

