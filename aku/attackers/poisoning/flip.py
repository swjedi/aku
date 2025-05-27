"""
_summary_
"""
from aku.attackers.base import BaseAttack

class LabelFlippingAttack(BaseAttack):
    """
    _summary_
    """
    def __init__(self,
        labels: list = [],
        flipping_map: dict = {},
        ):
        super().__init__()
        self.labels = labels
        self.flipping_map = self._patch_flipping_map(flipping_map)
    
    def _patch_flipping_map(self, flipping_map: dict) -> dict:
        """
        Patch `flipping_map` attribute to ensure consistent label flipping behavior by
        applying the following rules.

        The rules at default:
            - Remove target labels that are equal to their source label.
            - Remove source labels entirely if there is no valid target labels.

        The extra rules if `labels` attribute is defined:
            - Remove target labels that are not present in `labels` attribute.
            - Remove source labels that are not present in `labels` attribute.

        Parameters
        ----------
        flipping_map : dict
            _description_

        Returns
        -------
        dict
            _description_
        """
        raw_flipping_map = flipping_map.copy()
        for source_label, target_labels in raw_flipping_map.items():
            if self.labels and source_label not in self.labels:
                msg = f"Filtered out `{source_label}` source due to not defined in provided labels."
                self.log.warn(msg)
                flipping_map.pop(source_label, None)
                continue

            keep_target_labels = set()
            for target_label in target_labels:
                if target_label == source_label:
                    msg = f"Filtered out `{target_label}` target due to self-flipping is not allowed."
                    self.log.warn(msg)
                    continue
                if self.labels and target_label not in self.labels:
                    msg = f"Filtered out `{target_label}` target due to not defined in provided labels."
                    self.log.warn(msg)
                    continue
                keep_target_labels.add(target_label)

            if keep_target_labels:
                flipping_map[source_label] = keep_target_labels
            else:
                msg = f"Filtered out `{target_label}` source due to there is no valid target labels."
                self.log.warn(msg)
                flipping_map.pop(source_label, None)

        return flipping_map

    def execute(self):
        """
        _summary_
        """
        pass