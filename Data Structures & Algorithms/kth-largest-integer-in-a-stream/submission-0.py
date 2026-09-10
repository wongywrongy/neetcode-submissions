class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create min heap

        # for every number
            # add number to heap

            # if heap has more than k numbers 
                # remove smallest

        self.k = k
        self.heap = []

        for num in nums:
            heapq.heappush(self.heap, num)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # add val to heap

        # if heap has more than k numbers
            # remove smallest
        
        # remove smallest number in heap
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
