class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list=[]
        for element in strs:
          encoded_list.append(str(len(element))+ "#" + element)
        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0

        while i < len(s):
            j = i

            # Find the end of the numeric length
            while j < len(s) and s[j].isdigit():
                j += 1

            # Validate that the length is followed by "#"
            if j == i or j >= len(s) or s[j] != "#":
                raise ValueError("Invalid encoded string")

            word_length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + word_length

            # Ensure enough characters remain
            if word_end > len(s):
                raise ValueError("Invalid encoded string")

            decoded_strings.append(s[word_start:word_end])
            i = word_end
        return decoded_strings

