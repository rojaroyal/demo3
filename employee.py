class Employee:
    def __init__(self,eno,ename,edept,edesg,esalary):

        self.employeeid = eno
        self.employeename = ename
        self.employeedepartment = edept
        self.employeedesignation = edesg
        self.employeesalary = esalary

    def Display_employee_information(self):
        print("employee information")
        print("********************")
        print("employee id=",self.employeeid)
        print("employee name=",self.employeename)
        print("employee department=",self.employeedepartment)
        print("employee designation=",self.employeedesignation)
        print("employee salary=",self.employeesalary)


print("employee1 object")
print("***************")
employeenumber=input("enter employee id:")
employeename=input("enter employee name:")
employeedepartment=input("enter employee department:")
employeedesignation=input("enter employee designation:")
employeesalary=float(input("enter employee salary:"))


employee1=employee(employeenumber,employeename,employeedepartment,employeedesignatio,employeesalary)
employee1.display_employee_information()
print("employee1 object is completed")
        
              
              
        
