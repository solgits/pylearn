import random

class Dice(object) :
    def __init__(self, start,end) :
        print('init')
        self._start = start
        self._end = end

    def __call__(self):
        return random.randint(self._start,self._end)


dice = Dice(1,16)

print(dice())
print(dice())
print(dice())