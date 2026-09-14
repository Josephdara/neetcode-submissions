class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            frequency = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                frequency[index] += 1
            sig = tuple(frequency)

            if sig not in groups:
                groups[sig] = []
            
            groups[sig].append(word)
        
        return list(groups.values())