import java.io.*;

public class GeeksProgram2{
	static void hasArrayTwoCandidates(int [] arr,int len,int sum){
		sortAlgo(A,len);
	}
	
	public static void main (String [] args)throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in)){
			
			String nq=br.readLine().split("\\s");
			
			int N=Integer.parseInt(nq[0]);
			int Q=Integer.parseInt(nq[1]);
					
			
			String str=br.readLine();
			String [] s_arr=str.split("\\s");
			
			int [] A=new int[N+25];
			int len =s_arr.length();
			
			int n=0;
			for(int i=0; i<len; i++){
				A[n++]=Integer.parseInt(s_arr[i]);
			}
			
			if (hasArrayTwoCandidates(A,len,n)){
				System.out.println("Array has two elements with sum :"+ Q);
			}
			else{
				System.out.println("Array does not have two elements with sum :"+ Q);
			}
			
		}
		
		
	}
}