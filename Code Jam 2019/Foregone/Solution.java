	import java.io.BufferedReader;
	import java.io.InputStreamReader;
	import java.util.Scanner;
	import java.math.BigDecimal; 
	
	public class Solution {
		public static void main(String[] args) {
			Scanner input = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
	        int cases = input.nextInt(); 
	        BigDecimal A;
	        BigDecimal B;
	        BigDecimal number;
	        BigDecimal sub  = BigDecimal.valueOf(0);
	        
	       
	        for (int a = 1; a <= cases; a++) {
	        	number = input.nextBigDecimal();
	        	String snumber = number.toString();
	        	for (int k = 0; k < snumber.length(); k++) {
	        		if (snumber.charAt(k) == '4') {
	        			 int p = snumber.length() - k - 1;
	        			 sub = sub.add(new BigDecimal(Math.pow(10,p)));	
	        			 }}
	        	A = sub;
	        	B = number.subtract(sub);
	        	System.out.println("Case #" + a + " : " + A + " " + B);
	        	sub  = BigDecimal.valueOf(0);
	        }
	        
		}
	}