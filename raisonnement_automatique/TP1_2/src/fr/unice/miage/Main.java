package fr.unice.miage;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
		public static void main(String[] args) throws IOException {
			   
			File f = new File("./src/fr/unice/miage/hugo.txt");
			  
			SeLit sl = new SeLit(f);
			sl.lecture();
			sl.ecriture();
		}
}
