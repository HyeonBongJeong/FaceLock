
public class TestBreak {
	public static void main(String[] args) {
		int sum = 0;
		for (int i = 1;   ; i++) {
			sum += i;

			if (i == 100) {
				System.out.println("1부터 100까지의 합" + sum);
				break;
			}

		}

	}
}
