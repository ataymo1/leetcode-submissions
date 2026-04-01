class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isWord = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = self.TrieNode()
            cur_node = cur_node.children[c]
        cur_node.isWord = True

    def search(self, word: str) -> bool:
        cur_node = self.root

        for index, c in enumerate(word):
            if c == '.':
                print(f"{c} here")
                for child in cur_node.children:
                    copy = word[:index] + child + word[index+1:]
                    if self.search(copy):
                        return True
                return False
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
            
        return cur_node.isWord
        
