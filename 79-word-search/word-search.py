class Solution(object):
    def solve(self,r,c,m,n,ind,board,word):
        if ind==len(word):
            return True
        if r<0 or c<0 or r>=m or c>=n or board[r][c]!=word[ind]:
            return False
        temp=board[r][c]
        board[r][c]="#"
        down=self.solve(r + 1, c, m, n, ind + 1, board, word)
        up = self.solve(r - 1, c, m, n, ind + 1, board, word)
        left = self.solve(r, c - 1, m, n, ind + 1, board, word)
        right = self.solve(r, c + 1, m, n, ind + 1, board, word)
        board[r][c]=temp
        return up or down or left or right
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if self.solve(i,j,m,n,0,board,word):
                        return True
        return False