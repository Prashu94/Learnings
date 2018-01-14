import java.io.*

public class UniqueChar
{
	static boolean isUniqueString(String s){
		boolean [] char_set=new new Boolean[128];
		
		if(s.length()>128)
			return false;

		for (int i=0; i<s.length() ;i++ )
		{
			int val=s.charAt(i);
			if(char_set[val]){
				return false;
			}
			char_set[val]=true;
		}
		return true;

	}
	public static void main(String [] args) throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in)){
			
			String str=br.readLine();
			
			if (isUniqueString(str)==TRUE)
			{
				System.out.println("UNIQUE");
			}
			else{
				System.out.println("NOT UNIQUE");
			} 

			
		}
	}
}