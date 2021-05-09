from PyDictionary import PyDictionary

def define(word):
    ret = ""
    defs = PyDictionary.meaning(word)
    if defs is not None:
        ret += f"Definitions of **{word}**:\n\n"
        for type in defs:
            ret += f"*{type}*: \n"
            for i, definition in enumerate(defs[type]):
                ret += f"   {i+1}. `{definition}`\n"
            ret += "\n"
    else:
        ret = f"The word `{word}` does not exist!"
    return ret