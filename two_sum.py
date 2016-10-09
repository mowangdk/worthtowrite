import bisect

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # if numbers is not None or target is not None:
        #     return -1
        total_size = len(numbers)
        for i in range(total_size):
            if numbers[i] <= target:
                start = i + 1
                value = target - numbers[i]
                # list.index 的效率是O(n), 不能用在较大的数组中
                ano_index = bisect.bisect_left(numbers, value, lo=start)
                if ano_index != total_size and numbers[ano_index] == value:
                    return i + 1, ano_index + 1
                continue
            else:
                return -1

if __name__ == '__main__':
    result = Solution().twoSum([0, 0, 0, 0, 0, 0, 0, 0, 3, 4], 7)
    print result
