import java.io.*;
import java.lang.*;
public class Array_Std
{
	static double std_deviation(int [] a){
		double sum=0;
		double mean;
		double variance=0;
		
		for (int i = 0;i < a.length  ;i++ )
		{
			sum+=a[i];
		}
		mean = sum/(a.length)*1.0;
		
		for(int i = 0; i < a.length; i++){
			variance = (a[i] - mean)*(a[i] - mean);	
		}
		variance= variance / a.length;
		
		return(Math.sqrt(variance));

	}
	public static void main(String [] args) throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			
			Double std_dev;
			
			String [] nq = br.readLine().split("\\s");

			int N = Integer.parseInt(nq[0]);

			String str = br.readLine();
			String [] s_arr= str.split("\\s");

			int [] A= new int [N+20];
			int len=s_arr.length;

			for (int n = 0;n < len  ;n ++ )
			{
				A[n]=Integer.parseInt(s_arr[n]);
			}

			std_dev = std_deviation(A);
			
			System.out.println(std_dev);
		}
	}
}