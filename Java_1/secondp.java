/*Bubble Sort program*/
import java.util.*;
import java.io.*;
class BubbleSort{
	public void bsort(int [] a){
		int temp=0;
		for (int i=0; i<a.length;i++){
			for(int j=1; j<a.length-1;j++){
				if(a[j-1]>a[j]){
					temp=a[j-1];
					a[j-1]=a[j];
					a[j]=temp;
				}
			}
		}
	}
}

public class secondp extends BubbleSort{
	
	public static void main(String [] args){
		int n;
	
		System.out.println("Enter the length of the array");
		Scanner sc=new Scanner(System.in);
		n=sc.nextInt();
		
		int [] a=new int[n+1];

		System.out.println("Enter the elements of the array");

		for(int i=0; i<n;i++){
			a[i]=sc.nextInt();
		}

		BubbleSort bs=new BubbleSort();
		bs.bsort(a);

		System.out.println("The sorted Array is:");
		for(int i=0; i <n; i++){
		System.out.println(a[i]);
		}
	}

}