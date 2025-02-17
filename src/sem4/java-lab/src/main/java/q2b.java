public class q2b {
    public static void main(String[] args) {
        int n = 67;

        int i = 2;
        while (i <= (n / 2)) {
            if (n % i == 0) {
                System.out.println("Composite number.");
                return;
            }
            i += 1;
        }
        System.out.println("Prime number.");
    }
}
