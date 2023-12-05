# %%
from typing import List


# class Solution:
#     def minPairSum(self, nums: List[int]) -> int:
#         nums.sort()
#         result_list = [nums[i] + nums[-1 - i] for i in range(len(nums) // 2)]
#         return max(result_list)


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max([nums[i] + nums[-1 - i] for i in range(len(nums) // 2)])
        # return max(result_list)


s = Solution()
s.minPairSum([3, 5, 2, 3])
# %%

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        # count = 1
        while k >= 0:
            print(f"first nums: {nums}")
            print(f"k: {k}")
            diff_list = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            count_list = []
            for s in set(nums):
                print(f"s: {s}")
                count_list.append(
                    len([i for i in range(len(nums)) if nums[i] - s == 0])
                )
            count = max(count_list)
            if max(diff_list) <= 0:
                print("inside max")
                print(f"nums: {nums}")
                print(f"count: {count}")
                return count
            min_diff = min([x for x in diff_list if x != 0])
            print(f"min_diff: {min_diff}")
            if min_diff > k:
                print("inside if")
                print(f"nums: {nums}")
                print(f"count: {count}")
                return count
            else:
                print("inside else")
                min_diff_index = diff_list.index(min_diff)
                print(f"min_diff_index: {min_diff_index}")
                k = k - min_diff
                nums[min_diff_index] += min_diff
                count
        print(f"nums: {nums}")
        print(f"count: {count}")
        return count


# %%


# https://www.geeksforgeeks.org/window-sliding-technique/
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = res = total = 0
        while right < len(nums):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res


# %%
s = Solution()
# s.maxFrequency([1, 4, 8, 13], k=5)
# s.maxFrequency([1, 2, 4], k=50)
# s.maxFrequency([3, 9, 6], k=20)
s.maxFrequency(
    [
        9930,
        9923,
        9983,
        9997,
        9934,
        9952,
        9945,
        9914,
        9985,
        9982,
        9970,
        9932,
        9985,
        9902,
        9975,
        9990,
        9922,
        9990,
        9994,
        9937,
        9996,
        9964,
        9943,
        9963,
        9911,
        9925,
        9935,
        9945,
        9933,
        9916,
        9930,
        9938,
        10000,
        9916,
        9911,
        9959,
        9957,
        9907,
        9913,
        9916,
        9993,
        9930,
        9975,
        9924,
        9988,
        9923,
        9910,
        9925,
        9977,
        9981,
        9927,
        9930,
        9927,
        9925,
        9923,
        9904,
        9928,
        9928,
        9986,
        9903,
        9985,
        9954,
        9938,
        9911,
        9952,
        9974,
        9926,
        9920,
        9972,
        9983,
        9973,
        9917,
        9995,
        9973,
        9977,
        9947,
        9936,
        9975,
        9954,
        9932,
        9964,
        9972,
        9935,
        9946,
        9966,
    ],
    k=3056,
)


# %%
from typing import List


# class Solution:
#     def reductionOperations(self, nums: List[int]) -> int:
#         nums.sort()
#         count = 0
#         while True:
#             max_num = max(nums)
#             max_num_indices = [i for i, x in enumerate(nums) if x == max_num]
#             if max_num_indices[0] == 0:
#                 return count
#             second_max_num = max([x for x in nums if x != max_num])

#             for i in max_num_indices:
#                 nums[i] = second_max_num
#                 count += 1


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += i + 1
        return count


# %%
s = Solution()
s.reductionOperations([5, 1, 3])
# s.reductionOperations([1, 1, 1])
# s.reductionOperations([1, 1, 2, 2, 3])
