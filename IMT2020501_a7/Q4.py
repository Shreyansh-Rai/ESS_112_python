class Student:
	def __init__(self,roll_num,stu_name,department,jee_rank):
		self.roll_num=roll_num
		self.stu_name=stu_name
		self.department=department
		self.jee_rank=jee_rank
		self.courses_enrolled=[]
	
class Professor:
	def __init__(self,prof_id,prof_name,department,courses_taught):
		self.prof_name=prof_name
		self.prof_id=prof_id
		self.department=department
		self.courses_taught=courses_taught

class Institution:
	def __init__(self,inst_name,location,department_list,profs_list,students_list):
		self.inst_name=inst_name
		self.department_list=department_list
		self.location=location
		self.profs_list=profs_list
		self.students_list=students_list

	def __str__(self):
		return "Institution "+self.inst_name+" is located in "+self.location+" and has "+str(len(self.profs_list))+" professors and "+str(len(self.students_list))+" students. It has "+str(len(self.department_list))+" departments: "+", ".join(self.department_list)


	def enrollStudent(self,stu,course):

		k=-1
		dept=''
		stemp=-1
		for i in self.students_list :
			if stu.roll_num == i.roll_num:
				dept=i.department
				stemp=i
				break
			
		if stemp==-1 :
			print("Invalid roll number")
		else :
			for i in self.profs_list:
				if course in i.courses_taught :
					k=1
					if dept==i.department:
						stemp.courses_enrolled.append(course)
						print ("Enrolled successfully")
					else :
						print("Not eligible to enroll in "+course)
			if k==-1 :
				print("Invalid course name")



			# for i in self.profs_list:
			# 	if i.department == stemp.department :
			# 		if course in i.courses_taught:
			# 			stemp.courses_enrolled.append(course)
			# 			return ("Enrolled successfully")
			# 		else:
			# 			return("Invalid course name")
			# 	else:
			# 		return("Not eligible to enroll in "+course)


	def findToppers(self,n=1):
		l=len(self.students_list)
		arr=self.students_list
		for i in range(l): 
			for j in range(0, l-i-1): 
				if arr[j].jee_rank > arr[j+1].jee_rank : 
					arr[j], arr[j+1] = arr[j+1], arr[j] 
		return [arr[i].stu_name for i in range(n)]




def t4():
	s1 = Student(1, "Vikram", "CSE", 5500)
	s2 = Student(2, "Samrudhhi", "ECE", 2500)
	s3 = Student(3, "Apoorv", "ECE", 6300)
	s4 = Student(4, "Chaitanya", "CSE", 9500)
	s5 = Student(5, "Akanksha", "CSE", 3200)
	s6 = Student(6, "Akshita", "ECE", 5700)
	p1 = Professor(1, "Sanjay", "CSE", ["Java", "Computer Graphics"])
	p2 = Professor(2, "Ajeesh", "CSE", ["Programming Languages", "Compilers"])
	p3 = Professor(3, "Nirmal", "ECE", ["VLSI"])
	p4 = Professor(4, "Shantanu", "ECE", ["Processor Architecture", "RTOS"])
	p5 = Professor(5, "Rajesh", "CSE", ["ML", "Visual Recognition", "NLP"])
	p6 = Professor(6, "Geetha", "ECE", ["Digital Design"])
	p7 = Professor(7, "Anusha", "CSE", ["DSA", "Graph Theory"])
	inst1 = Institution("IIITB", "Bangalore", ["CSE", "ECE"],
	[p1, p2, p3, p6], [s1, s2, s3])
	inst2 = Institution("IITD", "Delhi", ["CSE", "ECE", "EEE"],
	[p4, p5, p7], [s4, s5, s6])
	inst1.enrollStudent(s1, "Java")
	inst1.enrollStudent(s1, "C")
	inst1.enrollStudent(s1, "Compilers")
	inst1.enrollStudent(s2, "Computer Graphics")
	print(inst1.findToppers(2))
	print(inst2.findToppers())
	print(inst2)
if __name__ == "__main__":
	t4()
