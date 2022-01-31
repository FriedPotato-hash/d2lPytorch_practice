import collections
import hashlib
import math
import os
import random
import re
import shutil
import sys
import tarfile
import time
import zipfile
from collections import defaultdict
import pandas as pd
import requests
from IPython import display
from matplotlib import pyplot as plt


import numpy as np
import torch
from PIL import Image
from torch import nn
from torch.utils import data
from torchvision import transforms

"""
import torch
from torch import nn
from torch.nn import functional as F

net = nn.Sequential(nn.Linear(20, 256), nn.Relu(), nn.Linear(256, 10))

X = torch.rand(2, 20)
print(X)
"""
