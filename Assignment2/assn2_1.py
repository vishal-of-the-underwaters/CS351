from math import ceil

def handleChoices(x, temp):	
	li = x.split(",")
	if len(li) <3:
		return 0
	choices = []
	for i in li:
		if int(i)<=5:
			choices.append(temp[int(i)-1])
		else:
			print("Invalid input")
	return choices
	


students = [["st1", "CS1001", 1], ["st2", "CS1002", 1], ["st3", "CS2001", 3], ["st4", "CS2002", 3], ["st5", "CS3001", 5], ["st6", "CS3002", 5], ["st7", "CS4001", 7], ["st8", "CS4002", 7]]

subjects = [["Math", "CS101"], ["Digital", "CS102"], ["Basic Elec.", "CS103"], ["Comp. Org.", "CS104"], ["Data Structures", "CS105"], ["Algorithms", "CS201"], ["FLAT", "CS202"], ["AI", "CS203"], ["DBMS", "CS204"], ["Cloud Computing", "CS301"], ["Networks", "CS302"], ["TOC", "CS303"], ["ML", "CS304"], ["Elective 1", "CS401"], ["Elective 2", "CS402"], ["Elective 3", "CS403"], ["Elective 4", "CS404"]]

print("Registration")
print("Enter roll number below: ")
roll_num = input()

flag=0
index= -1
counter=1
for i in range(len(students)):
	if students[i][1] == roll_num:
		flag=1
		index= i

if flag==0:
	print("Roll number invalid \n-----------------------")
	
else:
	print("\nStudent details: \n Name: " + students[index][0] + " Semester: " + str(students[index][2]))
	print("-----------------------")
	
	
	print("Please select atleast 3 subjects from the following:")
	year = ceil(students[index][2]/2)
	
	temp= []
	for i in range(len(subjects)):
		if subjects[i][1][2] == str(year):
			print(str(counter) + " "+ subjects[i][0])
			counter+=1
			temp.append(subjects[i][0])
	
	print("Enter the IDs of courses (1/2/3...) separated by a comma(,) :")
	choices = input()
	
	subs = handleChoices(choices, temp)
	if subs==0:
		print("Less than 3 subjects is not acceptable")
	else:
		print("Subjects chosen: \n ")
		for i in subs:
			print(i)
		
		f= open("student_course_information.txt", "a+")
		f.write(str(students[index]) + " - " + str(subs) + "\n")
		f.close()
		print("Registration Complete")
	
	
	
	
	

			
		
		