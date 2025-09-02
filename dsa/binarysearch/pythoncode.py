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
        """
        Finds the minimum element in a rotated sorted array (no duplicates).
        Approach: Modified binary search to find the inflection point (minimum).
        Time: O(log n), Space: O(1)
        Returns the minimum value in the array.
        Note: Only works for rotated sorted arrays (ascending order, no duplicates).
        """
        n = len(nums)
        low, high = 0, n - 1
        ans = float("inf")  # Initialize answer to infinity

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            # If the entire search space is sorted, the minimum is at low
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break

            # If the left half is sorted
            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])  # Update answer with leftmost value
                low = mid + 1  # Move to the right half
            else:
                # Otherwise, the right half is sorted or contains the min
                ans = min(ans, nums[mid])  # Update answer with mid value
                high = mid - 1  # Move to the left half
        return ans

    def find_k_rotation(self, nums: list[int]):
        """
        Finds the number of times a sorted array has been rotated (index of the minimum element).
        Approach: Modified binary search to find the index of the minimum element (rotation count).
        Time: O(log n), Space: O(1)
        Returns the index of the minimum value in the array (rotation count).
        Note: Only works for rotated sorted arrays (ascending order, no duplicates).
        """
        n = len(nums)
        low, high = 0, n - 1
        ans = float("inf")  # Initialize answer to infinity
        ans_idx = -1  # Initialize index of minimum

        while low <= high:
            # Calculate mid to avoid overflow
            mid = low + (high - low) // 2

            low_val = nums[low]
            mid_value = nums[mid]

            # If the entire search space is sorted, the minimum is at low
            if low_val <= nums[high]:
                if ans > low_val:
                    ans = low_val
                    ans_idx = low
                break

            # If the left half is sorted
            if low_val <= mid_value:
                if ans > low_val:
                    ans = low_val
                    ans_idx = low
                low = mid + 1  # Move to the right half
            else:
                # Otherwise, the right half is sorted or contains the min
                if ans > mid_value:
                    ans = mid_value
                    ans_idx = mid
                high = mid - 1  # Move to the left half
        return ans_idx

    def single_non_duplicate_number(self, nums: list[int]):
        """
        Finds the single non-duplicate element in a sorted array where every other element appears exactly twice.
        Approach: Binary search using index parity to find the unique element.
        Time: O(log n), Space: O(1)
        Returns the single non-duplicate number, or -1 if not found.
        Note: Only works for sorted arrays with exactly one non-duplicate and all others appearing twice.

        Before the single element, everything is (even, odd) index based, and after it (odd, even)
        based on this logic, we eliminated the halves
        """
        n = len(nums)
        low, high = (
            1,
            n - 2,
        )  # Start from 1 and n-2 to avoid out-of-bounds for mid-1/mid+1

        # Edge case: only one element
        if n == 1:
            return nums[0]
        # Edge case: unique element is at the start
        elif nums[0] != nums[1]:
            return nums[0]
        # Edge case: unique element is at the end
        elif nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        while low <= high:
            # Calculate mid
            mid = (low + high) // 2

            # Check if mid is the unique element
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # If mid is even and equals next, or mid is odd and equals previous, unique is to the right
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (
                mid % 2 == 1 and nums[mid] == nums[mid - 1]
            ):
                low = mid + 1
            else:
                # Otherwise, unique is to the left
                high = mid - 1
        return -1

    def find_peak_element(self, nums: list[int]):
        """
        Finds a peak element in the array (an element strictly greater than its neighbors).
        Approach: Binary search to find a peak (not necessarily the global maximum).
        Time: O(log n), Space: O(1)
        Returns the index of a peak element, or -1 if not found (should not happen for valid input).
        Note: For arrays with multiple peaks, any peak index may be returned. Edges are considered peaks if they are greater than their single neighbor.
        """
        n = len(nums)
        low, high = 1, n - 2  # Avoid out-of-bounds for mid-1 and mid+1

        # Edge case: only one element
        if n == 1:
            return 0
        # Edge case: peak at the start
        elif nums[0] > nums[1]:
            return 0
        # Edge case: peak at the end
        elif nums[n - 1] > nums[n - 2]:
            return n - 1

        while low <= high:
            # Calculate mid
            mid = (low + high) // 2

            # Check if mid is a peak
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            # If the left neighbor is less, move right
            elif nums[mid - 1] < nums[mid]:
                low = mid + 1
            else:
                # Otherwise, move left
                high = mid - 1
        return -1

    def square_root_number(self, target: int):
        """
        Finds the integer part of the square root of a non-negative integer using binary search.
        Approach: Binary search for the largest integer whose square is less than or equal to target.
        Time: O(log target), Space: O(1)
        Returns the integer square root (i.e., floor of the true square root).
        Note: Returns 0 for target = 0. For negative input, behavior is undefined.
        """
        low, high = 1, target  # Search space is [1, target]
        ans = 1  # Default answer for target >= 1

        while low <= high:
            # Calculate mid
            mid = (low + high) // 2

            # If mid*mid is less than or equal to target, mid is a candidate
            if mid * mid <= target:
                ans = mid  # Update answer
                low = mid + 1  # Try to find a larger square root
            else:
                high = mid - 1  # Try smaller values
        return ans

    def fn(self, i: int, m: int, n: int):
        result = 1

        for _ in range(n):
            result *= i
            if result > m:
                return result
        return result
        ...

    def nth_root_of_m(self, n: int, m: int):
        low, high = 1, m

        while low <= high:
            mid = (low + high) // 2

            power = self.fn(mid, m, n)

            if power == m:
                return mid
            elif power > m:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def get_total_time_to_eat_banana(self, bananas: list[int], rate: int):
        import math

        total_hours = 0
        for banana in bananas:
            total_hours += math.ceil(banana / rate)
        return total_hours

    def min_rate_to_eat_banana(self, bananas: list[int], given_time: int):
        low, high = 1, max(bananas)
        ans = float("inf")
        while low <= high:
            mid = (low + high) // 2

            taken_time = self.get_total_time_to_eat_banana(bananas, mid)

            if taken_time <= given_time:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
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
    print(
        f"How many times array has been rotated {bs.find_k_rotation([3, 4, 5, 1, 2])}"
    )
    print(f"Non duplicate number {bs.single_non_duplicate_number([1, 1, 3, 5, 5])}")
    print(f"Peak element {bs.find_peak_element([1, 2, 1, 3, 5, 6, 4])}")
    print(f"Square root of {bs.square_root_number(6)}")
    print(f"Nth Roor of a number {bs.nth_root_of_m(4, 256)}")
    print(f"Banana eaten per hour {bs.min_rate_to_eat_banana([25, 12, 8, 14, 19], 5)}")


test_binary_search()
