class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i can use a hashmap for this
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return sorted([seen[complement], i])
            if num not in seen:
                seen[num] = i
            

        return []



        