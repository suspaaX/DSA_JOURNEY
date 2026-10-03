num1 = [5,15,22,1,-15,24]


min_val = min(num1)
max_val = max(num1)

# print(min_val,max_val) # type: ignore

# for i in range(len(num1)):
#     if num1[i] == min_val:
#         # print(i)


'''maximum_subarray'''

# num1 = [1,2,3,4,5]

# n = len(num1)

# subarry = n*(n+1)/2
# # print(int(subarry))

# lst = []
# for i in range(1,len(num1)+1):
#     for k in range(1,len(num1)+1):
#         lst.append(num1[i:k])

# print(lst)



'''pair sum'''

num = [2,7,9,11] 
target = 9

lst = []
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j] == target:
            lst.append(i)
            lst.append(j)

# print(lst)
    
