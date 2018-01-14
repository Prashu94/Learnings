/* factorial program */
import java.util.*;
import java.io.*;

class Factorial{

	public long fact(long n){
		long fact=1;
		if (n==0){
			return 1;
		}
		else{
			for (long i=1 ;i<=n; i++){
				fact*=i;
			}
			return fact;
		}
	}
}

class thridp extends Factorial{
	public static void main(String [] args){
		long n;
		System.out.println("Enter the number:");

		Scanner sc=new Scanner(System.in);
		n= sc.nextLong();

		Factorial f=new Factorial();

		System.out.println("Thefactorial of the number is:"+ f.fact(n));
	}
}