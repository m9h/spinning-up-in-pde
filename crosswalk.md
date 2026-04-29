# Crosswalk: this curriculum vs. companion repositories

Every module in this curriculum can be anchored to a piece of working JAX or C code in the
companion repository constellation. This document maps modules → repos → specific files,
so you can compare a textbook scheme to a production implementation as you work through it.

The companion repos all live on GitHub (no plan to migrate them to HF). Where a repo is
actively used in a module, the curriculum's article and notebook will link to specific
files; this page is the index.

## Part 1 — Classical PDE Numerics

### Module 01 — Finite Differences & CFL

No companion repo: this module is the classical baseline that everything else is compared
against. The PDEBench reference implementations (PyTorch) and SciMLBenchmarks.jl reference
implementations (Julia) are the closest parallels.

### Module 02 — Finite Volume & Conservation Laws

| Repo | File / topic | Why |
|---|---|---|
| [jwave](https://github.com/m9h/jwave) | `jwave/discretization/` | Pseudospectral acoustic solver — a *non-finite-volume* counterpoint, useful for understanding when FV vs spectral is the right choice for waves vs shocks. |
| [vbjax](https://github.com/m9h/vbjax) | reaction–diffusion neural-mass models | Mixed hyperbolic/parabolic systems where FV-style flux conservation matters at long times. |

### Module 03 — Finite Elements & Variational Forms

| Repo | File / topic | Why |
|---|---|---|
| [Fijee-Project](https://github.com/m9h/Fijee-Project) | [`Fijee/Finite_element_method_models/tCS_model.ufl`](https://github.com/m9h/Fijee-Project/blob/master/Fijee/Finite_element_method_models/tCS_model.ufl) | A real-world **anisotropic Poisson** weak form on a tetrahedral mesh, as used for transcranial direct current stimulation (tDCS) modelling. Three lines of UFL: `a = inner(a_sigma * grad(u), grad(v)) * dx` and a current-injection Neumann boundary term. |
| [Fijee-Project](https://github.com/m9h/Fijee-Project) | `Fijee/Finite_element_method_models/SL_subtraction.cxx` | The **subtraction method** for source localization — handles the dipole singularity in the EEG forward problem. A canonical "real PDE has an awkward right-hand side" example. |
| [vpjax](https://github.com/m9h/vpjax) | cerebrovascular FEM | Differentiable FEM for blood flow, JAX-native. |

### Module 04 — Spectral & Pseudospectral

| Repo | File / topic | Why |
|---|---|---|
| [jwave](https://github.com/m9h/jwave) | k-space pseudospectral propagation | Differentiable acoustic FWI, Fourier-collocation in space, leapfrog in time. The reference implementation for Module 04's final problem. |

### Module 05 — Multigrid & Preconditioners

| Repo | File / topic | Why |
|---|---|---|
| [libspm](https://github.com/m9h/libspm) | `spm/field.h` | Production **Full Multigrid (FMG)** and Conjugate Gradient PDE solvers, separated out as a standalone C library from SPM. The clearest readable reference implementation of FMG — better than any textbook chapter, because it is real working code with all the boundary cases. |
| [libspm](https://github.com/m9h/libspm) | `spm/regularisers.h` | Membrane / bending / linear-elasticity regularisers as the elliptic operator the solver inverts. |
| [libspm](https://github.com/m9h/libspm) | `spm/bsplines.h` | B-spline interpolation (Thévenaz–Unser), essential for prolongation/restriction operators. |

## Part 2 — Differentiable Physics

### Module 06 — Adjoints & Automatic Differentiation

| Repo | File / topic | Why |
|---|---|---|
| [jaxctrl](https://github.com/m9h/jaxctrl) | Lyapunov, Riccati, Gramians | The *control-theoretic* face of the adjoint method. PDE-constrained optimization and optimal control share an adjoint. Module 06 makes the duality explicit and sends you to jaxctrl for the control side. |

### Module 07 — Differentiable Solvers in JAX

| Repo | File / topic | Why |
|---|---|---|
| [jwave](https://github.com/m9h/jwave) | full simulator | Differentiate through the whole pseudospectral simulator. |
| [vpjax](https://github.com/m9h/vpjax) | cerebrovascular models | Coupled hyperbolic + parabolic PDE system with closure terms — non-trivial differentiable physics. |
| [vbjax](https://github.com/m9h/vbjax) | virtual brain modelling | Reaction–diffusion + neural-mass coupling. |
| [dot-jax](https://github.com/m9h/dot-jax) | diffuse optical tomography | Parabolic forward, ill-posed inverse — natural pairing with Module 12. |

## Part 3 — Neural Operators

### Module 08 — Physics-Informed Neural Networks

No first-party PINN repo yet. We use [DeepXDE](https://github.com/lululxvi/deepxde) and
write the implementation from scratch in Equinox.

### Module 09 — DeepONet & FNO

No first-party operator repo yet. We reproduce against
[neuraloperator](https://github.com/neuraloperator/neuraloperator).

### Module 10 — Geometric & Mesh-Aware Operators

| Repo | File / topic | Why |
|---|---|---|
| [hgx](https://github.com/m9h/hgx) | hypergraph operators in JAX/Equinox | A natural superset of mesh-graph neural operators. The hgx primitives generalise GNO/MeshGraphNets to higher-order mesh elements. |
| [devograph](https://github.com/m9h/devograph) | geometric convolutions, optimal transport | Adjacent: developmental-biology extensions of hgx that share the same operator algebra. |

## Part 4 — Benchmarks, Inverse Problems, Discovery

### Module 11 — The Benchmark Landscape

External: [PDEBench](https://github.com/pdebench/PDEBench),
[PDEArena](https://github.com/microsoft/pdearena),
[SciMLBenchmarks.jl](https://github.com/SciML/SciMLBenchmarks.jl).
The adjacent benchmark communities — dynamical-systems identification
([DynaDojo, NeurIPS 2023 D&B](https://proceedings.neurips.cc/paper_files/paper/2023/hash/32093649cbbcff773d9a991d8c30a7fe-Abstract-Datasets_and_Benchmarks.html))
and control theory ([jaxctrl](https://github.com/m9h/jaxctrl), Module 06) —
share most of the numerical primitives the PDE benchmarks measure;
Module 11 makes the crosswalk explicit.

### Module 12 — Inverse Problems & FWI

| Repo | File / topic | Why |
|---|---|---|
| [brain-fwi](https://github.com/m9h/brain-fwi) | transcranial full waveform inversion | The capstone inverse problem: ultrasound through the skull, JAX-differentiable. |
| [jwave](https://github.com/m9h/jwave) | acoustic FWI | The forward solver brain-fwi inverts. |
| [Fijee-Project](https://github.com/m9h/Fijee-Project) | [`Fijee/Biophysics/Leadfield_matrix.cxx`](https://github.com/m9h/Fijee-Project/blob/master/Fijee/Biophysics/Leadfield_matrix.cxx) | The **leadfield matrix** — the linear map from cortical sources to scalp electrodes. Module 12 contrasts the EEG inverse problem (linear, ill-posed, regularised) with FWI (nonlinear, ill-posed, gradient-based). |
| [Fijee-Project](https://github.com/m9h/Fijee-Project) | `Fijee/Biophysics/Jansen_Rit_1995.cxx`, `Wendling_2002.cxx` | The biophysics that *generates* the cortical sources. Multi-scale story: PDE forward → ODE biophysics → linear leadfield → inverse. |

### Module 13 (planned) — Agent-driven PDE discovery

| Repo | File / topic | Why |
|---|---|---|
| [agentsciml](https://github.com/m9h/agentsciml) | multi-agent evolutionary framework | PDE-as-tool-use: agents that propose, run, and refine numerical experiments. Targeted at automated SciML discovery. |

## Notes

- This list is intentionally non-exhaustive on the user's repo side — only repos with a
  direct teaching anchor are listed. The full constellation is in the main
  [README.md](README.md#companion-repositories).
- If a module's "anchored to" pointer becomes stale (file renamed, repo restructured),
  open a discussion on the HF dataset page or a GitHub issue on the mirror.
