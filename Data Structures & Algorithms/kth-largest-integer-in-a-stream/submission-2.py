class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create min heap

        # for every number
            # add number to heap

            # if heap has more than k numbers 
                # remove smallest

        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        # add val to heap

        # if heap has more than k numbers
            # remove smallest
        
        # remove smallest number in heap
        self.arr.append(val)
        self.arr.sort()

        return self.arr[len(self.arr) - self.k]
