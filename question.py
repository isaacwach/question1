# BINARY SOLUTION
# 1. Create two pointers, left and right
# 2. Check for condition if left<= right
# 3. Get the mid point
# 4. Check for the condition of tooSweet, ie mid, and mid minus 1 equals false and return mid 

def binarysearchsolution( n ): # O(logn)
    left, right = 1 , n
    while left <= right:
        mid = ( left + right ) // 2
        if isTooSweet(mid - 1) == False and isTooSweet(mid) == True:
            return mid
        elif isTooSweet(mid):
            right = mid -1 
        elif not isTooSweet(mid):
            left = mid +1

print(binarysearchsolution())
