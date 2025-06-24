package striver.basics.recursion.javacode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Subsequence {
    public static void printSubsequence(int index, List<Integer> subs, int[] arr, int size) {
        if (index >= size) {
            System.out.println(Arrays.toString(subs.toArray()));
            return;

        }
        subs.add(arr[index]); // Take condition
        printSubsequence(index + 1, subs, arr, size);
        subs.remove(subs.size() - 1); // remove last added element
        printSubsequence(index + 1, subs, arr, size); // Non take condition
    }
    public static List<String> getSubsequences(int index, StringBuilder current, String text) {
        if (index == text.length()) {
            return new ArrayList<>(List.of(current.toString()));
        }

        // Include current character
        current.append(text.charAt(index));
        List<String> include = getSubsequences(index + 1, current, text);
        current.deleteCharAt(current.length() - 1); // backtrack

        // Exclude current character
        List<String> exclude = getSubsequences(index + 1, current, text);

        // Merge both results
        include.addAll(exclude);
        return include;
    }

     public static int longestCommonSubsequence(String text1, String text2) {
         List<String> subs1 = getSubsequences(0, new StringBuilder(), text1);
        List<String> subs2 = getSubsequences(0, new StringBuilder(), text2);
        int maxLen = 0;

        Set<String> set2 = new HashSet<>(subs2); // To optimize lookup

        for (String s1 : subs1) {
            if (set2.contains(s1)) {
                maxLen = Math.max(maxLen, s1.length());
            }
        }
        return maxLen;
    }
    
}
