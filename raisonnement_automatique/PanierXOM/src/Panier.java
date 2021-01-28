import java.util.ArrayList;
import java.util.List;

public class Panier {
	List<Ligne> lignes;
	int prix_total;
	
	public Panier() {
        super();
        this.setLignes(new ArrayList<>());
        this.setPrix_total(0);
    }

    public Panier(Ligne[] lignes) {
        super();
        this.setLignes(new ArrayList<>());
        this.setPrix_total(0);
        for(Ligne l : lignes) {
            this.setLigne(l);
        }
    }
	
	public void calculPrixTotal() {
		List<Ligne> lignes = this.getLignes();
		int prix = 0;
		for(Ligne l : lignes) {
			prix += l.getPrix_total();
		}
	}

	public List<Ligne> getLignes() {
		return lignes;
	}

	public void setLignes(List<Ligne> lignes) {
		this.lignes = lignes;
	}
	
	public void wolaLignes(List<Ligne> lignes) {
		this.lignes = lignes;
	}

	public int getPrix_total() {
		return prix_total;
	}

	public void setPrix_total(int prix_total) {
		this.prix_total = prix_total;
	}
	
	public void setLigne(Ligne ligne) {
		this.lignes.add(ligne);
	}


}