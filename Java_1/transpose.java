/*transpose of a matrix*/

import java.util.*;
import java.io.*;

public class transpose{

	public static void main(String [] args){

		Scanner sc= new Scanner(System.in);

		/*varaible declartion*/
		int row,col;
		
		System.out.println("Enter the number of rows:");
		row=sc.nextInt();

		System.out.println("Enter the number of columns:");
		col=sc.nextInt();

		int [][] a=new int[row][col];

		System.out.println("Enter the elements of the array:");
		for (int i=0; i < row; i++){
			for(int j=0; j< col; j++){
				a[i][j]=sc.nextInt();
			}
		}
		int [][] at=new int[col][row];

		for (int i=0; i < row; i++){
			for(int j=0; j< col; j++){
				at[j][i]=a[i][j];
			}
		}

		System.out.println("The transpose of the matrix is:");
		for(int i=0; i < col; i++){
			for(int j=0; j< row; j++ ){
				System.out.println(at[i][j]);
			}
		}


	}
}