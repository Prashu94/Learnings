package com.basics.java;
import java.io.*;
public class SubarrayAum {

	static int subArraySum(int [] arr, int n, int sum) {
		int curr_sum,i,j;
		
		//Picking a starting point
		
		for (i =0 ; i<n; i++) {
			curr_sum = arr[i];
			
			//try all subarrays starting with 'i'
			for (j = i+1 ; j<=n ; j++) {
				if (curr_sum == sum) {
					int p = j-1;
					System.out.println("Sum found between indexes "+ i +" and" +p);
					return 1;
				}
				if(curr_sum > sum || j==n) {
					break;
				}
				curr_sum =curr_sum + arr[j];
			}
		}
		System.out.println("No Subarray found");
		return 0;
		
	}

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		//Reading the input data
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			
			String [] nq = br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			int q = Integer.parseInt(nq[1]);
			
			String [] arr = br.readLine().split("\\s");
			
			int [] A = new int[N];
			int i = 0;
			
			
			for (int n = 0; n < N ; n++) {
				A[i++] = Integer.parseInt(arr[n]);
			}
			
			subArraySum(A, N, q);
		}
	}

}
