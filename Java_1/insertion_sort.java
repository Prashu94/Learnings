/* insertion sort program*/

import java.io.*;
import java.util.*;

class InsertionSort{
	public void isort(int a[]){
		int key;
		int i;
		for(int j=1; j < a.length; j++){
			key=a[j];
			i=j-1;
			while (i>-1 && a[i]>key){
				a[i+1]=a[i];
				i--;
			}
			a[i+1]=key;
		}
	}
}

public class insertion_sort extends InsertionSort{
	public static void main(String [] args){
		InsertionSort is= new InsertionSort();
		/*variable declaration*/
		int n;

		Scanner sc= new Scanner(System.in);
		System.out.println("Enter teh lebgth of the array:");

		n=sc.nextInt();
		int [] a=new int[n];
		System.out.println("Enter the array elements:");
		for (int i=0 ;i < n; i++){

			a[i]=sc.nextInt();
		}

		is.isort(a);

		System.out.println("The sorted array is:");

		for (int i=0; i<n; i++){

			System.out.println(a[i]);
		}

	}
}