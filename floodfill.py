class Solution(object):
"""
    def getPixelUpVal(self, image, pr, pc):
        if pr-1 >= 0: return image[pr-1][pc]
        else: return -1

    def getPixelDownVal(self, image, pr, pc):
        if pr+1 < len(image): return image[pr+1][pc]
        else: return -1

    def getPixelRightVal(self, image, pr, pc):
        if pc+1 < len(image[0]): return image[pr][pc+1]
        else: return -1

    def getPixelLeftVal(self, image, pr, pc):
        if pc-1 >= 0: return image[pr][pc-1]
        else: return -1
"""
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """







        """
        pixels = [(sr,sc)]

        startPixelColor = image[sr][sc]
        while len(pixels) != 0:
            (pr, pc) = pixels.pop()
            image[pr][pc] = newColor
            pixelUpColor = self.getPixelUpVal(image, pr, pc)
            pixelDownColor = self.getPixelDownVal(image, pr, pc)
            pixelRightColor = self.getPixelRightVal(image, pr, pc)
            pixelLeftColor = self.getPixelLeftVal(image, pr, pc)
            if pixelUpColor == startPixelColor: pixels.append((pr-1,pc))
            if pixelDownColor == startPixelColor: pixels.append((pr+1,pc))
            if pixelRightColor == startPixelColor: pixels.append((pr,pc+1))
            if pixelLeftColor == startPixelColor: pixels.append((pr,pc-1))
        return image

        """
