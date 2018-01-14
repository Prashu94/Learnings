/*palindrome number*/
import java.io.*;
import java.util.*;

public class palindrome{
	public static void main(String [] args){

		Scanner sc= new Scanner(System.in);
		/*variable declaration*/
		int n,temp,r,sum=0;

		System.out.println("Enter the number");
		n=sc.nextInt();
		temp=n;

		while(n>0){
			r=n%10;
			sum=(sum*10)+r;
			n=n/10;
		}
		if (sum==temp){
			System.out.println("YES");
		}
		else{
			System.out.println("NO");
		}
	}
}