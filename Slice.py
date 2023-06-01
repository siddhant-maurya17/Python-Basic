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

print("Extarct from last to first with step index -2: ",list[-1::-2])



