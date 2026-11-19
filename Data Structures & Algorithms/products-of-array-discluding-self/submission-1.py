class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Start with [1, 1, 1, 1]
        res = [1] * len(nums)

        # ---------- LEFT / PREFIX ----------
        # prefix = product of everything to the LEFT
        prefix = 1

        for i in range(len(nums)):

            # Store product of everything BEFORE nums[i]
            res[i] = prefix

            # Include current number for the NEXT position
            prefix *= nums[i]

        # After prefix loop:
        # res = [1, 1, 2, 6]
        #
        # index 0: nothing on left        = 1
        # index 1: 1                      = 1
        # index 2: 1*2                    = 2
        # index 3: 1*2*3                  = 6


        # ---------- RIGHT / POSTFIX ----------
        # postfix = product of everything to the RIGHT
        postfix = 1

        # Move RIGHT -> LEFT
        for i in range(len(nums) - 1, -1, -1):

            # Multiply left product by right product
            res[i] *= postfix

            # Include current number for the NEXT position
            postfix *= nums[i]

        return res