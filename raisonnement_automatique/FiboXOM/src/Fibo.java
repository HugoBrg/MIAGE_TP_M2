import java.util.ArrayList;

public class Fibo {
	private int n;
	private int itr;
	private int fn;
	private int fn1 = 0;
	private int fn2 = 1;
	private boolean goal = false;
	ArrayList<Integer> arr =  new ArrayList<Integer>() ;
	
	public Fibo(int n) {
		super();
		this.n = n;
		for (int i = 0; i < n-1; i++) {
			arr.add(i);
		}
	}
	

	public ArrayList<Integer> getArr() {
		return arr;
	}

	public void setArr(ArrayList<Integer> arr) {
		this.arr = arr;
	}

	public int getItr() {
		return itr;
	}

	public void setItr(int itr) {
		this.itr = itr;
	}

	public int getFn1() {
		return fn1;
	}

	public void setFn1(int fn1) {
		this.fn1 = fn1;
	}

	public int getFn2() {
		return fn2;
	}

	public void setFn2(int fn2) {
		this.fn2 = fn2;
	}

	public int getN() {
		return n;
	}
	
	public void setN(int n) {
		this.n = n;
	}
	
	public int getFn() {
		return fn;
	}
	
	public void setFn(int fn) {
		this.fn = fn;
	}
	
	public boolean isGoal() {
		return goal;
	}
	
	public void setGoal(boolean goal) {
		this.goal = goal;
	}
	
}


