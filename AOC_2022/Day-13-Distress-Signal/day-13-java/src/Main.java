import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Main {
    private static class Packet implements Comparable<Packet> {
        private int value;
        private String packetName;
        private boolean isInteger = true;
        private ArrayList<Packet> subPacket;

        // construct the packets recursively
        public Packet(String inputs) {
            subPacket = new ArrayList<Packet>();
            this.packetName = inputs;
            // empty list
            if (inputs.equals("[]")) {
                this.value = Integer.MIN_VALUE;
            }
            if (inputs.charAt(0) != '[') {
                // it is a number
                this.value = Integer.parseInt(inputs);
            } else {
                // it is a list, remove the front and last brackets
                inputs = inputs.substring(1, inputs.length()-1);
                int level = 0;
                String subInputs = "";
                for (var c : inputs.toCharArray()) {
                    if (c != ',' || level > 0) {
                        // it is a number or within a list
                        if (c == '[') { level += 1; }
                        else if (c == ']') { level -= 1; }
                        subInputs += c;
                    } else {
                        // it is a comma and at base level
                        subPacket.add(new Packet(subInputs));
                        subInputs = "";
                    }
                }
                if (!subInputs.equals("")) {
                    subPacket.add(new Packet(subInputs));
                }
                this.isInteger = false;
            }
        }

        public int getValue() { return this.value; }
        public int getSubPacketSize() { return subPacket.size(); }
        public boolean getIsInteger() { return this.isInteger; }
        public String getName() { return packetName; }

        public Packet getSubPacket(int i) {
            if (i >= subPacket.size() || i < 0) {
                System.out.println("index is invalid!");
                return null;
            }
            return subPacket.get(i);
        }

        public int compareTo(Packet next) {
            // if both packets are integers
            if (isInteger && next.getIsInteger()) {
                return value - next.getValue();
            }
            // if both packets are lists
            if (!isInteger && !next.getIsInteger()) {
                int nextSize = next.getSubPacketSize();
                for (int i = 0; i < Math.min(subPacket.size(), nextSize); i++) {
                    int value = subPacket.get(i).compareTo(next.getSubPacket(i));
                    if (value != 0) {
                        return value;
                    }
                }
                return subPacket.size() - nextSize;
            }
            // either packets is an integer, convert said packets to a list and compare again
            Packet sub1 = isInteger ? new Packet("["+value+"]") : this;
            Packet sub2 = next.getIsInteger() ? new Packet("["+next.getValue()+"]") : next;
            return sub1.compareTo(sub2);
        }
    }

    private static class Solution {
        private int ans1;
        private int ans2;
        private ArrayList<Packet> signal;

        public Solution() {
            Scanner sc = new Scanner(System.in);
            this.ans1 = 0;
            this.ans2 = 1;
            this.signal = new ArrayList<Packet>();
            int idx = 1;
            while (sc.hasNextLine()) {
                String line1 = sc.nextLine();
                String line2 = sc.nextLine();
                Packet obj1 = new Packet(line1);
                Packet obj2 = new Packet(line2);
                signal.add(obj1); signal.add(obj2);
                ans1 += (obj1.compareTo(obj2) < 0) ? idx : 0; idx++;
                if (sc.hasNextLine()) sc.nextLine();
            }
            sc.close();
        }

        public void q1Solution() {
            System.out.println(ans1);
        }

        public void q2Solution() {
            signal.add(new Packet("[[2]]"));
            signal.add(new Packet("[[6]]"));
            Collections.sort(signal);
            for (int i = 0; i < signal.size(); i++) {
                if (signal.get(i).getName().equals("[[2]]") ||
                        signal.get(i).getName().equals("[[6]]")) {
                    ans2 *= (i + 1);
                }
            }
            System.out.println(ans2);
        }
    }

    public static void main(String[] args) {
        Solution object = new Solution();
        object.q1Solution();
        object.q2Solution();
    }
}