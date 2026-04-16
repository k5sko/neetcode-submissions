class PrefixTree:

    def __init__(self):
        self.branches = [False]*27

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.branches[26] = True
            return
        
        idx = ord(word[0]) - ord('a')
        if self.branches[idx]:
            self.branches[idx].insert(word[1:])
        else:
            self.branches[idx] = PrefixTree()
            self.branches[idx].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.branches[26]
        idx = ord(word[0]) - ord('a')

        if self.branches[idx]:
            return self.branches[idx].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        
        idx = ord(prefix[0]) - ord('a')
        if self.branches[idx]:
            return self.branches[idx].startsWith(prefix[1:])
        else:
            return False
        
"""
[ d ]
[ o ]
[ g ] 
[27=True]


"""