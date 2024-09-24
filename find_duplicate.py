def find_duplicate(nums):
    slow = fast = nums[0]

    # Phase 1: Finding intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Finding the entrance to the cycle (duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate(nums))  # Output: 2
