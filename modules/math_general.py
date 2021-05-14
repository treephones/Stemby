import math
import re
import numpy as np
import quantities as q
from quantulum3 import parser
import matplotlib.pyplot as plt
from simpleeval import simple_eval, NumberTooHigh, InvalidExpression
from utils.cache import gen_cache_name
from utils.mathutils import get_units

async def convert(fro, to):
    try:
        fro = get_units(parser.parse(fro)[0].surface)
        fro[1] = fro[1].strip()
        #lazy check for temps lol
        if to.strip().lower() in ["f", "c", "k"]:
            to = f"deg{to}"
        if fro[1].lower() in ["f", "c", "k"]:
            fro[1] = f"deg{fro[1]}"
        quant = q.Quantity(float(fro[0]), fro[1])
        quant.units = to
        ret = f"{' '.join(fro)} -> {quant}"
    except IndexError:
        ret = "Something went wrong! Check spelling and only use the actual word or official short form when writing units."
    except ValueError:
        ret = f"Something went wrong! Cannot convert between the units `{fro[1]}` and `{to}`!"
    except LookupError:
        ret = f"One of `{fro[1]}` or `{to}` are spelled incorrectly or do not exist! \n **NOTE**: Do not make short forms plural (ex, use \"sec\" rather than \"secs\" ;) )!"
    except Exception:
        ret = "Something went wrong!"
    return ret

functions = {"log": lambda x: math.log(x),
                 "ln": lambda x: math.log(x, math.e),
                 "sin": lambda x: math.sin(x),
                 "cos": lambda x: math.cos(x),
                 "tan": lambda x: math.tan(x),
                 "arcsin": lambda x: math.asin(x),
                 "arccos": lambda x: math.acos(x),
                 "arctan": lambda x: math.atan(x),
                 "sqrt": lambda x: math.sqrt(x)
                 }

async def evaluate(expression):
    ret = "Evaluated expression:"
    clean_expression = expression.replace("^", "**").replace("pi", str(math.pi)).replace("e", str(math.e))
    try:
        ret += f"```python\n" \
              f"{expression}\n\n" \
              f"=\n\n" \
              f"{simple_eval(clean_expression, functions=functions)}" \
              f"```"
    except NumberTooHigh:
        ret = "Something went wrong! That number is too large to evaluate!"
    except InvalidExpression:
        ret = "Something went wrong! That is an invalid expression!"
    except Exception:
        ret = "Something went wrong!"
    return ret

whitelist = ["sin", "cos", "tan", "sqrt", "x"]
replace = {
    "sin": "math.sin",
    "cos": "math.cos",
    "tan": "math.tan",
    "sqrt": "math.sqrt",
    "^": "**"
}

def graph(expression):
    for word in re.findall('[a-zA-Z_]+', expression):
        if word not in whitelist:
            return f"Something went wrong! `{word}` cannot be used in an expression!"
    for fro, to in replace.items():
        expression.replace(fro, to)
    def f(x):
        return eval(expression)
    x = np.linspace(100, 100, 250)
    plt.plot(x, f(x))
    plt.xlim(100, 100)

    im_id = "test"#gen_cache_name()
    path = f'../caches/graphs/{im_id}.png'
    plt.savefig(path, bbox_inches='tight', pad_inches=0.5)
    plt.close()
    return path

print(graph("x**2"))