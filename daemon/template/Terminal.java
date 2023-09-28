// Will be enhanced with more functionality later.

import java.util.Scanner;

public class Terminal {

    private static Scanner jin = new Scanner(System.in);

    public static void print(Object obj) {
        System.out.print(obj);
    }
    public static void println(Object obj) {
        print(obj + "\n");
    }
    public static void debug(String line) {
        System.out.println("Executing: " + line);
        jin.next();
    }
}
