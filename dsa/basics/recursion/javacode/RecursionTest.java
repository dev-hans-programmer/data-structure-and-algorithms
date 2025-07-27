package dsa.basics.recursion.javacode;

import java.util.ArrayList;
import java.util.Arrays;

public class RecursionTest {
    public static void main(String[] args) {
        System.out.println("Print 1 To N");
        BasicRecursion.counter(1, 5);
        System.out.println("\nPrint Name 1 to N");
        BasicRecursion.printNameNTimes(5, 1);
        System.out.println("\nPrint N to 1");
        BasicRecursion.printNTo1(5, 5);
        System.out.println("\nPrint 1 to N with Backtracking");
        BasicRecursion.print1ToNBacktracking(5, 5);
        System.out.println("\nPrint N to 1 with Backtracking");
        BasicRecursion.printNTo1Backtracking(1, 5);
        System.out.println("Sum of N numbers using parameterised way:\n" + BasicRecursion.sumOfN(4, 0));
        System.out.println("Sum of N numbers using functional way:\n" + BasicRecursion.sumOfNFunctional(4));
        System.out.println("Factorial of N:\n" + BasicRecursion.factorial(3));
        System.out.println("Fibonacci position of N:\n" + BasicRecursion.fibo(3));
        System.out.println("Reverse an array using 2 pointer loop:\n"
                + Arrays.toString(BasicRecursion.reverseArrayLoop(new int[] { 1, 2, 3, 4 })));

        System.out.println("Reverse an array using 2 pointer recursion:\n"
                + Arrays.toString(BasicRecursion.reverseArrayRecursion(new int[] { 1, 2, 3, 4 }, 0, 3)));

        System.out.println("Reverse an array using single pointer recursion:\n"
                + Arrays.toString(BasicRecursion.reverseArraySinglePointerRecursion(new int[] { 1, 2, 3, 4 }, 4, 0)));

        System.out.println("Palindrome using recursion");
        char[] str = "margram".toCharArray();
        System.out.println(BasicRecursion.isPalindrome(str, str.length, 0));
        System.out.println("Print all subsequence of an array");
        Subsequence.printSubsequence(0, new ArrayList<>(), new int[] {3,1,2}, 3);
        System.out.println("Longest common subsequence");
        System.out.println( Subsequence.longestCommonSubsequence("abcde", "ace"));
        
        Subsequence.subsequenceWithSum(0, new ArrayList<>(), new int[] {1, 2, 1}, 3, 2, 0);

}
}
