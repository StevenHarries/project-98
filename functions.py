file_a =  input("Enter the path : ")                                     # open("C:/Users/ADMIN/Documents/Python/not.txt","r")
with open(file_a,'r') as f1:
    data_f1 = f1.read
file_b = input("Enter the Path : ")     #open("C:/Users/ADMIN/Documents/Python/not1.txt","r")
with open(file_b,'r') as f2:
    data_f2 = f2.read

with open("file_a","w") as f1:
    f1.write(data_f2)

with open("file_b","w") as f2:
    f2.write(data_f1)