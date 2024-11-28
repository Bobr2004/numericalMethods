def sep(inp: list) -> str:
    res = "+"
    for i in inp:
        res += "-" * i + "+"
    return res+"\n"


def pretty_table(a: list, b: list, c: list) -> str:
    mx_a = max(map(len, map(str, a))) + 2
    mx_b = max(map(len, map(str, b))) + 2
    mx_c = max(map(len, map(str, c))) + 2
    result = sep([mx_a, mx_b, mx_c])
    for i in range(len(a)):
        result += "| " + str(a[i]) + " " * (mx_a - len(str(a[i])) - 1)
        result += "| " + str(b[i]) + " " * (mx_b - len(str(b[i])) - 1)
        result += "| " + str(c[i]) + " " * (mx_c - len(str(c[i])) - 1)
        result += "| \n"
        result += sep([mx_a, mx_b, mx_c])
    return result
