
try:
    f = open("test/test.txt",'a')
    f.write(str(i)+" try")
    f.write("\n")
    f.close()
except:
    f = open("test/test.txt",'a')
    for i in range(100,1,1):
        f.write(str(i)+" except")
        f.write("\n")
    f.close()