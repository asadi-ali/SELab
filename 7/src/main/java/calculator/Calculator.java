package calculator;

public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int div(int a, int b) {
        return a / b;
    }

    public int pow(int a, int b) {
        int res = 1;
        for (int i = 0; i < b; i++)
            res *= a;
        return res;
    }
}
