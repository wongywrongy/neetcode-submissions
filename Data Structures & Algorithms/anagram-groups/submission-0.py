class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap
        # create a key for accesing the hashmap
        # value = list of strings with that representation

        # iterate through the string
            # create a character frequency representation

            # use that representation as the hashmap key

            # add that current string to that keys list

        # return all groups from the hashmap

        groups = {}

        for s in strs:
            count = [0]*26

            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())