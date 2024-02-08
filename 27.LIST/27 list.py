# LIST

# kumpulan data numbers
data_angka = [1,2,3,3]
print(data_angka)

# kumpulan data string
data_string = ["haerin","mamat","rusdi"]
print(data_string)

# kumpulan data boolean
data_boolean = [True,False,False]
print(data_boolean)

data_campur = ["mamat",False,2]
print(data_campur)

## cara alternatif membuat list
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# list pake for loop
list_for = [i**2 for i in range(0,10)]
print(list_for)

# list pake for ama if
list_for_if = [i for i in range(0,10) if i != 6]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_for_if)
