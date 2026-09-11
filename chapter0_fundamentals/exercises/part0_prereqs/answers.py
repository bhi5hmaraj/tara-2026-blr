# %%
import math
import sys
from pathlib import Path

import einops
import numpy as np
import torch as t
from torch import Tensor

EXERCISES_DIR = Path(__file__).resolve().parents[1]
SECTION_DIR = Path(__file__).resolve().parent
if str(EXERCISES_DIR) not in sys.path:
    sys.path.append(str(EXERCISES_DIR))

import part0_prereqs.tests as tests
from part0_prereqs.utils import display_array_as_img, display_soln_array_as_img

arr = np.load(SECTION_DIR / "numbers.npy")
