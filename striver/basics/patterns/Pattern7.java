package striver.basics.patterns;

public class Pattern7 {

     /**
     *                 *
     *                *  *
     *              *  *  *
     *             *  *  *  *
     *           *  *  *  *  *
     * 
     * @param args
     */

    public static void main(String[] args) {
        int row = 5, col = 9;
        boolean shouldPrint = true;

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (j >= (row + 1) - i && j <= (row - 1) + i && shouldPrint) {
                    System.out.print("*");
                    shouldPrint = false;
                } else {
                    System.out.print(" ");
                    shouldPrint = true;
                }
            }
            System.out.println();
        }

    }
}
