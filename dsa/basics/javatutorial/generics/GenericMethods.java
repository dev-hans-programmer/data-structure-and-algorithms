package dsa.basics.javatutorial.generics;

public class GenericMethods {
    public static int max(int a, int b) {
        return a > b ? a : b;
    }

    public static <T extends Comparable<T>> T maxGeneric(T a, T b) { // Generic method
        return a.compareTo(b) < 0 ? b : a; // If we don't give this bound, then it will give compile time error
    }
    public static <K,V> void printKey(K key, V value) {
        System.out.println("key" + "=" + value );
    }


}
