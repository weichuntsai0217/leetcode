# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
class Solution(object):
    def read(self, buf, n):
        idx = 0
        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = read4(buf4)
            # if no more char in file, return
            if not l:
                return idx
            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx