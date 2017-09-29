# import matplotlib.pyplot as plt
# bewirkt das gleich
from matplotlib import pyplot as plt

mp = plt()

mp.plot([1,2,3,4])
mp.plot([2,3,4,5])
mp.ylabel('some numbers')

mp.savefig('foo.png')