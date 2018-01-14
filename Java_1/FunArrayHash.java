import java.io.*;
import java.util.*;
public class FunArrayHash
{
	static int max_number(int [] a,int n){
		HashMap <Integer,Integer> h1= new HashMap<Integer,Integer>();

		for (int i=0;i < n ;i++ )
		{
			if (h1.containsValue(a[i])){
				int count= h1.get(a[i])+1;
				if(count > a.length /2){
					return a[i];
				}else
					h1.put(a[i],count);
			}
			else
				h1.put(a[i],1);
		}
		return -1;
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