class sales_sys:
    def __init__(self, name='', cname='', address='', gender='', contact='', age='',
                 c_age='', cpp='', pr='', x='', y='', z='', budgt=''):
        print("\n\n Welcome to Alpha Motors")

        self.name = name
        self.cname = cname
        self.address = address
        self.gender = gender
        self.contact = contact
        self.age = age
        self.c_age = c_age
        self.cpp = cpp
        self.pr = pr
        self.Rg1 = x
        self.Rg2 = y
        self.Rg3 = z
        self.budgt = budgt

    def selfdata(self):
        self.name = input("\n Enter Your Name: ")
        self.address = input("\n Enter address: ")
        self.age = input("\n Enter your Age: ")
        self.contact = input("\n Enter Contact no. :")
        self.gender = input("\n Enter gender: ")

    def budgt_rg(self):
        print("Select your Budget;")
        print("1. <800000")
        print("2. >800000 & <1200000")
        print("3. >1200000")

        rge = int(input("Enter your budget (1-3): "))
        if rge==1:
            self.budgt = self.Rg1 = "101. Hyundai Santro, 102. Volkswaggen Polo"
        elif rge==2:
            self.budgt = self.Rg2 = "201. Hyndai Elantra, 202. Honda City iVtec"
        elif rge==3:
            self.budgt = self.Rg3 = "301. Hyundai Creta, 303. JEEP compass"
        else:
            print("INVALID INPUT!")

        print("Your selected Budget Range is ", self.budgt)
        print("Please remember code of the car you wish to purchase.")

    def select_car(self):
        car = int(input("Enter Car Code: "))

        if car == 101:
            print("You have Selected Hyundai Santro, Excellent choice!")
            self.pr = 650000

        elif car == 102:
            print("You have Selected Volkswagen Polo, Excellent choice!")
            self.pr = 780000

        elif car == 201:
            print("You have Selected Hyudai Elantra, Excellent choice!")
            self.pr = 1165000

        elif car == 202:
            print("You have Selected Honda City iVtec, Excellent choice!")
            self.pr = 1000000

        elif car == 301:
            print("You have Selected Hyundai Creta, Excellent choice!")
            self.pr = 1900000

        elif car == 302:
            print("You have Selected JEEP Compass, Excellent choice!")
            self.pr = 2450000

        else:
            print("INVALID CODE")

        print("Your Selected Car price is - ", self.pr)

    def bill(self):
        print("*****ALPHA MOTORS*****")
        print("*********BILL*********")
        print("Customer Name: ", self.name)
        print("Customer Address: ", self.address)
        print("Customer Age: ", self.age)
        print("Customer Gender: ", self.gender)
        print("Customer Contact: ", self.contact)
        print("Car Amount: ", self.pr)
        print("Taxes = 110700")
        print("TOTAL PAYABLE AMOUNT: ", self.pr + 110700)
        print("THANK YOU FOR CHOOSING ALPHA MOTORS.")

    def sell(self):
        self.name = input("\n Enter Your Name: ")
        self.address = input("\n Enter address: ")
        self.age = input("\n Enter your Age: ")
        self.contact = input("\n Enter Contact no. :")
        self.gender = input("\n Enter gender: ")
        self.cname = input("\n Enter Car Model and company name: ")
        self.c_age = input("\n Enter Car Age: ")
        self.cpp = input("\n Enter purchase price of Car: ")
        print("Your Car has been listed for Sale.")

def main():
    x=sales_sys()
    while 1:
        print("0. Sell a Car")
        print("BUY NEW CAR")
        print("1. Fill Customer Details")
        print("2. View Options in Budget")
        print("3. Select Car")
        print("4. Bill Generator")

        y=int(input("*Enter the code (0-4) for the function to execute*"))
        if y==0:
            x.sell()
        elif y==1:
            x.selfdata()
        elif y==2:
            x.budgt_rg()
        elif y==3:
            x.select_car()
        elif y==4:
            x.bill()
main()




