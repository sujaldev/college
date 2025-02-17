public class q3 {
    public static void main(String[] args) {
        int x = 1;
        int y = 2;
        System.out.printf("x = %s; y = %s;\n", x, y);

        // Arithmetic Operators
        System.out.println("x + y = " + (x + y));
        System.out.println("x - y = " + (x - y));
        System.out.println("x * y = " + (x * y));
        System.out.println("x / y = " + ((float) x / y));
        System.out.println("x % y = " + (x % y));

        // Relational Operators
        System.out.println("x == y is " + (x == y));
        System.out.println("x != y is " + (x != y));
        System.out.println("x > y is " + (x > y));
        System.out.println("x < y is " + (x < y));
        System.out.println("x <= y is " + (x <= y));
        System.out.println("x >= y is " + (x >= y));

        // Unary Operators
        System.out.println("++x = " + (++x));
        System.out.println("--x = " + (--x));
    }
}
