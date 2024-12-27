class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    

    def insert(self, word: str) -> None:

        # node to traverse the hashMap:
        cur = self.root

        for c in word:

            # Check if c is not a children of current character
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # If it is, move current  -> make current the child of c 
            cur = cur.children[c]

        # reached end of the word, so set EOW flag true for current 
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:

        # node to traverse the hashMap:
        cur = self.root

        for c in word:
            # if current char 'c' is not in the child list of the current character 'curr', it does not exist. 
            if c not in cur.children:
                return False 
            # else, simply move on the next child character
            cur = cur.children[c]
        
        # Return True only if we have reached end of Trie with curr
        return True if cur.endOfWord else False 

    

    
    # This fn is why TRIE is used -> as finding prefix is O(no. of first characters -> in this case it is O(26) compared to a list where there could be million of such words).
    def startsWith(self, preFix: str) -> bool:

        # node to traverse the children's hashMap:
        cur = self.root

        count = 0

        for c in preFix:
            if c not in cur.children:
                return False 
            cur = cur.children[c]
            count += 1
        
        return True if count == len(preFix) else False 


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))