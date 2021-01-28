public class Ligne {
	Produit produit;
	int quantite;
	int prix_total;
	
	public Ligne(Produit produit, int quantite) {
		super();
		this.setProduit(produit);
		this.setQuantite(quantite);
		this.setPrix_total(produit.getPrix()*quantite);
	}

	public Produit getProduit() {
		return produit;
	}

	public void setProduit(Produit produit) {
		this.produit = produit;
	}

	public int getQuantite() {
		return quantite;
	}

	public void setQuantite(int quantite) {
		this.quantite = quantite;
	}

	public int getPrix_total() {
		return prix_total;
	}

	public void setPrix_total(int prix_total) {
		this.prix_total = prix_total;
	}

}