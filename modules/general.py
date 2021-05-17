from PyDictionary import PyDictionary

async def define(word):
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
        return (f"The word `{word}` does not exist!", False)
    return (ret, True)

async def synonyms(word):
    ret = ""
    syns = PyDictionary.synonym(word)
    if syns is not None:
        ret += f"Synonyms of **{word}**:\n\n`{', '.join(syns)}"[0:2028-len(word)]+"`"
    else:
        return ("There are no synonyms for that word!", False)
    return (ret, True)