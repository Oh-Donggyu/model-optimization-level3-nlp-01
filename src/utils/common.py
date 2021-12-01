import os
from typing import Any, Dict, Union, List

import numpy as np
import yaml
from sklearn.metrics import classification_report
from torchvision.datasets import ImageFolder, VisionDataset


def read_yaml(cfg: Union[str, Dict[str, Any]]):
    if not isinstance(cfg, dict):
        with open(cfg) as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    else:
        config = cfg
    return config


def get_label_counts(dataset_path: str):
    """Counts for each label."""
    if not dataset_path:
        return None
    td = ImageFolder(root=dataset_path)
    # get label distribution
    label_counts = [0] * len(td.classes)
    for p, l in td.samples:
        label_counts[l] += 1
    return label_counts

def save_classification_report(path: str, preds: List[int], gt: List[int]):
    """ save classification report in log directory when update new best result """
    result = classification_report(gt, preds, zero_division=1)
    log_path = os.path.join(path, 'classification_result.txt')
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(result)