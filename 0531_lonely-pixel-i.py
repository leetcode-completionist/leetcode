# https://leetcode.com/problems/lonely-pixel-i/
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        pixels = set()

        m, n = len(picture), len(picture[0])

        # Keep a pointer to the first seen "lonely" pixel.
        #
        # Clear this buffer when the pixel is found to
        # no longer be "lonely" (e.g. another pixel in the
        # same row or col).
        row_to_lonely_pixel = [None] * m
        col_to_lonely_pixel = [None] * n

        # Keep track of number of pixels seen on each row/col
        row_to_pixel_count = [0] * m
        col_to_pixel_count = [0] * n

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    row_to_pixel_count[i] += 1
                    col_to_pixel_count[j] += 1

                    if (row_to_pixel_count[i] == 1 and
                        col_to_pixel_count[j] == 1):

                        row_to_lonely_pixel[i] = (i, j)
                        col_to_lonely_pixel[j] = (i, j)
                        pixels.add((i, j))
                        continue

                    if row_to_pixel_count[i] > 1:
                        if row_to_lonely_pixel[i] != None:
                            if row_to_lonely_pixel[i] in pixels:
                                pixels.remove(row_to_lonely_pixel[i])

                            row_to_lonely_pixel[i] = None

                    if col_to_pixel_count[j] > 1:
                        if col_to_lonely_pixel[j] != None:
                            if col_to_lonely_pixel[j] in pixels:
                                pixels.remove(col_to_lonely_pixel[j])
                            col_to_lonely_pixel[j] = None

        return len(pixels)
