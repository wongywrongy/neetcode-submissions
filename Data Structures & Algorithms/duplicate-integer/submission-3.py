class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate once add numbers visited to dict
        # while iterating if in visited return false

        visited = set()

        for num in nums:
            if num in visited:
                return True
            visited.add(num)

        return False