# %%
import json
import sys
from collections import namedtuple
from dataclasses import dataclass
from pathlib import Path

import einops
import numpy as np
import torch as t
import torch.nn as nn
import torch.nn.functional as F
import torchinfo
from IPython.display import display
from jaxtyping import Float, Int
from PIL import Image
from rich import print as rprint
from rich.table import Table
from torch import Tensor
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, models, transforms
from tqdm.notebook import tqdm

EXERCISES_DIR = Path(__file__).resolve().parents[1]
SECTION_DIR = Path(__file__).resolve().parent
if str(EXERCISES_DIR) not in sys.path:
    sys.path.append(str(EXERCISES_DIR))

import part2_cnns.tests as tests
import part2_cnns.utils as utils
from plotly_utils import line

device = t.device(
    "mps"
    if t.backends.mps.is_available()
    else "cuda"
    if t.cuda.is_available()
    else "cpu"
)
