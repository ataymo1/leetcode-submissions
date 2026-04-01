class PrefixTree:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isWord = False

    def __init__(self):
        self.root = self.TrieNode()
        
    def insert(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = self.TrieNode()
            cur_node = cur_node.children[c]
        cur_node.isWord = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return cur_node.isWord
        
    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for c in prefix:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return True
        
        
        