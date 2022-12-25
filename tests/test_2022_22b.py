"""Unit test for this f#$%ing cube."""
import sys
import unittest

import pytest

from src.y2022.d22.b import process_warp  # pylint: disable=import-error

R_SECTION_LENGTH = 50
C_SECTION_LENGTH = 50

warp_map = {
    (0, 150, 0): (149, 99, 2),
    (49, 150, 0): (100, 99, 2),
    (50, 100, 0): (49, 100, 3),
    (99, 100, 0): (49, 149, 3),
    (100, 100, 0): (49, 149, 2),
    (149, 100, 0): (0, 149, 2),
    (150, 50, 0): (149, 50, 3),
    (199, 50, 0): (149, 99, 3),
    (200, 0, 1): (0, 100, 1),
    (200, 49, 1): (0, 149, 1),
    (150, 50, 1): (150, 49, 2),
    (150, 99, 1): (199, 49, 2),
    (50, 100, 1): (50, 99, 2),
    (50, 149, 1): (99, 99, 2),
    (0, 49, 2): (149, 0, 0),
    (49, 49, 2): (100, 0, 0),
    (50, 49, 2): (100, 0, 1),
    (99, 49, 2): (100, 49, 1),
    (100, -1, 2): (49, 50, 0),
    (149, -1, 2): (0, 50, 0),
    (150, -1, 2): (0, 50, 1),
    (199, -1, 2): (0, 99, 1),
    (99, 0, 3): (50, 50, 0),
    (99, 49, 3): (99, 50, 0),
    (-1, 50, 3): (150, 0, 0),
    (-1, 99, 3): (199, 0, 0),
    (-1, 100, 3): (199, 0, 3),
    (-1, 149, 3): (199, 49, 3),
}


class test_b_warps(unittest.TestCase):
    """Spin a cube and make sure we're spinning correctly."""

    def test_warps(self):
        """Do all the spins."""
        for k, v in warp_map.items():
            r, c, facing = k
            (r, c), facing = process_warp(
                (r, c), facing, R_SECTION_LENGTH, C_SECTION_LENGTH
            )
            self.assertEqual((r, c, facing), v)


if __name__ == "__main__":
    sys.exit(pytest.main())
