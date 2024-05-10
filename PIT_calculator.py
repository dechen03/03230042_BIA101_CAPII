#creating class Employee

class Employee:
    def __init__(self, name, income, position,num_child,expense_per_child):
        self.name = name
        self.income = income
        self.position = position
        self.num_child=num_child
        self.expense_per_child=expense_per_child
        
    # This method will calculate the taxable income by substracting deduction from income
    def calculate_taxable_income(self):
         # Creating an instance of Class Dduction
        dedu = Deduction(self.income, self.position, self.num_child,self.expense_per_child)
        total_deduction = dedu.calculate_deductions()
        #will return taxable income
        return self.income - total_deduction
# Class inheriteted from employee to calculate annual income
class AnnulIncome(Employee):
    # method to calculate annual income of employee
    def calculate_annual_income(self):
        return self.income* 12

# class to calculate the total deduction of employee(contract or regular)
class Deduction:
    def __init__(self,income,position,num_child,expense_per_child):
        self.income=income
        self.position=position
        self.num_child=num_child
        self.expense_per_child=expense_per_child

    def calculate_deductions(self):
        #setting total deduction as 0
        total_deduction = 0
       #this statement will run only if self.position is equal to regular
        if self.position == "Regular":
            # Specific deductions for regular employees
            total_deduction += self.income * 0.10 #  assuming PF deduction as 10%
            # Education allowance up a max of Nu. 350,000 per child. min method will return the lowest value
            total_deduction += min(350000*self.num_child ,self.expense_per_child* self.num_child) 
            total_deduction += 200  # assuming GIS as 200 yearly
        #this statement will run only if position is contract
        elif self.position == "Contract":
            total_deduction += 200  #  Assuming GIS as 200 yearly
            # Education allowance up a max of Nu. 350,000 per child. min method will return the lowest value
            total_deduction += min(350000 * self.num_child,self.expense_per_child*self.num_child)

        # will return the total deduction
        return total_deduction

# class to calculate tax
class TaxCalculator:
    # Decorator indicating this method is a static method
    @staticmethod
    #method to calculate tax based on rate
    def calculate_tax(income):
        if income <= 300000:
            return 0
        elif 300001 <= income <= 400000:
            return income  * 0.1
        elif 400001 <= income <= 650000:
            return  income * 0.15
        elif 650001 <= income <= 1000000:
            return  income * 0.2
        elif 1000001 <= income <= 1500000:
            return  income* 0.25
        else:
            return  income * 0.3

#main code 
try:
    #geting inputs from user
    name = input("Enter your name: ")
    income = float(input("Enter your monthly income: "))
    position = input("Enter employee position (Contract/Regular): ").capitalize()
    child=int(input('Enter number of child: '))
    expense=int(input('Enter expense per child:'))
    
    
    
    #creating a object for Employee class
    employee = Employee(name, income, position,child,expense)
    #creatring a object for AnnulIncome class
    annualincome=AnnulIncome(name,income,position,child,expense)
    annual_income=annualincome.calculate_annual_income()
    #printing the annual income of the employee
    print(name,' you have annual income of Nu. ',annual_income)
    
    #creating object for calculate_taxable_income
    taxable_income = employee.calculate_taxable_income()
    #object for deduction
    deduction=Deduction(annual_income,position,child,expense)
    #object for calculate_deduction
    total_deduction=deduction.calculate_deductions()
    #printing total amount of deduction
    print('Total deduction allowed is  ', total_deduction)
    # printing the taxable income
    print( name,'you have taxable income of ', taxable_income)
    # condition to check if the taxable income is less than 300000 
    if taxable_income < 300000:
        print(name, " Your Income is below taxable threshold. You are exampted from paying tax")
     #if the taxable income is more than 300000 this code will run
    else:
        # object for calculating tax
        tax=TaxCalculator.calculate_tax(taxable_income)

        print(name, 'you have  tax liabiity of  Nu.', tax)
    
# If user put invalid value this will run  and print invalid input 
except ValueError:
    print("Invalid input")
