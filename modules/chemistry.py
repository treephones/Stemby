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