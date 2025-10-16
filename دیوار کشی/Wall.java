import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Long wall_len = sc.nextLong();
        Long brick_len = sc.nextLong();
        System.out.println(wall_len % brick_len);
    }
}