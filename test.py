import re

txt = open("../Level6Words.txt", "r+")
str = txt.read()
txt.close()

key = str
p1 = r"(?= ).+?(?= /)"
pattern1 = re.compile(p1)
words = pattern1.findall(key)

f = open("../words1.txt", "w")
for i in words:
    f.write(i)
    f.write("\n")
f.close()