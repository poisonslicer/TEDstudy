#key: [id(0:5441), # of words in title, 0 = unamerican name; 1 = american name, # of views]
babiepath = "C:/Users/hayst/Documents/pyton/stats/babies.txt"
teddata = "C:/Users/hayst/Documents/pyton/stats/data.csv"
mydata = "C:/Users/hayst/Documents/pyton/stats/mydataset.csv"
counter = 0
g = open(babiepath, "r")
babynames = [ y for y in g.read().split(",") ]
g.close()

f = open(teddata, "r", encoding="UTF8")
data = f.read().split("\n")
f.close()
datafr = [ x.split(",") for x in data]
importdata = ["ID", "Number of words in title", "American name?", "View count"]

for z in datafr:
    for u in z:
        u = u.strip()

for index,x in enumerate(datafr[1:]):
    cu = []
    cu.append(index)
    cu.append(len(x[0].split(" ")))
    if x[-5].split(" ")[0] in babynames:
        cu.append(1)
    else:
        cu.append(0)
    cu.append(x[-3])
    importdata.append(cu)

h = open(mydata, "w")
for i in importdata:
    for n in i:
        h.write(str(n) + ",")
    h.write("\n")

h.close()