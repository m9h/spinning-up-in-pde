# Notebooks

Notebooks are kept in [jupytext](https://jupytext.readthedocs.io/) percent format (`.py`) for
clean diffs and reviewable PRs. Convert to `.ipynb` once before launching Jupyter:

```bash
# One-time conversion of all notebooks
jupytext --to notebook *.py

# Or pair an individual file (auto-syncs .py and .ipynb on save)
jupytext --set-formats py:percent,ipynb 01_finite_differences_cfl.py
```

The `.ipynb` files are listed in [`../.gitignore`](../.gitignore) and are not committed.

## Module notebooks

| | Notebook | Article | Status |
|---|---|---|---|
| 01 | [01_finite_differences_cfl.py](01_finite_differences_cfl.py) | [pde-series-part1-finite-differences.md](../articles/pde-series-part1-finite-differences.md) | ready |
| 02 | finite volume / conservation laws | _writing_ | -- |
| 03 | finite elements & variational forms | _writing_ | -- |
| 04 | spectral & pseudospectral | _writing_ | -- |
| 05 | multigrid & preconditioners | _writing_ | -- |
| 06 | adjoints & automatic differentiation | _writing_ | -- |
| 07 | differentiable solvers | _writing_ | -- |
| 08 | physics-informed neural networks | _writing_ | -- |
| 09 | DeepONet & FNO | _writing_ | -- |
| 10 | geometric / mesh-aware operators | _writing_ | -- |
| 11 | the benchmark landscape | _writing_ | -- |
| 12 | inverse problems & FWI | _writing_ | -- |
