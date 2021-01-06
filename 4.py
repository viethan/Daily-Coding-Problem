class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        smol, seto = 1, set()
        
        for num in nums:
            if num not in seto:
                seto.add(num)
                
        while True:
            if smol not in seto:
                return smol
            else:
                smol += 1
