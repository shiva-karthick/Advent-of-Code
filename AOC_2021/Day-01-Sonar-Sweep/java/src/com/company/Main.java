package com.company;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();

        int prevSum = 0;
        int count = 0;

        // Store the sum of the first 3 integers into the variable prevSum
        // Add the first 3 integers to the queue
        for (int i = 0; i < 3; i++) {
            int next = sc.nextInt();
            prevSum += next;
            queue.add(next);
        }

        System.out.println(prevSum);

        // 1997 is the remaining number of lines
        for (int i=0; i < 1997; i++) {

            int next = sc.nextInt();
            int newSum = prevSum - queue.poll() + next;
            count = newSum > prevSum ? count + 1 : count; // ternary operator

            queue.add(next);
            prevSum = newSum;
        }

        System.out.println(count);
        sc.close();

    }
}
