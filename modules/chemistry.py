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

if __name__ == "__main__":
    c = ChemistryFunctions({})
    print(c.mass("H2O"))

