class BinarySearch:
    def search_number(self, nums: list[int], target: int) -> int:
        """
        Iterative Binary Search.
        Note: Only works for sorted arrays (ascending order).
        Approach: Repeatedly divide the search interval in half. If the value of the search key is less than the item in the middle, narrow the interval to the lower half. Otherwise, narrow it to the upper half.
        Time: O(log n), Space: O(1)
        Returns the index of target if found, else -1.
        Overflow Note: In languages with fixed-width integers, use mid = low + (high - low) // 2 to avoid overflow. In Python, this is not an issue, but it's good practice for interviews and other languages.
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search_number_recursive(
        self, nums: list[int], low: int, high: int, target: int
    ):
        """
        Recursive Binary Search.
        Note: Only works for sorted arrays (ascending order).
        Approach: Recursively divide the search interval in half and search in the appropriate half.
        Time: O(log n), Space: O(log n) due to recursion stack.
        Returns the index of target if found, else -1.
        """
        if low > high:
            return -1
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            return self.search_number_recursive(nums, mid + 1, high, target)
        return self.search_number_recursive(nums, low, mid - 1, target)


def test_binary_search():
    bs = BinarySearch()
    inp = [3, 4, 6, 7, 9, 12, 16, 17]
    print(bs.search_number(inp, 17))
    print(bs.search_number_recursive(inp, 0, len(inp) - 1, 17))


test_binary_search()
