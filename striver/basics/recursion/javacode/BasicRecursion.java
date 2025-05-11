package striver.basics.recursion.javacode;

public class BasicRecursion {
    // Print 1-N linearly
    public static void counter(int count, int limit) {
        if (count > limit) {
            return;
        }
        System.out.println(count);
        count++;
        counter(count, limit);
    }

    // print name N times
    public static void printNameNTimes(int limit, int times) {
        String name = "Hasan Ali";

        if (times > limit)
            return;
        System.out.println(name);
        printNameNTimes(limit, times + 1);

    }

    // Print numbers from N to 1
    public static void printNTo1(int count, int limit) {
        if (count < 1)
            return;
        System.out.println(count);
        printNTo1(count - 1, limit);

    }

    // Print 1 to N in backtracking mechanism(not allowed + 1)
    public static void print1ToNBacktracking(int i, int n) {
        if (i < 1)
            return;
        print1ToNBacktracking(i - 1, n);
        System.out.println(i);

    }

    // Print 1 to N in backtracking mechanism(not allowed - 1)
    public static void printNTo1Backtracking(int i, int n) {
        if (i > n)
            return;
        printNTo1Backtracking(i + 1, n);
        System.out.println(i);

    }

    // Sum of N natural numbers(Parameterised way)
    public static int sumOfN(int N, int sum) {
        if (N < 1)
            return sum;

        return sumOfN(N - 1, sum + N);
    }

    // Sum of N natural numbers(Functional way)
    public static int sumOfNFunctional(int N) {
        if (N < 0)
            return 0;
        return N + sumOfNFunctional(N - 1);
    }

    // Factorial of N
    public static int factorial(int N) {
        if (N <= 1)
            return 1;
        if (N == 2)
            return 2;

        return N * factorial(N - 1);

    }

    // Fibonacci number
    public static int fibo(int N) {
        if (N == 0)
            return 0;
        if (N == 1)
            return 1;
        return fibo(N - 1) + fibo(N - 2);
    }

    public static void swap(int[] arr, int l, int r) {
        int temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;
    }

    // Reverse an array using 2 pointer(loop)
    public static int[] reverseArrayLoop(int[] arr) {
        int l = 0;
        int r = arr.length - 1;
        while (l < r) {
            // swap
            swap(arr, l, r);
            // update both pointer
            l++;
            r--;

        }
        return arr;

    }

    // Reverse an array using recursion
    public static int[] reverseArrayRecursion(int[] arr, int l, int r) {
        if (l > r)
            return arr;

        swap(arr, l, r);
        return reverseArrayRecursion(arr, l + 1, r - 1);

    }

    // Reverse an array using a single pointer(Recursion)
    public static int[] reverseArraySinglePointerRecursion(int[] arr, int n, int l) {
        if (l >= n / 2)
            return arr;
        swap(arr, l, n - 1 - l);
        return reverseArraySinglePointerRecursion(arr, n, l + 1);
    }

    // Palindrome using recursion
    public static boolean isPalindrome(char[] str, int n, int i) {
        if (i >= n / 2)
            return true;
        if (str[i] != str[n - 1 - i])
            return false;

        return isPalindrome(str, n, i + 1);
    }
}
