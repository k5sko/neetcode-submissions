class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            order = ''.join(sorted(string))

            if order not in anagrams:
                anagrams[order] = []

            anagrams[order].append(string)

        return list(anagrams.values())