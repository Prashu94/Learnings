package com.basics.java;
import java.io.*;
import java.util.Arrays;
public class MinimumPlatform {

	static int findPlatform(int a [], int d [], int N) {
		
		Arrays.sort(a);
		Arrays.sort(d);
		
		int platNeeded=1;
		int result =1;
		
		int i =1, j=0;
		
		while(i<N && j<N) {
			
			if (a[i] < d[j]) {
				platNeeded++;
				i++;
				if (platNeeded>result) {
					result = platNeeded;
				}
			}
			else {
				platNeeded--;
				j++;
			}
			
		}
		return result;
	}
	public static void main(String[] args)throws Exception {
		// TODO Auto-generated method stub
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			 String [] nq = br.readLine().split("\\s");
			 
			 int N = Integer.parseInt(nq[0]);
			 
			 String [] line1 = br.readLine().split("\\s");
			 int i = 0;
			 String [] line2 = br.readLine().split("\\s");
			 int j = 0 ;
			 int [] arr = new int [N+1];
			 int [] dep = new int [N+1];
			 for (int n = 0; n < N; i++ ) {
				 arr[i++] = Integer.parseInt(line1[n]);
				 dep[j++] = Integer.parseInt(line2[i]);
			 }
			 System.out.println("The result is:"+findPlatform(arr,dep,N));
			 
			 
		}
		
	}

}
