package fr.unice.miage;
import java.io.File;
import java.io.FilenameFilter;

public class ListerFNF{
	
	//INTERNE
	public class ListerInterne{
		private String chemin = ".";
		private File f = new File(chemin);	
		public ListerInterne() {
			ListerFNF.this.listerExtension(f);
		}
	}
	
	//ANONYME
	public FilenameFilter testAnonyme(String filter) {
		FilenameFilter f = new FilenameFilter() {
			@Override
			public boolean accept(File dir, String name) {
		        return name.toLowerCase().endsWith(filter);
			}
		};
		return f;
	}

	
	//LISTAGE
	public void lister(File f) {
		File[] lf = f.listFiles();
		afficher(lf);
	}
	
	//LISTAGE EN PROFONDEUR
	public void listerProfondeur(File f) {
		File[] lf = f.listFiles();
		for(int i=0;i<lf.length;i++) {
			if(lf[i].isDirectory()) {
				ListerFNF lister = new ListerFNF();
				lister.listerProfondeur(lf[i]);
				System.out.println(lf[i]);
			}
			else if(lf[i].isFile()) {
				System.out.println(lf[i]);
			}			
		}
	}
	
	//LISTAGE EN PROFONDEUR AVEC EXTENSIONS
	public void listerExtension(File f) {		
		File[] lf = f.listFiles();
		for(int i=0;i<lf.length;i++) {
			if(lf[i].isDirectory()) {
				ListerFNF lister = new ListerFNF();
				lister.listerExtension(lf[i]);
			}
			else if(lf[i].isFile()) {
			}		
		}		
			
		lf = f.listFiles(new ListerIndep(".class"));		//classe Independante
		afficher(lf);
	}
	
	//REGEX
	public void listerNomRegex(File f, String name) {
		ListerIndepRegex reg = new ListerIndepRegex();
		if(reg.accept(f, name))
			System.out.println("Le fichier/dossier est présent");
		else
			System.out.println("Le fichier/dossier n'est pas présent");
	}
	
	//AFFICHER
	public void afficher(File[] lf) {
		for(int i=0;i<lf.length;i++) {
			System.out.println(lf[i]);
		}
	}	
}
