f1 = open("new3", "r+")
seq = ['First line\n', 'Second line\n', 'Third line\n']
f1.writelines(seq)
print(f1.readlines())
f1.close()