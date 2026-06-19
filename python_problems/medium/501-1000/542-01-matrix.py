class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        queue = []
        directions  = (1, 0), (-1, 0), (0, -1), (0, 1)

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = -1
                else:
                    queue.append((i, j))

        
        for r, c in queue:
            for direc in directions:
                new_r = r + direc[0]
                new_c = c + direc[1]
                if 0 <= new_r < m and 0 <= new_c < n and mat[new_r][new_c] == -1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r, new_c))
        
        return mat
        

        

            
        
        