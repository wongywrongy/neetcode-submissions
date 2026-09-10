class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #hash map

        # create an empy hash map (consider 1 indexed positoins)

        # loop through array from 0 to n - 1
            # compute complement

            # if tmp exsits in hashmap return 

        mp = defaultdict(int)

        for i in range(len(numbers)):
            tmp = target - numbers[i]

            if mp[tmp]:
                return [mp[tmp], i+1]
            
            mp[numbers[i]] = i + 1

        return []