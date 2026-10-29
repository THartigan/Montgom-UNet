# UNet

A minimal starting point for Montgomery chest X-ray segmentation experiments,
following the `ct_segmentation_testing` project's setuptools and `src` layout.
Includes its data loader and loader tests; model architecture, training,
classical segmentation methods, and experiment outputs are not included.

## Setup

Use Python 3.12 or newer, from this directory:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m unittest discover -s tests -v
```

## Local data

Keep the existing dataset (ignored by Git) in this layout:

```text
data/MontgomerySet/
  CXR_png/MCUCXR_0001_0.png
  ClinicalReadings/MCUCXR_0001_0.txt
  ManualMask/leftMask/MCUCXR_0001_0.png
  ManualMask/rightMask/MCUCXR_0001_0.png
```

## Load data

```python
from mtunet import Patient, Trial

trial = Trial()  # finds this checkout's data/MontgomerySet
# Alternatively: Trial("/path/to/MontgomerySet") or Trial("/path/to/data")
patient = trial[0]  # or trial["MCUCXR_0001_0"]
image = patient.image
mask = patient.lung_mask  # boolean union of anatomical left and right masks
metadata = trial.data  # pandas DataFrame; pixel arrays are loaded on access
```

`DataSet` and `Dataset` are aliases for `Trial`. Original pixel values and
resolution are preserved; no resizing, normalization, tensor conversion, or
train/test splitting is performed. Missing masks or clinical files raise by
default; `Trial(strict=False)` allows missing sidecars and returns `None` for
unavailable values. The inherited loader excludes `MCUCXR_0354_1` because its
image and mask dimensions differ. Other shape issues appear in patient metadata.
When using a non-editable installation, pass the data directory explicitly.

`src/mtunet/` contains the package; `tests/` contains loader checks.
`scripts/`, `notebooks/`, and `results/` are placeholders for future work.
Dataset files, model checkpoints, and generated results stay out of version control.
