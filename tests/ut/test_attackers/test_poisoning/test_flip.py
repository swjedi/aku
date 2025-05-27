"""
_summary_
"""
from aku.attackers.poisoning.flip import LabelFlippingAttack

from tests.framework import BaseUnitTest

class TestLabelFlippingAttack(BaseUnitTest):
    """
    _summary_
    """
    def test_patch_flipping_map(self):
        """
        Verify the behaviors of `_path_flipping_map` method under
        different edge cases.
        """
        att = LabelFlippingAttack(
            labels=[1, 2, 3, 4, 5],
            flipping_map={
                0: {2, 3, 4},
                1: {2, 3, 4, 5},
                2: {3},
                3: {4, 5, 6},
                4: {6, 7, 8},
            }
        )

        self.assertEqual(
            att.flipping_map,
            {
                1: {2, 3, 4, 5},
                2: {3},
                3: {4, 5},
            }
        )
