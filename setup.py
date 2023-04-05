import os
import shutil
import setuptools
from distutils.core import setup

root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), encoding="utf-8") as f:
    long_description = f.read()
with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open("airxd/version.py").read())

extension = setuptools.Extension(
                "_mask",
                sources=["airxd/mask.cpp"],
                extra_compile_args=["-std=c++11"],
                )

setup(
    name='airxd',
    version=__version__,
    description='ML application for 2D XRD data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["airxd"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'numpy==1.21.6',
        'scipy==1.7.3',
        'matplotlib==3.5.2',
        'scikit-learn==1.0.2',
        'imageio==2.19.3',
        'xgboost==1.6.1',
        'notebook==6.4.12',
        'opencv-python==4.6.0.66',
    ],
    python_requires=">=3.7.9",
    ext_modules=[extension],
)
