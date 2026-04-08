nums = [int(input()) for _ in range(10)]
print([nums[i - 1] + nums[i + 1] for i in range(1,9)])
