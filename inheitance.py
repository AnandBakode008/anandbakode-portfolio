# Single Level Inheritance 
'''
class Employee(): # parent Class
	def __init__(self,eid,ename,esal,eaddr): # local varciable 
		self.eid=eid   # instance Variable 
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr


	def GetDetails(self):
		print("====== Employee Detils Are ======")
		print('id  =',self.eid)
		print('Name =',self.ename)
		print('Salary =',self.esal)
		print('Address =',self.eaddr)


class Manager(Employee):  #  child class =>  Child Class(Parent Class)
	def __init__(self, eid, ename, esal, eaddr):
		super().__init__(eid, ename, esal, eaddr)


	
#object Cretaion always object are created on Child Class 
m=Manager(101,'Anand Bakode',50000,'Seoni')
m.GetDetails()


'''





'''	
# Multilevel Inheritance
class Employee(): # parent Class
	det='Accenture'
	def __init__(self,eid,ename,esal,eaddr): # local varciable 
		self.eid=eid   # instance Variable 
		self.ename=ename
		self.esal=esal
		self.eaddr=eaddr


	def GetDetails(self):
		print()
		print("====== Employee Detils Are ======")
		print('Company Name ',self.det)
		print('id  =',self.eid)
		print('Name =',self.ename)
		print('Salary =',self.esal)
		print('Address =',self.eaddr)


class Manager(Employee):  #  child class =>  Child Class(Parent Class)
	def __init__(self, eid, ename, esal, eaddr):
		super().__init__(eid, ename, esal, eaddr)

	def getManager_Details(self):
		print("==Manager Details Are==")
		self.GetDetails()

class HR_Manager(Manager):  # Child of child class
	def __init__(self, eid, ename, esal, eaddr):
		super().__init__(eid, ename, esal, eaddr)
#object Cretaion always object are created on Child Class 
m=HR_Manager(101,'Anand Bakode',50000,'Seoni')
m.getManager_Details()


'''

'''
#multiple Inheritance 
# Multiple Inheritance Example
class Employee:  # Parent Class 1
    det = 'Accenture'
    def __init__(self, eid, ename, esal, eaddr):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def GetDetails(self):
        print()
        print("====== Employee Details Are ======")
        print('Company Name:', self.det)
        print('ID:', self.eid)
        print('Name:', self.ename)
        print('Salary:', self.esal)
        print('Address:', self.eaddr)


class Hr:  # Parent Class 2
    company = 'Google'
    def __init__(self, hrid, hrname, hrsal, hraddr):
        self.hrid = hrid
        self.hrname = hrname
        self.hrsal = hrsal
        self.hraddr = hraddr

    def GetHrDetails(self):
        print()
        print("====== HR Details Are ======")
        print('Company Name:', self.company)
        print('HR ID:', self.hrid)
        print('HR Name:', self.hrname)
        print('HR Salary:', self.hrsal)
        print('HR Address:', self.hraddr)


class HR_Manager(Employee, Hr):  # Child Class
    def __init__(self, eid, ename, esal, eaddr, hrid, hrname, hrsal, hraddr):
        # Explicitly call both parent constructors
        Employee.__init__(self, eid, ename, esal, eaddr)
        Hr.__init__(self, hrid, hrname, hrsal, hraddr)

    def Showall(self):
        print("\n==== HR Manager Full Details ====")
        self.GetDetails()
        self.GetHrDetails()


# Object Creation
m = HR_Manager(101, 'Anand Bakode', 50000, 'Seoni', 2002, 'Shubham', 60000, 'Nagpur')
m.Showall()
'''

'''
# Hybrid inheritance 

class Employee:  # Parent Class 1
    det = 'Accenture'
    def __init__(self, eid, ename, esal, eaddr):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def GetDetails(self):
        print()
        print("====== Employee Details Are ======")
        print('Company Name:', self.det)
        print('ID:', self.eid)
        print('Name:', self.ename)
        print('Salary:', self.esal)
        print('Address:', self.eaddr)
class Manager(Employee):
    def __init__(self, eid, ename, esal, eaddr):
        super().__init__(eid, ename, esal, eaddr)

    def ManagerDetails(Self):
        print('== Manager Details Are ==')

class Hr_Manager(Employee):
    def __init__(self, eid, ename, esal, eaddr):
        super().__init__(eid, ename, esal, eaddr)

    def Hr_ManagerDetails(self):
        print("== HR Manager Details Are ")

class towerleader(Manager,Hr_Manager):
    def __init__(self, eid, ename, esal, eaddr):
        super().__init__(eid, ename, esal, eaddr)

    def GetTowerdetails(self):
        print("== TowerManager details Are ==")


#object Creation 

ob1=towerleader()
ob1.GetDetails
ob1.ManagerDetails
ob1.Hr_ManagerDetails
ob1.GetTowerdetails
	


'''
'''
# Hybrid Inheritance Example

class Employee:  # Parent Class
    det = 'Accenture'

    def __init__(self, eid, ename, esal, eaddr):
        self.eid = eid
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def GetDetails(self):
        print()
        print("====== Employee Details Are ======")
        print('Company Name:', self.det)
        print('ID:', self.eid)
        print('Name:', self.ename)
        print('Salary:', self.esal)
        print('Address:', self.eaddr)


class Manager(Employee):  # Child class 1
    def __init__(self, eid, ename, esal, eaddr):
        super().__init__(eid, ename, esal, eaddr)

    def ManagerDetails(self):
        print('== Manager Details Are ==')


class Hr_Manager(Employee):  # Child class 2
    def __init__(self, eid, ename, esal, eaddr):
        super().__init__(eid, ename, esal, eaddr)

    def Hr_ManagerDetails(self):
        print("== HR Manager Details Are ==")


# TowerLeader 
class TowerLeader(Manager, Hr_Manager):
    def __init__(self, eid, ename, esal, eaddr):
        super().__init__(eid, ename, esal, eaddr)

    def GetTowerDetails(self):
        print("== Tower Leader Details Are ==")


# Object Creation
ob1 = TowerLeader(101, 'Anand', 85000, 'Nagpur')

ob1.GetDetails()
ob1.ManagerDetails()
ob1.Hr_ManagerDetails()
ob1.GetTowerDetails()
'''









#hybrid Inheritance Example


class Bank:
    def __init__(self,bid,bname,baddr):
        self.bid=bid
        self.bname=bname
        self.baddr=baddr
    def Bank_details(self):
        print('== Bank details Are ==')
        print('Bank Id',self.bid)
        print('Bank Name ',self.bname)
        print('Bank Addres  ',self.baddr)
class GoldLoan(Bank):
    def __init__(self, bid, bname, baddr):
        super().__init__(bid, bname, baddr)
    def GoldDetails(self):
        print('Godl Loan')
class CarLoan(Bank):
    def __init__(self, bid, bname, baddr):
        super().__init__(bid, bname, baddr)
    def CarDetails(self):
        print('Car Loan')
class PersonalLoan(Bank):
    def __init__(self, bid, bname, baddr):
        super().__init__(bid, bname, baddr)
    def PersonalloanDetails(self):
        print('Personal Loan')
ob=PersonalLoan(123,'HDFC','Bhoapl')
ob.Bank_details()
ob.PersonalloanDetails()


        


 