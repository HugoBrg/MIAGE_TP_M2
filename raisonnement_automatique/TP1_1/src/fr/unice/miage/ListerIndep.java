package fr.unice.miage;
import java.io.File;
import java.io.FilenameFilter;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ListerIndep implements FilenameFilter{

	private String filter;
	
	ListerIndep(String filter){
		this.filter=filter;
	}
	
	@Override
	public boolean accept(File dir, String name) {
        return name.toLowerCase().endsWith(filter);
	}

}
