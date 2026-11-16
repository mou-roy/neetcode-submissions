from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary where:
        # key   = sorted version of word
        # value = list of words having that sorted version
        res = defaultdict(list)

        # Go through each word
        for s in strs:

            # Sort the characters and join them back into a string
            # Example: "eat" -> ['a','e','t'] -> "aet"
            sortedS = ''.join(sorted(s))

            # Add original word to the group identified by sortedS
            # Example: res["aet"].append("eat")
            res[sortedS].append(s)

        # We only need the grouped words, not the sorted keys
        return list(res.values()) # We throw away the keys