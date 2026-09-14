class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        org_dict = {}
        for i in nums:
            org_dict[i] = org_dict.get(i, 0) + 1
            if org_dict[i] > 1:
                return True
        return False
        