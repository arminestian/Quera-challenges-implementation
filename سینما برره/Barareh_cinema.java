import java.util.Scanner;

public class CinemaBarara {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        long a = input.nextLong();
        long b = input.nextLong();
        System.out.println(Math.min(a,b));
    }
}