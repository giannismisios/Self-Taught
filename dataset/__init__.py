from .cars import Cars
from .cub import CUBirds
from .SOP import SOP
from .import utils
from .base import BaseDataset
from .gldv2 import GLDv2

_type = {
    'cub': CUBirds,
    'cars': Cars,
    'SOP': SOP,
    'gldv2': GLDv2,
}

def load(name, root, mode, transform = None, k_fold_eval = False, fold_idx = 0):
    return _type[name](root = root, mode = mode, transform = transform, k_fold_eval = k_fold_eval, fold_idx = fold_idx)