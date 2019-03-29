students = []


def get_students_titlecase():
	students_titlecase = []
	for student in students:
		try:
			students_titlecase = student["name"].title()
		except Exception as error:
			print("Unable to get Student in Titlecase")
			print(error)
			break
	return students_titlecase


def print_students_titlecase():
	students_titlecase = get_students_titlecase()
	print(students_titlecase)


def add_student(name, student_id=332):
	student = {"name": name, "student_id": student_id}
	students.append(student)


	#handles variable number of arguments with key value pairs kwargs
def var_args(name, **kwargs):
	print(name)
	print(kwargs["description"], kwargs["feedback"])

	
student_list = get_students_titlecase()

#add_student(name="Mark", student_id=15)

#var_args("Mark", description="Loves Python", feedback=None, pluralsight_subscriber=True)

student_name = input("Enter student name: ")
student_id = input("Enter student id: ")

add_student(student_name, student_id)
print_students_titlecase()
