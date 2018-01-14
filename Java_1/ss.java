/* second smallest number in array*/

import java.util.*;
import java.io.*;

public class ss{

	public static void main(String [] args){

		Scanner sc= new Scanner(System.in);

		/*variable declaration*/
		int n,smallest,ssmallest;

		System.out.println("Enter the length of the array");
		n=sc.nextInt();

		int [] a=new int[n];

		System.out.println("Enter the elements of the array:");
		for(int i=0; i < n; i++){

			a[i]=sc.nextInt();

		}

		smallest=a[0];
		ssmallest=a[0];

		for(int n1: a){
			if(n1<smallest){
				ssmallest=smallest;
				smallest=n1;
			}
			else if(n1 < ssmallest){
				ssmallest=n1;
			}
		}

		System.out.println(ssmallest);
	}
}