# example of ternary operator


stacks = 3
stack2 = 5
if stacks >= 3:
    print('Coding Dojo')

else:
    print('Not Dojo')

print('Coding Dojo' if stacks >= 3 else 'Not Dojo')
print('Coding Dojo' if stacks < 3 else 'Not Dojo')
print('Coding Dojo' if stacks >= 3 or stack2 < 5 else 'Not Dojo')

# example of lamda functions

def map(list, function):
    for i in range(len(list)):
        list[i] = function(list[i])
    return list

print(map([1,2,3,4], lambda num: num * num))

class Underscore:
    def map(self, iterable, callback):
        for i in range(len(iterable)):
            iterable[i] = callback(iterable[i])
        return iterable

    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i

    def filter(self, iterable, callback):
        newList = []
        for i in iterable:
            if callback(i):
                newList.append(i)
        return newList

    def reject(self, iterable, callback):
        newList = []
        for i in iterable:
            if not callback(i):
                newList.append(i)
        return newList



_ = Underscore()

print(_.map([1,2,3], lambda x: x*2))
print(_.find([1,2,3,4,5,6], lambda x: x>4))
print(_.filter([1,2,3,4,5,6], lambda x: x%2==0))
print(_.reject([1,2,3,4,5,6], lambda x: x%2==0))


        