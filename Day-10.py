# Day-10
class Bank:
    def func(self):
        input("Enter Your Name :")


class Branch(Bank):
    def func1(self):
        input("Enter Branch Name:")


class ACC(Bank):
    def func2(self):
        input("Enter Your Account Number :")


class IFSC(ACC):
    def func3(self):
        input("Enter IFSC CODE :")


class Amount(Bank):
    def func4(self):
        input("Enter Amount You Want to Deposit :")
        print("********Successful*********")
        print("Credited Amount with be Updated Soon")
        print("Thank You")


ob = Bank()
ob1 = Branch()
ob2 = ACC()
ob3 = IFSC()
ob4 = amount()
ob.func()
ob1.func1()
ob2.func2()
ob3.func3()
ob4.func4()
