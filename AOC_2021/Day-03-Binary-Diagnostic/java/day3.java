package java;

import java.util.Scanner;

public class day3 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // integer array
        int[] counts = new int[12];

        for (int i = 0; i < 1000; i++) {
            String line = sc.next();
            for (int j = 0; j < 12; j++) {
                char character = line.charAt(j);

                if (character == '1') {
                    counts[j] += 1;
                }
            }
        }

        int gamma = 0;
        for (int i = 0; i < 12; i++) {
            int index = (11 - i);
            if (counts[index] > 500) {
                gamma += Math.pow(2, i);
            }
        }
        int epsilon = 4095 - gamma;
        System.out.println(epsilon * gamma);
        sc.close();
    }
}
