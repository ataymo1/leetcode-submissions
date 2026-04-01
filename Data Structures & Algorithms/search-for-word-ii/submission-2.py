class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        found = set()

        for word in words:
            trie.insert(word)


        def dfs(pos, word, visited):
            row, col = pos
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or pos in visited:
                return
            word += board[row][col]
            if not trie.prefix(word):
                return
            if trie.search(word):
                found.add(word)
            visited.append(pos)
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for neighbor in neighbors:
                dfs(neighbor, word, visited)
            visited.pop()
            word = word[:-1]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs((i, j), "", [])

        return list(found)

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.isWord = True
    
    def search(self, word):
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return cur_node.isWord

    def prefix(self, word):
        cur_node = self.root
        
        for c in word:
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        return True
