package com.basics.java;
import java.io.*;
public class MissingNumber {

	public MissingNumber() {
		// TODO Auto-generated constructor stub
	}
	
	static int getMissingNo(int [] a, int n) {
		int x1 = a[0];
		int x2 = 1;
		/*Xor for all elements in the array*/
		for (int i = 1 ;i < n ; i++) {
			x1 = x1 ^ a[i];
		}
		/*Xor for all elements from 2 to n+1*/
		for (int i =2 ;i <= n+1; i++) {
			x2 = x2 ^ i;
		}
				
		return (x1 ^ x2);
	}

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			
			String [] nq=br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			int q = Integer.parseInt(nq[1]);
			String []  arr = br.readLine().split("\\s");
			
			int [] A = new int [N];
			int i = 0;
			
			for (int n = 0; n < N; n++) {
				A[i++] = Integer.parseInt(arr[n]);
			}
			
			int missing = getMissingNo(A,q);
			System.out.println(missing);
			}
}
}
