import re
c = "1==2 + 1=4"
print(re.findall("[^=]=[^=]", c))
for i in re.findall("[^=]=[^=]", c):
    c = c.replace(i, f"{i[0]}=={i[-1]}")
print(c)