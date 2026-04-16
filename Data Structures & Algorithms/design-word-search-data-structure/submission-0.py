class WordDictionary:

    def __init__(self):
        self.values = [None]*26
        self.end_word = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.end_word = True
            return
        
        idx = ord(word[0]) - ord('a')
        if self.values[idx]:
            self.values[idx].addWord(word[1:])
        else:
            self.values[idx] = WordDictionary()
            self.values[idx].addWord(word[1:])

    def search(self, word: str) -> bool:
        # try to avoid recursion to minimize space complexity
        # first implement recursion, then make iterative
        if len(word) == 0:
            return self.end_word

        if word[0] == '.':
            for val in [value for value in self.values if value]:
                if val.search(word[1:]):
                    return True
            return False
        else:
            idx = ord(word[0]) - ord('a')
            return self.values[idx] is not None and self.values[idx].search(word[1:])