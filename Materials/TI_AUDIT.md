# TI-Python compatibility audit

Date: 2026-11-02. Scope: Materials programs.

## Result

The Materials programs use built-ins and math only. No desktop file, network, process, or third-party module is required. The desktop suite passes 94 checks and compiles all Materials files. This is not proof of operation on the TI-84 Evo. No calculator or TI interpreter was available for this audit.

The [Evo Python page](https://education.ti.com/en/product-resources/eguides/eguide-84-evo/python) links to the [CE Python reference guide](https://education.ti.com/-/media/ti/education/files/product-resources/guide/ti-pyappprgg_v570_en.pdf). Its appendix lists the built-ins and math functions used here, including dictionaries, sum, exceptions, exp, log, sqrt, sin, asin, radians, and degrees. This is CE reference evidence. It does not confirm each feature on an Evo OS version.

## Corrections

- Diffusion reports numeric range errors instead of an unhandled overflow or zero divisor. It checks for a diffusivity-time product that becomes zero.
- The inverse error-function programs solve small diffusion ratios directly with erfc. They do not subtract a small ratio from one. A ratio of 1e-20 gives approximately 6.6028 with the approximation used here.
- Initial volume must be positive.
- Component distribution programs accept 1 to 20 components. This is a project memory limit, not a measured calculator limit.
- The chain program lists variable names without a string join method.
- Desktop behavior checks now include all 27 equation programs.

## Transfer and device checks

1. Record your calculator model, OS, and Python App version.
2. Transfer Materials/TICHECK.py under a name permitted by the calculator. Run it and enter 2. It must show Feature checks passed and a small value close to 1e-20. This test checks basic features only.
3. Transfer one solver at a time. Use the calculator's file-name rules. The descriptive repository names may need shorter transfer names. Programs have no shared imports, so this does not change their calculations.
4. Run a known example and each required inverse mode on the calculator. Check long prompts, input entry, and result display. A useful conduction example is q=1200 W, k=3 W/(m*K), A=2 m^2, Th=500 K, Tc=300 K, ell=1 m.
5. Do not transfer tests/check_materials.py. It uses desktop test modules.

The CE guide gives a shared 50K Python space limit. The Materials source files together exceed this value. Do not assume that all files can be loaded at once. Exact Evo storage limits, source conversion size, runtime memory, and supported transfer names remain unverified.

## Remaining limits

Inputs must be numeric literals, not expressions such as 2*3. Most solvers do not repeat a prompt after nonnumeric input. Extreme values can exceed numeric range in other equations. The erf functions are approximations; small tail values have limited accuracy. Calculated bond counts are continuous estimates. No claim of full calculator compatibility is made until device checks pass.
