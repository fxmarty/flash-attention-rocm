# Adapted from https://github.com/NVIDIA/apex/blob/master/setup.py
import sys
import warnings
import os
from packaging.version import parse, Version

import torch
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension, CUDA_HOME
from setuptools import setup, find_packages
import subprocess

# ninja build does not work unless include_dirs are abs path
this_dir = os.path.dirname(os.path.abspath(__file__))



print("\n\ntorch.__version__  = {}\n\n".format(torch.__version__))
TORCH_MAJOR = int(torch.__version__.split(".")[0])
TORCH_MINOR = int(torch.__version__.split(".")[1])

cmdclass = {}
ext_modules = []

ext_modules.append(
    CUDAExtension(
        'rotary_emb', [
            'rotary.cpp',
            'rotary_cda.cu',
        ],
        #extra_compile_args={'cxx': ['-g', '-march=native', '-funroll-loops']}
    )
)

setup(
    name="rotary_emb",
    version="0.1",
    ext_modules=ext_modules,
    cmdclass={"build_ext": BuildExtension} if ext_modules else {},
)
