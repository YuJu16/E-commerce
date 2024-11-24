import hashlib
import sqlite3

def hashMdp(mdp):
    mdp_byte = mdp.encode('utf-8') 
    mdp_hash = hashlib.sha256(mdp_byte).hexdigest()  
    return mdp_hash

def connexion_bdd():
    try:
        connexion = sqlite3.connect("bdd/Ecommerce.sql")
        print("Connexion à la base de données SQLite réussie")
        return connexion
    except sqlite3.Error as e:
        print("Erreur de connexion à la base de données SQLite :", e)
        return None

def vider_tables(curseur):
    curseur.execute("DELETE FROM panier_produit;")
    curseur.execute("DELETE FROM facture;")
    curseur.execute("DELETE FROM commande;")
    curseur.execute("DELETE FROM payement;")
    curseur.execute("DELETE FROM evaluation;")
    curseur.execute("DELETE FROM photo;")
    curseur.execute("DELETE FROM adresse;")
    curseur.execute("DELETE FROM produit;")
    curseur.execute("DELETE FROM user;")
    curseur.execute("DELETE FROM panier;")  

def remplir_tables():
    connexion = connexion_bdd()
    if connexion:
        try:
            curseur = connexion.cursor()

            vider_tables(curseur)

            utilisateurs = [
                (1, "Joeastar", "Johnny", "joeastar.johnny@gmail.com", hashMdp("mdp123"), "0123456789", "2021-01-01"),
                (2, "Zepelli", "Gyoro", "zeppeli.gyoro@gmail.com", hashMdp("mdp456"), "0123456789", "2021-01-02"),
                (3, "Brando", "Dio", "brando.dio@gmail.com", hashMdp("mdp789"), "0123456789", "2021-01-03"),
            ]

            produits = [
                (1, "Laptop", "Ordinateur portable", 1200, 10, "Électronique"),
                (2, "Smartphone", "Téléphone intelligent", 800, 15, "Électronique"),
                (3, "Tablet", "Tablette", 600, 5, "Électronique"),
            ]

            adresses = [
                (1, 1, "1 rue de Via Giovanni Giolitti", "Rome", "00185", "Italie"),
                (2, 2, "2 rue de Piazza della Repubblica", "Rome", "00185", "Italie"),
                (3, 3, "3 rue de Via del Corso", "Rome", "00185", "Italie"),
            ]

            commandes = [
                (1, 1, 1, "En cours", "2021-05-01", None),
                (2, 2, 1, "Livré", "2021-05-02", "2021-05-03"),
                (3, 3, 1, "En cours", "2021-05-03", None),
            ]

            paniers = [
                (1, 1),
                (2, 2),
                (3, 3),
            ]

            factures = [
                (1, 1, "2021-05-01", 1200),
                (2, 2, "2021-05-02", 800),
                (3, 3, "2021-05-03", 600),
            ]

            evaluations = [
                (1, 1, 1, 5, "Très bon produit"), 
                (2, 1, 2, 4, "Bon produit"),
                (3, 2, 1, 3, "Produit correct"),
            ]


            paniers_produits = [
                (1, 1, 1),
                (2, 2, 1),
                (3, 3, 1),
            ]

            paiements = [
                (1, 1, "Carte de crédit", "1234567812345678", "2025-12-31", 123),
                (2, 2, "PayPal", "N/A", "2025-12-31", 123),
                (3, 3, "Carte de crédit", "1234567812345678", "2025-12-31", 123),
            ]

            photos = [
                (1, "photo1.jpg"),
                (2, "photo2.jpg"),
                (3, "photo3.jpg"),
            ]

            curseur.executemany("INSERT INTO user (id_user, nom, prenom, email, mot_de_passe, numero_de_telephone, date_de_creation) VALUES (?, ?, ?, ?, ?, ?, ?)", utilisateurs)
            print("Utilisateurs insérés.")

            curseur.executemany("INSERT INTO produit (id_produit, nom, description, prix, quantite, categorie) VALUES (?, ?, ?, ?, ?, ?)", produits)
            print("Produits insérés.")

            curseur.executemany("INSERT INTO adresse (id_adresse, id_user, adresse, ville, code_postal, pays) VALUES (?, ?, ?, ?, ?, ?)", adresses)
            print("Adresses insérées.")

            curseur.executemany("INSERT INTO commande (id_commande, id_user, id_panier, statut, date_de_commande, date_de_livraison) VALUES (?, ?, ?, ?, ?, ?)", commandes)
            print("Commandes insérées.")

            curseur.executemany("INSERT INTO panier (id_panier, id_user) VALUES (?, ?)", paniers)
            print("Paniers insérés.")


            curseur.executemany("INSERT INTO facture (id_facture, id_commande, date_de_facturation, montant_total) VALUES (?, ?, ?, ?)", factures)
            print("Factures insérées.")

            curseur.executemany("INSERT INTO evaluation (id_evaluation, id_user, id_produit, note, commentaire) VALUES (?, ?, ?, ?, ?)", evaluations)
            print("Évaluations insérées.")

            curseur.executemany("INSERT INTO panier_produit (id_panier, id_produit, quantite) VALUES (?, ?, ?)", paniers_produits)
            print("Paniers_produits insérés.")

            curseur.executemany("INSERT INTO payement (id_payement, id_user, type, numero_de_carte, date_de_expiration, code_de_securite) VALUES (?, ?, ?, ?, ?, ?)", paiements)
            print("Paiements insérés.")

            curseur.executemany("INSERT INTO photo (id_photo, lien) VALUES (?, ?)", photos)
            print("Photos insérées.")

            connexion.commit() 
            print("Toutes les données ont été insérées avec succès.")
        except sqlite3.IntegrityError as e:
            print("Erreur lors du remplissage des tables :", e)
        finally:
            connexion.close()

if __name__ == "__main__":
    remplir_tables()
