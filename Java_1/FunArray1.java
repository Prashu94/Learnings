import java.io.*;
public class FunArray1
{
	static int max_number(int [] a,int n){
		int cand = findCandidate(a,n);
		
		if(isMajority(a,n,cand))
			return cand;
		else
			return -1;
	}
	static int findCandidate(int [] a, int size){
		int majorityInd=0, count=1;

		for (int i = 1 ;i < size;i++ )
		{
			if (a[majorityInd]==a[i])
			{
				count++;
			}
			else{
				count--;
			}
			if (count==0)
			{
				majorityInd = i;
				count=1;
			}
		}

		return(a[majorityInd]);
	}
	static boolean isMajority(int [] a,int size,int cand){
		int count=0;
		for (int i = 0;i<size ;i++ )
		{
			if(a[i]==cand){
				count++;
			}
		}
		if(count>=size/2)
			return true;
		else
			return false;
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