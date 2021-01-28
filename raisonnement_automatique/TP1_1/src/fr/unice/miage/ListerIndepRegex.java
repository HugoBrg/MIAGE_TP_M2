package fr.unice.miage;

import java.io.File;
import java.io.FilenameFilter;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ListerIndepRegex implements FilenameFilter {
	@Override
	public boolean accept(File dir, String name) {
		File[] lf = dir.listFiles();

		Pattern p = Pattern.compile(".*"+name+".*");
		
		for(int i=0; i<lf.length; i++) {
			Matcher m = p.matcher(lf[i].getName());
			if(m.matches()) {
				return true;
			}
		}
		return false;
	}
}
