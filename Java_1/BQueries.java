import java.io.BufferedReader;
import java.io.InputStreamReader;

class BQueries
{
    public static void main(String args[]) throws Exception
    {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in)))
        {
            StringBuilder output = new StringBuilder();

            String[] nq = br.readLine().split("\\s");
            int N = Integer.parseInt(nq[0]);
            int Q = Integer.parseInt(nq[1]);

            String arr = br.readLine();
            int[] A = new int[N];
            int len = arr.length();
            int i=0;
            for (int n = 0; n < len; n += 2)
            {
                A[i++] = arr.charAt(n) == '0' ? 0 : 1;
            }

            for (int q = 0; q < Q; q++)
            {
                String[] qry = br.readLine().split("\\s");
                int t = Integer.parseInt(qry[0]);
                if (t == 0)
                {
                    int R = Integer.parseInt(qry[2]);
                    if (A[R - 1] == 0)
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
                    A[x - 1] = 1 - A[x - 1];
                }
            }

            System.out.println(output);
        }
    }
}