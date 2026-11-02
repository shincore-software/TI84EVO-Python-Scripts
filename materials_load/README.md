# Materials calculator programs

Use this folder to select Materials programs for the TI-84 Evo Python App. Each file name has seven characters or fewer before `.py`. Each program starts with an equation name comment.

Calculator operation remains unverified. The source comments name each equation.

## Load and run a program

1. Select the program from the table below.
2. Transfer its `.py` file with the software supported by your calculator. Follow the calculator's program-name rules.
3. Open the Python App and run the program.
4. Select the unknown when the program asks for it.
5. Enter the known values in the units stated in this guide. Enter numeric values, such as `0.002` or `2e-3`. Do not enter unit names or expressions such as `2*3`.
6. Read the result and its units. If the program reports invalid values, check your data and run it again.

Transfer only the programs you need. The full folder can exceed the available Python memory. Do not transfer this README or the desktop test files.

Before use, run [TICHECK.py](TICHECK.py) on the calculator. Enter `2` when asked. A successful feature check does not test every solver. Check each required program with a known example on your calculator and OS.

## Program guide

| File | Calculation | Main units |
|---|---|---|
| AMOUNT.py | Transported mass: m = J*A*t | kg, kg/(m^2*s), m^2, s |
| CELL_V.py | Cell voltage: Ecell = Ecath - Ean | V |
| CHAIN.py | Projected chain length and random-chain distance | nm, degrees; bond count has no units |
| CONDUCT.py | Steady heat conduction through a plane layer | W, W/(m*K), m^2, K, m |
| CORRODE.py | Uniform corrosion depth from mass loss | m, kg, kg/m^3, m^2 |
| CRYSTAL.py | Percent crystallinity from density | percent, kg/m^3 |
| DEGPOLY.py | Degree of polymerization: M = DP*Mbar | g/mol; DP has no units |
| DIFFUSE.py | Arrhenius diffusion and concentration profiles | D and D0: m^2/s; Qd: J/mol; T: K; x: m; t: s; concentrations: kg/m^3 |
| ERF.py | erf, erfc, inverse erf, and diffusion ratio | No units |
| FARADAY.py | Deposited mass from electric current | kg, A, s, kg/mol; n has no units |
| FICK.py | Steady diffusion: Fick's first law | kg/(m^2*s), m^2/s, kg/m^3, m |
| FRAC.py | Convert mole fractions and weight fractions | g/mol; fractions have no units |
| HEAT.py | Sensible heat: Q = m*cp*(Tf-Ti) | J, kg, J/(kg*K), K |
| LATENT.py | Latent heat: Q = m*L | J, kg, J/kg |
| LINEXP.py | Linear thermal expansion | m, 1/K, K |
| MN.py | Number-average molecular weight | g/mol; fractions have no units |
| MOLAR.py | Molar concentration | mol/L, g, g/mol, L |
| MW.py | Weight-average molecular weight | g/mol; fractions have no units |
| NERNST.py | Half-cell potential with the supplied Nernst equation | V, K; activity and n have no units |
| OXIDE.py | Oxide thickness from oxygen mass gain | m, kg/m^2, kg/m^3, g/mol |
| PARABOL.py | Parabolic mass-gain rate law | kg/m^2, kg^2/(m^4*s), s |
| PDI.py | Dispersity: PDI = Mw/Mn | g/mol; PDI has no units |
| POWER.py | Heating energy, power, and time: Q = P*t | J, W, s |
| THDEPTH.py | Thermal penetration estimate: x = sqrt(a*t) | m, m^2/s, s |
| THDIFF.py | Thermal diffusivity: a = k/(rho*cp) | m^2/s, W/(m*K), kg/m^3, J/(kg*K) |
| VOLEXP.py | Volumetric thermal expansion | m^3, 1/K, K |

## Input rules

- The programs do not convert units. Convert your data before entry. The programs do not ask you to select units.
- Use kelvin for absolute temperatures. A temperature difference in kelvin has the same numerical value as a difference in degrees Celsius.
- Enter fractions as numbers from zero to one, not percentages. Component fractions must sum to one within the program's tolerance.
- Component distribution programs accept up to 20 components.
- For Faraday's law, enter molar mass in **kg/mol**. Most polymer programs use **g/mol**.
- For Nernst potential, enter a positive dimensionless activity relative to the standard state. Check that the equation sign matches your half reaction.

## Model limits

Use each equation only when its assumptions match the problem. Diffusion concentration uses a semi-infinite solid with constant diffusivity and constant surface concentration. Heat conduction assumes steady flow through a plane layer. Thermal penetration is an estimate. The error-function programs use numerical approximations.

Some inverse calculations have no unique answer. The weight-average molecular-weight equation can give two positive component masses. Use other data to select the applicable result.

## Source and verification

These files are the single source of truth. Edit them directly. Keep each file name at seven characters or fewer before `.py`.

Desktop Python checks do not confirm TI-Python operation. Test the transferred files on the target calculator before use in an exam or lab.

## Equation reference

The sections below give equations, units, and model limits for the programs.

## Molecular weights

Use masses in g/mol and mole fractions with no units. Fractions must be non-negative and sum to one within 0.001.

The number-average program uses Mn = sum(xi*Mi). The weight-average program uses Mw = sum(xi*Mi^2)/sum(xi*Mi). Each program can find the average, one component mass, or one component fraction. Do not enter a placeholder for the unknown.

A missing fraction follows from the fraction sum. The program also checks the supplied average. A zero fraction cannot give a unique component mass. The weight-average equation can give two positive masses. The program shows both. Use other data to select the correct mass.

## Degree of polymerization

Use M = DP*Mbar. Select DP, M, or Mbar. Use Mn with DPn or Mw with DPw. Mass values use g/mol. DP has no units. Enter Mbar directly or calculate it from mer fractions and mer masses. Mer fractions have no units and must sum to one.

## Polymer chain length

Select L = N*d*sin(theta/2) or r = d*sqrt(N). Then select any variable in that equation. Enter lengths in nm and the bond angle in degrees. N is a bond count with no units. A calculated N is an estimate; check whether an integer bond count fits your data. The angle must be greater than zero and less than 180 degrees. The random-chain equation is a model estimate.

## Diffusion

Modes 1 through 4 solve D = D0*exp(-Qd/(R*T)) for D, D0, Qd, or T. R = 8.314 J/(mol*K). Use D and D0 in m^2/s, Qd in J/mol, and T in K. The program does not ask for units.

Mode 5 calculates concentration from D0, Qd, and T. Use D0 in m^2/s, Qd in J/mol, and T in K. Concentration uses kg/m^3. The program does not ask for units.

Mode 6 solves C = C0 + (Cs-C0)*erfc(x/(2*sqrt(D*t))) for C, C0, Cs, x, t, or D. Use D in m^2/s, x in m, t in s, and C, C0, and Cs in kg/m^3. The program does not ask for units. The model requires constant D, uniform initial concentration C0, constant surface concentration Cs, and a semi-infinite solid. Use an Arrhenius mode first if you need D from temperature.

The program uses an erfc approximation. Boundary values can give no unique finite answer. The program reports those cases.

## Parabolic rate law

Solve delta_m = sqrt(Kp*t) for any variable. Enter mass gain per unit area in kg/m^2, Kp in kg^2/(m^4*s), and time in seconds.

## Error function

Use ERF.py for erf, erfc, inverse erf, or lambda from a diffusion ratio. All inputs and outputs have no units. The programs use numerical approximations.

## Calculator check

These changes have desktop Python checks. Operation on the TI-84 Evo is unverified. Check the math functions, prompts, and results on your calculator and OS before use.


## Additional equation solvers

Each program lets you select the unknown. Use the units in its prompts. Temperature differences in K have the same numerical value as differences in degrees Celsius. Use K for absolute temperatures.

| Program | Equation | Units |
|---|---|---|
| CRYSTAL.py | Xc = 100*rhoc*(rhos-rhoa)/(rhos*(rhoc-rhoa)) | Xc in percent; densities in kg/m^3 |
| HEAT.py | Q = m*cp*(Tf-Ti) | J, kg, J/(kg*K), K |
| POWER.py | Q = P*t | J, W, s |
| LATENT.py | Q = m*L | J, kg, J/kg |
| LINEXP.py | dL = alpha*L0*dT | m, 1/K, m, K |
| VOLEXP.py | dV = alphav*V0*dT | m^3, 1/K, m^3, K |
| CONDUCT.py | q = k*A*(Th-Tc)/ell | W, W/(m*K), m^2, K, m |
| THDIFF.py | a = k/(rho*cp) | m^2/s, W/(m*K), kg/m^3, J/(kg*K) |
| THDEPTH.py | x = sqrt(a*t) | m, m^2/s, s |
| FICK.py | J = -D*(C2-C1)/(x2-x1) | kg/(m^2*s), m^2/s, kg/m^3, m |
| AMOUNT.py | m = J*A*t | kg, kg/(m^2*s), m^2, s |
| NERNST.py | E = E0 + R*T*ln(C)/(n*F) | V, K; n and C have no units |
| CELL_V.py | Ecell = Ecath-Ean | V |
| FARADAY.py | m = I*t*M/(n*F) | kg, A, s, kg/mol; n has no units |
| MOLAR.py | C = m/(M*V) | mol/L, g, g/mol, L |
| OXIDE.py | x = dmA/rho*(a*MM+b*MO)/(b*MO) | m, kg/m^2, kg/m^3; matched molar masses |
| CORRODE.py | x = m/(rho*A) | m, kg, kg/m^3, m^2 |
| PDI.py | PDI = Mw/Mn | PDI has no units; masses in g/mol |
| FRAC.py | wi = xi*Mi/sum(xi*Mi); xi = (wi/Mi)/sum(wi/Mi) | Fractions have no units; masses in g/mol |

The weight-average program also accepts weight fractions and uses Mw = sum(wi*Mi).

The crystallinity equation gives a mass percentage from density. It assumes a material with crystalline and amorphous regions and known phase densities. The expansion equations assume a constant coefficient over the temperature range. The conduction equation assumes steady, one-dimensional flow through a plane layer with constant conductivity. The penetration equation is an estimate, not a temperature-profile solution.

The Nernst program uses the supplied plus-sign half-cell equation. C means dimensionless activity relative to a standard state. A concentration ratio can replace activity only under the ideal-solution approximation. Use the equation sign and reaction convention that match your half reaction. R is in J/(mol*K) and F is in C/mol. Faraday's law assumes that all current causes the stated reaction.

For oxide thickness, dmA is oxygen mass gain per unit area. The oxide formula is M_a O_b. The program solves thickness, oxygen mass gain per area, or oxide density; a, b, and molar masses are known inputs. Uniform corrosion depth assumes uniform mass loss over the stated area.

All new programs require the TI-84 Evo Python App. Their operation on the calculator and its OS remains unverified. No third-party packages or shared program imports are required.

## Desktop checks

Run `python tests/check_materials.py` from the repository root. This checks forward and inverse calculations, fraction conversion, and selected invalid inputs. Desktop checks do not confirm calculator support.

## TI-Python audit

Read [TI_AUDIT.md](TI_AUDIT.md) for the evidence, corrections, transfer limits, and device checks. Run TICHECK.py on the calculator before the solvers. Component distribution programs accept up to 20 components.

## Screen layout

Display text uses short print and input statements, with a maximum of 30 characters per line. Menus use at most eleven lines, including headings, spacing, and the selection prompt. Each numbered choice has its own line. Longer explanations use explicit line breaks. The eleven-line limit does not apply to calculation results. No general screen wrapper or automatic result paging is required.

Select variables with menu numbers. CHAIN first asks for equation 1 or 2, then shows numbered unknowns for that equation. No variable name or unit text is required.
