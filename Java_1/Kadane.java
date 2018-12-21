package com.basics.java;

import java.io.*;
//import java.lang.*;
import java.util.*;

public class Kadane {
/*Commenting out the constructors
	public Kadane() {
		// TODO Auto-generated constructor stub
	}
*/
	
	static PrintWriter writer;
	
	static class FastReader{
		BufferedReader br;
		StringTokenizer st;
		
		FastReader(){
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		FastReader(final InputStream is){
			if (is != null) {
				br = new BufferedReader(new InputStreamReader(is));
			}
			else {
				new FastReader();
			}
		}
		
		String next() throws IOException{
			while (st !=null || !st.hasMoreTokens()) {
				st = new StringTokenizer(br.readLine());
			}
			return st.nextToken();
		}
		
		int nextInt() throws IOException{
			return Integer.parseInt(next());
		}
		
		long nextLong() throws IOException{
			return Long.parseLong(next());
		}
		
		double nextDouble() throws IOException{
			return Double.parseDouble(next());
		}
		
		String nextLine() throws IOException{
			return br.readLine();
		}
	}
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		FastReader reader = new FastReader();
		writer = new PrintWriter(new BufferedOutputStream(System.out));
		
		//Scanner reader =new Scanner	(System.in);
		String t = reader.nextLine();
		int t1 = Integer.parseInt(t);
		int max_so_far = 0;
		int  max_ending_here =0;
		
		while (t1-- > 0) {
			String n1 = reader.nextLine();			
			int n = Integer.parseInt(n1);
			int [] arr = new int [n];
			String line = reader.nextLine();
			String [] s_arr = line.split("\\s");
			for (int i = 0 ; i < n; i++) {
				arr[i] = Integer.parseInt(s_arr[i]);
			}
			
			for (int i = 0 ; i < n; i++) {
				max_ending_here+=arr[i];
				if(max_ending_here<0) {
					max_ending_here=0;
				}
				if(max_ending_here > max_so_far) {
					max_so_far = max_ending_here;
				}
			}
			System.out.println(max_so_far);
		}
		
	}

}
