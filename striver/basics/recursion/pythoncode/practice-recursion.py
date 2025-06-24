class PracticeRecursion:
    def print_subsequence(self, index: int, subs: list[int], arr: list[int]):
        if index >= len(arr):
            print(subs)
            return
        subs.append(arr[index])
        self.print_subsequence(index + 1, subs, arr)
        subs.pop()
        self.print_subsequence(index + 1, subs, arr)



def test_practice_recursion():
    p = PracticeRecursion()
    p.print_subsequence(0, [], [3,1,2])

test_practice_recursion()
        