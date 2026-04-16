class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # So I think what they're asking about is RSA encryption
        # what if you padded each string on its right with a fixed 3 character length number describing the actual length of the string.
        # actually, we should pad to 203 by left padding with 0s, and leave the remaining 3 for the length. This way, we know where to start looking for the actual string length in the decode step
        for idx, string in enumerate(strs):
            len_str = len(string)
            strs[idx] = f'{strs[idx]:0<200}' + f'{len_str:0>3}'

        res = ''.join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # we now know each unit is of length 203
        decoded_list = []
        """
        for start, end in zip(range(0, len(s)-203, 203), range(203, len(s), 203)):
            unit = s[start:end]
            len_str = int(s[-3:])
            print(len_str)
            decoded_list.append(unit[:len_str])
        """
        for start in range(0, len(s), 203):
            unit = s[start:start+203]
            len_str = int(unit[-3:])
            decoded_list.append(unit[:len_str])

        return decoded_list
