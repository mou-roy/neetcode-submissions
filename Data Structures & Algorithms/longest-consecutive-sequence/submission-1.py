class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if n is the START of a sequence
            if (n - 1) not in numSet:
                length = 0

                # Keep counting while consecutive numbers exist
                while (n + length) in numSet:
                    length += 1

                # Update the longest sequence found
                longest = max(length, longest)

        return longest