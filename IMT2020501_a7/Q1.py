class Vehicle:

	def __init__ (self,name,brand,price,mileage):
		self.name=name
		self.brand=brand
		self.price=float(price)
		self.mileage=float(mileage)
	def __str__(self):
		return "Vehicle Name: "+self.name+", Brand: "+self.brand+", Price: "+str(self.price)+", Mileage: "+str(self.mileage)

	def checkLuxury(self):
		if self.price>1000000 :
			return True
		else:
			return False

	def checkEfficiency (self):
		if self.mileage>20 :
			return True
		else:
			return False


def efficientVehicles(l):
	ltr=[]
	for i in l:
		if i.checkEfficiency() :
			ltr.append(i.name)

	return ltr

def priceOfBrand(brand,l):
	sum=0
	for i in l :
		if brand==i.brand :
			sum+=i.price
	return sum

def t1():
	v1 = Vehicle("Alto", "Suzuki", 100000.0, 50.0)
	v2 = Vehicle("SX4", "Suzuki", 200000.0, 35.5)
	v3 = Vehicle("R8", "Audi", 1000000.0, 15.7)
	v4 = Vehicle("Q3", "Audi", 1500000.0, 18.5)
	print(v1.checkLuxury())
	print(v2.checkEfficiency())
	print("Efficient Vehicles: ", efficientVehicles([v1, v2, v3, v4]))
	audiPrice = priceOfBrand("Audi", [v1, v2, v3, v4])
	print("Audi price:", audiPrice)
	print(v1)

	# if str(v1)== "Vehicle Name: Alto, Brand: Suzuki, Price: 100000, Mileage: 50.0" :
	# 	print("True, Testcase passed")

if __name__ == '__main__':
	t1()
