class Employee :
	dept='IT' # Static Variable


	# Constructor
	def __init__(self,eid,ename,esal,edept): # Local Variable (eid,ename,esal,edept)
		self.Eid=eid    # instance Variable self.Eid
		self.Ename=ename
		self.Esal=esal
		self.Dept=edept
		print('Constructor Executed ')
	


	def GetEmpDetails(self):   # instance Method 
		print('Employee Details Are ')
		print("Employee id ",self.Eid)
		print("Employee  Name ",self.Ename)
		print("Employee Sal ",self.Esal)
		print("Employee  Department ",self.Dept)



#object Creation
e=Employee(101,'Anand',60000,'IT')
e.GetEmpDetails()