from quantulum3 import parser
from utils.mathutils import get_units
import quantities as q

def convert(fro, to):
    fro = get_units(parser.parse(fro)[0].surface)
    quant = q.Quantity(float(fro[0]), fro[1])
    quant.units = to
    return quant
    #return strings

print(convert("234s", "min"))