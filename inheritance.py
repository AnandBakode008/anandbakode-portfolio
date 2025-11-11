class Demo :
    i=10   #static variable   inside the class and outside the function 
    j=20   #static variable

    #instance method
    def m1(self,name):
        self.name=name
        print("------------ Instance Method ---------------")
        print("static variable i :",Demo.i,"   ",self.i)
        print("static variable i :",Demo.j,"   ",self.j)
        print("insatnce variable name :",self.name)
        print()
        self.m2(1000,2000) # static Method
        self.m3() # class Method

    #static method
    @staticmethod  #Decoretor
    def m2(a,b):
        print("------------ static Method ---------------")
        print("static variable i :",Demo.i,"   ",Demo.i)
        print("static variable i :",Demo.j,"   ",Demo.j)
        print("Local variable a :",a)
        print("Local variable b :",b)
        print()

    #class Method    
    @classmethod
    def m3(cls):
        print("------------ class Method ---------------")
        print("static variable i :",Demo.i,"   ",cls.i)
        print("static variable i :",Demo.j,"   ",cls.j)
        #print("insatnce variable name :",cls.name) instance variable  can not be called 
        print()
        #cls.m1("Rahul") # we can't call instance method 
        cls.m2(100,200) #We can call static method 

#Object Creation.....
d=Demo()

d.m1("Sudhir Koche")
d.m2(10,30)
Demo.m2(10,40)
d.m3()