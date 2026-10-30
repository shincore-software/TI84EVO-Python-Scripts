# Symbolic derivative for arithmetic expressions and log(...).
# Use explicit multiplication. Use x as the variable and uppercase names as constants.

def tokenize(source):
    result = []
    i = 0
    while i < len(source):
        ch = source[i]
        if ch == " ":
            i = i + 1
        elif ch in "+-*/^()":
            result.append(ch)
            i = i + 1
        elif ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            start = i
            while i < len(source) and source[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789":
                i = i + 1
            result.append(source[start:i])
        elif ch in "0123456789.":
            start = i
            dot_count = 0
            while i < len(source) and source[i] in "0123456789.":
                if source[i] == ".":
                    dot_count = dot_count + 1
                i = i + 1
            if dot_count > 1:
                raise ValueError("Invalid number")
            result.append(float(source[start:i]))
        else:
            raise ValueError("Use numbers, x, log, and + - * / ^ ( )")
    result.append("END")
    return result


def parse(source):
    global tokens, pos
    tokens = tokenize(source)
    pos = 0
    tree = parse_sum()
    if tokens[pos] != "END":
        raise ValueError("Check the expression")
    return tree


def parse_sum():
    global pos
    node = parse_product()
    while tokens[pos] == "+" or tokens[pos] == "-":
        op = tokens[pos]
        pos = pos + 1
        right = parse_product()
        node = (op, node, right)
    return node


def parse_product():
    global pos
    node = parse_power()
    while tokens[pos] == "*" or tokens[pos] == "/":
        op = tokens[pos]
        pos = pos + 1
        right = parse_power()
        node = (op, node, right)
    return node


def parse_power():
    global pos
    node = parse_unary()
    if tokens[pos] == "^":
        pos = pos + 1
        node = ("^", node, parse_power())
    return node


def parse_unary():
    global pos
    if tokens[pos] == "+":
        pos = pos + 1
        return parse_unary()
    if tokens[pos] == "-":
        pos = pos + 1
        return ("neg", parse_unary())
    return parse_atom()


def parse_atom():
    global pos
    token = tokens[pos]
    if isinstance(token, float):
        pos = pos + 1
        return ("num", token)
    if token == "log":
        pos = pos + 1
        if tokens[pos] != "(":
            raise ValueError("Write log(expression)")
        pos = pos + 1
        node = parse_sum()
        if tokens[pos] != ")":
            raise ValueError("Missing )")
        pos = pos + 1
        return ("log", node)
    if isinstance(token, str) and token not in ("END", "+", "-", "*", "/", "^", "(", ")"):
        pos = pos + 1
        if token == "x":
            return ("var", "x")
        return ("var", token)
    if token == "(":
        pos = pos + 1
        node = parse_sum()
        if tokens[pos] != ")":
            raise ValueError("Missing )")
        pos = pos + 1
        return node
    raise ValueError("Expected a number, x, ln(...), or (")


def number(value):
    return ("num", float(value))


def simplify(node):
    op = node[0]
    if op in ("num", "var"):
        return node
    if op == "log":
        return (op, simplify(node[1]))
    if op == "neg":
        child = simplify(node[1])
        if child[0] == "num":
            return number(-child[1])
        return ("neg", child)
    left = simplify(node[1])
    right = simplify(node[2])
    if left[0] == "num" and right[0] == "num":
        a = left[1]
        b = right[1]
        if op == "+": return number(a + b)
        if op == "-": return number(a - b)
        if op == "*": return number(a * b)
        if op == "/" and b != 0: return number(a / b)
        if op == "^": return number(a ** b)
    if op == "+":
        if left == number(0): return right
        if right == number(0): return left
    if op == "-":
        if right == number(0): return left
    if op == "*":
        if left == number(0) or right == number(0): return number(0)
        if left == number(1): return right
        if right == number(1): return left
    if op == "/":
        if left == number(0): return number(0)
        if right == number(1): return left
    if op == "^":
        if right == number(0): return number(1)
        if right == number(1): return left
    return (op, left, right)


def derivative(node):
    op = node[0]
    if op == "num": return number(0)
    if op == "var":
        if node[1] == "x": return number(1)
        return number(0)
    if op == "neg": return ("neg", derivative(node[1]))
    if op == "log": return ("/", derivative(node[1]), node[1])
    u = node[1]
    v = node[2]
    du = derivative(u)
    dv = derivative(v)
    if op == "+": return ("+", du, dv)
    if op == "-": return ("-", du, dv)
    if op == "*": return ("+", ("*", du, v), ("*", u, dv))
    if op == "/": return ("/", ("-", ("*", du, v), ("*", u, dv)), ("^", v, number(2)))
    if op == "^":
        if v[0] == "num":
            return ("*", ("*", v, ("^", u, number(v[1] - 1))), du)
        return ("*", node, ("+", ("*", dv, ("ln", u)), ("/", ("*", v, du), u)))


def show(node):
    op = node[0]
    if op == "num":
        value = node[1]
        if value == int(value): return str(int(value))
        return str(value)
    if op == "var": return node[1]
    if op == "log": return "log(" + show(node[1]) + ")"
    if op == "neg": return "(-" + show(node[1]) + ")"
    return "(" + show(node[1]) + " " + op + " " + show(node[2]) + ")"


try:
    expression = input("Expression in x: ")
    result = simplify(derivative(parse(expression)))
    print("Derivative:")
    print(show(result))
except Exception as error:
    print("Input error:")
    print(error)
