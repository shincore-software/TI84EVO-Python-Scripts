# Materials calculator programs

Use this folder to select Materials programs for the TI-84 Evo Python App. Each file name has seven characters or fewer before `.py`. Source comments are included in these copies.

The source programs with descriptive names are in [Materials](../Materials/README.md). Calculator operation remains unverified.

## Load and run a program

1. Select the program from the table below.
2. Transfer its `.py` file with the software supported by your calculator. Follow the calculator's program-name rules.
3. Open the Python App and run the program.
4. Select the unknown when the program asks for it.
5. Enter the known values in the units shown. Enter numeric values, such as `0.002` or `2e-3`. Do not enter expressions such as `2*3`.
6. Read the result and its units. If the program reports invalid values, check your data and run it again.

Transfer only the programs you need. The full folder can exceed the available Python memory. Do not transfer this README or the desktop test files.

Before use, run [TICHECK.py](../Materials/TICHECK.py) from the source folder on the calculator. Enter `2` when asked. A successful feature check does not test every solver. Check each required program with a known example on your calculator and OS.

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
| DIFFUSE.py | Arrhenius diffusion and concentration profiles | Follow the selected mode's prompts |
| ERF.py | erf, erfc, inverse erf, and diffusion ratio | No units |
| FARADAY.py | Deposited mass from electric current | kg, A, s, kg/mol; n has no units |
| FICK.py | Steady diffusion: Fick's first law | kg/(m^2*s), m^2/s, kg/m^3, m |
| FRAC.py | Convert mole fractions and weight fractions | g/mol; fractions have no units |
| HEAT.py | Sensible heat: Q = m*cp*(Tf-Ti) | J, kg, J/(kg*K), K |
| INVERF.py | Inverse erf and inverse diffusion ratio | No units |
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

- The programs do not convert units. Convert your data before entry.
- Use kelvin for absolute temperatures. A temperature difference in kelvin has the same numerical value as a difference in degrees Celsius.
- Enter fractions as numbers from zero to one, not percentages. Component fractions must sum to one within the program's tolerance.
- Component distribution programs accept up to 20 components.
- For Faraday's law, enter molar mass in **kg/mol**. Most polymer programs use **g/mol**.
- For Nernst potential, enter a positive dimensionless activity relative to the standard state. Check that the equation sign matches your half reaction.

## Model limits

Use each equation only when its assumptions match the problem. Diffusion concentration uses a semi-infinite solid with constant diffusivity and constant surface concentration. Heat conduction assumes steady flow through a plane layer. Thermal penetration is an estimate. The error-function programs use numerical approximations.

Some inverse calculations have no unique answer. The weight-average molecular-weight equation can give two positive component masses. Use other data to select the applicable result.

## Source and verification

Edit the descriptive files in `Materials` first, then update these copies. A change to a source file does not automatically change its load copy.

Desktop Python checks do not confirm TI-Python operation. Test the transferred files on the target calculator before use in an exam or lab.
