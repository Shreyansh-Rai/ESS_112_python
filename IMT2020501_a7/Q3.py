
emp_count=0
class Employee:
	def __init__(self,emp_name,dob):
		global emp_count
		global emp_id
		self.emp_name=emp_name
		self.dob=dob
		self.work_exp=[]
		emp_count+=1
		self.emp_id=emp_count
	
	
	def age(self):
	
		l=list(self.dob)
		age=2021-l[2]
		return age

	def __str__(self):
		global emp_id
		return "Employee ID: "+str(self.emp_id)+", Employee Name: "+self.emp_name+", Employee Age = "+str(self.age())+" years"

	def checkSpecialEligibility(self):
		if self.age() >=50 :
			return True
		else :
			return False

	def addWorkExperience(self,previous_companies):
		self.work_exp=self.work_exp+previous_companies

	def getWorkExperience(self):
		return self.work_exp


def t3():
	e1 = Employee("Ajay", (21,3,1992))
	e2 = Employee("Rakesh", (31,12, 1990))
	e3 = Employee("Manoj", (2,2,1970))
	print(e1.checkSpecialEligibility())
	print(e3.checkSpecialEligibility())
	e2.addWorkExperience(["Amazon", "Morgan Stanley"])
	e2.addWorkExperience(["Microsoft", "Goldman Sachs"])
	print(e2.getWorkExperience())
	print(e1)
	print(e2)
	print(e3)
if __name__ == "__main__":
	t3()








