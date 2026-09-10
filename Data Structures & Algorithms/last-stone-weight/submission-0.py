class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use python min heap
        # always gives smallest value first

        # since we need largest, turn every value negative
        # heapify the list

        # while there are at least 2 stones
            # remove biggest stone
            # remove second biggest stone

            # if they are different
                # calculate the leftover
                # put the leftover back in the heap

            # if they are the same
                # remove both

        # if one stone remains 
            # return its weight
        
        #return 0

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones) 
            x = -heapq.heappop(stones) 

            if y != x:
                heapq.heappush(stones, -(y-x))

        if stones:
            return -stones[0]

        return 0