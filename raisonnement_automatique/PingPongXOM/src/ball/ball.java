package ball;

public class ball {
	
	public ball(String name, String sound) {
		super();
		this.name = name;
		this.sound = sound;
	}
	private String name;
	private String sound;
	private int numberOfHits;
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSound() {
		return sound;
	}
	public void setSound(String sound) {
		this.sound = sound;
	}
	public int getNumberOfHits() {
		return numberOfHits;
	}
	public void setNumberOfHits(int numberOfHits) {
		this.numberOfHits = numberOfHits;
	}
	
	
}


