# s = 'aaaabbсaaaabbb' is converted into 'a4b2с1a4b3'
s = input()
res = []
n = 0
i = 0
while i < len(s):
    res.append(s[i])
    for j in range(i, len(s)):
        if s[i] == s[j]:
            n += 1
        else:
            break
    res.append(n)
    i = i + n
    n = 0
for i in res:
    print(i, end='')

"""
string = input() + '_'
string = 'aaaabbсaaaabbb '
newstr = []
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        newstr.append(string[i] + str(count))
        count = 1
print(''.join(newstr))
"""
