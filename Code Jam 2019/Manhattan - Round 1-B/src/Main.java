import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cases = input.nextInt();

        for (int a = 1; a <= cases; a++) {
            int people = input.nextInt();
            int length = input.nextInt();

            int[] xa = new int[length];
            int[] yarray = new int[length];

            for (int b = 1; b <= people; b++) {

                int xd = input.nextInt();
                int yd = input.nextInt();
                String direction = input.next();

                if (direction.equals("N")) {
                    for (int c = (yd + 1); c < length; c++) {
                        yarray[c]+=1;
                    }
                }
                else if (direction.equals("S")) {
                    for (int v = (yd - 1); v >= 0; v--) {
                        yarray[v]+=1;
                    }
                }
                else if (direction.equals("E")) {
                    for (int o = (xd + 1); o < length; o++) {
                        xa[o]+=1;
                    }
                }
                else if (direction.equals("W")) {
                    for (int m = (xd - 1); m >= 0; m--) {
                        xa[m]+=1;
                    }
                }
            }
            int max = xa[0];
            int xcord = 0;
            for(int i = 0; i < length; i++)
            {
                if(max < xa[i])
                {
                    max = xa[i];
                    xcord=i;
                }
            }

            int maxy = yarray[0];
            int ycor=0;

            for(int i = 0; i < length; i++)
            {
                if(maxy < yarray[i]) {
                    maxy = yarray[i];
                    ycor=i;
                }
            }

            System.out.println("Case #" + a + ": " + xcord + " "+ ycor);

        }

    }
}
