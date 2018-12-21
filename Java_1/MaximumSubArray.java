package com.basics.java;

import java.io.*;
public class MaximumSubArray {
	
	static void printSubMax(int a [],int n, int k) {
		  int j, max;
		  
		  for (int i = 0; i<=n-k; i++) {
			  max = a[i];
			  
			  for (j = 1; j<k ;j++) {
				  if (a[i+j]>max) {
					  max = a[i+j];
				  }
			  }
			  System.out.println(max+" ");
		  }
	}

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			String [] nq = br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			int K = Integer.parseInt(nq[1]);
			String [] line = br.readLine().split("\\s");
			
			int [] A = new int[N+1];
			int i = 0;
			
			for (int n = 0; n < N; n++) {
				A[i++] = Integer.parseInt(line[n]);
			}
		}
	}

}
