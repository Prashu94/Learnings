/* fibonacci sequence*/
import java.util.*;
import java.io.*;

class fibonacci{

	public static void main(String [] args){
		int n,n1,n2,n3;
		Scanner sc =new Scanner (System.in);

		System.out.println("Enter the length of teh fibonacci sequence");

		n=sc.nextInt();
		n1=0;
		n2=1;
		System.out.print(n1+" "+n2);

		for(int i=2; i<=n;i++){
			n3=n1+n2;
			System.out.print(" " +n3);
			n1=n2;
			n2=n3;
		}
	}

}