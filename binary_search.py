

def binary_serach(arr,item):
    low = 0
    high = len(arr)-1

    while low<=high:

        mid = (low+high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        
        elif guess > item:
            mid = high -1 

        else:
            low = mid+1
    
    return None




arr = [1,3,5,7,9]
item = 3

print(binary_serach(arr,item))