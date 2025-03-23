package striver.basics.patterns;

public class Pattern4 {
    /**
     *    * * * * *
     *      * * * *
     *        * * *
     *          * *
     *            *
     * @param args
     */
    public static void main(String[] args) {
        int n = 5;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (j >= i)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.print("\n");
        }
    }
}
