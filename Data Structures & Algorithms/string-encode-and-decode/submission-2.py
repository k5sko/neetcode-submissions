class Solution:

    def encode(self, strs: List[str]) -> str:
        # that soln was really dumb, add the length as a prefix not a suffix
        strings = []
        for idx in range(len(strs)):
            string = strs[idx]
            strings.append(f'{len(string)}_{string}')

        return ''.join(strings)
    
    def decode(self, s: str) -> List[str]:
        decoded_string = []
        idx = 0
        while idx < len(s):
            delimiter_idx = s[idx:].index("_") + idx
            len_string = int(s[idx:delimiter_idx])
            string = s[delimiter_idx+1:delimiter_idx+1+len_string]
            decoded_string.append(string)
            idx = delimiter_idx+1+len_string

        return decoded_string
        