name = raw_input('Enter file: ')
handle = open(name, 'r')

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = count.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)


#Refer to notes for defintions on the lists below
Sequential_code_lines = [1, 2, 3, 10, 11, 18]
Repeated_code_lines = [5, 6, 7, 8, 13]
Conditional_code_lines = [14, 15, 16]