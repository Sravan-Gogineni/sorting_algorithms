array = [2, 6, 3, 8, 4, 1, 9, 5, 7]
i = 0
f = 0
s = 1
while i<len(array):
    while s < len(array):
        if array[s] < array[f]:
            array[f],array[s] = array[s],array[f]
        f = f+1
        s = f+1
    i = i +1
    f = 0
    s = 1
print(array)


