from setuptools import setup, find_packages

setup(
    name="AdaptiveThresholding",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "skimage",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "adaptive-thresholding=adaptive_thresholding.main:main",
        ],
    },
)