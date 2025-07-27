package dsa.basics.patterns.javacode;

public class Pattern5 {
     /**
     *      * * * * *
     *      * * * *
     *      * * *
     *      * *
     *      *
     * @param args
     */

    public static void main(String[] args) {
        int n = 5;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (j <= n + 1 - i)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.print("\n");
        }
    }
}
