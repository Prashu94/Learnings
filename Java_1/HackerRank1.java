import java.util.*;

public class HackerRank1
{
	static long b = 0;

	static String canConstruct(int [] a){
		
			if (b%3 == 0)
			{
				return "Yes";
			}
			else{
				return "No";
			}
	}
	public static void main (String [] args){
	
	Scanner sn =new Scanner(System.in);

	int t =sn.nextInt();

		for (int i = 0 ;i<t ;i++ )
		{
			int q = sn.nextInt();

			int [] a = new int [q];

			b = 0;
			
			for (int j = 0;j<q ;j++ )
			{
				a[j] = sn.nextInt();

				b += a[j];
			}

		String result = canConstruct(a);
		System.out.println(result);
		}
		sn.close();
	}
}