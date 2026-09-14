class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            order = ""
            
            for char in sorted(string):
                order += char

            if order not in anagrams:
                anagrams[order] = []

            anagrams[order].append(string)

        print(anagrams.values())
        return [[]]