class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers
        #obv your value is the number[i] - target

        #do a for loop to go through each index
            # calculate the tmp your looking for

            #perform binary search 

        for i in range(len(numbers)): # iterate through each number (iindex so need to +1)
            l = i + 1 # start from the past as you iterate through
            r = len(numbers) - 1 # the boundary - 1
            tmp = target - numbers[i] # we look for target - number (numbers r in order)

            while l <= r: # stay in bounds
                mid = l + (r - l)//2 # middle = start + half
                
                if numbers[mid] == tmp: # if value = tmp
                    return [i + 1, mid + 1] # return the 1-indexed values (first, and tmp)
                elif numbers[mid] < tmp: # if the number is less than tmp (need to go right)
                    l = mid + 1
                else: # if the number is greater than tmp (need to go left)
                    r = mid - 1
                
        return []

