def sort_genotype(genotype):
    if len(genotype) == 4:
        s = sorted([genotype[0], genotype[1]])
        s.extend(sorted([genotype[2], genotype[3]]))
    else:
        s = sorted(genotype)
    return "".join(s)