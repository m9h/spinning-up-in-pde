# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: spinning-up-pde
#     language: python
#     name: spinning-up-pde
# ---

# %% [markdown]
# # Module 01 — Finite Differences and the CFL Condition
#
# Companion to [`articles/pde-series-part1-finite-differences.md`](../articles/pde-series-part1-finite-differences.md).
#
# **Goal:** implement the FTCS (Forward-Time, Centred-Space) scheme for the 1D heat equation in
# JAX, observe the CFL stability boundary directly, and benchmark against an analytical Gaussian
# diffusion solution and an unconditionally stable Crank-Nicolson reference.
#
# By the end you will have *been* the grey baseline line at the bottom of every PDEBench plot,
# and you will know exactly why the line is there.

# %% [markdown]
# ## Setup

# %%
import jax
import jax.numpy as jnp
import numpy as np
import matplotlib.pyplot as plt

jax.config.update("jax_enable_x64", True)
print(f"JAX backend: {jax.default_backend()}  device: {jax.devices()[0]}")

# %% [markdown]
# ## The 1D heat equation
#
# We solve
#
# $$\frac{\partial u}{\partial t} = \alpha \, \frac{\partial^2 u}{\partial x^2},
#   \qquad x \in [0, L], \quad t \in [0, T],$$
#
# with periodic boundary conditions and a Gaussian initial condition,
# $u(x, 0) = \exp\!\bigl(-(x - L/2)^2 / (2\sigma_0^2)\bigr)$.
#
# The exact solution under periodic boundaries on a sufficiently long domain is another Gaussian
# whose variance grows linearly: $\sigma^2(t) = \sigma_0^2 + 2\alpha t$. We will use this for
# error measurement.

# %%
def initial_condition(x: jnp.ndarray, L: float, sigma0: float) -> jnp.ndarray:
    return jnp.exp(-((x - L / 2) ** 2) / (2 * sigma0 ** 2))

def analytical_gaussian(x: jnp.ndarray, t: float, L: float, sigma0: float, alpha: float) -> jnp.ndarray:
    sigma2 = sigma0 ** 2 + 2 * alpha * t
    amp = sigma0 / jnp.sqrt(sigma2)
    return amp * jnp.exp(-((x - L / 2) ** 2) / (2 * sigma2))


# %% [markdown]
# ## The FTCS update
#
# Discretising on a uniform grid $x_i = i \, \Delta x$, $t^n = n \, \Delta t$, with
# $u_i^n \approx u(x_i, t^n)$, the forward-Euler / centred-space scheme is
#
# $$u_i^{n+1} = u_i^n + r \, \bigl( u_{i+1}^n - 2\,u_i^n + u_{i-1}^n \bigr),
#   \qquad r := \alpha \, \Delta t / \Delta x^2.$$
#
# The **diffusion CFL number** $r$ is the only free knob. Stability requires $r \le 1/2$.
# We will verify this directly.

# %%
def ftcs_step(u: jnp.ndarray, r: float) -> jnp.ndarray:
    # Periodic stencil via jnp.roll.
    return u + r * (jnp.roll(u, -1) - 2 * u + jnp.roll(u, 1))

@jax.jit
def ftcs_run(u0: jnp.ndarray, r: float, n_steps: int) -> jnp.ndarray:
    def step(u, _):
        u_next = ftcs_step(u, r)
        return u_next, u_next
    _, traj = jax.lax.scan(step, u0, xs=None, length=n_steps)
    return traj  # shape (n_steps, N)


# %% [markdown]
# ## Stable run: $r = 0.4$

# %%
N = 256
L = 1.0
alpha = 1.0e-2
sigma0 = 0.05
T = 4.0

dx = L / N
x = jnp.linspace(0.0, L - dx, N)
u0 = initial_condition(x, L, sigma0)

r_stable = 0.4
dt_stable = r_stable * dx ** 2 / alpha
n_steps_stable = int(T / dt_stable)
print(f"r = {r_stable}, dt = {dt_stable:.4e}, n_steps = {n_steps_stable}")

traj_stable = ftcs_run(u0, r_stable, n_steps_stable)
traj_stable.block_until_ready()

# %%
fig, ax = plt.subplots(figsize=(8, 4))
times_to_show = [0, n_steps_stable // 4, n_steps_stable // 2, n_steps_stable - 1]
for n in times_to_show:
    t = (n + 1) * dt_stable
    ax.plot(x, traj_stable[n], label=f"t = {t:.2f}")
ax.plot(x, u0, "k--", alpha=0.5, label="t = 0")
ax.set_xlabel("x"); ax.set_ylabel("u")
ax.set_title(f"Stable FTCS (r = {r_stable})")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()


# %% [markdown]
# Smooth Gaussian diffusion. Looks right.

# %% [markdown]
# ## Unstable run: $r = 0.6$
#
# Same scheme, same code, just one knob outside the CFL bound. Watch what happens.

# %%
r_unstable = 0.6
# Use a budget of ~200 steps to make instability obvious without overflowing.
n_steps_unstable = 200
dt_unstable = r_unstable * dx ** 2 / alpha
print(f"r = {r_unstable}, dt = {dt_unstable:.4e}, n_steps = {n_steps_unstable}")

traj_unstable = ftcs_run(u0, r_unstable, n_steps_unstable)
traj_unstable.block_until_ready()

print(f"max |u| at end: {float(jnp.max(jnp.abs(traj_unstable[-1]))):.3e}")

# %%
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
for n, ax in zip([0, 50, 100, 199], (axes[0], axes[0], axes[1], axes[1])):
    ax.plot(x, traj_unstable[n], label=f"step {n}")
axes[0].set_title("Early steps — checkerboard mode emerging")
axes[1].set_title("Late steps — diverged")
for ax in axes:
    ax.set_xlabel("x"); ax.set_ylabel("u"); ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()


# %% [markdown]
# Checkerboard high-frequency mode, amplifying every step. This is exactly what Lewis Fry
# Richardson saw in 1922 — except his pressure tendencies blew up to 145 hPa instead of his
# data norm.

# %% [markdown]
# ## Von Neumann analysis (by hand)
#
# Substitute the trial mode $u_j^n = g^n e^{i k j \Delta x}$ into the FTCS update.
# After cancellation,
#
# $$g(k) = 1 - 4 r \sin^2(k \Delta x / 2).$$
#
# Stability requires $|g(k)| \le 1$ for every wavenumber. The worst case is $\sin^2 = 1$
# (the checkerboard mode, $k\Delta x = \pi$), giving the bound $r \le 1/2$.

# %%
k_dx = np.linspace(0, np.pi, 200)
fig, ax = plt.subplots(figsize=(7, 4))
for r in [0.25, 0.5, 0.6, 0.8]:
    g = 1.0 - 4 * r * np.sin(k_dx / 2) ** 2
    ax.plot(k_dx, g, label=f"r = {r}")
ax.axhline(1.0, color="k", lw=0.6)
ax.axhline(-1.0, color="k", lw=0.6)
ax.fill_between(k_dx, -1, 1, color="green", alpha=0.07, label="stable region")
ax.set_xlabel(r"$k \, \Delta x$"); ax.set_ylabel("amplification factor g(k)")
ax.set_title("Von Neumann analysis of FTCS")
ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()


# %% [markdown]
# Any curve that exits the green band amplifies that wavenumber. The bound $r \le 1/2$ falls
# out by inspection.

# %% [markdown]
# ## Crank-Nicolson — unconditionally stable
#
# Average the spatial Laplacian at $n$ and $n+1$. The update becomes a tridiagonal solve:
#
# $$\bigl(I - \tfrac{r}{2} L\bigr) u^{n+1} = \bigl(I + \tfrac{r}{2} L\bigr) u^n,$$
#
# where $L$ is the periodic discrete Laplacian. The amplification factor is now
# $g(k) = (1 - 2r\sin^2)/(1 + 2r\sin^2)$, which has $|g| \le 1$ for *every* $r > 0$.
# We push $r = 5$ to demonstrate.

# %%
def build_lap_periodic(n: int) -> jnp.ndarray:
    L = -2 * jnp.eye(n) + jnp.eye(n, k=1) + jnp.eye(n, k=-1)
    L = L.at[0, -1].set(1.0)
    L = L.at[-1, 0].set(1.0)
    return L

def crank_nicolson_step(u: jnp.ndarray, r: float, A_minus: jnp.ndarray) -> jnp.ndarray:
    rhs = u + 0.5 * r * (jnp.roll(u, -1) - 2 * u + jnp.roll(u, 1))
    return jnp.linalg.solve(A_minus, rhs)

def crank_nicolson_run(u0: jnp.ndarray, r: float, n_steps: int) -> jnp.ndarray:
    n = u0.shape[0]
    Lmat = build_lap_periodic(n)
    A_minus = jnp.eye(n) - 0.5 * r * Lmat

    def step(u, _):
        u_next = crank_nicolson_step(u, r, A_minus)
        return u_next, u_next

    _, traj = jax.lax.scan(step, u0, xs=None, length=n_steps)
    return traj

# %%
r_implicit = 5.0
dt_implicit = r_implicit * dx ** 2 / alpha
n_steps_implicit = int(T / dt_implicit)
print(f"Crank-Nicolson r = {r_implicit}, dt = {dt_implicit:.4e}, n_steps = {n_steps_implicit}")

traj_cn = crank_nicolson_run(u0, r_implicit, n_steps_implicit)
traj_cn.block_until_ready()

print(f"max |u| at end: {float(jnp.max(jnp.abs(traj_cn[-1]))):.4f}  "
      f"(stable at r = {r_implicit}, ~10x the FTCS limit)")


# %% [markdown]
# ## Comparison against the analytical solution
#
# Both schemes converge in space at $O(\Delta x^2)$. FTCS is $O(\Delta t)$ in time;
# Crank-Nicolson is $O(\Delta t^2)$.

# %%
u_exact_T = analytical_gaussian(x, T, L, sigma0, alpha)
u_ftcs_T = traj_stable[-1]
u_cn_T = traj_cn[-1]

err_ftcs = float(jnp.linalg.norm(u_ftcs_T - u_exact_T) / jnp.linalg.norm(u_exact_T))
err_cn = float(jnp.linalg.norm(u_cn_T - u_exact_T) / jnp.linalg.norm(u_exact_T))
print(f"FTCS  rel-L2 err: {err_ftcs:.4e}")
print(f"CN    rel-L2 err: {err_cn:.4e}")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, u_exact_T, "k", lw=2, label="analytical")
ax.plot(x, u_ftcs_T, "C0--", label="FTCS  r = 0.4")
ax.plot(x, u_cn_T, "C1:", label="Crank-Nicolson  r = 5")
ax.set_xlabel("x"); ax.set_ylabel(f"u(x, T={T})")
ax.set_title("Final-time comparison against analytical Gaussian"); ax.legend(); ax.grid(alpha=0.3)
plt.tight_layout(); plt.show()


# %% [markdown]
# ## PDEBench-style metrics
#
# PDEBench evaluates surrogate models with metrics designed to expose where they fail in ways
# pointwise MSE does not. Two of the most informative are:
#
# 1. **Conservation RMSE** — is total mass / energy conserved? For the heat equation with
#    periodic BCs, $\int u\,dx$ is conserved exactly. We check the discrete analogue.
# 2. **Spectral RMSE** — pointwise error stratified by Fourier wavenumber. Surrogate models
#    often nail low frequencies and miss high ones (or vice versa); a single L2 number hides this.
#
# Here we compute both for our FTCS run. These are the numbers an FNO trained on this problem
# has to beat — and they are also what the FTCS line on a PDEBench chart represents.

# %%
def conservation_residual(traj: jnp.ndarray, dx: float) -> jnp.ndarray:
    mass = jnp.sum(traj, axis=1) * dx
    return mass - mass[0]

def spectral_rmse(u_pred: jnp.ndarray, u_true: jnp.ndarray) -> dict[str, float]:
    Up = jnp.fft.rfft(u_pred)
    Ut = jnp.fft.rfft(u_true)
    err_per_k = jnp.abs(Up - Ut)
    K = err_per_k.shape[0]
    low = float(jnp.sqrt(jnp.mean(err_per_k[: K // 4] ** 2)))
    mid = float(jnp.sqrt(jnp.mean(err_per_k[K // 4 : 3 * K // 4] ** 2)))
    high = float(jnp.sqrt(jnp.mean(err_per_k[3 * K // 4 :] ** 2)))
    total = float(jnp.sqrt(jnp.mean(err_per_k ** 2)))
    return dict(low_k=low, mid_k=mid, high_k=high, total=total)

cons_resid = conservation_residual(traj_stable, dx)
print(f"Conservation drift over run: max |delta mass| = {float(jnp.max(jnp.abs(cons_resid))):.3e}")
print(f"  (FTCS conserves mass to floating-point round-off — this is by construction.)")
print()
sp = spectral_rmse(u_ftcs_T, u_exact_T)
print("Spectral RMSE breakdown vs. analytical:")
for band, val in sp.items():
    print(f"  {band:>6}: {val:.4e}")


# %% [markdown]
# ## Summary
#
# - FTCS for the 1D heat equation is three lines of code; you wrote them.
# - The CFL bound $r \le 1/2$ is *not* a heuristic. Von Neumann analysis derives it from the
#   amplification factor $g(k) = 1 - 4r\sin^2(k\Delta x / 2)$.
# - Crank-Nicolson removes the bound at the cost of a per-step linear solve. For 1D that's a
#   tridiagonal system; for 3D it becomes the elliptic-solve bottleneck that motivates
#   multigrid (Module 5).
# - PDEBench's conservation and spectral RMSE metrics are not harder than pointwise L2 — they
#   just look at the same prediction through more lenses. Surrogate-model papers report them
#   because pointwise L2 hides too much.
#
# **Next module:** [Part 2 — Finite Volume and Conservation Laws](../articles/).
# We move from heat to Burgers, meet the first shock, and discover that FTCS — no matter how
# small you make $\Delta t$ — produces unphysical oscillations near discontinuities.
# That's the moment the field invented finite volume.
