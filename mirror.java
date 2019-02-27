package practice;

public class mirror {
	
	public static void check(int row) {
		for(int i=1; i<=row; i++) {
			if((i%2)==0) {
				for(int j=0; j<=row; j++) {
					if(j<1) {
						System.out.print(i+1);
					}else
					{	
						System.out.print(i);
						if(j==row)
						System.out.println();
					}
					
				}
			}else
			{
				for(int j=0; j<=row; j++) {
					if(j<row) {
						System.out.print(i);
					}else
					{	
						System.out.print(i+1);
						System.out.println();
					}
					
				}
			}
			
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		check(99);
	}

}
