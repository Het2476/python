def fc(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def lis(flist):
    return [fc(temp) for temp in flist]


flist = [32, 68, 100, 212]
cl = lis(flist)
print(cl)