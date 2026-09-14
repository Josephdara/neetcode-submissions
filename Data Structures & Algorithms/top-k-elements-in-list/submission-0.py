class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        maxnums = []
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
        dict_val_list = sorted(list(nums_dict.values()))
        for number , value in nums_dict.items():
            if value >= dict_val_list[-k]:
                maxnums.append(number)
        
        return(maxnums)