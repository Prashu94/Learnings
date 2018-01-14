import java.util.*;

public class CodeChef4
{
	public static void main(String [] args){
		
		Scanner s =new Scanner(System.in);
		int cases = s.nextLineInt();

		for (int i = 0; i < cases ;i++)
		{
			String str = s.next();
			
			ArrayList <Integer> as =new ArrayList();
			ArrayList <Integer> bs =new ArrayList();

			for (int j = 0;j < str.length() ;j++ )
			{
				if (str.charAt(j) == 'A')
				{
					as.add(j);
				}else if (str.charAt(j) == 'B')
				{
					bs.add(j);
				}
			}

			int aDots = 0;
			int bDots = 0;

			for (int j = 0 ;j < as.size()-1 ;j++ )
			{
				int controlBetween = true;

				for (int k = 0;k < as.get(j+1)-as.get(j) ;k++ )
				{
					if (str.charAt(as.get(j)+k) == 'B')
					{
						controlBetween =false;
					}
				}
				if(controlBetween){
					aDots += as.get(j+1) - as.get(j) - 1;
				}
			}

			for (int j = 0 ;j < bs.size()-1 ;j++ )
			{
				int controlBetween = true;

				for (int k = 0;k < bs.get(j+1)-bs.get(j) ;k++ )
				{
					if (str.charAt(as.get(j)+k) == 'A')
					{
						controlBetween =false;
					}
				}
				if(controlBetween){
					bDots += bs.get(j+1) - bs.get(j) - 1;
				}
			}

		}

	}
}