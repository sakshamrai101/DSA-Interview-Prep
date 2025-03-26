class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:

        def dfs(index, node):

            if index == len(word):
                return node.endOfWord
            
            c = word[index]
            if c == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                
                return False
            else:
                if c not in node.children:
                    return False 
                return dfs(index + 1, node.children[c])
        
        return dfs(0, self.root)
    
dictionary = WordDictionary()
dictionary.addWord("bad")
dictionary.addWord("dad")
dictionary.addWord("mad")
print(dictionary.search("pad"))
print(dictionary.search("bad"))
print(dictionary.search(".ad"))
print(dictionary.search("b.."))