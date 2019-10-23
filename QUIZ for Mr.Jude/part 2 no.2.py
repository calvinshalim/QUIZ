#%% 2
filename = "data.txt"

def displaydata(filename):
    staffs = []
    for line in open(filename,'r'):
        spl = line.rstrip().split("#")
        staffs.append(staff(spl[0],spl[1],spl[2],spl[3]))
    return staffs 

class staff():
    __ID = 0
    __Name = ""
    __Position = ""
    __Salary = 0
    def __init__(self,ID,Name,Position,Salary):
        self.__ID = ID
        self.__Name = Name
        self.__Position = Position
        self.__Salary = Salary
        
    def __str__(self):
        return self.__ID +"  " +self.__Name+"  "+self.__Position+"  "+self.__Salary
    
    def getID(self):
        return self.__ID
    
    def getName(self):
        return self.__Name
    
    def getPosition(self):
        return self.__Position
    
    def getSalary(self):
        return self.__Salary
    
    def addstaff(self):
        newid = int(input("Enter New ID:"))
        if len(newid) <= 5:
            print("ID must have 5 characters ONLY!")
        if len(newid[0]) == "S":
            print("ID must start with an S")
        newname = str(input("Input Name:"))
        if len(newname) >= 20:
            print("Name Too Long")
        newpos = str(input("Input Position:"))      
#%%            
    
def menu():
    print("1.New  Staff\n2.Delete Stadd\n3.View Summary Data\n4.Save & Exit")
    choice = str(input("input Choice"))
    while True:
        if choice == "1":     
            print("New staff\n")
        return addstaff()
        
        elif choice == "2":
            delstaff = str(input("Input ID: "))
            if delstaff == staff:
                staffs.remove(delstaff)
            else:
                print("ID not exist")
                
        elif choice == "3":
            
        