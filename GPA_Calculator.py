def letter_to_gpa(letter):
	dictionary =	dict({
  	'A' :	4.0,
	'A-':	3.67,
	'B+':	3.33,
	'B'	:	3.0,
	'B-':	2.67,
	'C+':	2.33,
	'C'	:	2.0,
	'C-':	1.67,
	'D+':	1.33,
	'D'	:	1.0,
	'D-':	.67,
	'S'	:	  0,
	'P' : 	  0,
	'blank':  -1,
	})
	return(dictionary[letter])
list2 = []
class Course(object): #Nodes are use to create lists of data,addresses, etc. imported from excel
    def __init__(self,Name =  None, Credits = None, Grade = None,GPA = None):
        self.Name = Name
        self.Credits = Credits
        self.Grade = Grade
def print_course_list(node_list):
	count = 0
	weight_GPA = 0
	tot_GP = 0
	for node in node_list:
		print(node.Name)
		print(node.Grade)
		print(node.Credits)
		print('\n')
		course_GPA = letter_to_gpa(node.Grade)
		course_credits = float(node.Credits)
		#print(course_credits)
		#print(course_GPA)
		course_something = course_GPA*(course_credits)
		weight_GPA =weight_GPA + course_something
		if(node.Grade == "B" or node.Grade == "B+" or node.Grade =="B-"):
			count +=1
			list2.append(node)
		if(course_something<0):
			break
		if (course_something!=0):
			tot_GP = tot_GP + course_credits
		else:
			continue
		final_gpa = weight_GPA/tot_GP
	print(final_gpa)
	for items in list2:
		print(items.Name)
	print(count)
		
course_list = []
html_file= open('/Users/jacquelinesamuelson/Desktop/path2.html', 'r+', encoding="utf-8")
keyword =("Grade")
for line in html_file:
	if "Course History" in line:
		grades = line
words = grades.split()


for i in range(len(words)):
	if words[i]==keyword:
		new_course = Course()
		new_course.Name = words[i-8:i-2]
		new_course.Credits = words[i-1][:-1]
		new_course.Grade = words[i+1][:-1]
		course_list.append(new_course)
	else:
		continue
print("Your current GPA is:")
print_course_list(course_list)
continue_this = True
'''
while(continue_this):
	temp_class = Course()
	quest_credits = 10#input("How many credits is the class?")
	temp_class.Name = quest_credits
	quest_Grade = "C" #input("What is Your Expected Grade? A A-... etc")
	temp_class.Credits = quest_Grade

	continue_this = input("Do you want to continue (Y/N?")
	if(continue_this == "Y"):
			list.append(temp_class)
			continue
	else:
		continue_this = False
		break
		
temp_class = Course()
quest_credits = 10#input("How many credits is the class?")
quest_Grade = "C" #input("What is Your Expected Grade? A A-... etc")
temp_class.Grade = quest_Grade
temp_class.Credits = quest_credits
course_list.append(temp_class)
print("Your Future GPA is:")
print_course_list(course_list)
'''



		
		
		

class Course(object): #Nodes are use to create lists of data,addresses, etc. imported from excel
    def __init__(self,Name =  None, Credits = None, Grade = None,GPA = None):
        self.Name = Name
        self.Credits = Credits
        self.Grade = Grade
      
'''
for l in words:
	index = words.index(keyword )
	print(words[index+1:index+12])
'''

