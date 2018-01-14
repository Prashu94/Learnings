import java.lang.*;
import java.util.*;
class CodeChef2
{
	public static void main(String args[])
	{
		Scanner s=new Scanner (System.in);
		int t;
		t=s.nextInt();
		for(int i=0;i<t;i++)
		{
			int n,q;
			n=s.nextInt();
			q=s.nextInt();
			int d[]=new int[n];
			for(int j=0;j<n;j++)
			d[j]=s.nextInt();
			int xi[]=new int[q];
			for(int j=0;j<q;j++)
			xi[j]=s.nextInt();  // values os x
			for(int k=0;k<q;k++)
			{
				for(int j=0;j<n;j++)
				{
					xi[k]=xi[k]/d[j];
					if(xi[k]==0)
					break;
				}
			}
			for(int k=0;k<q;k++)
				System.out.println(xi[k]);
 
		}
	}
}