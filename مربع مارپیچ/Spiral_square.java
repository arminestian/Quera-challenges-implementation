import java.util.Scanner;
public class Marpich {
    public static int counter = 1 ;
    public static boolean recursive (int [][] a , int i , int j , int direction) {
        if (i == a.length | j == a[0].length | i == -1 | j == -1) return false;
        if (a[i][j] != 0) return false;
        a[i][j] = counter;
        counter++;
        if (direction == 1)//right//
        {
            if (!recursive(a, i, j + 1, 1)) {
                recursive(a, i + 1, j, 2);
            }
        } else if (direction == 2)//down
        {
            if (!recursive(a, i + 1, j, 2)) {
                recursive(a, i, j - 1, 3);
            }
        } else if (direction == 3)//left
        {
            if (!recursive(a, i, j - 1, 3)) {
                recursive(a, i - 1, j, 4);
            }
        } else if (direction == 4)//up
        {
            if (!recursive(a, i - 1, j, 4)) {
                recursive(a, i, j + 1, 1);
            }
        }
        return true;
    }
    public static int [] IndexOf (int [][] a , int value1 , int value2){
        int [] result = new int[4] ;
        for (int i = 0 ; i < a.length ; i++){
            for (int j = 0 ; j < a[0].length ; j++){
                if (a[i][j] == value1){
                    result[0] = i;
                    result[1] = j;
                }
                if (a[i][j] == value2){
                    result [2] = i;
                    result [3] = j;
                }
            }
        }
        return result;
    }
    public static void main (String [] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int [][] a = new int[n][n];
        recursive(a,0,0,1);
        int s = input.nextInt();
        int d = input.nextInt();
        int [] result = IndexOf(a,s,d);
        int RightLeft = result[3] - result[1];
        int UpDown = result[2] - result[0];
        if (RightLeft > 0){
            System.out.println(RightLeft + " R");
        }
        else if (RightLeft < 0){
            System.out.println(-RightLeft + " L");
        }
        if (UpDown > 0){
            System.out.println(UpDown + " U");
        }
        else if (UpDown < 0){
            System.out.println(-UpDown + " D");
        }

//
//        for (int i = 0 ; i < n ; i++){
//            for (int j = 0 ; j < n ; j++){
//                System.out.print(a[i][j]+"  ");
//            }
//            System.out.println();
//        }

    }
}