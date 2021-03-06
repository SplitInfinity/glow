from __future__ import absolute_import, division, print_function, unicode_literals

import torch

from tests.utils import jitVsGlow


def test_addmm_basic():
    """Basic test of the PyTorch addmm Node on Glow."""

    def test_f(a, b, c):
        return (a+a).addmm(b, c)

    x = torch.randn(6, 4)
    y = torch.randn(6, 10)
    z = torch.randn(10, 4)

    jitVsGlow(test_f, x, y, z, expected_fused_ops={"aten::addmm"})


def test_addmm_broadcast():
    """Test of the PyTorch addmm with broadcasting add on Glow."""

    def test_f(a, b, c):
        return (a+a).addmm(b, c)

    x = torch.randn(4)
    y = torch.randn(6, 10)
    z = torch.randn(10, 4)

    jitVsGlow(test_f, x, y, z, expected_fused_ops={"aten::addmm"})


def test_addmm_broadcast_with_alpha_and_beta():
    """Test of the PyTorch addmm with broadcasting add on Glow."""

    def test_f(a, b, c):
        return (a+a).addmm(b, c, alpha=2.0, beta=3.0)

    x = torch.randn(4)
    y = torch.randn(6, 10)
    z = torch.randn(10, 4)

    jitVsGlow(test_f, x, y, z, expected_fused_ops={"aten::addmm"})
