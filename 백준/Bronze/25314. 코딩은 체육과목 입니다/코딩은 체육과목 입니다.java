import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		String str = "";
		scan.close();
		
		for(int i=1; i<=n/4; i++) {
			str += "long ";
		}
		System.out.println(str + "int");

	}
}