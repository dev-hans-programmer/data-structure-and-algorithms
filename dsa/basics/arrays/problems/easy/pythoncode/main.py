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

    def linear_Search(self, nums: list[int], target: int):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def union_arr_brute(self, nums1: list[int], nums2: list[int]):
        """
        Computes the union of two arrays using brute force.
        Approach: Concatenate both arrays and use a set to remove duplicates.
        Time: O(n + m), Space: O(n + m), where n and m are lengths of nums1 and nums2.
        """
        return sorted(list(set(nums1 + nums2)))

    def union_arr_optimal(self, nums1: list[int], nums2: list[int]):
        """
        Computes the union of two sorted arrays using a true two-pointer approach.
        Approach: Traverse both arrays, add unique elements to the result, skip duplicates efficiently.
        Time: O(n + m), Space: O(n + m), where n and m are lengths of nums1 and nums2.
        """
        i, j = 0, 0
        union = []
        n1 = len(nums1)
        n2 = len(nums2)
        while i < n1 and j < n2:
            # Skip duplicates in nums1
            if i > 0 and nums1[i] == nums1[i - 1]:
                i += 1
                continue
            # Skip duplicates in nums2
            if j > 0 and nums2[j] == nums2[j - 1]:
                j += 1
                continue
            if nums1[i] < nums2[j]:
                union.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                union.append(nums2[j])
                j += 1
            else:
                union.append(nums1[i])
                i += 1
                j += 1
        while i < n1:
            if i == 0 or nums1[i] != nums1[i - 1]:
                union.append(nums1[i])
            i += 1
        while j < n2:
            if j == 0 or nums2[j] != nums2[j - 1]:
                union.append(nums2[j])
            j += 1
        return union

    def union_arr_optimal_2(self, nums1: list[int], nums2: list[int]):
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        union = []
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if len(union) == 0 or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1
        while i < n1:
            if len(union) == 0 or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1
        while j < n2:
            if len(union) == 0 or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1
        return union

    def merge_2_sorted_arrays(self, nums1: list[int], m: int, nums2: list[int], n: int):
        """
        Merges two sorted arrays into one sorted array in-place (LeetCode style).
        Approach: Start from the end of both arrays and fill nums1 from the back, comparing elements.
        Time: O(n + m), Space: O(1) (in-place, assuming nums1 has enough space).
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
        return nums1

    def union_arr(self, nums1: list[int], nums2: list[int]):
        # return self.union_arr_brute(nums1, nums2)
        # return self.union_arr_optimal(nums1, nums2)
        return self.union_arr_optimal_2(nums1, nums2)

    def missing_number_brute(self, nums: list[int]):
        """
        Finds the missing number in an array containing numbers from 0 to n using brute force.
        Approach: Check for each number from 0 to n if it is present in the array.
        Time: O(n^2), Space: O(1)
        """
        n = len(nums)
        for i in range(n + 1):
            if i not in nums:
                return i
        return None

    def mising_number_better(self, nums: list[int]):
        """
        Finds the missing number using a hash array.
        Approach: Mark presence of each number, then find the missing one.
        Time: O(n), Space: O(n)
        """
        hash_arr = [0] * (len(nums) + 1)
        for i in nums:
            hash_arr[i] = 1
        for idx, val in enumerate(hash_arr):
            if val == 0:
                return idx
        return None

    def missing_number_optimal(self, nums: list[int]):
        """
        Finds the missing number using sum formula.
        Approach: Calculate expected sum and subtract actual sum.
        Time: O(n), Space: O(1)
        """
        n = len(nums)
        s2 = n * (n + 1) // 2
        return s2 - sum(nums)

    def missing_number(self, nums: list[int]) -> int | None:
        """
        Finds the missing number in an array from 0 to n using the optimal method by default.
        Approach: Uses the optimal sum formula method.
        Time: O(n), Space: O(1)
        """
        # return self.missing_number_brute(nums)
        # return self.mising_number_better(nums)
        return self.missing_number_optimal(nums)

    def max_consecutive_ones(self, nums: list[int]):
        """
        Finds the maximum number of consecutive 1s in a binary array.
        Approach: Count consecutive 1s, reset count on 0, track max.
        Time: O(n), Space: O(1)
        """
        max_count = 0
        count = 0
        for i in nums:
            if i != 0:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 0
        return max_count

    def single_number_optimal_xor(self, nums: list[int]):
        """
        Finds the single number in an array where every other element appears twice using XOR.
        Approach: XOR all elements; pairs cancel out, leaving the single number.
        Time: O(n), Space: O(1)
        """
        res = 0
        for num in nums:
            res ^= num
        return res

    def single_number_brute(self, nums: list[int]):
        """
        Finds the single number using a frequency dictionary.
        Approach: Count occurrences, return the number with count 1.
        Time: O(n), Space: O(n)
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for f in freq:
            if freq[f] < 2:
                return f

    def single_number(self, nums: list[int]):
        """
        Finds the single number in an array using the optimal XOR method by default.
        Approach: Uses the optimal XOR method.
        Time: O(n), Space: O(1)
        """
        # return self.single_number_brute(nums)
        return self.single_number_optimal_xor(nums)

    def longest_sub_arr_with_sum_k_brute1(self, nums: list[int], k: int):
        """
        Finds the length of the longest subarray with sum k using brute force (3 loops).
        Approach: Check all possible subarrays and calculate their sum.
        Time: O(n^3), Space: O(1)
        """
        n = len(nums)
        max_length = 0
        for i in range(n):
            for j in range(i, n):
                s = 0
                for temp in range(i, j + 1):
                    s += nums[temp]
                if s == k:
                    max_length = max(max_length, j - i + 1)
        return max_length

    def longest_sub_arr_with_sum_k_brute2(self, nums: list[int], k: int):
        """
        Finds the length of the longest subarray with sum k using improved brute force (2 loops).
        Approach: For each start index, accumulate sum and check for k.
        Time: O(n^2), Space: O(1)
        """
        n = len(nums)
        max_length = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    max_length = max(max_length, j - i + 1)
        return max_length

    def longest_sub_arr_with_sum_k_optimal(self, nums: list[int], k: int):
        """
        Finds the length of the longest subarray with sum k using prefix sum and hashing.
        Approach: Use a hashmap to store the first occurrence of each prefix sum. For each index, check if (prefix_sum - k) exists; if so, update max length.
        Time: O(n), Space: O(n)
        """
        n = len(nums)
        max_length = 0
        first_index = {}
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == k:
                max_length = max(max_length, i + 1)
            want = prefix_sum - k
            if want in first_index:
                length = i - first_index[want]
                max_length = max(max_length, length)
            if prefix_sum not in first_index:
                first_index[prefix_sum] = i
        return max_length

    def longest_sub_arr_with_sum_k(self, nums: list[int], k: int):
        """
        Finds the length of the longest subarray with sum k using the improved brute force method by default.
        Approach: Uses the improved brute force (O(n^2)) method.
        Time: O(n^2), Space: O(1)
        """
        # return self.longest_sub_arr_with_sum_k_brute1(nums, k)
        # return self.longest_sub_arr_with_sum_k_brute2(nums, k)
        return self.longest_sub_arr_with_sum_k_optimal(nums, k)


def test_easy_array_problems():
    nums = [1, 4, 2, 3, 10]
    sorted_nums = [3, 4, 5, 1, 2]
    duplicated = [1, 1, 3, 2, 2, 10]
    # left_rotated_arr = [1, 2, 3, 4, 5, 6]
    right_rotated_arr = [1, 2, 3, 4, 5, 6, 7]
    moving_zeros = [1, 0, 9, 4, 0, 0, 3]
    missing_number_arr = [0, 1]
    consecutive_1s = [1, 1, 0, 0, 1, 1, 1, 0]
    single_number = [2, 2, 1]
    longest_sub_arr_sum_k = [1, 2, 3, 1, 1, 1, 1]
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
    print(f"Union f{p.union_arr([1, 2, 3, 4, 5], [1, 2, 7])}")
    print(
        f"Merge 2 sorted array leetcode {p.merge_2_sorted_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)}"
    )
    print(f"Missing number {p.missing_number(missing_number_arr)}")
    print(f"Max consecutive ones {p.max_consecutive_ones(consecutive_1s)}")
    print(f"Single Number {p.single_number(single_number)}")
    print(
        f"Longest sub array with Sum {p.longest_sub_arr_with_sum_k(longest_sub_arr_sum_k, 3)}"
    )


if __name__ == "__main__":
    test_easy_array_problems()
