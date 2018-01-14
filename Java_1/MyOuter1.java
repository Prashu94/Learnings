class MyOuter1
{
	private int x = 7;
	
	class MyInner
	{
		public void seeOuter(){
			System.out.println("Outer x is:" + x);
		}
	}
	public static void main(String [] args){
		MyOuter1.MyInner inner = new MyOuter1().new MyInner();
		inner.seeOuter();
	}
}