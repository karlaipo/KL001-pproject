from typing import List

print("hello world")
print("if else-------------------------------")
a=1
b=2
if a>b:
            print("a groter dan b")
else:
            print("b groter dan a")
print("a groter dan b") if a>b else print("b groter dan a")

print("len functie-------------------------------")
var1="lengte is 12"
print(len(var1))

var2=10
print(len(str(var2)))

print("list bewerken------------------------------")
var_list=[]  # type: List[str]
print(len(var_list))
var_list.append("twee")
print(len(var_list))
var_list.insert(0,"een")
print(var_list)
var_list.append("vier")
print(len(var_list))
var_list.insert(-1,"drie")
print(var_list)
del var_list[-1]
print(var_list)
var_list.append("vier")
var_list.append("vijf")
var_list.append("zes")
var_list.append("zeven")
var_list.insert(0,"nul")
print(var_list)
lengte=len(var_list)
print(lengte)
print("hallo {0}, helemaal achteraan komt {1}".format(var_list[1], var_list[lengte-1]))

print("slicing of lists------------------------------")
print(var_list[:2]) # geeft alles tot de eerste 2
print(var_list[2:]) # geeft alles behalve de eerste 2
print(var_list[1:-1]) # geeft alles behalve de eerste en de laatste
print(var_list[2:5]) # geeft alles na de eerste 2 en tot de vijfde

print("FOR LOOP--------------------------------------")
print("variant1------------------------")
for x in var_list:
            print("variabele is {0}".format(x))
            print("volgende")
print("variant2------------------------")
x=0
for teller in range(3,10,2): # van 3 tot 10 in stappen van 2
            print("{0} is {1}".format(x,var_list[x]))
            x+=1
print("variant3------------------------")
x=0
for teller in range(5):  # 5 keer
   print("{0} is {1}".format(x, var_list[x]))
   x += 1
print("met break en continue------------------------")
var2_list=[1,2,3,4,5,6,7,8,9]  # type: List[int]
for var in var2_list:
	print(var)
	if var == 4:
		print("geen volgende")
		continue
	if var == 8:
		print("stop bij 8")
		break
	print("volgende is {0}".format(var+1))

print("Dictionaries---------------------------")
student = {"name":"naam1", "id":12345, "adres": "straat1", "magweg": "nvt"}
print(student)
del student["magweg"]
print(student)
print(student["name"])
print(student.get("last_name", "onbekend"))
student["last_name"] = "achternaam1"
print(student.get("last_name", "onbekend"))
print(student)
print(student.keys())
print(student.values())

print("List of dictionaries---------------------")
all_students = [
    {"name": "naam1", "id": 12345},
    {"name": "naam2", "id": 12346},
    {"name": "naam3", "id": 12347}
]
print(all_students[-1])
del all_students[-1]
print(all_students[-1])

print("exception handling-------------------")
student = {"naam": "naam1", "id": 12345}
try:
    student["achternaam"] = "achternaam1"
    tel = student["achternaam"] + 1
except KeyError:
    print("foute sleutel")
except TypeError as error:
    print("eigen melding voor TypeError")
    print(error)
print("ga gewoon verder")
print("data types andere ----------------")
list1 = [3,1,5,3,7,8,5,7,1]
print(list1)
print(set(list1))


