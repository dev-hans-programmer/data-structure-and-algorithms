class PracticeRecursion {
    printSubsequence(index = 0, subs = [], arr = []) {
        // Base condition
        if(index >= arr.length) {
            console.log(subs);
            return
        }
        // Take
        subs.push(arr[index])
        // call
        this.printSubsequence(index + 1, subs, arr)
        subs.pop()
        this.printSubsequence(index + 1, subs, arr)
        //Non-take
    }
    printSubsequenceWithSum(index = 0, subs = [], arr = [], currentSum = 0, target) {
        if(index >= arr.length) {
            if(currentSum === target) {
                console.log(subs)
            }
            return
        }
        subs.push(arr[index])
        currentSum += arr[index]
        this.printSubsequenceWithSum(index + 1, subs, arr, currentSum, target)
        subs.pop()
        currentSum -= arr[index]
        this.printSubsequenceWithSum(index + 1, subs, arr, currentSum, target)
        
    }
    // print only once
    printSubsequenceWithSumOnce(index = 0, subs = [], arr = [], currentSum = 0, target) {
        if(index >= arr.length) {
            if(currentSum === target) {
                console.log(subs)
                return true
            }
            return false
        }

        subs.push(arr[index])
        currentSum += arr[index]
        if(this.printSubsequenceWithSumOnce(index + 1, subs, arr, currentSum, target)) return true
        subs.pop()
        currentSum -= arr[index]
        if(this.printSubsequenceWithSumOnce(index + 1, subs, arr, currentSum, target)) return true
        return false
    }


}

function testPracticeRecursion() {
    const recursion = new PracticeRecursion();
    // recursion.printSubsequence(0, [], [3,1,2]);
    // recursion.printSubsequenceWithSum(0, [], [1,2,1], 0, 2)
    recursion.printSubsequenceWithSumOnce(0, [], [1,2,1], 0, 2)
}
testPracticeRecursion()