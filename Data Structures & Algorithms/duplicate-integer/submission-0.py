class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #i think that this is a hashmap so i can create a seen map since it 
        # has an O(1) lookup time
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False
        