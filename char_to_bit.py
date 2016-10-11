#!/usr/bin/env python
# fileencoding=utf-8


class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        elements = [0] * n
        # 也可以使用set() & set() 但是效率较低,处理大量的数组的时候会出现超时
        # 所以这里将字符串装换成数字, 判断在一个bit位上的数字是否相同
        for i, s in enumerate(words):
            for c in s:
                elements[i] |= 1 << (ord(c) - 97)

        ans = 0
        for i in xrange(n):
            for j in xrange(i + i, n):
                if not (elements[i] & elements[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


if __name__ == '__main__':
    ans = Solution().maxProduct(['a', 'b', 'c', 'abc', 'cbsss', 'def'])
    print ans
