package com.basics.java;
import java.io.*;
public class MinimumCoins {
	static int minimumCoins(int [] coins, int total) {
		int [] r = new int[total+1];
		int [] p = new int[total+1];
		
		r[0] = 0 ;
		
		for (int i = 0; i< total+1; i++) {
			r[i] = Integer.MAX_VALUE-1;
		}
		
		for (int i = 0; i< total+1; i++) {
			p[i] = -1;
		}
		
		for (int i = 0; i< coins.length; i++) {
			for (int j =1, h=0; j< total+1;j++) {
				if (j>= coins[i]) {
					int notTaken = r[j];
					int Taken = r[j-coins[i]]+1;
					
					if (Taken <= notTaken) {
						r[j] = Taken;
						p[j] = i;
					}
				}
			}
		}
		return r[total];
	}
	public static void main(String[] args)throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			String [] nq = br.readLine().split("\\s");
			
			int N = Integer.parseInt(nq[0]);
			int q = Integer.parseInt(nq[1]);
			
			String [] line = br.readLine().split("\\s");
			
			int [] A = new int[N];
			int i = 0;
			
			for (int n = 0; n< N; n++) {
				A[i++] = Integer.parseInt(line[n]);
			}
			System.out.println(minimumCoins(A,q));
		}
		
	}

}
