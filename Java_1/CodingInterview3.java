import java.io.*;

public class CodingInterview3{

	static void replaceSpaces(String s1, int trueLength){
		int spaceCount=0,index;
		char [] str=s1.toCharArray();		
		for (int i=0;i<trueLength ;i++ )
		{
			if (str[i]==' ')
			{
				spaceCount++;
			}
		}

		index=trueLength+spaceCount*2;
		
		if (trueLength<str.length)
		{
			str[trueLength]='\0';
		}

		for (int i=trueLength-1; i >= 0 ; i-- )
		{
			if(str[i]=' '){
				str[index-1]='%';
				str[index-2]='2';
				str[index-3]='0';
			}
			else{
				str[index-1]=str[i];
			}
			index--;
			System.out.print(str[i]);
		}


	}
	public static void main(String [] args) throws Exception{
		try(BufferedReader br=new BufferedReader(new InputStreamReader(System.in))){
			
			

			String [] nq=br.readLine().split("\\s");
			
			String s1=nq[0];
			int trueLength=Integer.parseInt(nq[1]);
			
			replaceSpaces(s1,trueLength);
		}
	}
}