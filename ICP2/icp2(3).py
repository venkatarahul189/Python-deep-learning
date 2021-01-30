T = open("sample.txt", "r")
d = dict()
for line in T:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
                if word in d:
                        d[word] = d[word] + 1
                else:
                        d[word] = 1
for k in list(d.keys()):
        print(k, ":", d[k])
        f = open("sample.txt", "a+")
        for k in list(d.keys()):
                f.write("\n")
                f.write(k)
                f.write(" : ")
                f.write(str(d[k]))
        f.close()