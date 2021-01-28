package primeNumbersXOM;


public class primeNumbersXOM {

	private int number;
	private boolean prime;

	public primeNumbersXOM(int number) {
		this.number = number;
		this.prime = this.isPrime();
	}
	
	public boolean isPrime() {
		for (int i = 1; i < this.number /2 ; i++) {
			if(this.number % i == 0) {
				return false;
			}
		}
		return true;
		
	}
	
	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}

	public void setPrime(boolean prime) {
		this.prime = prime;
	}
	
}
