import java.io.*;
import java.util.*;

public class BuggyCal{
	
	static long code(Scanner in){
		long a = in.nextLong();
		long b = in.nextLong();
		
		long ans = 0;
		int m = 1;

		while (a > 0 || b > 0)
		{
			ans = ans * 10 + (a % 10 + b % 10) % 10;

			if ((ans == 0)
			{
				m * = 10;
			}
			 a/=10;
			 b/=10;
		}
		long na = 0;
		int n = 1;
		while (ans > 0)
		{
			na = na * 10 + ans % 10;
			ans/=10;
		}

		return (ans * m);

	}
	public static void main(String [] args) {
			Scanner in = new Scanner(System.in);	
			int t = in.nextInt();
			
			long [] ans = new long [t];

			for (int i = 0;i < t  ;i++ )
			{
				ans[i] = code(in);
			}
			for (int i = 0 ;i < t ;i++ )
			{
				System.out.println(ans[i]);
			}

		}
	}
}