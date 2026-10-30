# Python program plans

This file describes how to write each calculator program. The three first programs already exist. The other programs are plans for later work.

## Solver design rule

For each tool, let the user select a meaningful result to calculate. Ask for the required known values and model parameters. Solve for another variable only when the available equations and known values give one unique result. Use an algebraic rearrangement when one is available. Use a numerical solver for an implicit equation. For numerical solving, ask for a valid search range or starting values and report when the solver cannot find a result.

One equation usually cannot give a unique answer for several unknown variables at the same time. Ask for enough independent equations and known values before you solve a system with more than one unknown. Do not treat model parameters as unknowns unless a separate parameter-fitting mode has enough data.

## 1. Linear interpolation

File: `linear_interpolation.py`

Ask which value to solve for. In the current interpolation tool, `x0`, `y0`, `x1`, and `y1` are known, and the user enters `x` to find `y`. To solve for a different value, rearrange the same equation and ask for the other four values. Check for a zero divisor. Check that the result is inside the two-point interval when the user requests interpolation. Allow extrapolation only if the user selects it.

$$
y = y_0 + (x - x_0)\frac{y_1-y_0}{x_1-x_0}
$$

**Useful to solve for:** `y` or `x` when the other values are known. The same equation can solve for one endpoint value when the other values are known.

Display the estimated y-value. The current program follows this method.

## 2. Bilinear interpolation

File: `bilinear_interpolation.py`

Ask which value to solve for. A typical use has the cell bounds, four corner values, and query coordinates as known values, and finds `z`. To solve for a different value, use the bilinear equation and numerical solving if an algebraic rearrangement is not practical. Check that each lower coordinate is less than its upper coordinate. Check that the requested point is inside the cell. State that a single equation does not determine multiple unknown coordinates or corner values at once.

First interpolate along x at the lower and upper y coordinates. Then interpolate between those two results along y. Display the estimated z-value. The current program follows this method.

$$
t_x=\frac{x-x_0}{x_1-x_0},\qquad t_y=\frac{y-y_0}{y_1-y_0}
$$

$$
z=z_{00}+t_x(z_{10}-z_{00})+t_y\left[z_{01}+t_x(z_{11}-z_{01})-z_{00}-t_x(z_{10}-z_{00})\right]
$$

**Useful to solve for:** the interpolated value `z` or one corner value. A query coordinate can also be found with a numerical solver. It can have more than one solution.

## 3. Antoine equation

File: `antoine_equation.py`

Ask whether to solve for pressure `P` or temperature `T`. Treat `A`, `B`, and `C` as input constants. Ask for the known temperature or pressure. Use the natural-log form:

$$
\ln(P) = A - \frac{B}{T+C}
$$

Use these rearrangements:

$$
P = \exp\left(A - \frac{B}{T+C}\right),
\qquad
T = \frac{B}{A-\ln(P)} - C
$$

**Useful to solve for:** `P` or `T`. Treat `A`, `B`, and `C` as known constants.

Check that `P` is positive before taking its logarithm. Check all divisors and denominators. Display the result. The current program follows this method. The user must enter constants and units that match the natural-log form.

## 4. Bubble-point pressure

Ask which value to solve for. The direct mode calculates `P` from known `x_i`, `gamma_i`, and `P_i_sat`. A component mode can calculate one selected `x_i`, `gamma_i`, or `P_i_sat` when all other terms are known. Rearrange the sum for that term. Check that the mole fractions are non-negative and sum to one when the full composition is provided. Calculate:

$$
P = \sum_i x_i \gamma_i P_i^{\mathrm{sat}}
$$

**Useful to solve for:** total pressure `P`, or one component's `x_i`, `gamma_i`, or `P_i_sat` when all other terms are known. A full composition must also satisfy `sum(x_i)=1`.

Display the total pressure. Add an ideal-liquid option that sets every activity coefficient to one only if the user selects it.

## 5. Dew-point pressure

Ask which value to solve for. The direct mode calculates `P` from known `y_i`, `gamma_i`, and `P_i_sat`. A component mode can solve for one selected term if the other terms are known. For composition-dependent activity coefficients, use iteration. Do not try to find multiple unknown composition values from this one equation alone. Calculate:

$$
P = \frac{1}{\displaystyle \sum_i \frac{y_i}{\gamma_i P_i^{\mathrm{sat}}}}
$$

**Useful to solve for:** total pressure `P`, or one component term when all other terms are known. For composition-dependent activity coefficients, solve for the liquid composition and coefficients together with enough independent constraints.

For an ideal liquid, set each activity coefficient to one. For a non-ideal liquid, the activity coefficients depend on the unknown liquid composition. Use an iteration and ask for a convergence tolerance and a maximum iteration count.

## 6. Bubble-point temperature

Ask which value to solve for. For `T`, ask for pressure, liquid composition, Antoine constants, and a starting temperature range. At each trial temperature, calculate each saturation pressure and activity coefficient. Use bisection until the calculated pressure matches the given pressure. For a selected composition or coefficient, rearrange the bubble equation when possible. Require enough known component data. Require a range that brackets a solution for numerical solving.

At each trial temperature, calculate:

$$
P_i^{\mathrm{sat}} = \exp\left(A_i - \frac{B_i}{T+C_i}\right),
\qquad
y_i = \frac{x_i\gamma_i P_i^{\mathrm{sat}}}{P}
$$

**Useful to solve for:** `P_i_sat` or `T` with the Antoine equation when `A_i`, `B_i`, and `C_i` are known. Use the bubble-point condition below to solve for mixture temperature.

The bubble-point condition is:

$$
\sum_i y_i = 1
$$

**Useful to solve for:** bubble-point temperature `T` by numerical search at known pressure and liquid composition. The normalized vapor composition can also be calculated when `T` and `P` are known.

## 7. Dew-point temperature

Ask which value to solve for. For `T`, ask for pressure, vapor composition, Antoine constants, and a starting temperature range. At each trial temperature, calculate saturation pressures and solve for liquid composition and activity coefficients. Adjust temperature with bisection until the dew-point equation is satisfied. For a selected composition or coefficient, require all other needed component values. Do not solve for several unknowns from one dew-point equation.

At each trial temperature, calculate:

$$
P_i^{\mathrm{sat}} = \exp\left(A_i - \frac{B_i}{T+C_i}\right),
\qquad
x_i = \frac{y_i P}{\gamma_i P_i^{\mathrm{sat}}}
$$

**Useful to solve for:** `P_i_sat` or `T` with the Antoine equation when `A_i`, `B_i`, and `C_i` are known. Use the dew-point condition below to solve for mixture temperature.

The dew-point condition is:

$$
\sum_i x_i = 1
$$

**Useful to solve for:** dew-point temperature `T` by numerical search at known pressure and vapor composition. The liquid composition can also be calculated when `T` and `P` are known.

## 8. Isothermal flash

Ask which flash result to solve for. The usual mode finds vapor fraction `V` from known feed fractions `z_i` and equilibrium ratios `K_i`. Other modes can calculate a phase composition from known `V`, `z_i`, and `K_i`. Ask for temperature, pressure, and model data when the tool must calculate `K_i`. Check that the feed fractions sum to one and that each `K_i` is positive. Do not claim that one flash equation can determine several unknown feed and phase values at once.

Evaluate the Rachford-Rice function at vapor fractions zero and one. If the values bracket zero, use bisection to solve for vapor fraction `V`. Then calculate:

$$
y_i = \frac{z_i K_i}{1 + V(K_i-1)},
\qquad
x_i = \frac{y_i}{K_i}
$$

Display `V`, `x_i`, and `y_i`. If the function does not bracket zero, report that the feed is outside the two-phase flash range. State that this check assumes the selected equilibrium model is valid.

Solve the Rachford-Rice equation:

$$
\sum_{i=1}^{N} \frac{z_i(K_i-1)}{1+V(K_i-1)}=0,
\qquad 0\leq V\leq1
$$

For modified Raoult's law, calculate:

$$
K_i = \frac{y_i}{x_i} = \frac{\gamma_i P_i^{\mathrm{sat}}}{P}
$$

**Useful to solve for:** `K_i`, `gamma_i`, `P_i_sat`, or `P` when the other terms are known.

**Useful to solve for in the flash equation:** vapor fraction `V` with bisection. Then calculate liquid and vapor compositions `x_i` and `y_i` from the feed `z_i`, `K_i`, and `V`.

## 9. Binary activity coefficients

Create one program with a model menu: one-parameter Margules, two-parameter Margules, van Laar, Wilson, or NRTL. Ask which result to find: an activity coefficient, its logarithm, a composition value, or one model parameter. Ask for all other required values. Calculate directly or use a numerical solver for a selected parameter that cannot be isolated safely. Check composition limits, zero denominators, and the number of independent equations. Display the selected result and state when several solutions are possible.

For NRTL, also ask for temperature, gas constant `R`, energy parameters `b_12` and `b_21`, and non-randomness parameter `alpha`. Use consistent energy and temperature units.

One-parameter Margules:

$$
\ln\gamma_1=Ax_2^2,
\qquad
\ln\gamma_2=Ax_1^2
$$

Two-parameter Margules:

$$
\ln\gamma_1=x_2^2[A_{12}+2(A_{21}-A_{12})x_1]
$$

$$
\ln\gamma_2=x_1^2[A_{21}+2(A_{12}-A_{21})x_2]
$$

**Useful to solve for in the Margules equations:** `ln(gamma_1)` or `ln(gamma_2)`. Solve for one model parameter from measured activity data when enough independent data are available.

van Laar:

$$
\ln\gamma_1=A'_{12}\left(1+\frac{A'_{12}x_1}{A'_{21}x_2}\right)^{-2},
\qquad
\ln\gamma_2=A'_{21}\left(1+\frac{A'_{21}x_2}{A'_{12}x_1}\right)^{-2}
$$

**Useful to solve for in the van Laar equations:** either logarithmic activity coefficient. Fit a model parameter only from enough independent data.

Wilson:

$$
\ln\gamma_1=-\ln(x_1+x_2\Lambda_{12})+x_2\left(\frac{\Lambda_{12}}{x_1+x_2\Lambda_{12}}-\frac{\Lambda_{21}}{x_2+x_1\Lambda_{21}}\right)
$$

**Useful to solve for in the Wilson equation:** `ln(gamma_1)`. The equation for component 2 can be added to solve for `ln(gamma_2)`. Fit `Lambda` parameters from enough measured data.

NRTL:

$$
\tau_{12}=\frac{b_{12}}{RT},\quad \tau_{21}=\frac{b_{21}}{RT},
\qquad G_{12}=\exp(-\alpha\tau_{12}),\quad G_{21}=\exp(-\alpha\tau_{21})
$$

$$
\ln\gamma_1=x_2^2\left[\tau_{21}\left(\frac{G_{21}}{x_1+x_2G_{21}}\right)^2+\frac{G_{12}\tau_{12}}{(x_2+x_1G_{12})^2}\right]
$$

$$
\ln\gamma_2=x_1^2\left[\tau_{12}\left(\frac{G_{12}}{x_2+x_1G_{12}}\right)^2+\frac{G_{21}\tau_{21}}{(x_1+x_2G_{21})^2}\right]
$$

**Useful to solve for in the NRTL equations:** `ln(gamma_1)` and `ln(gamma_2)`. Calculate `tau` and `G` from the given temperature and model parameters. Fit parameters only when enough independent measurements are available.

## 10. Azeotrope test and composition

Ask which value to find. For the existence test, ask for saturation pressures and infinite-dilution activity coefficients, then calculate both relative-volatility limits. For azeotrope composition, ask for the model parameter and saturation pressures, then calculate composition. Where possible, allow the user to select one missing input such as a saturation pressure or activity coefficient and rearrange the selected equation to solve for it. Report when an equation does not give a unique answer.

For the one-parameter Margules model, also ask for parameter `A`. Calculate the stated azeotrope composition. Check that the result is between zero and one. State that this composition formula applies only to that model and its stated assumptions.

Calculate the relative-volatility limits:

$$
\alpha_{12}(x_1\to0)=\frac{\gamma_1^{\infty}P_1^{\mathrm{sat}}}{P_2^{\mathrm{sat}}},
\qquad
\alpha_{12}(x_1\to1)=\frac{P_1^{\mathrm{sat}}}{\gamma_2^{\infty}P_2^{\mathrm{sat}}}
$$

The stated test predicts an azeotrope if one limit is above one and the other is below one. For one-parameter Margules:

$$
x_1^{\mathrm{az}}=\frac12+\frac{\ln(P_1^{\mathrm{sat}}/P_2^{\mathrm{sat}})}{2A}
$$

**Useful to solve for:** the two relative-volatility limits for the existence test, or azeotropic composition `x_1_az` for the one-parameter Margules model. Treat the saturation pressures and `A` as known inputs.

## 11. Henry's law

Ask which variable to solve for: `y_i`, `P`, `x_i`, or `H_i`. Ask for the other three values. Rearrange:

$$
y_i P = x_i \mathcal{H}_i
$$

**Useful to solve for:** `y_i`, `P`, `x_i`, or Henry's constant `H_i`, when the other three values are known.

Calculate the selected variable. Check that every divisor is non-zero. Display the requested quantity and its units.

## 12. Infinite-dilution coefficients and Henry's constants

Create a model menu for Margules, van Laar, Wilson, and NRTL. Ask which variable to find: an infinite-dilution coefficient, its logarithm, a model parameter, or Henry's constant. Ask for all other required model values. Calculate directly or use numerical solving for a selected parameter. Convert with `gamma_i_inf = exp(ln(gamma_i_inf))`. Calculate:

$$
\mathcal{H}_i = \gamma_i^{\infty}P_i^{\mathrm{sat}}
$$

Display the infinite-dilution coefficient and Henry's constant. Keep pressure units consistent.

Use these infinite-dilution equations:

$$
\text{One-parameter Margules: }\ln\gamma_1^{\infty}=\ln\gamma_2^{\infty}=A_0
$$

$$
\text{Two-parameter Margules: }\ln\gamma_1^{\infty}=A_{12},\quad \ln\gamma_2^{\infty}=A_{21}
$$

$$
\text{van Laar: }\ln\gamma_1^{\infty}=A'_{12},\quad \ln\gamma_2^{\infty}=A'_{21}
$$

$$
\text{Wilson: }\ln\gamma_1^{\infty}=-\ln\Lambda_{12}+1-\Lambda_{21},\quad
\ln\gamma_2^{\infty}=-\ln\Lambda_{21}+1-\Lambda_{12}
$$

$$
\text{NRTL: }\ln\gamma_1^{\infty}=\tau_{21}+\tau_{12}\exp(-\alpha\tau_{12}),\quad
\ln\gamma_2^{\infty}=\tau_{12}+\tau_{21}\exp(-\alpha\tau_{21})
$$

**Useful to solve for:** `ln(gamma_i_inf)` and `gamma_i_inf` for the selected model. The Henry equation then gives `H_i`. Treat model parameters as inputs unless the user supplies data for parameter fitting.

## 13. Gibbs-Duhem consistency check

Ask which result to find: excess Gibbs energy, a residual, or a model parameter. Ask for a small set of measured liquid compositions and activity coefficients. Ask for calculated activity coefficients from a selected model. For each data point, calculate the experimental excess Gibbs energy and the stated residual in `ln(gamma_1/gamma_2)`. Use numerical fitting if the selected unknown is a model parameter. Display each residual and the average residual. Keep the data set small to fit calculator memory.

Report the stated `-0.1` to `+0.1` residual range as a course criterion. Do not label data as valid from this range alone. Also inspect the residual pattern and compare it with course instructions.

Calculate the experimental excess Gibbs energy and residual:

$$
\left(\frac{G^E}{RT}\right)^{\mathrm{exp}}=x_1\ln\gamma_1^*+x_2\ln\gamma_2^*
$$

$$
\delta\ln\left(\frac{\gamma_1}{\gamma_2}\right)=
\ln\left(\frac{\gamma_1^*}{\gamma_2^*}\right)-
\ln\left(\frac{\gamma_1^{\mathrm{calc}}}{\gamma_2^{\mathrm{calc}}}\right)
$$

**Useful to solve for:** experimental `G^E/RT` or the residual at each data point. The residual is a check, not a standalone equation for unknown model parameters.

## 14. Poynting factor

Ask which variable to solve for: the correction factor, liquid molar volume, pressure, saturation pressure, or temperature. Ask for the other values and gas constant. Use algebraic rearrangement for a selected variable. Calculate the exponential factor with consistent units:

$$
\exp\left(\frac{V_i^l(P-P_i^{\mathrm{sat}})}{RT}\right)
$$

**Useful to solve for:** the Poynting factor. With the factor and all but one of `V_i_l`, `P`, `P_i_sat`, or `T` known, rearrange the exponent to solve for the remaining variable.

Display the factor. Keep the correction direction and sign consistent with the course equation used in the related equilibrium calculation.

$$
\Phi_i=\frac{\hat{\phi}_i^v}{\phi_i^{\mathrm{sat}}}
\exp\left[-\frac{V_i^l(P-P_i^{\mathrm{sat}})}{RT}\right]
$$

The standalone Poynting factor in the review packet uses the positive exponent shown above. Confirm the course convention before you combine these expressions; they use opposite signs.

## 15. Liquid-phase stability

Ask which result to find: stability curvature or a model input that controls it. Ask for liquid composition and the second derivative of `G^E/RT` with respect to `x_1`, from a supported activity model or from user input. Calculate:

$$
\frac{1}{x_1x_2} + \frac{d^2(G^E/RT)}{dx_1^2}
$$

Check that `0 < x_1 < 1` and `x_2 = 1 - x_1`. If the result is positive, report local stability for the stated test. If it is zero or negative, report possible instability. This local test alone does not calculate the two equilibrium liquid phases.

$$
\frac{d^2(\Delta G/RT)}{dx_1^2}=
\frac{1}{x_1x_2}+\frac{d^2(G^E/RT)}{dx_1^2}>0
\quad\text{(stable single phase)}
$$

The stated instability condition is:

$$
\frac{d^2(G^E/RT)}{dx_1^2}\leq-\frac{1}{x_1x_2}
$$

**Useful to solve for:** the stability curvature from composition and the excess-Gibbs-energy derivative. The sign gives the local stability result. A composition at the stability limit requires a numerical solve and a model for the derivative.

## 16. Temperature adjustment of excess Gibbs energy

Ask which value to find: final `G^E/RT`, initial `G^E/RT`, or a temperature. Ask for the other required values and a model for excess enthalpy `H^E` as a function of temperature. Integrate:

$$
\frac{\partial(G^E/RT)}{\partial T} = -\frac{H^E}{RT^2}
$$

**Useful to solve for:** final `G^E/RT` from initial `G^E/RT` and `H^E(T)`. A target temperature can be found by numerical search when the target `G^E/RT` and enthalpy model are known.

Use small temperature steps and a numerical integration method. A single `H^E` value is not enough for an accurate temperature adjustment unless the user chooses and accepts a constant-enthalpy approximation. Display the estimated final `G^E/RT` and the assumptions.

## Development order

1. Keep the linear interpolation, bilinear interpolation, and Antoine programs as separate tools.
2. Add bubble-point pressure and Henry's law. These need direct calculations.
3. Add activity-coefficient models and infinite-dilution calculations.
4. Add bubble/dew temperature and pressure calculations. These need iteration.
5. Add flash, consistency, stability, and temperature-adjustment tools. These need more inputs and stronger checks.

Keep each program small enough for the calculator. Ask for only the data that the selected calculation needs.
