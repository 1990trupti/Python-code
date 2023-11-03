import re

text = '''
abcdefghijklmnopqrstuvwxyz
yyyyyyyy
ABCDEFGHIJKLMNOPQRSTUVWXYZ
yyyyyyyy
45627154
Ha Haha
Metacharacters(Need to be escaped):
yyyyyyy
Mr
MrMmith
Mrs
Mrt

aaab
aaa
hrt
hdj
abc
www.example.com
HDFC1113456
'''
pattern = re.compile("\w\w\w")

# \w --  characters (small or Capital or number or _)
# pattern = re.compile("Mr\w+")
# match =  pattern.findall(text)
# print(match)

# --------------finditer-----------------------------#
# it return a iterator object of the matches found in the string

# matches = pattern.finditer(text)
# matches = pattern.finditer(text, pos=60)  # start with 60th position
# matches = pattern.finditer(text, endpos=60) # will stop at 60th position
# matches = pattern.finditer(text, pos=60, endpos=120) #will start from 60th position and ends with 120th position
# print(matches)
#
# for match in matches:
#     print(match)
    # print(match.string)
    # print(match.start())
    # print(match.end())
    # print(match.span())

# ---------findall - returns the list of all matches

# matches = pattern.findall(text)
matches = pattern.findall(text, pos=60)
# print(matches)


# -------search - returns the first match object
# match = pattern.search(text)
match = pattern.search(text, pos=60)
# print(match)


# ------split() -  splits the results with the match
data = pattern.split(text)
print(data)




