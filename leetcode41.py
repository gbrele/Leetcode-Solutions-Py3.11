class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)

        for j in range(len(nums)):
            if nums[j] != j + 1:
                return j + 1

        return len(nums) + 1


    def swap(self, larg, i, j):
        temp = larg[i]
        larg[i] = larg[j]
        larg[j] = temp
