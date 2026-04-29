# Resources

A longer-form companion to the [README](README.md). The README's _Where the work happens_, _Open-source PDE software_, and _Recurring seminars and talks_ sections cite a curated subset of what is collected here. This document is the broader survey: institutes, software ecosystems, textbooks, seminar archives, and pedagogical onramps that the curriculum draws on or points students at.

Pull requests adding institutions, software, or reading material are welcome — especially for European, Asian, and South American groups, which are systematically under-represented in this initial pass.

## Institutes and research groups

### United States — applied-math and SciML hubs

- **[Courant Institute (NYU)](https://cims.nyu.edu/)** — Founded by Richard Courant. The C of CFL, and the institutional home of mathematical PDE numerics. Lineage: Friedrichs, Lewy, Lax, Morawetz, Greengard, Trefethen-trained students.
- **[Brown University, Division of Applied Mathematics](https://appliedmath.brown.edu/)** — Lax-Wendroff lineage; modern: George Em Karniadakis (CRUNCH Group, PINNs and DeepONet). The CRUNCH Group YouTube archive is cited in the README.
- **[Caltech Computing + Mathematical Sciences](https://www.cms.caltech.edu/)** — Andrew Stuart (operator learning, Bayesian inverse problems), Houman Owhadi (operator-valued kernels), [Anima Anandkumar](https://www.cms.caltech.edu/people/anima) (co-creator of FNO). Currently one of the densest concentrations of SciML thought.
- **[University of Washington — AI Institute in Dynamic Systems](https://dynamicsai.org/)** — NSF-funded institute led by Steve Brunton, Nathan Kutz, and Bing Brunton. The home of the data-driven dynamical-systems community: [Dynamic Mode Decomposition](https://www.cambridge.org/core/books/dynamic-mode-decomposition/), [SINDy](https://www.pnas.org/doi/10.1073/pnas.1517384113), Koopman-operator approximations. The conceptual bridge from PDE numerics into dynamical-systems identification and control theory runs through this group's work.
- **[UT Austin Oden Institute](https://www.oden.utexas.edu/)** — Tinsley Oden's institutional legacy; PDE-constrained optimization, UQ, SciML. Directed by Karen Willcox.
- **[Stanford ICME](https://icme.stanford.edu/)** — Computational and mathematical engineering. Tom Hughes's FEM legacy; modern: Charbel Farhat (CFD, ROM), Eric Darve.
- **[MIT Center for Computational Science and Engineering](https://cse.mit.edu/)** — Anthony Patera (reduced-order modelling); Steven G. Johnson (FFTW, electromagnetic PDEs); the broader Aero / Math / EECS PDE ecosystem.
- **[Princeton Applied + Computational Math (PACM)](https://www.pacm.princeton.edu/)** — IAS-adjacent. Where von Neumann did the first ENIAC weather forecasts.
- **[Flatiron Institute — Center for Computational Mathematics (CCM)](https://www.simonsfoundation.org/flatiron/center-for-computational-mathematics/)** — Simons Foundation. Leslie Greengard (Fast Multipole Method), Charlie Epstein, Manas Rachh.
- **[UC Berkeley Mathematics + LBNL Computational Research](https://math.berkeley.edu/)** — James Sethian (level sets), Phil Colella (joint with LBNL), Jamie Sethian's level-set lineage.

### United States — DOE national laboratories

Each lab carries a distinct numerical-software tradition; see the README for the curated short list. Software ecosystems detailed in the next section.

- **Los Alamos (LANL)** — von Neumann's nuclear simulations; ALE methods; FLAG, xRAGE.
- **Argonne (ANL)** — [PETSc](https://petsc.org/), [MPICH](https://www.mpich.org/).
- **Lawrence Berkeley (LBNL)** — Phil Colella's AMR lineage; [BoxLib / AMReX](https://amrex-codes.github.io/amrex/), [Chombo](https://commons.lbl.gov/display/chombo/).
- **Lawrence Livermore (LLNL)** — [hypre](https://hypre.readthedocs.io/), [MFEM](https://mfem.org/), [SUNDIALS](https://computing.llnl.gov/projects/sundials), [libROM](https://www.librom.net/), and the [DDPS webinar series](https://www.librom.net/ddps.html).
- **Sandia (SNL)** — [Trilinos](https://trilinos.github.io/), [Kokkos](https://kokkos.org/).
- **Oak Ridge (ORNL)** — Jack Dongarra's group; [LAPACK / ScaLAPACK / MAGMA](https://www.icl.utk.edu/research/magma); the [Frontier exascale system](https://www.olcf.ornl.gov/frontier/).
- **Idaho National Lab (INL)** — [MOOSE framework](https://mooseframework.inl.gov/) (multi-physics).
- **NREL (Renewable Energy)** — wind, solar, climate-coupled CFD.
- **PNNL (Pacific Northwest)** — atmospheric and subsurface modelling.

### Europe

- **[INRIA (France)](https://www.inria.fr/)** — National applied-math + HPC institute, multi-site (Paris, Sophia, Bordeaux, Grenoble). Olivier Pironneau (mesh adaptation, optimal control), birthplace of [FreeFEM](https://freefem.org/).
- **[MPI for Mathematics in the Sciences, Leipzig](https://www.mis.mpg.de/)** — Wolfgang Hackbusch's institute. Hackbusch invented multigrid (1976); the institutional lineage anchors Module 05.
- **[ETH Zurich SAM (Seminar for Applied Mathematics)](https://math.ethz.ch/sam)** — Christoph Schwab and Ralf Hiptmair lead Europe's strongest concentration of FEM theory and UQ.
- **[Oxford Mathematical Institute, Numerical Analysis Group](https://www.maths.ox.ac.uk/groups/numerical-analysis)** — Lloyd N. Trefethen, Endre Süli. Anchors the curriculum's reading list for Modules 04+.
- **[Cambridge DAMTP](https://www.damtp.cam.ac.uk/)** — Department of Applied Mathematics and Theoretical Physics. Lighthill, Batchelor lineage; modern fluid mechanics and continuum modelling.
- **[Imperial College London Mathematics](https://www.imperial.ac.uk/mathematics/)** — Colin Cotter; the [Firedrake project](https://www.firedrakeproject.org/) home.
- **[Heidelberg IWR (Interdisciplinary Center for Scientific Computing)](https://www.iwr.uni-heidelberg.de/)** — Peter Bastian's group; home of [DUNE](https://dune-project.org/), Hans Georg Bock's optimization-and-control lineage.
- **[TU Munich (TUM) Munich Center for Computational Sciences](https://www.mcsc.tum.de/)** — Hans-Joachim Bungartz (sparse grids); home of [JAX-Fluids](https://github.com/tumaer/JAXFLUIDS) and [PhiFlow](https://github.com/tum-pbs/PhiFlow).
- **[EPFL Mathematics](https://www.epfl.ch/schools/sb/research/math/)** — Marco Picasso (FEM); historically Annalisa Buffa.
- **[KTH Royal Institute of Technology, Stockholm](https://www.kth.se/en/sci/institutioner/math)** — Anders Logg's FEniCS contributions.
- **[Edinburgh ICMS (International Centre for Mathematical Sciences)](https://www.icms.org.uk/)** — Workshop host for European applied-math community.
- **[BCAM — Basque Center for Applied Mathematics](https://www.bcamath.org/)** — Bilbao. Strong in computational mechanics, biomechanics.
- **[ICTP — Abdus Salam International Centre for Theoretical Physics, Trieste](https://www.ictp.it/)** — Mathematical physics, applied-PDE workshops with global-south outreach.

### Asia and Pacific

- **[RIKEN Center for Computational Science (R-CCS), Kobe, Japan](https://www.r-ccs.riken.jp/en/)** — Home of [Fugaku supercomputer](https://www.r-ccs.riken.jp/en/fugaku/about/). Climate, materials, life sciences PDE workloads.
- **[JAXA (Japan Aerospace Exploration Agency)](https://www.jaxa.jp/)** — Aerospace CFD.
- **[Tsinghua University](https://www.tsinghua.edu.cn/en/)** and **[Peking University](https://english.pku.edu.cn/)** — Major applied-math groups in PRC.
- **[NUS Centre for Computational Science (Singapore)](https://www.science.nus.edu.sg/)**
- **[Australian National University, Mathematical Sciences Institute](https://maths.anu.edu.au/)** — Applied math + climate.

### Cross-institutional and online

- **[Santa Fe Institute](https://www.santafe.edu/)** — Complex-systems framings; Crutchfield, West, Kauffman lineage.
- **[IPAM at UCLA](https://www.ipam.ucla.edu/)** — Long-program semesters where SciML consensus gets worked out.
- **[SIAM Activity Group on Computational Science and Engineering](https://www.siam.org/Membership/Activity-Groups/Detail/computational-science-and-engineering)** — The professional community; runs the SIAM CSE conference.

## Open-source PDE software

### FEM and multi-physics frameworks

| Project | Origin / lead | Niche |
|---|---|---|
| [FEniCS](https://fenicsproject.org/) | SIMULA / KTH (Logg, Langtangen) | Python FEM; UFL weak-form compilation |
| [Firedrake](https://www.firedrakeproject.org/) | Imperial (Cotter, Ham) | FEniCS-fork; tighter PETSc + adjoint integration |
| [dolfin-adjoint / pyadjoint](https://www.dolfin-adjoint.org/) | Simula / Imperial | Automatic adjoint for FEniCS / Firedrake |
| [deal.II](https://www.dealii.org/) | Heidelberg / Texas A&M | C++ FEM; the reference for adaptive mesh refinement |
| [NGSolve](https://ngsolve.org/) | TU Wien (Schöberl) | Python/C++ FEM; HDG, mixed methods |
| [MOOSE](https://mooseframework.inl.gov/) | Idaho National Lab | Multi-physics; nuclear-reactor scale |
| [DUNE](https://dune-project.org/) | Heidelberg IWR (Bastian) | Modular FEM/FV/DG in C++ |
| [FreeFEM](https://freefem.org/) | INRIA / Sorbonne (Pironneau) | DSL-driven FEM; large French ecosystem |
| [Elmer](https://www.elmerfem.org/) | CSC Finland | Multi-physics FEM |
| [Code_Aster](https://www.code-aster.org/) | EDF (France) | Solid-mechanics FEM (industrial) |
| [Gridap.jl](https://gridap.github.io/Gridap.jl/) | UPC / IGTea | Julia FEM |
| [Ferrite.jl](https://ferrite-fem.github.io/) | Chalmers / community | Julia FEM (Chalmers / community) |

### Finite-volume CFD

- [OpenFOAM](https://www.openfoam.com/) — the dominant open-source CFD package; industrial standard.
- [SU2](https://su2code.github.io/) — Stanford-origin; gradient-based shape and topology optimization via discrete adjoint.
- [Clawpack](https://www.clawpack.org/) — Randall LeVeque's lineage; canonical reference for hyperbolic PDEs and shock capturing.
- [Trixi.jl](https://trixi-framework.github.io/) — Julia-native discontinuous Galerkin solver.
- [Nektar++](https://www.nektar.info/) — high-order spectral/hp element CFD.

### Sparse / scalable linear-algebra and solver toolkits

- [PETSc](https://petsc.org/) (ANL) — the dominant scalable PDE-solver toolkit.
- [Trilinos](https://trilinos.github.io/) (Sandia) — package suite around solvers, partitioning, etc.
- [Kokkos](https://kokkos.org/) (Sandia) — performance-portability templates.
- [hypre](https://hypre.readthedocs.io/) (LLNL) — algebraic multigrid.
- [MFEM](https://mfem.org/) (LLNL) — high-order FEM.
- [SUNDIALS](https://computing.llnl.gov/projects/sundials) (LLNL) — ODE/DAE solvers.
- [AMReX](https://amrex-codes.github.io/amrex/) (LBNL) — block-structured AMR.
- [MAGMA](https://www.icl.utk.edu/research/magma) (UTK / ORNL) — hybrid CPU+GPU LAPACK.
- [MUMPS](https://mumps-solver.org/) — sparse direct solver.
- [SuperLU](https://portal.nersc.gov/project/sparse/superlu/) — sparse direct.
- [ARPACK](https://www.arpack.org/) — large-scale eigenvalue.
- [SuiteSparse](https://people.engr.tamu.edu/davis/suitesparse.html) (Davis, Texas A&M) — UMFPACK, CHOLMOD, etc.

### Mesh generation

Mesh quality is half of every nontrivial PDE simulation. The curriculum's Module 03 example is generated with these tools.

- [Gmsh](https://gmsh.info/) — Christophe Geuzaine and Jean-François Remacle (Liège). The de facto open-source mesh generator. Built-in geometry kernel, OpenCASCADE backend; scriptable in Python and a custom `.geo` DSL; outputs every mesh format you'd want. Pairs natively with FEniCS, Firedrake, deal.II, MFEM.
- [CGAL](https://www.cgal.org/) — Computational Geometry Algorithms Library. C++ reference implementation for triangulations, surface and volume meshing, surface reconstruction, polygon partitioning, alpha shapes, and the algorithms underlying most modern meshers. Originally INRIA / GeometryFactory; broad academic-industrial collaboration.
- [TetGen](https://www.tetgen.org/) — Hang Si (Berlin). Quality tetrahedral mesh generator from PLC (piecewise linear complex) input.
- [Triangle](https://www.cs.cmu.edu/~quake/triangle.html) — Jonathan Shewchuk (Berkeley). Two-dimensional Delaunay triangulation, the reference implementation.
- [MeshPy](https://documen.tician.de/meshpy/) — Andreas Klöckner. Python bindings around TetGen and Triangle.
- [Cubit / Coreform](https://coreform.com/) — Sandia-origin commercial mesher with substantial open-source releases via [Coreform Cubit](https://coreform.com/products/coreform-cubit/learn/).
- [Netgen](https://ngsolve.org/about) — companion to NGSolve (Schöberl).
- [Mmg](https://www.mmgtools.org/) — INRIA. Anisotropic mesh adaptation.
- [iso2mesh](https://iso2mesh.sourceforge.net/) — Qianqian Fang (Northeastern). MATLAB toolbox for generating tetrahedral meshes from medical-image segmentations; widely used in EEG / MEG / DOT / fMRI head-model construction.
- [Meshfix](https://github.com/MarcoAttene/MeshFix-V2.1) — Marco Attene. Mesh repair and self-intersection removal — an essential preprocessing step before any biomedical FEM workflow.

### Visualization

- [VTK](https://vtk.org/) — Visualization Toolkit. The C++ engine underneath ParaView, VisIt, ITK-SNAP, and most scientific visualization tools.
- [ParaView](https://www.paraview.org/) — Kitware. The standard interactive PDE-data visualization GUI; reads MFEM, FEniCS, OpenFOAM output natively.
- [VisIt](https://visit-dav.github.io/visit-website/) — LLNL. Comparable scope to ParaView; stronger on adaptive-mesh-refinement data.
- [PyVista](https://pyvista.org/) — Pythonic VTK; the path of least resistance for in-notebook 3D visualization.
- [Mayavi](https://docs.enthought.com/mayavi/mayavi/) — older Pythonic VTK frontend.

### Differentiable simulators (JAX-first)

- [JAX-CFD](https://github.com/google/jax-cfd) — Google. Pseudospectral and finite-volume Navier-Stokes.
- [JAX-Fluids](https://github.com/tumaer/JAXFLUIDS) — TUM. Differentiable compressible Navier-Stokes; shock capturing, multi-phase.
- [PhiFlow](https://github.com/tum-pbs/PhiFlow) — TUM Physics-based Simulation Group; multi-backend (JAX/PyTorch/TF).
- [Diffrax](https://github.com/patrick-kidger/diffrax) — Patrick Kidger; ODE/SDE/CDE solvers with adjoint.
- [Equinox](https://github.com/patrick-kidger/equinox) — Patrick Kidger; PyTorch-style NN library on JAX.
- [jax-md](https://github.com/jax-md/jax-md) — molecular dynamics in JAX.
- [jwave](https://github.com/m9h/jwave) — differentiable acoustic FWI.

### Differentiable simulators (Julia / SciML)

- [DifferentialEquations.jl](https://docs.sciml.ai/DiffEqDocs/stable/) — the SciML stack's flagship.
- [ModelingToolkit.jl](https://docs.sciml.ai/ModelingToolkit/stable/) — symbolic-numeric modelling.
- [Gridap.jl](https://gridap.github.io/Gridap.jl/), [Ferrite.jl](https://ferrite-fem.github.io/), [Trixi.jl](https://trixi-framework.github.io/) — FEM / DG.

### Neural-operator and SciML libraries

- [neuraloperator](https://github.com/neuraloperator/neuraloperator) — FNO, GNO, Tensor-FNO. Caltech-NVIDIA.
- [DeepXDE](https://github.com/lululxvi/deepxde) — PINN framework, multi-backend.
- [DeepInverse / `deepinv`](https://deepinv.github.io/) — learned-prior inverse problems in PyTorch.
- [Modulus](https://github.com/NVIDIA/modulus) — NVIDIA's SciML framework.

## Textbooks and reference works

### Classical numerics

- LeVeque, R. — *Finite Difference Methods for Ordinary and Partial Differential Equations* (SIAM, 2007). Module 01.
- LeVeque, R. — *Finite Volume Methods for Hyperbolic Problems* (Cambridge, 2002). Module 02.
- Trefethen, L. N. — *Spectral Methods in MATLAB* (SIAM, 2000). Module 04. Short, beautiful.
- Boyd, J. P. — *Chebyshev and Fourier Spectral Methods* (Dover, 2001). Module 04.
- Canuto, Hussaini, Quarteroni, Zang — *Spectral Methods* (Springer). Reference-level, exhaustive.
- Hesthaven & Warburton — *Nodal Discontinuous Galerkin Methods* (Springer, 2008).
- Karniadakis & Sherwin — *Spectral/hp Element Methods for CFD* (Oxford, 2005).
- Brenner & Scott — *The Mathematical Theory of Finite Element Methods* (Springer, 2008). FEM theory.
- Brezzi & Fortin — *Mixed and Hybrid Finite Element Methods* (Springer, 1991).
- Hackbusch, W. — *Multi-Grid Methods and Applications* (Springer, 1985). Module 05; the canonical reference.
- Briggs, Henson, McCormick — *A Multigrid Tutorial* (SIAM, 2000). The teaching companion.

### Numerical analysis and linear algebra

- Trefethen & Bau — *Numerical Linear Algebra* (SIAM, 1997). The textbook to read first.
- Strang, G. — *Computational Science and Engineering* (Wellesley-Cambridge, 2007).
- Iserles, A. — *A First Course in the Numerical Analysis of Differential Equations* (Cambridge).
- Süli & Mayers — *An Introduction to Numerical Analysis* (Cambridge).
- Quarteroni, Sacco, Saleri — *Numerical Mathematics* (Springer).
- Press, Teukolsky, Vetterling, Flannery — *Numerical Recipes*, 3rd ed. (Cambridge, 2007).

### History and philosophy

- Lynch, P. — *The Emergence of Numerical Weather Prediction: Richardson's Dream* (Cambridge, 2006). Definitive history of Richardson, ENIAC, and the chain in between.
- Aspray, W. — *John von Neumann and the Origins of Modern Computing* (MIT, 1990).

## Online courses and pedagogical onramps

- [**12 steps to Navier-Stokes**](https://github.com/barbagroup/CFDPython) (Lorena Barba) — Twelve Python notebooks taking the reader from 1D linear convection to 2D incompressible Navier-Stokes. Genuinely the best free CFD onramp; pairs perfectly with Module 02.
- **Lloyd N. Trefethen's Oxford DPhil scientific-computing courses** — biennial graduate-level scientific computing instruction at Oxford NA, gateway course for incoming DPhil students. Trefethen moved to Harvard as Professor of Applied Mathematics in Residence in September 2023, but his teaching archive remains at [people.maths.ox.ac.uk/trefethen](https://people.maths.ox.ac.uk/trefethen/), including [video lectures](https://people.maths.ox.ac.uk/trefethen/lectures.html) and the [Chebfun](https://www.chebfun.org/) software tool that anchors his approximation-theory teaching.
- [MIT 18.085 Computational Science and Engineering](https://ocw.mit.edu/courses/18-085-computational-science-and-engineering-i-fall-2008/) (Strang).
- [MIT 18.086 Computing for Engineers](https://ocw.mit.edu/courses/18-086-mathematical-methods-for-engineers-ii-spring-2006/).
- [MIT 16.920 Numerical Methods for PDEs](https://ocw.mit.edu/courses/16-920j-numerical-methods-for-partial-differential-equations-sma-5212-spring-2003/).
- [Stanford CME 306 Numerical Solution of PDEs](https://web.stanford.edu/class/cme306/).
- [Trefethen Approximation Theory and Approximation Practice](https://people.maths.ox.ac.uk/trefethen/atap/) — book + Chebfun-based notebooks.

## Recurring seminars and lecture archives

- [DDPS — Data-Driven Physical Simulations](https://www.librom.net/ddps.html) (LLNL libROM team). Weekly. Recorded archive 2020+.
- [CRUNCH Group YouTube](https://www.brown.edu/research/projects/crunch/) (Karniadakis, Brown). Lecture archive on PINNs, DeepONet.
- [SIAM Visualization (Activity Group)](https://www.siam.org/Membership/Activity-Groups/Detail/computational-science-and-engineering) — recordings from SIAM CSE.
- [Simons Foundation Public Lectures](https://www.simonsfoundation.org/event-series/public-lectures/) — Flatiron CCM and broader applied-math talks.
- [IPAM Workshop YouTube](https://www.youtube.com/c/IPAMUCLA) — long-program tutorial recordings; the closest the field has to a working consensus when one exists.
- [SIAM Conference on Applications of Dynamical Systems (DSWeb)](https://dsweb.siam.org/).

---

_This document grows. Suggestions, corrections, missing institutions and software, additional historical references — all welcome via [Discussion on Hugging Face](https://huggingface.co/datasets/mhough/spinning-up-in-pde/discussions) or PR on either mirror._
