# Task
file1 = open("30 days 30 hour operations.txt", "w")
file1.write("I have completed 10 days successfully \n")
file1 = open("30 days 30 hour operations.txt", "a")
file1.write("Urvi Rathod")
file1 = open("30 days 30 hour operations.txt", "r")
print(file1.read())
file1.close()
