class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            s_charmap = frozenset((c, s.count(c)) for c in s)
            if s_charmap in anagrams:
                anagrams[s_charmap] += [s]
            else:
                anagrams[s_charmap] = [s]

        return list(anagrams.values())