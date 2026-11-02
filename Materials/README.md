# Materials equation solvers

Select the unknown before you enter the known values. The programs do not convert units. Each prompt gives the required units. A value with no units is dimensionless.

## Molecular weights

Use masses in g/mol and mole fractions with no units. Fractions must be non-negative and sum to one within 0.001.

The number-average program uses Mn = sum(xi*Mi). The weight-average program uses Mw = sum(xi*Mi^2)/sum(xi*Mi). Each program can find the average, one component mass, or one component fraction. Do not enter a placeholder for the unknown.

A missing fraction follows from the fraction sum. The program also checks the supplied average. A zero fraction cannot give a unique component mass. The weight-average equation can give two positive masses. The program shows both. Use other data to select the correct mass.

## Degree of polymerization

Use M = DP*Mbar. Select DP, M, or Mbar. Use Mn with DPn or Mw with DPw. Mass values use g/mol. DP has no units. Enter Mbar directly or calculate it from mer fractions and mer masses. Mer fractions have no units and must sum to one.

## Polymer chain length

Select L = N*d*sin(theta/2) or r = d*sqrt(N). Then select any variable in that equation. Enter lengths in nm and the bond angle in degrees. N is a bond count with no units. A calculated N is an estimate; check whether an integer bond count fits your data. The angle must be greater than zero and less than 180 degrees. The random-chain equation is a model estimate.

## Diffusion

Modes 1 through 4 solve D = D0*exp(-Qd/(R*T)) for D, D0, Qd, or T. R = 8.314 J/(mol*K). Enter Qd in J/mol and T in K. Enter the same diffusivity units for D and D0.

Mode 5 calculates concentration from D0, Qd, and T. Use length and time units that match the diffusivity units.

Mode 6 solves C = C0 + (Cs-C0)*erfc(x/(2*sqrt(D*t))) for C, C0, Cs, x, t, or D. Enter D in m^2/s, x in m, and t in s. Select one concentration unit and use it for all concentrations. The model requires constant D, uniform initial concentration C0, constant surface concentration Cs, and a semi-infinite solid. Use an Arrhenius mode first if you need D from temperature.

The program uses an erfc approximation. Boundary values can give no unique finite answer. The program reports those cases.

## Parabolic rate law

Solve delta_m = sqrt(Kp*t) for any variable. Enter mass gain per unit area in kg/m^2, Kp in kg^2/(m^4*s), and time in seconds.

## Error function

Use erf_solver.py for erf, erfc, inverse erf, or lambda from a diffusion ratio. Use inverse_erf_solver.py for the inverse calculations. All inputs and outputs have no units. The programs use numerical approximations.

## Calculator check

These changes have desktop Python checks. Operation on the TI-84 Evo is unverified. Check the math functions, prompts, and results on your calculator and OS before use.


## Additional equation solvers

Each program lets you select the unknown. Use the units in its prompts. Temperature differences in K have the same numerical value as differences in degrees Celsius. Use K for absolute temperatures.

| Program | Equation | Units |
|---|---|---|
| percent_crystallinity.py | Xc = 100*rhoc*(rhos-rhoa)/(rhos*(rhoc-rhoa)) | Xc in percent; densities in kg/m^3 |
| sensible_heat.py | Q = m*cp*(Tf-Ti) | J, kg, J/(kg*K), K |
| heating_power.py | Q = P*t | J, W, s |
| latent_heat.py | Q = m*L | J, kg, J/kg |
| linear_expansion.py | dL = alpha*L0*dT | m, 1/K, m, K |
| volume_expansion.py | dV = alphav*V0*dT | m^3, 1/K, m^3, K |
| heat_conduction.py | q = k*A*(Th-Tc)/ell | W, W/(m*K), m^2, K, m |
| thermal_diffusivity.py | a = k/(rho*cp) | m^2/s, W/(m*K), kg/m^3, J/(kg*K) |
| thermal_penetration.py | x = sqrt(a*t) | m, m^2/s, s |
| fick_first_law.py | J = -D*(C2-C1)/(x2-x1) | kg/(m^2*s), m^2/s, kg/m^3, m |
| amount_transported.py | m = J*A*t | kg, kg/(m^2*s), m^2, s |
| nernst_potential.py | E = E0 + R*T*ln(C)/(n*F) | V, K; n and C have no units |
| cell_voltage.py | Ecell = Ecath-Ean | V |
| faraday_law.py | m = I*t*M/(n*F) | kg, A, s, kg/mol; n has no units |
| molar_concentration.py | C = m/(M*V) | mol/L, g, g/mol, L |
| oxide_thickness.py | x = dmA/rho*(a*MM+b*MO)/(b*MO) | m, kg/m^2, kg/m^3; matched molar masses |
| corrosion_depth.py | x = m/(rho*A) | m, kg, kg/m^3, m^2 |
| dispersity.py | PDI = Mw/Mn | PDI has no units; masses in g/mol |
| fraction_conversion.py | wi = xi*Mi/sum(xi*Mi); xi = (wi/Mi)/sum(wi/Mi) | Fractions have no units; masses in g/mol |

The weight-average program also accepts weight fractions and uses Mw = sum(wi*Mi).

The crystallinity equation gives a mass percentage from density. It assumes a material with crystalline and amorphous regions and known phase densities. The expansion equations assume a constant coefficient over the temperature range. The conduction equation assumes steady, one-dimensional flow through a plane layer with constant conductivity. The penetration equation is an estimate, not a temperature-profile solution.

The Nernst program uses the supplied plus-sign half-cell equation. C means dimensionless activity relative to a standard state. A concentration ratio can replace activity only under the ideal-solution approximation. Use the equation sign and reaction convention that match your half reaction. R is in J/(mol*K) and F is in C/mol. Faraday's law assumes that all current causes the stated reaction.

For oxide thickness, dmA is oxygen mass gain per unit area. The oxide formula is M_a O_b. The program solves thickness, oxygen mass gain per area, or oxide density; a, b, and molar masses are known inputs. Uniform corrosion depth assumes uniform mass loss over the stated area.

All new programs require the TI-84 Evo Python App. Their operation on the calculator and its OS remains unverified. No third-party packages or shared program imports are required.

## Desktop checks

Run `python tests/check_materials.py` from the repository root. This checks forward and inverse calculations, fraction conversion, and selected invalid inputs. Desktop checks do not confirm calculator support.

## TI-Python audit

Read [TI_AUDIT.md](TI_AUDIT.md) for the evidence, corrections, transfer limits, and device checks. Run TICHECK.py on the calculator before the solvers. Component distribution programs accept up to 20 components.
