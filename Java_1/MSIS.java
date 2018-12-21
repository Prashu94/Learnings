package com.basics.java;
import java.io.*;
public class MSIS {

	static int maxSumIs(int [] arr,int n) {
		int i,j,max=0;
		int [] msis = new int [n];
		
		for (i = 0;i<n; i++) {
			msis[i]=arr[i];
		}
		
		/*Compute the maximum sum values*/
		for (i=1; i<n; i++) {
			for (j = 0 ;j<i; j++) {
				if(arr[i] > arr[j] && msis[i]< msis[j]+arr[i]) {
					msis[i] = msis[j]+arr[i];
				}
			}
		}
		
		for (i=0; i < n;i++) {
			if (max < msis[i]) {
				max =msis[i];
			}
		}
		
		return max;
	}
	public static void main(String[] args)throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br= new BufferedReader(new InputStreamReader(System.in))){
			
			String [] nq = br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			
			String [] line = br.readLine().split("\\s");
			
			int [] A = new int[N];
			int i = 0;
			for (int n =0 ;n < N; n++) {
				A[i++]= Integer.parseInt(line[n]);
			}
			
			System.out.println(maxSumIs(A,N));
			
		}
	}

}
