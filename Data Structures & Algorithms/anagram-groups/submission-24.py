class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            counts = [0] * 26

            for char in string:
                counts[ord(char) - ord('a')] += 1

            counts = tuple(counts)
            
            if counts not in anagrams:
                anagrams[counts] = []

            anagrams[counts].append(string)

        return list(anagrams.values())