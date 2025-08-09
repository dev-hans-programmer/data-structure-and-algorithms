import copy


class EasyArrayProblems:
    def test(self):
        """
        Prints a test message to verify class instantiation.
        Time: O(1), Space: O(1)
        """
        print("Hello Array Test")

    def get_largest_element(self, nums: list[int]):
        """
        Finds the largest element in the array by linear scan.
        Approach: Iterate through the array and keep track of the largest value.
        Time: O(n), Space: O(1)
        """
        largest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
        return largest

    def get_second_largest_brute(self, nums: list[int]):
        """
        Finds the second largest element using brute force.
        Approach: Find the largest, remove it, then find the largest again.
        Time: O(n), Space: O(n) (due to copy)
        """
        largest = self.get_largest_element(nums)
        new_list = copy.copy(nums)
        new_list.remove(largest)
        second_largest = self.get_largest_element(new_list)
        return second_largest

    def get_second_largest_better(self, nums: list[int]):
        """
        Finds the second largest element in two passes.
        Approach: First pass to find largest, second pass to find next largest.
        Time: O(n), Space: O(1)
        """
        largest = nums[0]
        second_largest = 0
        for num in nums:
            if num > largest:
                largest = num
        for num in nums:
            if num > second_largest and num != largest:
                second_largest = num
        return second_largest

    def get_second_largest_optimal(self, nums: list[int]) -> int:
        """
        Finds the second largest element in a single pass.
        Approach: Track largest and second largest while iterating.
        Time: O(n), Space: O(1)
        """
        largest = second_largest = float("-inf")
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        return int(second_largest)

    def check_array_sorted_or_rotated(self, nums: list[int]) -> bool:
        """
        Checks if the array is sorted and then rotated.
        Approach: Count the number of places where the order breaks; if more than one, it's not sorted and rotated.
        Time: O(n), Space: O(1)
        """
        count = 0
        length = len(nums)
        for i in range(length):
            prev = (i + 1) % length
            if nums[i] > nums[prev]:
                count += 1
                if count >= 2:
                    return False
        return True

    def r_duplicates_brute(self, nums):
        """
        Removes duplicates using set.
        Approach: Convert to set and count unique elements.
        Time: O(n), Space: O(n)
        """
        return len(list(set(nums)))

    def r_duplicates_better(self, nums: list[int]):
        """
        Removes duplicates using a frequency dictionary.
        Approach: Count frequency, overwrite array with unique elements, fill rest with zeros.
        Time: O(n), Space: O(n)
        """
        freq = {}
        idx = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for f in freq:
            nums[idx] = f
            idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
        return (idx, nums)

    def r_ruplicates_best(self, nums: list[int]):
        """
        Removes duplicates from sorted array using two-pointer approach.
        Approach: Move unique elements to the front, count them.
        Time: O(n), Space: O(1)
        """
        i = 0
        j = i + 1
        while j < len(nums) - 1:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

    def remove_duplicates_from_sorted_array(self, nums: list[int]):
        """
        Removes duplicates from sorted array in-place.
        Approach: Uses the best (two-pointer) method for efficiency.
        Time: O(n), Space: O(1)
        """
        # return self.r_duplicates_brute(nums)
        # return self.r_duplicates_better(nums)
        return self.r_ruplicates_best(nums)

    def reverse_array(self, nums: list[int], start: int, end: int):
        """
        Reverses a portion of the array in-place.
        Approach: Swap elements from both ends moving towards the center.
        Time: O(n), Space: O(1)
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def left_rotate_by_one(self, nums: list[int]):
        """
        Rotates the array to the left by one position.
        Approach: Store first element, shift all left, put first at end.
        Time: O(n), Space: O(1)
        """
        temp = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]
        nums[i + 1] = temp

    def right_rotate_by_one(self, nums: list[int]):
        """
        Rotates the array to the right by one position.
        Approach: Store last element, shift all right, put last at start.
        Time: O(n), Space: O(1)
        """
        temp = nums[len(nums) - 1]
        i = len(nums) - 1
        while i > 0:
            nums[i] = nums[i - 1]
            i -= 1
        nums[i] = temp

    def left_rotate_by_kth_brute(self, nums: list[int], k: int):
        """
        Rotates the array to the left by k positions (brute force).
        Approach: Rotate by one, k times.
        Time: O(n*k), Space: O(1)
        """
        n = len(nums)
        for _ in range(k):
            temp = nums[0]
            j = 0
            while j < n - 1:
                nums[j] = nums[j + 1]
                j += 1
            nums[j] = temp

    def left_rotate_by_kth_optimal(self, nums: list[int], k: int):
        """
        Rotates the array to the left by k positions (optimal).
        Approach: Reverse first k, reverse rest, reverse all.
        Time: O(n), Space: O(1)
        """
        n = len(nums)
        k = k % n
        if n == 0 or k == 0:
            return
        self.reverse_array(nums, 0, k - 1)
        self.reverse_array(nums, k, n - 1)
        self.reverse_array(nums, 0, n - 1)

    def right_rotate_by_kth_brute(self, nums: list[int], k: int):
        """
        Rotates the array to the right by k positions (brute force).
        Approach: Rotate by one, k times.
        Time: O(n*k), Space: O(1)
        """
        n = len(nums)
        for _ in range(k):
            temp = nums[n - 1]
            j = n - 1
            while j > 0:
                nums[j] = nums[j - 1]
                j -= 1
            nums[j] = temp

    def right_rotate_by_kth_better(self, nums: list[int], k: int):
        """
        Rotates the array to the right by k positions (optimal).
        Approach: Reverse all, reverse first k, reverse rest.
        Time: O(n), Space: O(1)
        """
        k = k % len(nums)
        self.reverse_array(nums, 0, len(nums) - 1)
        self.reverse_array(nums, 0, k - 1)
        self.reverse_array(nums, k, len(nums) - 1)
        print(nums)

    def right_rotate_by_kth(self, nums: list[int], k: int):
        """
        Rotates the array to the right by k positions (calls optimal).
        Approach: Uses the better (optimal) method.
        Time: O(n), Space: O(1)
        """
        # self.right_rotate_by_kth_brute(nums, k)
        self.right_rotate_by_kth_better(nums, k)

    def move_zeros_brute(self, nums: list[int]):
        """
        Moves all zeros to the end using brute force.
        Approach: For each zero, shift elements left and put zero at end.
        Time: O(n^2), Space: O(1)
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                j = i
                temp = nums[i]
                while j < n - 1:
                    nums[j] = nums[j + 1]
                    j += 1
                nums[j] = temp
                n -= 1
            else:
                i += 1
        return nums

    def move_zeros_optimal(self, nums: list[int]):
        """
        Moves all zeros to the end using two-pointer approach.
        Approach: Move non-zeros to front, fill rest with zeros.
        Time: O(n), Space: O(1)
        """
        j = 0  # to move non zero elements at the first element
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < n:
            nums[j] = 0
            j += 1
        return nums

    def move_zeros(self, nums: list[int]):
        """
        Moves all zeros to the end (calls brute force).
        Approach: Uses brute force method by default.
        Time: O(n^2), Space: O(1)
        """
        return self.move_zeros_brute(nums)
        # return self.move_zeros_optimal(nums)


def test_easy_array_problems():
    nums = [1, 4, 2, 3, 10]
    sorted_nums = [3, 4, 5, 1, 2]
    duplicated = [1, 1, 3, 2, 2, 10]
    left_rotated_arr = [1, 2, 3, 4, 5, 6]
    right_rotated_arr = [1, 2, 3, 4, 5, 6, 7]
    moving_zeros = [1, 0, 9, 4, 0, 0, 3]
    p = EasyArrayProblems()
    p.test()
    print(p.get_largest_element(nums))
    print(p.get_second_largest_brute(nums))
    print(p.get_second_largest_better(nums))
    print(p.get_second_largest_optimal(nums))
    print(p.check_array_sorted_or_rotated(sorted_nums))
    print(p.remove_duplicates_from_sorted_array(duplicated))
    # p.left_rotate_by_one(left_rotated_arr)
    # p.left_rotate_by_kth_brute(left_rotated_arr, 2)
    # print(f"After rotation {left_rotated_arr}")
    # p.right_rotate_by_one(right_rotated_arr)
    p.right_rotate_by_kth(right_rotated_arr, 3)
    # print(f"After right rotation {right_rotated_arr}")
    print(f"Zeros at the last {p.move_zeros(moving_zeros)}")


if __name__ == "__main__":
    test_easy_array_problems()
