import java.io.*;

public class SingleArray{

	static int findNonRepeating(int [] a,int n){
	
	int res =0;
		for(int i=0 ; i< n;i++){
			res = res ^ a[i];
		}
	return res;
	}
	public static void main(String [] args)throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			

			String [] nq =br.readLine().split("\\s");

			int N= Integer.parseInt(nq[0]);

			String str =br.readLine();

			String [] s_arr = str.split("\\s");

			int [] A= new int[N+20];

			int len= s_arr.length;
			for (int i=0;i<len ;i++ )
			{
				A [i] =Integer.parseInt(s_arr[i]);
			}

			int result=findNonRepeating(A,len);

			System.out.println(result);
		}	
	}
}