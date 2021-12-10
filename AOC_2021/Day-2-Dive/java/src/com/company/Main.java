package com.company;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int horizontal = 0;
        int vertical = 0;

        for (int i = 0; i < 1000; i++) {
            String instr = sc.next();
            int value = sc.nextInt();
            System.out.printf("sc.next = %s, sc.nextInt() = %d", instr, value);

            switch (instr) {
                case "forward":
                    horizontal += value;
                    break;
                case "up":
                    vertical -= value;
                    break;
                case "down":
                    vertical += value;
                    break;
                default:
                    break;
            }
        }

        System.out.println(vertical * horizontal);
        sc.close();
    }
}