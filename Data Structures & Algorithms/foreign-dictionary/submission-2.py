class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # create edges, go through words and create graph

        # run through topological sort, checking for cycles

        adj = defaultdict(set)
        letters = set()

        for word in words:
            for c in word:
                letters.add(c)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            maxCount = min(len(word1), len(word2))
            
            count = 0
            
            while count < maxCount and word1[count] == word2[count]:
                count += 1
            
            if count == maxCount:
                if len(word2) < len(word1):
                    return ""
                continue
            
            adj[word1[count]].add(word2[count])
            

        print(adj)
        
        visited = set()
        res = []

        for letter in letters:
            if not self.dfs(letter, adj, set(), res, visited):
                return ""

        sol = ""
        res.reverse()
        for i in range(len(res)):
            sol += res[i]

        return sol


    def dfs(self, letter, adj, path, res, visited):
        print(f"{letter} : {path}")
        
        if letter in path:
            return False
        if letter in visited:
            return True

        visited.add(letter)
        path.add(letter)

        for postLetter in adj[letter]:
            if not self.dfs(postLetter, adj, path, res, visited):
                print("already visited")
                return False

        res.append(letter)
        print(res)
        
        path.remove(letter)
        return True
        



