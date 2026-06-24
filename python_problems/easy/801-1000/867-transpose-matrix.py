class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m = len(matrix)
        n = len(matrix[0])

        transpose = []

        for i in range(n):
            row = []
            for j in range(m):
                row.append(matrix[j][i])
            transpose += [row]
        
        return transpose