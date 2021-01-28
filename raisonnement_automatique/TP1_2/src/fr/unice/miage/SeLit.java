package fr.unice.miage;

import java.io.File;  
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;   
  
public class SeLit {  
	
	private File f;
	private Scanner sc;
	private List<String> buff = new ArrayList<String>();
	
	public SeLit(File f) {
		this.f=f;
		try {
			this.sc= new Scanner(f);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}
   
	void lecture() throws IOException {  
		Scanner sc = new Scanner(f);
		int i = 0;
		while(sc.hasNextLine()) {  
			String s = sc.nextLine();          
			System.out.println("LU: "+s);
	        Pattern pattern = Pattern.compile("^\\/\\/");
	        Matcher matcher = pattern.matcher(s);
	        if(matcher.find()) {
	            System.out.println("Trouvé ! : "+s);
	        }else {
	        	buff.add(s);
	        }
	        i++;
		}  
		for(int x=0;x<buff.size();x++) {
			System.out.println(buff.get(x));
		}
	}  
	
	void ecriture() throws IOException {
        FileWriter wr = new FileWriter(f.getCanonicalPath());
		for(int x=0;x<buff.size();x++) {
	        try (PrintWriter pw = new PrintWriter(wr)) {
				pw.write(buff.get(x));
			}	
		}
	}
  
	public static void main(String[] args) {  

	}  
}  