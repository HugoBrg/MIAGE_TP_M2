package fr.unice.miage;

import java.io.File;
import java.io.IOException;
import java.nio.file.FileVisitResult;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;

public class Main {	
	private static String chemin = ".";
	private static File f = new File(chemin);	
	
	public static void main(String[] args) throws IOException {
		/*ListerFNF listerFNF = new ListerFNF();
		listerFNF.lister(f);
		listerFNF.listerProfondeur(f);
		listerFNF.listerExtension(f); 									  	//classe independante
		ListerFNF.ListerInterne li = new ListerFNF().new ListerInterne(); 	//classe interne
		listerFNF.listerNomRegex(f,"src");									//expression régulière
		listerFNF.listerNomRegex(f,"blablabla");*/
		
		ListerSFV listerSFV = new ListerSFV();								//SimpleFileVisitor
		Path fPath = Paths.get(f.getPath());
		Files.walkFileTree(fPath, listerSFV);
	}

}
