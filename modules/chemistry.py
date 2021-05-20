from chempy import balance_stoichiometry as b
from molmass import Formula, FormulaError

class ChemistryFunctions():

    def __init__(self, pt: dict):
        self.pt = pt

    async def get_element_name_by_symbol(self, symbol):
        for i, elem in enumerate(self.pt):
            if i > 0 and self.pt[elem]['symbol'].lower() == symbol:
                return self.pt[elem]['name'].lower()
        return None

    def get_all_properties(self, element):
        return self.pt[element]

    def format_property(self, element, property, from_all=False):
        if not from_all:
            return f"{property.upper()} of **{element['name']}**\n\n{property}: {element[property]}\n\n"
        return f"{property}: {element[property]}\n\n"

    def format_all_properties(self, element: dict):
        ret = f"Properties of **{element['name']}**:\n\n"
        for prop in element.keys():
            ret += self.format_property(element, prop, True)
        return ret

    def mass(self, compound):
        try:
            f = Formula(compound)
            ret = f"Mass for **{compound}**:\n```js\n"
            for elem in f.composition():
                ret += f"{elem[0]} x {elem[1]} = {round(elem[2], 2)}\n\n"
            ret += f"Total: {round(f.mass, 2)} g/mol\n```"
        except FormulaError:
            return (f"Something went wrong! `{compound}` is not a valid formula!\nNOTE: Use the chemical symbols when entering formula. (ex Hydrogen = H NOT h)", False)
        return (ret, True)

    def balance(self, compounds):
        try:
            reacs, prods = b(compounds["reacs"], compounds["prods"])
            ret = "**Balanced Equation**:\n```julia\n"
            for reac in reacs:
                ret += f"({reacs[reac]}){reac} + "
            ret = ret[:-2]
            ret += "-> "
            for prod in prods:
                ret += f"({prods[prod]}){prod} + "
            ret = ret[:-2]
            ret += "\n```"
            return (ret, True)
        except Exception:
            ret = "Something went wrong! Couldn't parse equation! Make sure all compounds are correct and seperated by a +."
            return (ret, False)

if __name__ == "__main__":
    c = ChemistryFunctions({})
    c.balance("a + v -> 3 + 2")

