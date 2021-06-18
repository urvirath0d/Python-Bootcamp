# task1
def value():
    print("Addition of Two numbers is:", value1 + value2)
    print("Subtraction of Two numbers is:", value1 - value2)
    print("Division of Two numbers is:", value1 / value2)
    print("Multiplication of Two numbers is:", value1 * value2)


value1 = int(input("Enter The First Number:"))
value2 = int(input("Enter The Second Number:"))
value()

# task2
name = input("Enter patient name:")
temp = input("Enter patient body temperature:")


# default temp is 98F
def covid():
    if len(temp) == 0:
        print("Patient body temperature is: 98 F")
    else:
        print("Patient body temperature is:", temp, "F")


print("Patient name is:", name)
covid()
