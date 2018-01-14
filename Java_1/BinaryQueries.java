import java.io.*;

public class BinaryQueries{

public static void main(String [] args) throws Exception
{	
	
	try(BufferedReader bf1=new BufferedReader(new InputStreamReader(System.in))){
	/*first line input N&Q*/	
		
		StringBuilder output= new StringBuilder();

		String [] nq=bf1.readLine().split("\\s");
		int N1=Integer.parseInt(nq[0]);
		int Q1=Integer.parseInt(nq[1]);

	/*read the array elements from the user*/
		String arr=bf1.readLine();
		int [] A1=new int [N1];
		int len=arr.length();
		int i=0;

		for (int n=0; n<len; n++){
			//Note: trick to convert char to integer without using function
			A1[i++]= arr.charAt(n)=='0' ? 0 : 1;
		}
	/*now read the queries starting with 0or1*/
		
		for (int q = 0; q < Q1; q++)
            {
                String[] qry = bf1.readLine().split("\\s");
                int t = Integer.parseInt(qry[0]);

                if (t == 0)
                {
                    int R = Integer.parseInt(qry[2]);
                    if (A1[R - 1] == 0)
                    {
                        output.append("EVEN");
                    }
                    else
                    {
                        output.append("ODD");
                    }
                    output.append('\n');
                }
                else
                {
                    int x = Integer.parseInt(qry[1]);
                    A1[x - 1] = 1 - A1[x - 1];
                }

            }
        System.out.println(output);
	}
}
}