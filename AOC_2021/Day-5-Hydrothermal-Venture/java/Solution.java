import java.util.Scanner;
import java.util.*;

public class Solution{
    
    private static int part1() {
        Scanner fs = new Scanner(System.in);
        int[][] arr = new int[1000][1000];
        int x1, y1, x2, y2;
        int count = 0;
        for (int i = 0; i < 500; i++) {
            x1 = fs.nextInt();
            y1 = fs.nextInt();
            x2 = fs.nextInt();
            y2 = fs.nextInt();

            // Store all the possible combinations in an array
            if (x1 == x2) {
                for (int j = Math.min(y1, y2); j <= Math.max(y1, y2); j++) {
                    arr[x1][j]++;
                }
            } else if (y1 == y2) {
                for (int j = Math.min(x1, x2); j <= Math.max(x1, x2); j++) {
                    arr[j][y1]++;
                }
            }
        }

        for (int[] ints : arr) {
            for (int j = 0; j < arr[0].length; j++) {
                if (ints[j] > 1) {
                    count++;
                }
            }
        }
        
        fs.close();
        return count;
    }

    public static void main(String[] arguments){
        System.out.println(part1());
        
    }
}
