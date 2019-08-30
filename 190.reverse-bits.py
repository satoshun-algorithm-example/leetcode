class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = format(n, '032b')
        rb = b[::-1]
        return int(rb, 2)
