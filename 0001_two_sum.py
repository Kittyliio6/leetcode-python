class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 字典，保存 数字:下标
        record = {}
        for i, num in enumerate(nums):
            need = target - num
            # 找到了另一半
            if need in record:
                return [record[need], i]
            # 没找到，把当前数字存进字典
            record[num] = i

# =========测试代码，本地运行用=========
if __name__ == "__main__":
    sol = Solution()
    # 样例输入
    nums = [2,7,11,15]
    target = 9
    print(sol.twoSum(nums, target))
