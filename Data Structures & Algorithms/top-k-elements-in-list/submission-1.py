class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hash table
        
        # iterate through the list 
            # for the number i would take the hash table index
            # add by 1 

        # take the k number of highleft elements and output as a list.

        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            
            count[num] += 1

        sorted_nums = sorted(count, key=count.get, reverse = True)

        return sorted_nums[:k]