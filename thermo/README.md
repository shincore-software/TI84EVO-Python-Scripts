# Thermodynamics tools

This folder contains small Python tools for thermodynamics calculations. Enter values in the units required by the equation and its constants. The programs do not convert units.

## Interpolation

### `linear_interpolation.py`

Use two known points to estimate a y-value between them. Enter `x0`, `y0`, `x1`, and `y1`, then enter the query value `x`.

$$y=y_0+(x-x_0)\frac{y_1-y_0}{x_1-x_0}$$

### `bilinear_interpolation.py`

Use four corner values in one rectangular cell to estimate `z` at a point inside the cell. Enter the x and y bounds, the four corner values, then the query coordinates. The program requires `x0 < x1` and `y0 < y1`.

## Vapor-liquid equilibrium

### `antoine_equation.py`

Calculate vapor pressure `P` from temperature `T`, or temperature from pressure. Enter Antoine constants `A`, `B`, and `C`. This program uses natural logarithms:

$$\ln(P)=A-\frac{B}{T+C}$$

Use constants whose log base and units match this form.

### `bubble_pressure.py`

Calculate bubble pressure from liquid fractions, activity coefficients, and pure-component saturation pressures:

$$P=\sum_i x_i\gamma_iP_i^{\mathrm{sat}}$$

Enter each component's `x`, `gamma`, and `Psat`. The fractions `x_i` must sum to one. The program can also solve for one selected component value when the other values and total pressure are known.

### `dew_pressure.py`

Calculate dew pressure from vapor fractions, activity coefficients, and saturation pressures:

$$P=\left(\sum_i\frac{y_i}{\gamma_iP_i^{\mathrm{sat}}}\right)^{-1}$$

Enter each component's `y`, `gamma`, and `Psat`. The fractions `y_i` must sum to one. Composition-dependent activity coefficients need a suitable liquid-composition iteration.

### `bubble_temperature.py`

Find bubble temperature at a given pressure. Enter the pressure, a temperature search range, and each component's liquid fraction, activity coefficient, and Antoine constants. The program uses bisection. The range must contain a solution.

### `dew_temperature.py`

Find dew temperature at a given pressure. Enter the pressure, a temperature search range, and each component's vapor fraction, activity coefficient, and Antoine constants. The program uses bisection. The range must contain a solution.

### `flash_solver.py`

Find vapor fraction `V` from feed fractions `z_i` and equilibrium ratios `K_i`. Enter those values for each component. The program solves:

$$\sum_i\frac{z_i(K_i-1)}{1+V(K_i-1)}=0$$

It then reports liquid and vapor fractions:

$$x_i=\frac{z_i}{1+V(K_i-1)},\qquad y_i=K_ix_i$$

### `activity_coefficients.py`

Calculate binary activity coefficients with one-parameter Margules, two-parameter Margules, van Laar, Wilson, or NRTL. Select a model, enter liquid fraction `x1`, then enter that model's parameters. The program reports `ln(gamma1)`, `gamma1`, `ln(gamma2)`, and `gamma2`.

### `azeotrope.py`

Use mode 1 to compare relative-volatility limits from saturation pressures and infinite-dilution coefficients. Use mode 2 to calculate one-parameter Margules azeotrope composition. Enter saturation pressures and, for mode 2, parameter `A`.

### `infinite_dilution.py`

Select an activity model and component. Enter model parameters and saturation pressure. The program calculates the infinite-dilution activity coefficient and Henry constant.

## Other thermodynamics tools

### `henry_law.py`

Solve for `y`, total pressure `P`, liquid fraction `x`, or Henry constant `H`. Select the unknown and enter the other values:

$$yP=xH$$

### `gibbs_duhem_check.py`

For each data point, enter `x1`, measured activity coefficients, and model activity coefficients. The program reports excess Gibbs energy and the residual in `ln(gamma1/gamma2)`.

### `poynting_factor.py`

Calculate a Poynting factor or solve for a related input. Enter the factor mode or known factor, then enter the required pressure, volume, temperature, and gas constant values:

$$F=\exp\left(\frac{V^l(P-P^{\mathrm{sat}})}{RT}\right)$$

Check the sign convention used in your course before you use this correction in another equation.

### `stability_check.py`

Enter liquid fraction `x1` and the second derivative of `GE/RT`. The program calculates:

$$\frac{1}{x_1x_2}+\frac{d^2(G^E/RT)}{dx_1^2}$$

A positive result indicates local stability for this test. This tool does not calculate phase compositions.

### `excess_gibbs_temperature.py`

Estimate end `GE/RT` from start `GE/RT` and a constant excess enthalpy. Enter `R`, start and end temperatures, start `GE/RT`, and `HE`. The program assumes `HE` is constant.

$$\frac{\partial(G^E/RT)}{\partial T}=-\frac{H^E}{RT^2}$$

## Calculator limits

These programs use simple input and output. Check them on the target TI-84 Evo before relying on them in an exam or lab. Several programs require model assumptions and coefficient values from the course material.
