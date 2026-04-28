# Part 1 — Finite Differences and the CFL Condition

*Why the worst baseline in every neural-operator paper is also the most important number on the chart.*

---

## The forgotten loser at the bottom of the chart

Open any PDEBench plot. The Fourier Neural Operator wins. The U-Net is a step behind. There's a PINN somewhere in the middle, and at the bottom of the chart, often unlabelled, there is a thin grey line: the classical finite-difference solver. It is the *baseline*. It is older than electronic computers. It is the line everything else is measured against.

This article is about that line.

The scheme it represents — Forward-Time, Centred-Space, or **FTCS** — is so old that the first person who tried to use it to forecast the weather did so by hand, in 1916, in a notebook he carried through the front lines of the First World War. His forecast was catastrophically wrong. Twelve years later, three mathematicians explained why. Twenty years after that, a small team at Princeton ran the same scheme on ENIAC, got the right answer, and the modern field of computational fluid dynamics began.

Today, when you look at a PDEBench plot and dismiss the grey line at the bottom, you are looking at the direct technical descendant of that 1916 notebook. Understanding why it works — and exactly when it doesn't — is the first move in spinning up on PDE solvers.

## 1768: Euler takes a step

The story has to begin with Euler. In *Institutionum Calculi Integralis* (Volume 1, 1768), Leonhard Euler describes the scheme that bears his name: to integrate dy/dt = f(t, y), pick a small step h, and compute

```
y(t + h) ≈ y(t) + h · f(t, y(t)).
```

This is the simplest possible numerical method for an ordinary differential equation. It is also the seed from which finite-difference schemes for partial differential equations grow. The rule is the same: where the differential equation calls for a derivative, replace the derivative with a difference quotient on a grid, and march.

For a PDE, "the grid" gains a second dimension. The 1D heat equation,

```
∂u/∂t = α · ∂²u/∂x²,
```

becomes — under the FTCS recipe — a grid of values `u[i, n]` indexed by spatial cell `i` and timestep `n`, related by:

```
u[i, n+1] = u[i, n] + α · (Δt / Δx²) · (u[i+1, n] - 2·u[i, n] + u[i-1, n]).
```

The right-hand side uses only values at the current timestep `n`. To advance the simulation, you sweep across `i` once per timestep. This is finite differences in three lines.

It is also, exactly, what Lewis Fry Richardson tried to do to the atmosphere.

## 1910–1922: Richardson and the forecast factory

Lewis Fry Richardson was a Quaker mathematician working at the British Meteorological Office. In 1910 he had begun working out, on paper, what it would take to forecast the weather numerically. The atmosphere obeys equations — primitive equations, derived from Navier-Stokes plus thermodynamics — and Richardson realised that you could in principle discretise them on a grid, apply finite differences, and march forward in time. He spent the war years driving an ambulance in the Friends' Ambulance Unit on the Western Front, working on his manuscript between calls, and lost it twice. (Once to the wreckage of a bombed-out billet; the second time he rewrote it from memory.)

In 1922 the manuscript was published as *Weather Prediction by Numerical Process*, and it included a six-hour test forecast — performed by Richardson himself, by hand, over a small region of central Europe. Two columns on a single page contained the entire forecast: pressure tendency, wind tendency, the works. The pressure changes he predicted were two orders of magnitude larger than anything ever observed in the actual atmosphere.

It was a complete numerical disaster. And he knew it; he says so in the book.

But Richardson also estimated, on the back of an envelope, the human compute requirements to make the scheme run faster than the real weather. His answer was 64,000 people, seated in a vast circular amphitheatre, each operating a desk calculator on one finite-difference cell, with conductors orchestrating them like an orchestra. He called it the **forecast factory**, and it remains the most beautiful pre-electronic vision of parallel computing on record. It is the spiritual ancestor of every TPU pod since.

What Richardson did *not* know was why his hand-rolled FTCS scheme had blown up. He blamed the data — initial conditions weren't smooth enough, and high-frequency noise had amplified. He was *partly* right, but not completely. The deeper reason had to wait six years.

## 1928: Courant, Friedrichs, and Lewy

In 1928, Richard Courant, Kurt Friedrichs, and Hans Lewy published a paper in *Mathematische Annalen* with a title that, translated, reads "On the partial difference equations of mathematical physics." It is the paper that introduced the **CFL condition** — the stability bound that bears their initials — and it explained, mathematically, what had gone wrong with Richardson's 1922 forecast.

The argument runs as follows. For a hyperbolic PDE — say, the wave equation `∂u/∂t = c · ∂u/∂x` — information travels at finite speed `c`. If you discretise the equation on a grid with cell size `Δx` and march forward with timestep `Δt`, the *numerical* domain of dependence (the cells the scheme actually reads from to compute the next value) must contain the *physical* domain of dependence (the cells where the true PDE solution depends on the past). If `Δt` is too large for `Δx`, the physical signal can outrun the numerical scheme — the scheme cannot "see" the data it needs — and the simulation diverges.

For the 1D wave equation with FTCS, the bound is:

```
c · Δt / Δx ≤ 1.
```

For the 1D heat equation, the bound has a different form because the heat equation has infinite signal speed but vanishing high-frequency growth:

```
α · Δt / Δx² ≤ 1/2.
```

This is the **diffusion CFL number**. When you choose `Δt` larger than `Δx² / (2α)`, the scheme amplifies high-frequency Fourier modes by a factor greater than 1 each timestep. After a few hundred steps, those modes blow up to numerical infinity. This is, with hindsight, exactly what happened to Richardson — he used a one-hour timestep on a grid where stability required minutes.

The CFL condition is the **first thing to know** about any explicit time-marching PDE solver, and it is the first thing this curriculum has you observe directly. We will run FTCS at `r = 0.4`, watch it work; run it at `r = 0.6`, watch it fail; and look at the eigenvalues of the update matrix to see *why*.

## 1947–1950: ENIAC and the first numerical forecast

Twenty-five years after Richardson, John von Neumann arrived at the Institute for Advanced Study in Princeton with a problem and a tool. The problem was numerical weather prediction — the same one Richardson had attacked. The tool was ENIAC, the U.S. Army's room-sized vacuum-tube computer at Aberdeen Proving Ground.

In April 1950, Jule Charney, Ragnar Fjørtoft, and von Neumann ran the first successful numerical weather forecast on ENIAC. They simplified the atmosphere to a single 2D barotropic vorticity equation — abandoning Richardson's full primitive equations — and used a finite-difference scheme on a 270 × 220 km grid covering North America. Each 24-hour forecast required about 24 hours of ENIAC time, including human re-wiring between phases. The forecasts were imperfect but recognisably useful.

What the Princeton team had that Richardson did not was **von Neumann stability analysis** — a systematic way to test whether a finite-difference scheme amplifies or damps Fourier modes, and therefore whether it satisfies the CFL bound. Von Neumann derived it in unpublished notes in 1944 and 1947; Crank and Nicolson, working in Britain in 1947, used the same idea to construct an unconditionally stable implicit scheme for the heat equation. The Crank-Nicolson scheme — average the spatial derivatives at timestep `n` and `n+1`, solve a tridiagonal system per step — is the workhorse implicit method to this day, and you will implement it in this week's notebook.

By 1955 the U.S. Joint Numerical Weather Prediction Unit was producing daily operational forecasts. The forecast factory had been built, in silicon, with seven orders of magnitude fewer humans than Richardson's amphitheatre.

## 1980s–2010s: the boring baseline era

For the next thirty years, finite differences were everywhere. Numerical Recipes (Press, Teukolsky, Vetterling, Flannery), first published in 1986, dedicated chapters to FTCS, Crank-Nicolson, leapfrog, ADI (alternating-direction implicit), and the explicit-implicit family. Every undergraduate engineering course taught FTCS as the first PDE method. Every research code shipped a finite-difference baseline alongside whatever else was on offer.

This is the period in which finite differences became "boring." Spectral methods (we'll meet them in Module 4) were faster on smooth problems. Finite elements (Module 3) handled complex geometries. Multigrid (Module 5) gave you O(N) elliptic solves. Finite volume (Module 2) was the right choice for shocks. Finite differences became the thing you *compared against*, not the thing you *did*.

But "boring" is not "irrelevant." A boring baseline is what makes a comparison meaningful. When PDEBench reports that FNO achieves 30× lower error than FTCS on a Burgers benchmark, that statement only carries information because everyone reading the paper knows what FTCS is, what its convergence order is, and what its computational cost is. The grey line at the bottom of the chart is doing real work.

## 2022 onwards: PDEBench and the return of the baseline

PDEBench, introduced at NeurIPS 2022 by Takamoto et al., made a deliberate choice that is worth dwelling on. They did not compare neural operators only against each other. They compared them against finite-difference and finite-volume reference solutions, on the same datasets, with the same error metrics. They invented metrics — *spectral RMSE*, *conservation RMSE* — designed to expose where neural methods *under-perform* the classical baseline, not just where they win.

This is a healthy methodological move, and it is part of why PDEBench has become the de facto benchmark for SciML. PDEArena (Microsoft, 2023) followed the same convention. SciMLBenchmarks.jl, in Julia, has been doing it since 2018 with work-precision diagrams that explicitly map cost vs accuracy across classical and ML methods.

For the practitioner, the takeaway is: **when you read a neural operator paper, find the FTCS or finite-volume baseline before you look at the headline number.** The relative gain over that baseline, at the *same wall-clock cost*, is the only number that means anything. The headline number on its own — "0.001 relative L2 error" — could mean a triumph or a tautology, depending on whether the classical method got 0.0001 in less time.

This curriculum trains you to read those plots correctly. We start, this week, by *being* the grey line.

## Hands-on: this week's notebook

The companion notebook for this module is [`notebooks/01_finite_differences_cfl.py`](../notebooks/01_finite_differences_cfl.py) (jupytext format; convert with `jupytext --to notebook 01_finite_differences_cfl.py`). It will walk you through:

1. **A NumPy reference implementation** of FTCS for the 1D heat equation. About thirty lines, no JAX yet, no tricks. This is the line at the bottom of the chart.
2. **A JAX port** with `jax.jit`. Same scheme, ~10× faster on a laptop CPU, no algorithmic change.
3. **The CFL boundary, observed.** Run the scheme at `r = α Δt / Δx² = 0.4` (stable) and `r = 0.6` (unstable). Plot both. Watch one diverge into checkerboard noise.
4. **Von Neumann analysis, by hand.** Compute the amplification factor `g(k) = 1 - 4r sin²(k Δx / 2)` and verify that `|g| ≤ 1` requires `r ≤ 1/2`.
5. **Crank-Nicolson.** The implicit scheme. Tridiagonal solve via `jax.scipy.linalg.solve_banded`. Show that it is *unconditionally stable* — push `r = 5` and watch it stay sane.
6. **Compare to the analytical solution** — a Gaussian initial condition diffuses into a wider Gaussian with known variance growth. Measure the FTCS L2 error.
7. **Your line on the PDEBench plot.** Run the same FTCS solver on a PDEBench-style 1D heat dataset, report the conservation RMSE and spectral RMSE. This is the number an FNO has to beat.

If you complete only one notebook in this curriculum, make it this one. Every later module will treat this material as known.

## Where this leads

Next week (Module 2, Finite Volume and Conservation Laws), we move from the heat equation to Burgers' equation — and immediately discover that FTCS produces *Gibbs oscillations* near shocks, no matter how small your timestep is. The CFL bound gives you stability; it does not give you physics. To capture shocks correctly, we need a different idea: discretise the *integral* form of the conservation law, not the differential form, and write our update as the difference of fluxes through cell faces. That's Godunov 1959, Roe 1981, and the entire shock-capturing literature.

After that, Module 3 takes us into finite elements via Galerkin's method (1915), the Ritz method (1908), and a real-world example: an anisotropic Poisson equation on a tetrahedral mesh of the human head, used for transcranial direct current stimulation modelling. (Source: [`tCS_model.ufl`](https://github.com/m9h/Fijee-Project/blob/master/Fijee/Finite_element_method_models/tCS_model.ufl) in the Fijee-Project repo — a real PDE, in production, with three lines of weak form.)

The journey from Richardson's 1922 amphitheatre to a tetrahedral mesh of someone's brain is shorter than it sounds. Both are finite-difference cousins solving variational problems on grids. The difference is fifty years of mathematical refinement, and it is exactly the kind of context PDEBench leaderboards omit. We're filling it in.

---

## Further reading

**Primary sources:**
- Euler, L. (1768). *Institutionum Calculi Integralis*, Vol. 1.
- Richardson, L. F. (1922). *Weather Prediction by Numerical Process*. Cambridge University Press.
- Courant, R., Friedrichs, K., & Lewy, H. (1928). "Über die partiellen Differenzengleichungen der mathematischen Physik." *Mathematische Annalen* 100: 32–74.
- Charney, J., Fjørtoft, R., & von Neumann, J. (1950). "Numerical Integration of the Barotropic Vorticity Equation." *Tellus* 2: 237–254.
- Crank, J. & Nicolson, P. (1947). "A practical method for numerical evaluation of solutions of partial differential equations of the heat-conduction type." *Proc. Cambridge Phil. Soc.* 43: 50–67.

**Modern textbooks:**
- LeVeque, R. (2007). *Finite Difference Methods for Ordinary and Partial Differential Equations*. SIAM. The clearest modern treatment.
- Press, W. et al. (2007). *Numerical Recipes*, 3rd ed. Chapters 19–20.
- Trefethen, L. N. (1996). *Finite Difference and Spectral Methods for ODEs and PDEs*. Unpublished but widely circulated; available from his Oxford page.

**Historical:**
- Lynch, P. (2006). *The Emergence of Numerical Weather Prediction: Richardson's Dream*. Cambridge University Press. The definitive account of Richardson, ENIAC, and the chain in between.
- Aspray, W. (1990). *John von Neumann and the Origins of Modern Computing*. MIT Press. Chapter 6.

**Modern benchmarks (set up here, deepened in Module 11):**
- Takamoto, M. et al. (2022). "PDEBench: An extensive benchmark for scientific machine learning." *NeurIPS 2022 Datasets and Benchmarks Track*.
- Gupta, J. K. & Brandstetter, J. (2023). "Towards Multi-spatiotemporal-scale Generalized PDE Modeling." *Transactions on Machine Learning Research* (PDEArena).

---

*Next: Part 2 — Finite Volume and Conservation Laws.*
