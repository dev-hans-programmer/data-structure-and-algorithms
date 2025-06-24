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


}

function testPracticeRecursion() {
    const recursion = new PracticeRecursion();
    recursion.printSubsequence(0, [], [3,1,2]);
}
testPracticeRecursion()