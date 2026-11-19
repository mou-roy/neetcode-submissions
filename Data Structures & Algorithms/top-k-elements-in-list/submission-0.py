nums = [1, 2, 2, 3, 3, 3]
k = 2

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Dictionary to store:
        # number -> how many times it appears
        count = {}

        # Bucket array:
        # index = frequency
        # value = numbers having that frequency
        # +1 because maximum possible frequency is len(nums)
        freq = [[] for i in range(len(nums) + 1)]

        # Count how many times each number appears
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # count becomes:
        # {
        #   1: 1,   # 1 appears 1 time
        #   2: 2,   # 2 appears 2 times
        #   3: 3    # 3 appears 3 times
        # }

        # Put each number into the bucket matching its frequency
        for n, c in count.items():
            freq[c].append(n)

        # freq becomes:
        # index:  0    1     2     3     4  5  6
        #        [[], [1],  [2],  [3],   [], [], []]
        #
        # freq[1] = [1] because 1 appears once
        # freq[2] = [2] because 2 appears twice
        # freq[3] = [3] because 3 appears three times

        res = []

        # Start from highest frequency and move backwards
        # i = 6, 5, 4, 3, 2, 1
        for i in range(len(freq) - 1, 0, -1):

            # Get numbers that appeared i times
            for n in freq[i]:

                # Add that number to result
                res.append(n)

                # Once we have k=2 numbers, return
                if len(res) == k:
                    return res