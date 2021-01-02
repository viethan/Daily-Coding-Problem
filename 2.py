class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        product = 1 * nums[0]
        for i in range(1, len(nums)):
            output[i] = output[i] * product
            product = product * nums[i]
            
        product = 1 * nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            output[i] = output[i] * product
            product = product * nums[i]
            
        return output
