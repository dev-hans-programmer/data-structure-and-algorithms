package striver.basics.patterns;

public class Pattern8 {
     /**
     *             1
     *             1 2
     *             1 2 3
     *             1 2 3 4
     *             1 2 3 4 5
     * 
     * @param args
     */
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            for (int j = 1; j <= 5; j++) {
                if (j <= i) {
                    System.out.print(j + "");
                } else
                    System.out.print(" ");
            }
            System.out.println();
        }
    }
}
