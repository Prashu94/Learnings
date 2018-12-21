package com.basics.java;
import java.io.*;

public class CountZot {

	static void sort012(int [] arr, int arr_size) {
		int lo = 0 ;
		int hi = arr_size-1;
		int mid = 0;
		int temp = 0;
		
		while (mid <= hi) {
			switch (arr[mid]) {
			case 0:
				temp = arr[lo];
				arr[lo] = arr[mid];
				arr[mid] = temp;
				lo++;
				mid++;
				break;
			case 1:
				mid++;
				break;
			case 2:
				temp = arr[mid];
				arr[mid] = arr[hi];
				arr[hi] = temp;
				hi--;
				break;
			}
		}
	
	}
	static void printArray(int arr[], int arr_size) 
    { 
        int i; 
        for (i = 0; i < arr_size; i++) 
            System.out.print(arr[i]+" "); 
        System.out.println(""); 
    } 
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br= new BufferedReader(new InputStreamReader(System.in))){

			String [] nq = br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			
			
			String [] line = br.readLine().split("\\s");
			 
			int [] A = new int[N];
			int i = 0;
			
			for (int n = 0; n < N; n++) {
				A[i++] = Integer.parseInt(line[n]);
			}
			
			sort012(A,N);
			printArray(A, N);
		}
	}

}
