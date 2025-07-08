class PracticeRecursion:
    def print_subsequence(self, index: int, subs: list[int], arr: list[int]):
        if index >= len(arr):
            print(subs)
            return
        subs.append(arr[index])
        self.print_subsequence(index + 1, subs, arr)
        subs.pop()
        self.print_subsequence(index + 1, subs, arr)

    def subsequence_with_sum(self, idx, subs: list[int], arr: list[int], current_sum: int, target_sum: int):
        if idx >= len(arr):
            if current_sum == target_sum:
                print(subs)
            return
        # take
        subs.append(arr[idx])
        current_sum += arr[idx]
        self.subsequence_with_sum(idx + 1, subs, arr, current_sum, target_sum)

        subs.pop()
        current_sum -= arr[idx]
        self.subsequence_with_sum(idx + 1, subs, arr, current_sum, target_sum)

    def get_subsequence_count(self, index: int, subs: list[int], arr: list[int]) -> int:
        if index >= len(arr):
            return 1
        subs.append(arr[index])
        left = self.get_subsequence_count(index + 1, subs, arr)
        subs.pop()
        right = self.get_subsequence_count(index + 1,subs, arr)
        return left + right
    
    def get_all_subsequences(self, index: int, subs: list[int], arr: list[int]) -> list[list[int]]:
        if index >= len(arr):
            return [subs[:]] # Creating a copy of this subs
        subs.append(arr[index])
        left_subs = self.get_all_subsequences(index + 1, subs, arr)
        subs.pop()
        right_subs = self.get_all_subsequences(index + 1, subs, arr)
        return left_subs + right_subs



def test_practice_recursion():
    p = PracticeRecursion()
    # p.print_subsequence(0, [], [3,1,2])
    # p.subsequence_with_sum(0, [], [1,2,1], 0, 2 )
    print(p.get_subsequence_count(0, [], [3,1,2]))
    print(p.get_all_subsequences(0, [], [3,1,2]))

test_practice_recursion()
        