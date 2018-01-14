import java.util.Scanner;
import java.math.BigInteger;

class CodeChef3
{
	public static void main(String [] args){
		
		Scanner s = new Scanner (System.in);
		/*Input Section*/
		long N = s.nextLong();
		long K = s.nextLong();

		if (N<=K)
		{
			System.out.println("1"); return;
		}

		long [] arr = new long [(int)N + 1];

		int i;

		for (i = 1 ;i <= N ;i++ )
		{
			if (i <= K) arr[i] = 1;
			else if ( i == K+1) 
				arr[i] = K;
			else
				arr[i] = (2*arr[i-1] - arr[i-1-(int)K])%(1000000007);
		}

		System.out.println(arr[(int)N]);


	}
}