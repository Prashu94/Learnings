package com.basics.java;
import java.io.*;
public class Equilibrium {

	int equilibrium(int [] arr,int arr_size) {
		
		int leftsum;
		int rightsum;
		int i, j=0;
		for (i = 0; i < arr_size; ++i) { 
			  
            /* get left sum */
            leftsum = 0;   
            for (j = 0; j < i; j++) 
                leftsum += arr[j]; 
  
            /* get right sum */
            rightsum = 0; 
            for (j = i + 1; j < arr_size; j++) 
                rightsum += arr[j]; 
  
            /* if leftsum and rightsum are same,  
               then we are done */
            if (leftsum == rightsum) 
                return i; 
        } 
  
        /* return -1 if no equilibrium index is found */
        return -1; 
		}
	public static void main(String[] args) throws Exception {
	
		// TODO Auto-generated method stub
		Equilibrium eq = new Equilibrium();
		try(BufferedReader br = new BufferedReader(new InputStreamReader(System.in))){
			
			String [] nq = br.readLine().split("\\s");
			int N = Integer.parseInt(nq[0]);
			
			String [] line = br.readLine().split("\\s");
			
			int [] A = new int[N];
			int i =0;
			
			for (int n = 0; n<N; n++ ) {
				A[i++] = Integer.parseInt(line[n]);
			}
			
			System.out.println(eq.equilibrium(A,N));
		}
	}
}