# Materials

This folder is for materials science programs.

## Molecular weight averages

Enter each molecular weight in the same units. The result uses those units.

### Number-average molecular weight, Mn

Use `number_average_molecular_weight.py`. Enter the number of components. For each component, enter molecular weight `Mi` and mole fraction `xi`. The mole fractions must sum to one.

$$M_n=\sum_i x_iM_i$$

This calculation gives each molecule the same weight in the average.

### Weight-average molecular weight, Mw

Use `weight_average_molecular_weight.py`. Enter the number of components. For each component, enter molecular weight `Mi` and mole fraction `xi`. The program calculates weight fractions `wi` and then calculates `Mw`.

Convert mole fraction to weight fraction with:

$$w_i=\frac{x_iM_i}{\sum_j x_jM_j}$$

$$M_w=\sum_i w_iM_i$$

This calculation gives more influence to components with more mass.

## Degree of polymerization

Use `degree_of_polymerization.py`. Select number average or weight average. Enter `Mn` or `Mw`. Then enter the number of mer types. For each mer type, enter its chain fraction `xj` and molecular weight `Mj`. Chain fractions must sum to one. Use the same mass units for all molecular weights.

First calculate `Mbar`, the average molecular weight (weight) of one mer:

$$\bar M=\sum_j x_jM_j$$

Then calculate degree of polymerization:

$$DP_n=\frac{M_n}{\bar M},\qquad DP_w=\frac{M_w}{\bar M}$$

The result is dimensionless. For a homopolymer, use one mer type with chain fraction one.

## Polymer chain length

Use `polymer_chain_length.py`. Select `L`, `r`, or both. Enter bond length `d` and number of bonds `N`. Enter backbone angle `theta` in degrees when you calculate `L`. Use the units for `d` as the units for the length results.

Select the option to find `d` when you know `r` and `N`:

$$d=\frac{r}{\sqrt{N}}$$

Calculate the projected chain length:

$$L=Nd\sin\left(\frac{\theta}{2}\right)$$

Calculate the average end-to-end distance for a random chain:

$$r=d\sqrt{N}$$

The second equation is a random-chain estimate. Use the angle definition and assumptions from your course.

## Diffusion

Use `diffusion.py`. Select `D`, `D0`, `Qd`, `T`, or `C(x,t)` as the value to calculate. Enter the other values. The program uses `R = 8.314 J/(mol K)`. Enter temperature in kelvin and activation energy `Qd` in joules per mole. Enter the diffusivity units; use the same units for `D` and `D0`. The result includes its units. The program does not convert units.

$$D=D_0\exp\left(-\frac{Q_d}{RT}\right)$$

Select `C(x,t)` to calculate concentration at depth `x` and time `t`. Enter `D0`, `Qd`, `T`, `x`, `t`, initial concentration `C0`, and constant surface concentration `Cs`. Use matching units so `D*t` has units of length squared. For this mode, the program uses the semi-infinite-solid solution with constant surface concentration:

$$\frac{C(x,t)-C_0}{C_s-C_0}=\operatorname{erfc}\left(\frac{x}{2\sqrt{Dt}}\right)=1-\operatorname{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

The program uses an approximation for `erfc`. This solution assumes constant `D`, a uniform initial concentration, and a surface concentration that stays constant.

Use `parabolic_rate_law.py` to solve for `delta_m`, `Kp`, or time `t`:

$$\Delta m=\sqrt{K_p t}$$

The program uses `delta_m` in kg/m^2, time in seconds, and `Kp` in kg^2/(m^4 s). Here, `delta_m` means mass gain per unit area. Convert input values to these units before you enter them. The program does not convert units.

## Error function

Use `erf_solver.py` to calculate approximate `erf(x)` and `erfc(x)`, or to find `lambda` from an area or diffusion concentration ratio. Select the calculation when the program starts. The calculator's TI-Python math module does not list these functions, so the program uses an approximation.

The inverse erf option solves `erf(lambda) = area`. The diffusion option solves:

$$\frac{C-C_0}{C_s-C_0}=\operatorname{erfc}(\lambda)=1-\operatorname{erf}(\lambda)$$

For the diffusion option, enter a ratio greater than zero and at most one. To use the inverse erf option, enter an area greater than -1 and less than 1. The result is dimensionless.

### Fraction terms

- **Mole fraction** `x_i`: moles of component `i` divided by total moles.
- **Chain fraction** `x_j`: number of mer units of type `j` divided by the total number of mer units in the chain composition. Use this fraction to calculate `Mbar`.
- **Weight fraction** `w_i`: mass of component `i` divided by total mass. A heavier mer has a larger weight fraction than its chain fraction.

For the weight-fraction equation, `M_i` is the molecular weight of component `i`. The subscripts identify the components in each sum.
