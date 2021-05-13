from quantulum3 import parser
from utils.mathutils import get_units
import quantities as q

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