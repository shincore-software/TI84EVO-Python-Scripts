"""Run desktop checks. This does not confirm calculator support."""
from pathlib import Path
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
from math import log

ROOT = Path(__file__).resolve().parents[1] / "materials_load"
FILES = {'amount_transported': 'AMOUNT', 'cell_voltage': 'CELL_V', 'polymer_chain_length': 'CHAIN', 'heat_conduction': 'CONDUCT', 'corrosion_depth': 'CORRODE', 'percent_crystallinity': 'CRYSTAL', 'degree_of_polymerization': 'DEGPOLY', 'diffusion': 'DIFFUSE', 'erf_solver': 'ERF', 'faraday_law': 'FARADAY', 'fick_first_law': 'FICK', 'fraction_conversion': 'FRAC', 'sensible_heat': 'HEAT', 'latent_heat': 'LATENT', 'linear_expansion': 'LINEXP', 'number_average_molecular_weight': 'MN', 'molar_concentration': 'MOLAR', 'weight_average_molecular_weight': 'MW', 'nernst_potential': 'NERNST', 'oxide_thickness': 'OXIDE', 'parabolic_rate_law': 'PARABOL', 'dispersity': 'PDI', 'heating_power': 'POWER', 'thermal_penetration': 'THDEPTH', 'thermal_diffusivity': 'THDIFF', 'volume_expansion': 'VOLEXP'}


def run(file, answers):
    output = StringIO()
    values = iter(str(x) for x in answers)
    last_line = [0]
    def reply(prompt):
        lines = output.getvalue().splitlines()
        if prompt.startswith(("Select", "Find", "Unknown", "Equation", "Solve")):
            assert len(lines) - last_line[0] + 1 <= 11, (file, prompt, lines[last_line[0]:])
        last_line[0] = len(lines)
        assert len(prompt) <= 30, prompt
        return next(values)
    with patch("builtins.input", side_effect=reply), redirect_stdout(output):
        exec(compile((ROOT / (FILES[file] + ".py")).read_text(), file, "exec"), {})
    assert all(len(line) <= 30 for line in output.getvalue().splitlines()), (file, output.getvalue())
    return output.getvalue()


def result(output):
    line = output.strip().splitlines()[-1]
    return float(line.split("=")[-1].strip().split()[0])


# Each row gives one known solution. Check every unknown against it.
cases = {
    "percent_crystallinity": (["X", "rhoc", "rhos", "rhoa"], [50, 1200, 960, 800]),
    "oxide_thickness": (["x", "dmA", "rho"], [.00003, .1, 5000]),
    "corrosion_depth": (["x", "m", "rho", "A"], [.001, 1, 1000, 1]),
    "dispersity": (["PDI", "Mw", "Mn"], [2, 200, 100]),
    "fick_first_law": (["J", "D", "C1", "C2", "x1", "x2"], [2e-6, 1e-6, 3, 1, 0, 1]),
    "amount_transported": (["m", "J", "A", "t"], [12, 2, 2, 3]),
    "nernst_potential": (["E", "E0", "T", "n", "C"], [.5+8.314*300/(2*96485)*log(10), .5, 300, 2, 10]),
    "cell_voltage": (["Ecell", "Ecath", "Ean"], [1, .8, -.2]),
    "faraday_law": (["m", "I", "t", "M", "n"], [2*100*.05/(2*96485), 2, 100, .05, 2]),
    "molar_concentration": (["C", "m", "M", "V"], [2, 40, 10, 2]),
}
count = 0
for file, (names, values) in cases.items():
    for k, name in enumerate(names):
        answers = [k+1]
        if file == "oxide_thickness":
            answers += [1, 1, 8, 16]
        answers += [v for i, v in enumerate(values) if i != k]
        actual = result(run(file, answers))
        assert abs(actual-values[k]) < 1e-8*max(1, abs(values[k])), (file, name, actual)
        count += 1

thermal = {
    "sensible_heat": {"Q":1200, "m":2, "cp":3, "Tf":500, "Ti":300},
    "heating_power": {"Q":1200, "P":100, "t":12},
    "latent_heat": {"Q":1200, "m":2, "L":600},
    "linear_expansion": {"dL":.002, "alpha":.00001, "L0":2, "dT":100},
    "volume_expansion": {"dV":.006, "av":.00003, "V0":2, "dT":100},
    "heat_conduction": {"q":1200, "k":3, "A":2, "Th":500, "Tc":300, "ell":1},
    "thermal_diffusivity": {"a":.001, "k":3, "rho":1000, "cp":3},
    "thermal_penetration": {"x":2, "a":.1, "t":40},
}
for file, values in thermal.items():
    for target, expected in values.items():
        selection = str(list(values).index(target) + 1)
        def answer(prompt):
            assert len(prompt) <= 30, prompt
            if prompt.startswith("Select"):
                return selection
            key = prompt.split()[0]
            assert key != target, (file, target, prompt)
            return str(values[key])
        output = StringIO()
        with patch("builtins.input", side_effect=answer), redirect_stdout(output):
            exec(compile((ROOT / (FILES[file] + ".py")).read_text(), file, "exec"), {})
        assert all(len(line) <= 30 for line in output.getvalue().splitlines()), (file, output.getvalue())
        actual = result(output.getvalue())
        assert abs(actual-expected) < 1e-8*max(1, abs(expected)), (file, target, output.getvalue())
        count += 1

for mode, expected in [(1, 50000/300), (4, 150)]:
    assert abs(result(run("weight_average_molecular_weight", [mode, 2, 100, .5, 200, .5]))-expected) < 1e-8
    count += 1
assert abs(result(run("fraction_conversion", [1,2,100,.5,200,.5]))-2/3) < 1e-8
assert abs(result(run("fraction_conversion", [2,2,100,1/3,200,2/3]))-.5) < 1e-8
count += 2
for file, inputs, phrase in [
    ("nernst_potential", [4,.5,.5,300,1], "No unique n"),
    ("fick_first_law", [1,-1,3,1,0,1], "D must"),
    ("percent_crystallinity", [2,0,800,800], "no unique"),
    ("sensible_heat", [2,100,1,300,300], "No unique"),
    ("heat_conduction", [1,3,2,500,300,-1], "ell > 0"),
]:
    assert phrase in " ".join(run(file, inputs).split()), file
    count += 1
# Cover the earlier programs as well as the new solvers.
for file, inputs, expected in [
    ("degree_of_polymerization", [2,100,1,50],5000),
    ("number_average_molecular_weight", [1,2,100,.5,200,.5],150),
    ("parabolic_rate_law", [1,4,9],6),
    ("polymer_chain_length", [2,3,10,1],100),
    ("diffusion", [6,1,0,100,.002,1,1e-6],15.7299207),
    ("erf_solver", [3,1e-20],6.60279566),
    ("erf_solver", [3,1e-20],6.60279566),
    ("erf_solver", [3,1],0),
]:
    actual = result(run(file,inputs))
    assert abs(actual-expected) < 1e-6*max(1,abs(expected)), (file,actual)
    count += 1
for file, inputs, phrase in [
    ("volume_expansion", [3,-1,1,1], "V0 must"),
    ("diffusion", [2,1,1e9,1], "numeric range"),
    ("diffusion", [5,1,1e9,1,.1,1,0,1], "numeric range"),
    ("fraction_conversion", [1,100000], "1 to 20"),
]:
    assert phrase in " ".join(run(file,inputs).split()),file
    count += 1
for file in ROOT.glob("*.py"):
    compile(file.read_text(), str(file), "exec")
print(str(count) + " checks passed. All materials_load files compile.")
