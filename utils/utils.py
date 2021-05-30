def levenshtein_distance(string1, string2):
    if len(string1) < len(string2):
        string1, string2 = string2, string1
    if len(string2) == 0:
        return len(string1)
    prev_row = range(len(string2) + 1)
    for i, col1 in enumerate(string1):
        curr_row = [i + 1]
        for j, col2 in enumerate(string2):
            curr_row.append(min(prev_row[j + 1] + 1, curr_row[j] + 1, prev_row[j] + (col1 != col2)))
        prev_row = curr_row
    return prev_row[-1]
