input_text = '%3c%61%20%68%72%65%66%3d%22%6d%61%69%6c%74%6f%3a%6e%6f%74%79%69%61%5f%38%38%38%40%75%6b%72%2e%6e%65%74%22\
%3e%6e%6f%74%79%69%61%5f%38%38%38%40%75%6b%72%2e%6e%65%74%3c%2f%61%3e'

res = []
for i in input_text.rstrip().split('%'):
    if i != '':
        res.append(chr(int(i, 16)))
print(''.join(res))
