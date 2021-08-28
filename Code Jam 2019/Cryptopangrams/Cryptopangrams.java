import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public static void main(String[] args) {
        Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int cases = input.nextInt();
        for (int b = 1; b <= cases; ++b) {
            int maxp = input.nextInt();
            int length = input.nextInt();
            if (maxp <= 10000) {
                List<Integer> listvalues = new ArrayList<>();
                for (int c = 0; c < length; c++) {
                    listvalues.add(input.nextInt());
                }
                System.out.println("Case #" + b + ": " + smallvalues(listvalues));
            } else {
                List<BigInteger> listvalues = new ArrayList<>();
                for (int c = 0; c < length; c++) {
                    listvalues.add( input.nextBigInteger());
                }
                System.out.println("Case #" + b + ": " + bigvalues(listvalues));
            }
        }
    }

    private static String bigvalues(List<BigInteger> listvalues) {
        int gcrypt = 0;
        while (listvalues.get(gcrypt).equals(listvalues.get(gcrypt + 1))) {
            gcrypt++;
        }
        BigInteger FirstGCD = listvalues.get(gcrypt).gcd(listvalues.get(gcrypt + 1));

        List<BigInteger> key = new ArrayList<>(Arrays.asList(
                listvalues.get(gcrypt).divide(FirstGCD),
                FirstGCD,
                listvalues.get(gcrypt + 1).divide(FirstGCD)
        ));

        for (int b = gcrypt - 1; b >= 0; b--) key.add(0, key.get(1));

        for (int b = gcrypt + 2; b < listvalues.size(); b++) {
            BigInteger next = listvalues.get(b).divide(key.get(key.size() - 1));
            key.add(next);
        }

        List<BigInteger> sortedEncodeVal =
                key.stream()
                           .distinct()
                           .sorted()
                           .collect(Collectors.toList());

        Map<BigInteger, Character> decodeMap = new HashMap<>();
        for (int b = 0; b < sortedEncodeVal.size(); b++)
            decodeMap.put(sortedEncodeVal.get(b), (char) ('A' + b));
        StringBuilder sbuffer = new StringBuilder();
        for (BigInteger encodedVal : key) sbuffer.append(decodeMap.get(encodedVal));
        return sbuffer.toString();
    }

    private static String smallvalues(List<Integer> listvalues) {
        int gcrypt = 0;
        while (listvalues.get(gcrypt).equals(listvalues.get(gcrypt + 1))) {
            gcrypt++;
        }
        int FirstGCD = GCD(listvalues.get(gcrypt), listvalues.get(gcrypt + 1));

        List<Integer> key = new ArrayList<>(Arrays.asList(
                listvalues.get(gcrypt) / FirstGCD,
                FirstGCD,
                listvalues.get(gcrypt + 1) / FirstGCD
        ));

        for (int b = gcrypt - 1; b >= 0; b--) key.add(0, key.get(1));

        for (int b = gcrypt + 2; b < listvalues.size(); b++) {
            int next = listvalues.get(b) / key.get(key.size() - 1);
            key.add(next);
        }

        List<Integer> sortedEncodeVal =
                key.stream()
                           .distinct()
                           .sorted()
                           .collect(Collectors.toList());

        Map<Integer, Character> decodeMap = new HashMap<>();
        for (int b = 0; b < sortedEncodeVal.size(); b++)
            decodeMap.put(sortedEncodeVal.get(b), (char) ('A' + b));
        StringBuilder sbuffer = new StringBuilder();
        for (Integer encodedVal : key) sbuffer.append(decodeMap.get(encodedVal));
        return sbuffer.toString();
    }

    private static int GCD(int a, int b) {
        if (a == 0 && b == 0) return 0;
        if (b == 0) return a;
        return GCD(b, a % b);
    }
}
