class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            val = "."
            for j in range(1, n):
                val += ("#" if i != m-1 else ".")
            grid.append(val)
        return grid