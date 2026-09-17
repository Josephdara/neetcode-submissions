class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            if i == 0:
                product[i] = 1
            else:
                product[i] = nums[i-1] * prefix
            prefix = product[i]
        suffix = 1
        for j in range(len(nums) - 1, -1 , -1):
            if j == len(nums):
                continue
            else:
                product[j] = product[j] * suffix
            suffix = nums[j] * suffix
    
        return product
            
        