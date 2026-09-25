class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])
        class Trie:
            def __init__(self):
                self.child = {}
                self.word = None
        root=Trie()
        for word in words:
            node=root
            for i in word:
                if i not in node.child:
                    node.child[i]=Trie()
                node=node.child[i]
            node.word=word
        ans = []
        def solve(i,j,node):
            if(i<0 or j<0 or i>=m or j>=n):return
            c=board[i][j]
            if c not in node.child or c=='#':return
            node=node.child[c]
            if node.word is not None:
                ans.append(node.word)
                node.word=None
            board[i][j]='#'
            solve(i+1,j,node)
            solve(i-1,j,node)
            solve(i,j+1,node)  
            solve(i,j-1,node)
            board[i][j]=c
        for i in range(m):
            for j in range(n):
                solve(i,j,root)
        return ans