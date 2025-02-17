public class q2a {
    public static void main(String[] args) {
        int n = 67;

        for (int i = 2; i <= (n / 2); i++) {
            if (n % i == 0) {
                System.out.println("Composite number.");
                return;
            }
        }
        System.out.println("Prime number.");
    }
}
