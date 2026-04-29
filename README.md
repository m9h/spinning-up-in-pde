---
license: apache-2.0
pretty_name: Spinning Up in PDE Solvers
language:
  - en
tags:
  - education
  - curriculum
  - scientific-machine-learning
  - sciml
  - pde
  - partial-differential-equations
  - jax
  - finite-differences
  - finite-elements
  - spectral-methods
  - neural-operators
  - pinns
  - differentiable-physics
size_categories:
  - n<1K
---

# Spinning Up in PDE Solvers

**From Lewis Fry Richardson's forecast factory to differentiable physics — a hands-on curriculum tracing the lineage of computational PDE solvers**

<p align="center">
  <img src="https://img.shields.io/badge/modules-12-blue" alt="12 modules"/>
  <img src="https://img.shields.io/badge/JAX-first-green" alt="JAX-first"/>
  <img src="https://img.shields.io/badge/license-Apache_2.0-orange" alt="License"/>
  <img src="https://img.shields.io/badge/community-HF_Science_%23pde-yellow" alt="HF Science #pde"/>
</p>

---

In 1922, Lewis Fry Richardson published *Weather Prediction by Numerical Process* — a 236-page proposal to forecast the atmosphere by hand, using a "forecast factory" of 64,000 human computers seated in a vast amphitheatre, each solving a finite-difference cell. His own six-hour test forecast diverged into nonsense. Six years later, Courant, Friedrichs, and Lewy explained why: he had violated a stability bound on the timestep. By 1950, Charney, Fjørtoft, and von Neumann ran the same idea on ENIAC and got a forecast that worked. The scheme they used — forward-time centred-space, FTCS — is the same baseline you'll find in every PDEBench plot today, three quarters of a century later.

This curriculum traces that intellectual lineage from Euler's 1768 forward step through finite elements, spectral methods, multigrid, and adjoints, into modern differentiable physics and neural operators. You will implement every method on a small problem, see why each one was invented, and understand what the modern benchmarks (PDEBench, PDEArena, SciMLBenchmarks, DyNoBench) are actually measuring.

> Modeled on OpenAI's [Spinning Up in RL](https://spinningup.openai.com/) and the author's [Spinning Up in Active Inference](https://github.com/m9h/spinning-up-alf). Companion to the [Hugging Face Science](https://huggingface.co/HuggingFaceScience) Discord, channel **#pde**, with a weekly community session.

## How this fits with other resources

There are excellent neural-operator benchmarks already. This curriculum exists to give them a backstory.

|  | [PDEBench](https://github.com/pdebench/PDEBench) | [PDEArena](https://github.com/microsoft/pdearena) | [SciMLBenchmarks](https://github.com/SciML/SciMLBenchmarks.jl) | [DeepXDE](https://github.com/lululxvi/deepxde) | [DeepInverse](https://deepinv.github.io/) | **This curriculum** |
|---|---|---|---|---|---|---|
| **Classical PDE numerics** | -- | -- | Some | -- | -- | Modules 1-5 (FD, FV, FEM, spectral, multigrid) |
| **Adjoint & AD** | -- | -- | Implicit (Julia AD) | -- | Yes (gradients through forward op) | Module 6, with jaxctrl crosswalk |
| **Differentiable solvers** | -- | -- | -- | -- | -- | Module 7 (JAX-CFD, PhiFlow, jwave) |
| **PINNs** | -- | -- | -- | Yes | -- | Module 8 |
| **Neural operators** | FNO, U-Net | FNO, U-Net, GNO | -- | -- | -- | Modules 9-10 |
| **Standardised metrics** | Conservation, spectral RMSE | Trajectory rollout | Work-precision diagrams | -- | PSNR / SSIM / LPIPS for imaging IPs | Module 11 (uses all of the above) |
| **Inverse problems / FWI** | -- | -- | -- | -- | Yes — learned priors, plug-and-play, diffusion-based | Module 12 (brain-fwi, jwave, fijee leadfield) |
| **Historical narrative** | -- | -- | -- | -- | -- | Every module |
| **Primary language** | PyTorch | PyTorch | Julia | TF/PyTorch/JAX | PyTorch | JAX |
| **Format** | Datasets + baselines | Datasets + baselines | Benchmarks + WPDs | Solver framework | Inverse-problem framework | Curriculum + weekly sessions |

**The gap we fill:** PDEBench tells you which architecture wins on Burgers. It does not tell you what FTCS is, why CFL exists, or why the FEM community spent thirty years arguing about test functions. This curriculum is the "spinning-up" prequel: read it, run the notebooks, and the benchmark papers will read like the next chapter instead of an alien language.

## Where the work happens

The history of computational PDE solvers is also a history of specific institutions, and the modern SciML community is concentrated in a recognisable set of them. The curriculum cites them where their work is load-bearing; this section is the orienting map.

- **[Courant Institute (NYU)](https://cims.nyu.edu/)** — Founded by Richard Courant, who put the **C** in CFL (Module 01). The lineage runs from Friedrichs and Lewy through Peter Lax, Cathleen Morawetz, Leslie Greengard (FMM), and a generation of mathematical-PDE-numerics PhDs who staffed every other institution on this list. Still the gravitational centre for theoretical PDE numerics.
- **US Department of Energy national laboratories.** Each lab carries a distinct numerical tradition:
  - **[Los Alamos (LANL)](https://www.lanl.gov/)** — von Neumann's nuclear simulations; the institutional context in which his stability analysis (Module 01) matured. Modern: ALE methods, kinetic codes, FLAG, xRAGE.
  - **[Argonne (ANL)](https://www.anl.gov/)** — home of [PETSc](https://petsc.org/), the dominant scalable PDE-solver toolkit; also the [MPICH](https://www.mpich.org/) reference implementation.
  - **[Lawrence Berkeley (LBNL)](https://www.lbl.gov/)** — Phil Colella's adaptive-mesh-refinement lineage; [BoxLib / AMReX](https://amrex-codes.github.io/amrex/), [Chombo](https://commons.lbl.gov/display/chombo/Chombo+-+Software+for+Adaptive+Solutions+of+Partial+Differential+Equations).
  - **[Lawrence Livermore (LLNL)](https://www.llnl.gov/)** — [hypre](https://hypre.readthedocs.io/) (algebraic multigrid; the production analogue of Module 05), [MFEM](https://mfem.org/), [SUNDIALS](https://computing.llnl.gov/projects/sundials), and [libROM](https://www.librom.net/) (reduced-order modelling). LLNL's libROM team also hosts the [**DDPS** webinar series](https://www.librom.net/ddps.html) — see _Recurring seminars_ below.
  - **[Sandia](https://www.sandia.gov/)** — [Trilinos](https://trilinos.github.io/), [Kokkos](https://kokkos.org/) — the performance-portability stack underneath much of US HPC.
  - **[Oak Ridge (ORNL)](https://www.ornl.gov/)** — Jack Dongarra's group; [LAPACK / ScaLAPACK / MAGMA](https://www.icl.utk.edu/research/magma); the [Frontier exascale system](https://www.olcf.ornl.gov/frontier/), now the world's flagship machine for climate, fusion, and materials PDE workloads.
- **[SIMULA Research Laboratory](https://www.simula.no/) (Oslo)** — Hans Petter Langtangen's legacy; long-time home of [FEniCS](https://fenicsproject.org/) and the broader Python finite-element ecosystem. The UFL variational form referenced in [Module 03](crosswalk.md#module-03--finite-elements--variational-forms) — `a = inner(a_sigma * grad(u), grad(v)) * dx` — is FEniCS syntax, written at SIMULA.
- **[Santa Fe Institute](https://www.santafe.edu/)** — The complex-systems and dynamical-systems framings of the SciML problem. The Crutchfield / West / Kauffman lineage shaped the data-driven-dynamics community; their conceptual gravity informs DyNoBench and dynamicsai.org below.
- **[IPAM at UCLA](https://www.ipam.ucla.edu/)** — The Institute for Pure and Applied Mathematics hosts long-program semesters where the SciML field's working consensus actually gets worked out: *Machine Learning for Physical Sciences* (2019), *Tensor Methods and Emerging Applications* (2021), and the ongoing PDE-and-learning workshops. Recordings of the long-program tutorials are on the IPAM YouTube channel and worth your time.
- **[dynamicsai.org / DyNoBench](https://dynamicsai.org/)** — A coordinated benchmarking effort on data-driven discovery of dynamical systems, parallel and complementary to PDEBench (see Module 11). Read the two together when evaluating neural operators on time-series ODEs.

This list grossly under-credits Europe (INRIA, Max Planck, Oxford NA group, Cambridge DAMTP, Imperial), Asia (RIKEN, Tsinghua, NCAR's atmospheric modelling community), and the wider open-source SciML ecosystem (the JuliaSciML and JAX-CFD groups, the mesh-software community around Gmsh and CGAL). Each module will cite the institutions whose work it builds on; corrections and additions welcome via Discussion or PR.

## Recurring seminars and talks

If you want to keep the field at peripheral vision while you work through the curriculum, the following recurring seminars and webinar series are the easiest way in. Most have full archives going back several years.

- **[DDPS — Data-Driven Physical Simulations](https://www.librom.net/ddps.html)** (LLNL libROM team). Weekly webinar on machine learning + AI methods for computational science and physical simulation: deep learning for simulation, generative models, data assimilation, fluid dynamics, plasma physics. Recorded archive from 2020 onwards. Subscribe on the page. Organised by Youngsoo Choi and Siu Wun Cheung.

_(More seminars and resources will be added here as the curriculum grows; suggestions welcome via Discord or PR.)_

## Who is this for?

- ML researchers entering SciML who want to understand what they're benchmarking against
- Computational scientists whose first move is FEniCS or PETSc, curious about JAX-native differentiable solvers
- Graduate students preparing to read [Karniadakis et al.](https://www.nature.com/articles/s42254-021-00314-5), [Li et al. (FNO)](https://arxiv.org/abs/2010.08895), or [Lu et al. (DeepONet)](https://arxiv.org/abs/1910.03193) and wanting context
- Anyone in the [Hugging Face Science](https://huggingface.co/HuggingFaceScience) Discord #pde channel who wants to follow along week by week

**Prerequisites:** Python, NumPy, ODE basics. Vector calculus helpful but reviewed as we go. No prior FEM or neural-operator experience required.

---

## The Curriculum

### Part 1 — Classical PDE Numerics

The 250-year backstory. What every modern surrogate model is compared against, and why those comparisons are the right ones.

| | Module | What you'll build | Anchored to |
|---|---|---|---|
| [01](articles/pde-series-part1-finite-differences.md) | **Finite Differences & CFL** | 1D heat equation in JAX, explicit FTCS vs Crank-Nicolson, watch the CFL boundary in real time. | PDEBench FTCS baseline |
| 02 | **Finite Volume & Conservation Laws** | 1D Burgers with Godunov / Roe / minmod limiters. Why shocks need conservative discretisation. | PDEBench compressible flow |
| 03 | **Finite Elements & Variational Forms** | Anisotropic Poisson on a tetrahedral mesh in FEniCSx, reading from a real `.ufl` file. | [`fijee/Finite_element_method_models/tCS_model.ufl`](https://github.com/m9h/Fijee-Project/blob/master/Fijee/Finite_element_method_models/tCS_model.ufl) |
| 04 | **Spectral & Pseudospectral Methods** | 2D Navier-Stokes with FFT-based pseudospectral, Orszag's 2/3 dealiasing rule. | [jwave](https://github.com/m9h/jwave) k-Wave-style propagation |
| 05 | **Multigrid & Preconditioners** | Full Multigrid V-cycles on a Poisson problem, comparison vs CG / PCG. | [`libspm/field.h`](https://github.com/m9h/libspm) — production FMG/CG in C |

### Part 2 — Differentiable Physics

Where adjoints meet automatic differentiation, and the simulator becomes a layer.

| | Module | What you'll build | Anchored to |
|---|---|---|---|
| 06 | **Adjoints & Automatic Differentiation** | Hand-derived adjoint of a 1D advection solver, then `jax.grad` through the same solver. The two answers had better match. | [jaxctrl](https://github.com/m9h/jaxctrl) (Lyapunov / Riccati adjoints) |
| 07 | **Differentiable Solvers in JAX** | Tour of JAX-CFD, PhiFlow, jwave: how a forward solver becomes a gradient operator. Train a learned closure on a coarse grid. | [jwave](https://github.com/m9h/jwave), [vpjax](https://github.com/m9h/vpjax), [vbjax](https://github.com/m9h/vbjax), [dot-jax](https://github.com/m9h/dot-jax) |

### Part 3 — Neural Operators

Surrogate models that learn maps between function spaces, not point values.

| | Module | What you'll build | Anchored to |
|---|---|---|---|
| 08 | **Physics-Informed Neural Networks** | A PINN for 1D Burgers from scratch in Equinox, then read [Raissi et al. 2019](https://www.sciencedirect.com/science/article/pii/S0021999118307125). Discuss: when do PINNs beat classical solvers, and when don't they? | [DeepXDE](https://github.com/lululxvi/deepxde) baseline comparison |
| 09 | **DeepONet & Fourier Neural Operators** | Reproduce a small FNO on Darcy flow. Spectral bias, resolution invariance, the operator-learning premise. | [neuraloperator](https://github.com/neuraloperator/neuraloperator) |
| 10 | **Geometric & Mesh-Aware Operators** | GraphNet-based operators (MeshGraphNets style) on irregular meshes. Why FNO's regular-grid assumption breaks for engineering problems. | [hgx](https://github.com/m9h/hgx) hypergraph operator overlap |

### Part 4 — Benchmarks, Inverse Problems, Discovery

What "good" looks like, and what real problems look like.

| | Module | What you'll build | Anchored to |
|---|---|---|---|
| 11 | **The Benchmark Landscape** | Run the same FNO on PDEBench Burgers, then on PDEArena Navier-Stokes, then on a SciMLBenchmarks WPD. Read the metric definitions: spectral RMSE, conservation RMSE, work-precision. | [PDEBench](https://github.com/pdebench/PDEBench), [PDEArena](https://github.com/microsoft/pdearena), [DyNoBench (dynamicsai.org)](https://dynamicsai.org/) |
| 12 | **Inverse Problems & FWI** | Full-waveform inversion on a small acoustic test case in jwave; brief tour of brain-fwi (transcranial FWI) and the EEG forward-inverse problem (fijee leadfield → source localization). Compare classical regularised inversion against learned-prior approaches via [DeepInverse](https://deepinv.github.io/). | [brain-fwi](https://github.com/m9h/brain-fwi), [jwave](https://github.com/m9h/jwave), [Fijee-Project](https://github.com/m9h/Fijee-Project), [DeepInverse](https://deepinv.github.io/) |

A 13th module — **Agent-driven PDE discovery** — is planned but not scheduled, pending [agentsciml](https://github.com/m9h/agentsciml) maturity.

---

## The Voice

Each module ships as both a notebook and a companion article. The articles follow the [Fedora Magazine](https://fedoramagazine.org/) cadence the author has used in the [linear-algebra series](https://github.com/m9h/fedora-linear-algebra-mag-series): a hook tied to a real-world artifact, the historical motivation (people, places, dates), the math, the code you can run today, and a forward link to the next idea in the sequence.

The companion notebooks are written in [jupytext](https://jupytext.readthedocs.io/) `.py` percent format for clean diffs, and convert to `.ipynb` with one command. See the [notebooks README](notebooks/) for the conversion recipe.

## Companion repositories

This curriculum is the front door to a constellation of JAX-native scientific-computing repositories by the same author. Each module names the relevant ones above; here is the full crosswalk:

| Repo | Role in the curriculum |
|---|---|
| [jaxctrl](https://github.com/m9h/jaxctrl) | Differentiable control (Lyapunov, Riccati, Gramians). Adjoint duality with PDE-constrained optimization. |
| [agentsciml](https://github.com/m9h/agentsciml) | Multi-agent evolutionary framework for SciML discovery. PDE-as-tool-use. |
| [jwave](https://github.com/m9h/jwave) | Differentiable acoustics in JAX, pseudospectral. Module 4, Module 7, Module 12. |
| [vpjax](https://github.com/m9h/vpjax) | Differentiable cerebrovascular models. Coupled hyperbolic / parabolic systems. |
| [vbjax](https://github.com/m9h/vbjax) | Virtual brain modelling — neural mass + integration. |
| [dot-jax](https://github.com/m9h/dot-jax) | Diffuse Optical Tomography (a parabolic forward, ill-posed inverse). |
| [brain-fwi](https://github.com/m9h/brain-fwi) | Full waveform inversion through the skull. Capstone-grade inverse problem. |
| [libspm](https://github.com/m9h/libspm) | Standalone C library for SPM's PDE solvers — Full Multigrid, B-splines, regularizers. Module 5. |
| [Fijee-Project](https://github.com/m9h/Fijee-Project) | FEM forward EEG (anisotropic Poisson) + Jansen-Rit/Wendling biophysics. Module 3, Module 12. |

See [crosswalk.md](crosswalk.md) for module-by-module pointers.

## Installation

This repository is mirrored on both Hugging Face and GitHub:

```bash
# From Hugging Face (primary; uses the `hf` CLI):
git clone https://huggingface.co/datasets/mhough/spinning-up-in-pde
cd spinning-up-in-pde

# Or from GitHub (mirror):
# git clone https://github.com/m9h/spinning-up-in-pde.git

# Create environment (requires uv: https://docs.astral.sh/uv/)
uv venv .venv --python 3.13
source .venv/bin/activate

# Core dependencies
uv pip install -r requirements.txt

# Convert jupytext .py notebooks to .ipynb
jupytext --to notebook notebooks/*.py

# Launch
jupyter lab
```

JAX install: on Linux/CUDA add `jax[cuda12]`; on Apple Silicon use the standard `jax` wheel (CPU) or `jax-mps` for MLX-backed acceleration on M-series hardware. See [JAX install docs](https://docs.jax.dev/en/latest/installation.html).

## Community

- **Discord:** [Hugging Face Science](https://huggingface.co/HuggingFaceScience), channel `#pde`
- **Weekly session:** one module per week, walkthrough + open Q&A. Time TBA in the channel.
- **Issues / PRs:** corrections, extra references, alternative implementations all welcome — especially historical citations we missed.

## License

Apache 2.0. Content is reusable; please cite the curriculum if you adapt it.
