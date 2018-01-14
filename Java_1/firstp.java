import java.io.*;
import java.util.*;

class firstp{
	public static void main(String [] args){
		int n,temp,a,c=0;

		Scanner sc=new Scanner(System.in);
		System.out.println("Enter a number");

		n=sc.nextInt();
		temp=n;

		while(n>0){
			a=n%10;
			n=n/10;
			c+=(a*a*a);
		}
		if(temp==c)
			System.out.println("YES");
		else
			System.out.println("NO");


	}

}