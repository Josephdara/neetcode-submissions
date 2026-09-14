class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for word in strs:
            new_word = tuple(sorted(word))
            if new_word not in new_dict:
                new_dict[new_word] = []
            new_dict[new_word].append(word)
        return list(new_dict.values())