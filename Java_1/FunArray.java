import java.io.*;
public class FunArray
{
	static int max_number(int [] a,int n){
		
		int max = a[0];
		
		for (int i = 0;i<n ;i++ )
		{
			if(a[i+1]>=max){
				max	= a[i+1];
			}
		}
		return max;

	}
	public static void main(String [] args)throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			
			int f;
			String  []nq= br.readLine().split("\\s");
			
			int N=Integer.parseInt(nq[0]);
			
			String str = br.readLine();
			String [] s_arr=str.split("\\s");

			int [] A= new int [N+20];
			int len= s_arr.length;
			
			for (int n = 0;n<len ;n++ )
			{
				A[n]= Integer.parseInt(s_arr[n]);
			}

			f = max_number(A,len);

			System.out.println(f);

		}
	}
}