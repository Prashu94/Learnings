import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;

public class Frequency {

    private Scanner scan = new Scanner(System.in);

    public static void main(String args[]) {
        userInput();
    }

    public static void userInput() {
        Scanner scan = new Scanner(System.in);
        System.out
                .println("Please tell me the amount of numbers you will be entering (Up to 50): ");
        int[] arr = new int[scan.nextInt()];

        for (int i = 0; i < arr.length; i++) {
            scan = new Scanner(System.in);
            System.out.println("Please enter a number: ");
            while (scan.hasNextInt()) {
                int x = scan.nextInt();
                arr[i] = x;
                break;
            }
        }

        System.out.println(" ");
        System.out.println("Results of Data Entry");
        System.out.println("_____________________");

        Map<Integer, Integer> counts = countOccurences (arr);

        Iterator itr = counts.entrySet().iterator();
        while (itr.hasNext()) {
            Map.Entry pairs = (Map.Entry)itr.next();
            System.out.println(pairs.getKey() + " occurs " + pairs.getValue());
        }
    }

    public static Map<Integer, Integer> countOccurences (int[] arr) {
        int len = arr.length;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i < len; i++) {
            int key = arr[i];
            if (map.containsKey(key)) {
                int value = map.get(key);
                map.put(key, value + 1);
            } else {
                map.put(key, 1);
            }
        }

        return map;
    }
}