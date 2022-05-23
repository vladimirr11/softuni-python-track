nums = list(map(int, input().split(', ')))
target_index = int(input())

helper_stack = []
num_at_index = nums[target_index]

for i in range(len(nums)):
    if i == target_index:
        continue
    if nums[i] <= num_at_index:
        helper_stack.append(nums[i])

print(sum(helper_stack) + num_at_index)
