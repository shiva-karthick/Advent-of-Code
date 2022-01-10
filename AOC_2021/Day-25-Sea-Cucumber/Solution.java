import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// https://replit.com/@shankarAdvaita/AdventOfCode2021#Days/Days22-25/Day24.java
public class Solution {

    private static char[][] grid;
    private static final char EAST = '>';
    private static final char SOUTH = 'v';
    private static final char BLANK = '.';

    public static void main(String[] args) {
        // Create a scanner class
        System.out.println("Input > ");
        Scanner reader = new Scanner(System.in);

        List<String> input = new ArrayList<String>();
        while (reader.hasNext()) {
            input.add(reader.nextLine());
        }
        reader.close();

        grid = new char[input.size()][input.get(0).length()];
        int r = 0;
        for (String line : input) {
            grid[r] = line.toCharArray();
            r += 1;
        }

        part1();
    }

    public static void part1() {

        int steps = 0;
        boolean movedEast = true;
        boolean movedSouth = true;

        while (movedEast || movedSouth) {
            steps += 1;
            movedEast = moveEast();
            movedSouth = moveSouth();
        }
        System.out.printf("Number of steps = %d \n", steps);
    }

    private static boolean moveEast() {
        boolean moved = false;

        for (int row = 0; row < grid.length; row += 1) {
            boolean moveOG = false;

            for (int column = 0; column < grid[0].length; column += 1) {
                if (grid[row][column] == EAST) {
                    if (column <= grid[0].length - 2 && grid[row][column + 1] == BLANK) {
                        moved = true;
                        if (column == 0) {
                            moveOG = true;
                        }
                        // Swap the places
                        grid[row][column] = BLANK;
                        grid[row][column + 1] = EAST;
                        column += 1;
                    } else if (column == grid.length - 1 && grid[row][0] == BLANK && !moveOG) {
                        moved = true;
                        grid[row][column] = BLANK;
                        grid[row][0] = EAST;
                    }
                }
            }
        }
        return moved;
    }

    private static boolean moveSouth() {
        boolean moved = false;

        for (int column = 0; column < grid[0].length; column += 1) {
            boolean movedOG = false;
            for (int row = 0; row < grid.length; row += 1) {
                if (grid[row][column] == SOUTH) {
                    if (row <= grid.length - 2 && grid[row + 1][column] == BLANK) {
                        // Swap positions
                        moved = true;
                        if (row == 0) {
                            movedOG = true; // Ensure that at the end of the row, it doesn't move again,
                            // resulting in duplicate moves
                        }
                        grid[row][column] = BLANK;
                        grid[row + 1][column] = SOUTH;
                        row += 1;
                    } else if (row == grid.length - 1 && grid[0][column] == BLANK && !movedOG) {
                        moved = true;
                        grid[row][column] = BLANK;
                        grid[0][column] = SOUTH;
                    }
                }
            }
        }
        return moved;
    }
}
