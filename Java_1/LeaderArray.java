package com.basics.java;
import java.io.*;
public class LeaderArray {

	static void printLeader(int [] arr, int n) {
		for (int i = 0; i < n; i++) {
			int j;
			for (j = i+1 ; j<n ;j++) {
				if(arr[i] <arr[j]) {
					break;
				}
			}
			if (j == n) {
				System.out.println(arr[i]+ " ");
			}
		}
	}
	public static void main(String[] args)throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			String [] nq = br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			
			String [] line = br.readLine().split("\\s");
			
			int [] A = new int[N];
			int i = 0 ;
			
			for(int n = 0; n<N; n++){
				A[i++] = Integer.parseInt(line[n]);
			}
			
			
		}
	}

}
