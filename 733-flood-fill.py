class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        org_color = image[sr][sc]
        if org_color == color:
            return image

        max_r = len(image)
        max_c = len(image[0])

        

        def is_org_color(img, r, c):
            return img[r][c] == org_color
        
        def self_floodFill(image, r, c):
            image[r][c] = color
            if r+1 < max_r and is_org_color(image,r+1,c):
                image = self_floodFill(image, r+1, c)
            if r-1 > -1 and is_org_color(image,r-1,c):
                image = self_floodFill(image, r-1, c)
            if c+1 < max_c and is_org_color(image,r,c+1):
                image = self_floodFill(image, r, c+1)
            if c-1 > -1 and is_org_color(image,r,c-1):
                image = self_floodFill(image, r, c-1)
            return image

        return self_floodFill(image, sr, sc)
        
