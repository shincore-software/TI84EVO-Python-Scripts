# Thermodynamics equation reference

This file records the equations for the Chapter 12 and Chapter 13 review topics. Check each equation, model, unit, and parameter convention against the course material before use.

## 1. Bubble-point and dew-point calculations

### Bubble-point pressure

For a liquid mixture with liquid mole fractions `x_i`:

$$
P = \sum_i x_i \gamma_i P_i^{\mathrm{sat}}
$$

### Dew-point pressure

For a vapor mixture with vapor mole fractions `y_i`:

$$
P = \frac{1}{\displaystyle \sum_i \frac{y_i}{\gamma_i P_i^{\mathrm{sat}}}}
$$

If `gamma_i` depends on liquid composition, solve for the liquid composition and activity coefficients iteratively.

### Bubble-point and dew-point temperature

Use the Antoine equation to calculate each saturation pressure. Iterate on temperature until the phase-composition sum is one:

$$
\sum_i y_i = 1 \quad \text{(bubble point)}
$$

$$
\sum_i x_i = 1 \quad \text{(dew point)}
$$

## 2. Isothermal flash calculation

For a feed with mole fractions `z_i`, solve the Rachford-Rice equation for the vapor fraction `V`:

$$
\sum_{i=1}^{N} \frac{z_i (K_i - 1)}{1 + V(K_i - 1)} = 0,
\qquad 0 \leq V \leq 1
$$

For modified Raoult's law:

$$
K_i = \frac{y_i}{x_i} = \frac{\gamma_i P_i^{\mathrm{sat}}}{P}
$$

After you solve for `V`, calculate the phase compositions:

$$
y_i = \frac{z_i K_i}{1 + V(K_i - 1)}
$$

$$
x_i = \frac{y_i}{K_i}
$$

## 3. Binary activity-coefficient models

For a binary mixture:

$$
x_1 + x_2 = 1
$$

### One-parameter Margules model

$$
\ln \gamma_1 = A x_2^2,
\qquad
\ln \gamma_2 = A x_1^2
$$

### Two-parameter Margules model

$$
\ln \gamma_1 = x_2^2 \left[A_{12} + 2(A_{21} - A_{12})x_1\right]
$$

$$
\ln \gamma_2 = x_1^2 \left[A_{21} + 2(A_{12} - A_{21})x_2\right]
$$

### van Laar model

$$
\ln \gamma_1 = A'_{12}
\left(1 + \frac{A'_{12}x_1}{A'_{21}x_2}\right)^{-2}
$$

$$
\ln \gamma_2 = A'_{21}
\left(1 + \frac{A'_{21}x_2}{A'_{12}x_1}\right)^{-2}
$$

### Wilson model

$$
\ln \gamma_1 = -\ln(x_1 + x_2\Lambda_{12})
+ x_2 \left(
\frac{\Lambda_{12}}{x_1 + x_2\Lambda_{12}}
- \frac{\Lambda_{21}}{x_2 + x_1\Lambda_{21}}
\right)
$$

## 4. Azeotrope calculations

### Relative volatility at the pure-component limits

$$
\alpha_{12}(x_1 \to 0) =
\frac{\gamma_1^{\infty} P_1^{\mathrm{sat}}}{P_2^{\mathrm{sat}}}
$$

$$
\alpha_{12}(x_1 \to 1) =
\frac{P_1^{\mathrm{sat}}}{\gamma_2^{\infty} P_2^{\mathrm{sat}}}
$$

The stated test predicts an azeotrope if one limit is greater than one and the other limit is less than one.

### Azeotrope composition for the one-parameter Margules model

$$
x_1^{\mathrm{az}} = \frac{1}{2} +
\frac{\ln\left(P_1^{\mathrm{sat}}/P_2^{\mathrm{sat}}\right)}{2A}
$$

## 5. Henry's law

For a dilute gas dissolved in a liquid:

$$
y_i P = x_i \mathcal{H}_i
$$

The equation can solve for liquid mole fraction `x_i` or partial pressure `y_i P` when you know Henry's constant `H_i`.

## 6. NRTL activity-coefficient model

$$
\tau_{12} = \frac{b_{12}}{RT},
\qquad
\tau_{21} = \frac{b_{21}}{RT}
$$

$$
G_{12} = \exp(-\alpha\tau_{12}),
\qquad
G_{21} = \exp(-\alpha\tau_{21})
$$

$$
\ln \gamma_1 = x_2^2 \left[
\tau_{21}\left(\frac{G_{21}}{x_1 + x_2G_{21}}\right)^2
+ \frac{G_{12}\tau_{12}}{(x_2 + x_1G_{12})^2}
\right]
$$

$$
\ln \gamma_2 = x_1^2 \left[
\tau_{12}\left(\frac{G_{12}}{x_2 + x_1G_{12}}\right)^2
+ \frac{G_{21}\tau_{21}}{(x_1 + x_2G_{21})^2}
\right]
$$

## 7. Infinite-dilution activity coefficients

The following equations give the stated infinite-dilution limits.

### One-parameter Margules model

$$
\ln \gamma_1^{\infty} = \ln \gamma_2^{\infty} = A_0
$$

### Two-parameter Margules model

$$
\ln \gamma_1^{\infty} = A_{12},
\qquad
\ln \gamma_2^{\infty} = A_{21}
$$

### van Laar model

$$
\ln \gamma_1^{\infty} = A'_{12},
\qquad
\ln \gamma_2^{\infty} = A'_{21}
$$

### Wilson model

$$
\ln \gamma_1^{\infty} = -\ln \Lambda_{12} + 1 - \Lambda_{21}
$$

$$
\ln \gamma_2^{\infty} = -\ln \Lambda_{21} + 1 - \Lambda_{12}
$$

### NRTL model

$$
\ln \gamma_1^{\infty} =
\tau_{21} + \tau_{12}\exp(-\alpha\tau_{12})
$$

$$
\ln \gamma_2^{\infty} =
\tau_{12} + \tau_{21}\exp(-\alpha\tau_{21})
$$

### Henry's constant from an infinite-dilution coefficient

$$
\mathcal{H}_i = \gamma_i^{\infty} P_i^{\mathrm{sat}}
$$

## 8. Gibbs-Duhem consistency test

Calculate the experimental excess Gibbs energy:

$$
\left(\frac{G^E}{RT}\right)^{\mathrm{exp}}
= x_1 \ln \gamma_1^* + x_2 \ln \gamma_2^*
$$

Calculate the residual in the activity-coefficient ratio:

$$
\delta \ln\left(\frac{\gamma_1}{\gamma_2}\right)
= \ln\left(\frac{\gamma_1^*}{\gamma_2^*}\right)
- \ln\left(\frac{\gamma_1^{\mathrm{calc}}}{\gamma_2^{\mathrm{calc}}}\right)
$$

The stated criterion is that the average residuals scatter randomly between `-0.1` and `+0.1`.

## 9. Poynting factor and pressure correction

The stated fugacity-coefficient correction is:

$$
\Phi_i = \frac{\hat{\phi}_i^v}{\phi_i^{\mathrm{sat}}}
\exp\left[-\frac{V_i^l(P - P_i^{\mathrm{sat}})}{RT}\right]
$$

The stated Poynting factor is:

$$
\text{Poynting factor} =
\exp\left[\frac{V_i^l(P - P_i^{\mathrm{sat}})}{RT}\right]
$$

## 10. Liquid-phase stability test

For a binary liquid mixture, the stated curvature test is:

$$
\frac{d^2(\Delta G/RT)}{dx_1^2}
= \frac{1}{x_1x_2}
+ \frac{d^2(G^E/RT)}{dx_1^2} > 0
\quad \text{(stable single phase)}
$$

The stated instability condition is:

$$
\frac{d^2(G^E/RT)}{dx_1^2}
\leq -\frac{1}{x_1x_2}
\quad \text{(unstable; liquid phase splitting can occur)}
$$

## 11. Temperature dependence of excess Gibbs energy

The stated temperature relation is:

$$
\frac{\partial(G^E/RT)}{\partial T}
= -\frac{H^E}{RT^2}
$$
