#%% 2
filename = "data.txt"
import re

class staff():
    __ID = 0
    Name = ""
    __Position = ""
    __Salary = 0
    def __init__(self,ID,Name,Position,Salary):
        self.__ID = ID
        self.Name = Name
        self.__Position = Position
        self.__Salary = Salary
        
    def __str__(self):
        return f"staff(__ID={self.__ID},name={self.Name},Position={self.__Position},Salary={self.__Salary})"
    
    def __repr__(self):
        return f"staff(__ID={self.__ID},name={self.Name},Position={self.__Position},Salary={self.__Salary})"
    
    def __eq__(self,strID):
        return self.__ID == strID
    
    def getID(self):
        return self.__ID
    
    def getName(self):
        return self.__Name
    
    def getPosition(self):
        return self.__Position
    
    def getSalary(self):
        return self.__Salary
    
salary_range = {
        "Staff":{
            "MIN":3500000,
            "MAX":7000000
            },
        "Officer":{
                "MIN":7000001,
                "MAX":10000000
                },
        "Manager":{
                "MIN":10000001,
                "MAX":1E+130
            }
        }
 

def opendata(filename):
    staffs = []
    for line in open(filename,'r'):
        spl = line.rstrip().split("#")
        staffs.append(staff(spl[0],spl[1],spl[2],spl[3]))
    return staffs 

def savedata(staffs,filename):
    _temp = ""
    for staff in staffs:
        _temp += f"{staff.getID()}#{staff.Name}#{staff.getPosition()}#{staff.getSalary()}\n" 
    with open(filename, "w") as fp:
        fp.write(_temp)
        
def printStaffs(staffs):
    data = [["ID","Name","Position","Salary"]]
    data += [[staff.getID(), staff.Name, staff.getPosition(), staff.getSalary()]
            for staff in staffs] 
    col_width = max(len(word) for wor in data for word in row) + 2
    for row in data:
        print("|".join(word.ljust(col_width) for word in row))
#%%            
    
def menu(staffs):
    printStaffs(staffs)
    while True:
        print("1.New  Staff\n2.Delete Stadd\n3.View Summary Data\n4.Save & Exit")
        try:
        choice = str(input("input Choice"))
        if choice == "1":  
            while True:
                __ID = input("input new ID[Sxxxx]:")
        if not re.match(r"S\d{4}", _id):
            print("The format have to be SXXXX!")
            continue
        name = input("Input name [0..20]: ")
        if len(name) >= 20:
            print("Your name must not exceed 20 characters!")
            continue
        position = input(
            "Input desired position [staff|officer|manager]: ").upper()
        if position not in positions:
            print("Position not available!")
            continue
        try:
            salary = int(input(
                f"Input desired salary for {position} [{positions[position]['min']}..{positions[position]['max']}]: "))
            if not (salary >= positions[position]["min"] and salary <= positions[position]["max"]):
                print("Salary not in range!")
                continue
        except ValueError:
            print("Salary have to be int!")
            continue
        staff = Staff(_id, name, position, salary)
        staffs.append(staff)
        print(f"Successfully added a new staff!\n{staff}")
        break
    elif choice == 2:
        idDelete = input("Input id [SXXXX]")
        if not re.match(r"S\d{4}", idDelete):
            print("The format have to be SXXXX!")
            continue
        if idDelete not in staffs:
            print("ID not found!")
            continue
        staffs.pop(staffs.index(idDelete))
        print("ID Removed!")
    elif choice == 3:
        staffSal = []
        officerSal = []
        managerSal = []
        for staff in staffs:
            if staff.getPosition() == "STAFF":
                staffSal.append(int(staff.getSalary()))
            elif staff.getPosition() == "OFFICER":
                officerSal.append(int(staff.getSalary()))
            elif staff.getPosition() == "MANAGER":
                managerSal.append(int(staff.getSalary()))
        printOut = "1. Staff\n"
        printOut += f"Minimum Salary: {positions['STAFF']['min']}\n"
        printOut += f"Maximum Salary: {positions['STAFF']['max']}\n"
        try:
            printOut += f"Average Salary: {sum(staffSal)/len(staffSal)}\n\n"
        except ZeroDivisionError:
            printOut += "Average Salary: 0\n\n"
        printOut += "2. Officer\n"
        printOut += f"Minimum Salary: {positions['OFFICER']['min']}\n"
        printOut += f"Maximum Salary: {positions['OFFICER']['max']}\n"
        try:
            printOut += f"Average Salary: {sum(officerSal)/len(officerSal)}\n\n"
        except ZeroDivisionError:
            printOut += "Average Salary: 0\n\n"
        printOut += "3. Manager\n"
        printOut += f"Minimum Salary: {positions['MANAGER']['min']}\n"
        printOut += f"Maximum Salary: {positions['MANAGER']['max']}\n"
        try:
            printOut += f"Average Salary: {sum(managerSal)/len(managerSal)}\n\n"
        except ZeroDivisionError:
            printOut += "Average Salary: 0\n\n"
        print(printOut)
    elif choice == 4:
        break
   except ValueError:
       continue
   
stfs = opendata("data.txt")
menu(stfs)
savedata(stfs,"data2.txt")
        