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

    def lower_bound(self, nums: list[int], target: int):
        """
        Finds the index of the first element not less than target (lower bound) in a sorted array.
        Approach: Binary search to find the smallest index where nums[index] >= target.
        Time: O(log n), Space: O(1)
        Returns n if all elements are less than target.
        """
        n = len(nums)
        lower_bound = n  # Default to n if no element >= target
        low = 0
        high = n - 1

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            # If current element is greater than or equal to target,
            # it could be a potential answer, so move left to find smaller index
            if nums[mid] >= target:
                high = mid - 1
                lower_bound = mid
            else:
                # Otherwise, move right
                low = mid + 1
        return lower_bound

    def upper_bound(self, nums: list[int], target: int):
        """
        Finds the index of the first element greater than target (upper bound) in a sorted array.
        Approach: Binary search to find the smallest index where nums[index] > target.
        Time: O(log n), Space: O(1)
        Returns n if all elements are less than or equal to target.
        Note: Only works for sorted arrays (ascending order).
        Overflow Note: In languages with fixed-width integers, use mid = low + (high - low) // 2 to avoid overflow. In Python, this is not an issue, but it's good practice for interviews and other languages.
        """
        n = len(nums)
        upper = n  # Default to n if no element > target
        low, high = 0, n - 1

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            # If current element is greater than target,
            # it could be a potential answer, so move left to find smaller index
            if nums[mid] > target:
                upper = mid
                high = mid - 1
            else:
                # Otherwise, move right
                low = mid + 1
        return upper

    def search_insert_position(self, nums: list[int], target: int):
        """
        Finds the index where the target should be inserted in a sorted array to maintain order.
        Approach: Binary search to find the smallest index where nums[index] >= target.
        Time: O(log n), Space: O(1)
        Returns the index if target is found, or the position where it should be inserted.
        Note: Only works for sorted arrays (ascending order).
        Overflow Note: In languages with fixed-width integers, use mid = low + (high - low) // 2 to avoid overflow. In Python, this is not an issue, but it's good practice for interviews and other languages.

        This is a similar problem to lower bound or celing
        """
        n = len(nums)
        position = n  # Default to n if target is greater than all elements
        low, high = 0, n - 1

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            # If current element is greater than or equal to target,
            # it could be a potential answer, so move left to find smaller index
            if nums[mid] >= target:
                position = mid
                high = mid - 1
            else:
                # Otherwise, move right
                low = mid + 1
        return position


def test_binary_search():
    bs = BinarySearch()
    inp = [3, 4, 6, 7, 9, 12, 16, 17]
    print(bs.search_number(inp, 17))
    print(bs.search_number_recursive(inp, 0, len(inp) - 1, 17))


test_binary_search()
