public class Produit {
	String nom;
	String categorie;
	int prix;
	
	public Produit(String nom, String categorie, int prix) {
		super();
		this.setNom(nom);
		this.setCategorie(categorie);
		this.setPrix(prix);
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public String getCategorie() {
		return categorie;
	}

	public void setCategorie(String categorie) {
		this.categorie = categorie;
	}

	public int getPrix() {
		return prix;
	}

	public void setPrix(int prix) {
		this.prix = prix;
	}	
}