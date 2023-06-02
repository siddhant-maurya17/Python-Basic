list=[1,2,3,4,5,6,7,8,9,0,-1,-2,-3,-7]
n=len(list)
# [start_index:last_index+1:step_index]
print("Without slicing: ",list)

'''let slice my list in different way'''

print("Default slice: ",list[0:n:1])

print("Extract first five element from list: ", list[0:5:1])

print("Extract last five element from list: ", list[-5::1])

print("Step index of 2 :", list[::2])

print("Start from index is 4 and Step index must be 3: ",list[4::3])

print("Extract last five Element and Step index must be 2: ",list[-5:n:2])

print("Extract from last to First: ",list[::-1])

print("Extract from last to first with step index -2: ",list[-1::-2])

#New list added

list_1=["A","B","C","D","E","F","G","H"]

m=len(list_1)

print("Extract BDFH from list_1: ",list_1[1::2])

print("Extract BCDE from list_1: ",list_1[1:5:1])

print("Extract ADG from list_1: ",list_1[::3])

print("Extract HGFE from list_1: ",list_1[:-5:-1])

a=10;b=20;c=30;d=40;e=50;f=90
list_2=[a+b,b+c,c+d,d+e,e+f,f+a]

print("Two pair sum in the list",list_2[::])

list_2[1:4]=[10,20,30]
print("override new values from index 0 to 3 and list_2 look like: ",list_2[::])