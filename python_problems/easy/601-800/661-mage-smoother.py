class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])

        arr = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):

                avg_num = 0
                sum_num = 0

                avg_num = img[i][j] + (img[i-1][j] if i-1 > -1 else 0) + (img[i][j-1] if j-1 > -1 else 0)
                avg_num += (img[i+1][j] if i+1 < m else 0) + (img[i][j+1] if j+1 < n else 0) + (img[i+1][j+1] if i+1 < m and j+1 < n else 0)
                avg_num += (img[i+1][j-1] if i+1 < m and j-1 > -1 else 0) + (img[i-1][j+1] if j+1 < n and i-1 > -1 else 0) + (img[i-1][j-1] if i-1 > -1 and j-1 > -1 else 0)


                sum_num = 1 + (1 if i-1 > -1 else 0) + (1 if j-1 > -1 else 0) + (1 if i+1 < m else 0) + (1 if j+1 < n else 0) + (1 if i+1 < m and j+1 < n else 0) + (1 if i+1 < m and j-1 > -1 else 0) + (1 if j+1 < n and i-1 > -1 else 0) + (1 if i-1 > -1 and j-1 > -1 else 0)

                arr[i][j] = avg_num/sum_num

        return arr
