f = open('ddab.txt')
lines = f.readline()
start = int(lines[1:5])
f.seek(0)
lines = f.readlines()

f.close()

data = [0]*2600

for line in lines:
    x = int(line[1:5])
    y = int(line[7:11])
    a = int(line[13:])
    data[x] += a
last = x
print(start, last)

f = open('out.txt', "w")
for i in range(start, last):
    f.write(f'{i:5}{data[i]:12}\n')
f.close()
    
