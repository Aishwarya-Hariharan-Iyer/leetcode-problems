class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        l = len(colors)
        if l == 2:
            return 1

        dist = [[-1] * l for i in range(l)]
        max_val = 0

        for i in range(l):
            for j in range(l):
                if dist[j][i] != -1:
                    dist[i][j] = dist[j][i]
                dist[i][j] = abs(i-j)
                if colors[i] != colors[j]:
                    max_val = max(dist[i][j], max_val)

        return max_val



