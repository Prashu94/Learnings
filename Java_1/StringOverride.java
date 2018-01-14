import java.io.*;

class Bob
{
	int shoeSize;
	String nickName;

	Bob(String nickName, int shoeSize){
		this.nickName = nickName;
		this.shoeSize = shoeSize;
	}
	
	public String toString(){
		
		return("I am Prashant but you call me "+ nickName +". My shoesize is" +shoeSize); 
	}
		
}

public class StringOverride
{
	public static void main(String [] args){
	
		Bob b =new Bob ("Prashu",8);
		System.out.println(b);
	}
}