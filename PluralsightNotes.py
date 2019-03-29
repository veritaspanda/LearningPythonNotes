#Pluralsight Notes
print("*****Pluralsight Notes*****")

#Can use single, double, or triple quotes
#'Hello World' == "Hello World" == """Hello World"""
#Tripple quotes apparently used freqnetly for class description or to replace the missing multi-line comment

#"hello".capitalize() == "Hello"
#"hello".replace("e", "a") == "hallo"
#"hello".isalpha() == True
#"123"isdigit() == True #Useful when converting to int
#"some,csv,values".split(",") == ["some", "csv", "values"]

print("*****Begin String Format Section************")
name = "PythonBo"
machine = "HAL"

printValue = "Nice to meet you {0}. I am {1}".format(name, machine)

print(printValue)

newName = "Joe"
machineName = "BOB"

newFormatedValue = f"Nice to meet you {newName}. I am {machineName}"
#f format string
#r won't replae backslashes and such
#u unicode string

print(newFormatedValue)

print("*****End String Format Section**************")
print("********************************************")


print("*****Begin Boolean and If statement Section************")

true_variable = True

if true_variable: #don't need anything like true_variable == True
	print("This will execute")

false_variable = None #none also equals false apparently

#if value != valueToCheck
#if not value = valueToCheck

if false_variable:
	print("This will NOT exeute")

#indents matter for if statments


numberVal = 3

if numberVal == 3 and true_variable:
	print("This will exeute")

if numberVal == 17 or true_variable:
	print("This will also execute")


#ternary if statement example
a = 1
b = 2

bigOrSmall = "bigger" if a > b else "smaller"

print(bigOrSmall)


print("*****End Boolean and If statement Section**************")
print("********************************************")

print("*****Begin List Section************")

student_names = ["Mark", "Katarina", "Jessica"]
print(student_names)

#0,1,2
#get last element would be -1 (jessica)

#replace value
student_names[0] = "James"
print(student_names)

#if item doesn't exist yet, ie: student_names[3] = "Homer" this will not work. need to add it like
student_names.append("Homer")

#remove item from list
del student_names[2] #jessica is removed
print(student_names)

#len(student_names) == 4 #elements in list

#start partway through list
#student_names[1:] == ["Katarina", "Homer"]

#student_names[1:-1] == ["Katarina"]

print("*****End List Section**************")
print("********************************************")


print("*****Begin Loop Section************")

#for loop actually acts more like a foreach loop
for name in student_names:
	print("Student name is {0}".format(name))

x = 0
for index in range(10):
	x += 10
	print("The value of x is {0}".format(x))

#range can also start at a different point and increment by more than one
#range(5, 10, 2)
#range(start, stop, step)

student_names.append("Jessica")
student_names.append("Mark")
student_names.append("Bort")

print(student_names)

for name in student_names:
	if name == "Homer":
		print("Fount him! " + name)
		break #continue is the other option
	print("Currently testing " + name)


print("*****End Loop Section**************")
print("********************************************")

print("*****Begin Dictonaries Section************")

#python dictonaries are very similar to if not exactly json
#key value pairs

student = {
	"name": "Mark",
	"student_id": 15163,
	"feedback": None
}

print(student)

#student["name"] == "Mark"

#student.get("last_name", "Unknown") == "Unknown"

#student.keys() #gets keys
#student.values() #gets values
#del student["name"]

student["last_name"] = "Kowalski"

try:
	last_name = student["last_name"]
	numbered_last_name = 3 + last_name
except KeyError:
	print("Error finding last_name")
except TypeError:
	print("I cannot add these two together")
except Exception as error:
	print("Unknown Error")
	print(error)
	
print("This code executes")

print("*****End Dictonaries Section**************")
print("********************************************")

print("*****Begin Next Section************")