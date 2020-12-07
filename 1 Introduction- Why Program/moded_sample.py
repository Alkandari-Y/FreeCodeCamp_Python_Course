import os
#Original code available in sample.py
#Took the code and made it run using notes file and os module.

name = input('Enter a file: ')
cwd_path = os.getcwd()
doc_path = os.path.join(cwd_path, '1 Introduction- Why Program', name)
handle = open(doc_path)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(doc_path)
print(counts)

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)