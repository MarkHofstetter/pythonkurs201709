a = 11
b = 7

print(a,"geteilt durch",b,"ergibt",str(a/b)+"!")

# pythonic
print("{0:d} geteilt durch {1:d} (nochmals {1:d}) ergibt {2:0.3f}".format(a,b,a/b))

# C style - printf
print("%d geteilt durch %d ergibt %-12.3f=" % (a,b,a/b))