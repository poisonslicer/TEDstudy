path = "C:/Users/hayst/Documents/pyton/stats/baby.txt"
path1 = "C:/Users/hayst/Documents/pyton/stats/babies.txt"
names = []
f = open(path, "r")
data = f.read().split("\n")
data = [ x.split(",") for x in data ]
print(len(data))
for x in data[1:]:
    if x[1][1:-1].strip() not in names:
        names.append(x[1][1:-1].strip())

f.close()
g = open(path1, "w")
for y in names:
    g.write(y + ",")
g.close()
print("done! " + str(len(names)) + " wrote!")