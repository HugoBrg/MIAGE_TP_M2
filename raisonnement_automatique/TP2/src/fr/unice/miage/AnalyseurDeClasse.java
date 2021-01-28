package fr.unice.miage;

import java.lang.reflect.*;
import java.io.*;

public class AnalyseurDeClasse {

	public static void analyseClasse(String nomClasse) throws ClassNotFoundException {
		// Récupération d'un objet de type Class correspondant au nom passé en paramètres
		Class cl = Class.forName(nomClasse);

		afficheEnTeteClasse(cl);

		System.out.println();
		afficheAttributs(cl);

		System.out.println();
		afficheConstructeurs(cl);

		System.out.println();
		afficheMethodes(cl);

		// L'accolade fermante de fin de classe !
		System.out.println("}");
	}


	/** Retourne la classe dont le nom est passé en paramètre */
	public static Class getClasse(String nomClasse) throws ClassNotFoundException {
		Class<?> cl = Class.forName(nomClasse);
		return cl;
	}

	/** Cette méthode affiche par ex "public class Toto extends Tata implements Titi, Tutu {" */
	public static void afficheEnTeteClasse(Class cl) {
		//  Affichage du modifier et du nom de la classe
		int x = cl.getModifiers();
	    String retval = Modifier.toString(x);
		System.out.print("\n\n"+retval+" ");
		System.out.print(cl.getName());
		// CODE A ECRIRE

		// Récupération de la superclasse si elle existe (null si cl est le type Object)
		Class supercl = cl.getSuperclass();// CODE A ECRIRE

		// On ecrit le "extends " que si la superclasse est non nulle et
		// différente de Object
		// CODE A ECRIRE
		if(supercl != null) {
			System.out.print(" extends "+supercl.getName());
		}

		// Affichage des interfaces que la classe implemente
		// CODE A ECRIRE
		if(cl.getInterfaces() != null) {
			System.out.print(" implements ");
		}
		for(int i = 0;i<cl.getInterfaces().length; i++) {
			System.out.print(cl.getInterfaces()[i]);
		}

		// Enfin, l'accolade ouvrante !
		System.out.println(" {");
	}

	public static void afficheAttributs(Class cl) {
		for(int i = 0;i<cl.getDeclaredFields().length; i++) {
			System.out.println("	"+cl.getDeclaredFields()[i]);
		}
	}

	public static void afficheConstructeurs(Class cl) {
		for(int i = 0;i<cl.getConstructors().length; i++) {
			System.out.println("	"+cl.getConstructors()[i]+"{}");
		}

	}


	public static void afficheMethodes(Class cl) {
		for(int i = 0;i<cl.getMethods().length; i++) {
			System.out.println("	"+cl.getMethods()[i]+"{}");
		}

	}


	public static String litChaineAuClavier() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		return br.readLine();
	}

	public static void main(String[] args) {
		boolean ok = false;

		while(!ok) {
			try {
				System.out.print("Entrez le nom d'une classe (ex : java.util.Date): ");
				String nomClasse = litChaineAuClavier();

				analyseClasse(nomClasse);

				ok = true;
			} catch(ClassNotFoundException e) {
				System.out.println("Classe non trouvée.");
			}catch(IOException e) {
				System.out.println("Erreur d'E/S!");
			}
		}
	}
}