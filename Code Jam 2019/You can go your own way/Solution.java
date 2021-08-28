import java.util.*;

public class Solution{


    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int cases = input.nextInt();
        int Tcases = cases;
        for (int a = 1; a <= cases; a++) {
            int length = input.nextInt();
            input.nextLine();
            String Lydia = input.nextLine();
            String myMove = change(Lydia);
            System.out.println("Case #" + a + ": " + myMove);
        }

    }

    private static String change(String move) {
        String changed = move.replace("E", "X");
        changed = changed.replace("S", "E");
        return changed.replace("X", "S");
    }
}