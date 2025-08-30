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

    def floor(self, nums: list[int], target: int):
        """
        Finds the index of the largest element less than or equal to target (floor) in a sorted array. nums[idx] <= target
        Note: Returns -1 if all elements are greater than target. Only works for sorted arrays (ascending order).
        """
        n = len(nums)
        ans = -1
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] <= target:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def ceil(self, nums: list[int], target: int):
        """
        Finds the index of the smallest element greater than or equal to target (ceil) in a sorted array. nums[idx] >= target
        Note: Returns n if all elements are less than target. Only works for sorted arrays (ascending order).
        """
        n = len(nums)
        ans = n
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def search_in_rotated_sorted_array(self, nums: list[int], target: int):
        """
        Searches for target in a rotated sorted array with no duplicates.
        Approach: Modified binary search to determine which half is sorted and adjust search accordingly.
        Time: O(log n), Space: O(1)
        Returns the index if found, else -1.
        Note: Only works for rotated sorted arrays (ascending order, no duplicates).
        """
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            # If the mid element is the target, return its index
            if nums[mid] == target:
                return mid

            # Check which half is sorted
            if nums[low] <= nums[mid]:
                # Left half is sorted
                if nums[low] <= target <= nums[mid]:
                    # Target is in the left half
                    high = mid - 1
                else:
                    # Target is in the right half
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[high]:
                    # Target is in the right half
                    low = mid + 1
                else:
                    # Target is in the left half
                    high = mid - 1
        return -1

    def search_in_rotated_sorted_array_2(self, nums: list[int], target: int):
        """
        Searches for target in a rotated sorted array that may contain duplicates.
        Approach: Modified binary search with extra checks for duplicates.
        Time: O(log n) average, O(n) worst case (when duplicates are present).
        Returns True if found, else False.
        Note: Handles rotated sorted arrays with duplicates.
        """
        n = len(nums)
        low, high = 0, n - 1

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            # If the mid element is the target, return True
            if nums[mid] == target:
                return True

            # If low, mid, and high are all equal, we can't determine the sorted half, so shrink the window
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            # Left half is sorted
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    # Target is in the left half
                    high = mid - 1
                else:
                    # Target is in the right half
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    # Target is in the right half
                    low = mid + 1
                else:
                    # Target is in the left half
                    high = mid - 1
        return False

    def find_min(self, nums: list[int]):
        n = len(nums)
        low, high = 0, n - 1

        ans = float("inf")

        while low <= high:
            mid = low + (high - low) // 2

            # if the entire search space is sorted
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break

            # find first half is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1
        return ans


def test_binary_search():
    bs = BinarySearch()
    inp = [3, 4, 6, 7, 9, 12, 16, 17]
    print(bs.search_number(inp, 17))
    print(bs.search_number_recursive(inp, 0, len(inp) - 1, 17))
    # Test floor and ceil
    print("Floor of 10:", bs.floor(inp, 10))  # Should print index of 9 (which is 4)
    print("Ceil of 10:", bs.ceil(inp, 10))  # Should print index of 12 (which is 5)
    print(
        f"Search in Rotated sorted array {bs.search_in_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 5)}"
    )
    print(
        f"Search in Rotated sorted array 2 {bs.search_in_rotated_sorted_array_2([2, 5, 6, 0, 0, 1, 2], 2)}"
    )
    print(f"Find Mind {bs.find_min([3, 4, 5, 1, 2])}")


test_binary_search()
