# ---------- Array in python using array module
import array
import numpy

val1 = array.array('I',[1,3,4,5,6]) # -- for 4byte integer ('I' typecode)
print(type(val1))
for i in range(len(val1)):
    print(val1[i],end=" ")

print("\n")

val2 = array.array('f',[1,3,4,5,6.5]) # -- for float ('f' typecode)
for i in range(len(val2)):
    print(val2[i],end=" ")

print("\n")

val3 = array.array('u',['a','b','c','d']) # -- for character ('u' typecode)
for i in range(len(val3)):
    print(val3[i],end=" ")

print("\n")

#--- array methods ----
val3.reverse()
print(val3)

val3.insert(2,'m')
print(val3)

val3.append('z')
print(val3)


# --------------- Array using numpy module -----------------

val4 = numpy.array([1, 2, 3])
print(type(val4))

val4 = numpy.array([1, 2, 3, 4.5])
print(type(val4[0]))

# multi dimensonal array
two = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(two)
three = numpy.array([[[1, 2, 3], [6, 7, 8]], [[7, 4, 6], [8, 3, 6]]])
print(three[0][0][0])