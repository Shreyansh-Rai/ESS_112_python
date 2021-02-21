class Date:
	
	def isleapyear(self):
		if ((self.year%4==0 and self.year%100!=0) or self.year%400==0) :
			return True
		elif self.year%100==0 and self.year%400!=0 :
			return False
		else:
			return False

	def isvalid(self):
		if (self.day<=0 or self.month<=0 or self.month>12 or self.year<=0 or self.year>2021):
			return False
		
		if(self.month==2) :
			if (self.isleapyear() and (self.day<1 or self.day>29)) :
				return False
			elif self.isleapyear()==False and (self.day<1 or self.day>28):
				return False
			else :
				return True

		elif (self.month==1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month==10 or self.month==12) and (self.day<1 or self.day>31) :
				return False
		elif (self.month==4 or self.month==6 or self.month==9 or self.month==11) and (self.day<1 or self.day>30) :
				return False
		else:
			return True

	def tomorrow(self):
		if(self.isvalid()):
			if self.month==2:
				if self.isleapyear():
					if(self.day<29):
						return (self.day+1,self.month,self.year)
					else:
						return (1,self.month+1,self.year)
				else:
					if(self.day<28):
						return (self.day+1,self.month,self.year)
					else:
						return (1,self.month+1,self.year)
			elif (self.month==1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month==10):
				if(self.day<31):
					return (self.day+1,self.month,self.year)
				else:
					return (1,self.month+1,self.year)

			elif (self.month==12):
				if(self.day<31):
					return (self.day+1,self.month,self.year)
				else:
					return (1,1,self.year+1)

			else:
				if(self.day<30):
					return (self.day+1,self.month,self.year)
				else:
					return (1,self.month+1,self.year)


		else :
			return 'Cannot find next day for invalid date'

	def __init__(self,day,month,year):
		self.day=day
		self.month=month
		self.year=year
		if(self.isvalid()==False):
			print("Invalid date")




def t2():
	d1 = Date(15, 8, 2002)
	print(d1.tomorrow())
	d2 = Date(29, 2, 2021)
	print(d2.tomorrow())
	d3 = Date(31, 6, 1842)
	print(d3.tomorrow())
	d4 = Date(25, 3, 2022)
	print(d4.tomorrow())
	d5 = Date(16, 13, 1257)
	print(d5.tomorrow())
	d6 = Date(-7, -3, -2001)
	print(d6.tomorrow())
	d7 = Date(28, 2, 2020)
	print(d7.tomorrow())
	d8 = Date(31, 12, 1999)
	print(d8.tomorrow())

if __name__ == "__main__":
	t2()

