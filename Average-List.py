start=int(input("Enter the start index: "))
end=int(input("Enter the end index: "))
step=int(input("Enter the step index: "))

num_list=list(range(start,end,step))

# print("Numlist is",num_list)

list_len=len(num_list)

# print("Length of list:",list_len)

sum=0
for i in range(list_len+1):
    sum+=i
    # print("Sum:",sum)



print("Average of the given list is:",sum/list_len)