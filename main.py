from flask import Flask, render_template, request, redirect, session
from pendu import Pendu
import random

# On crée l'application
app = Flask("MonApplication")
app.secret_key = "cookiesSansGluten"

# Lorsqu'on lance l'application, on réinitialise le jeu et on redirige vers la route /jeu
@app.route("/")
def accueil():
  # Initialisation du pendu
  liste_mots = ["journee","regarder","bizarre","fantome","espoir","voiture","reponse","message"]
  mot = random.choice(liste_mots)
  vies = 6
  # Notre état de jeu sera stocké dans un cookie
  session["etat_jeu"] = Pendu.initialiser(mot, vies)
  # On redirige vers /jeu (réactualise la page)
  return redirect("/jeu")

# Route principale qui affiche la page du pendu
@app.route("/jeu")
def jeu():
  # On réaffiche la page index.html, en lui passant
  # l'état du jeu stocké dans une variable "data"
  return render_template('index.html', data = session["etat_jeu"])

# Route lancée à chaque fois qu'on clique sur "Valider" : on met à jour l'état du jeu à partir de l'entrée donnée par l'utilisateur, puis on redirige vers la route principale
@app.route("/deviner", methods=["POST"])
def deviner():
  # Récupération de l'entrée utilisateur (input)
  input = request.form["entree"]
  # Mise à jour de l'état du jeu avec cet input
  session["etat_jeu"] = Pendu.deviner(session["etat_jeu"], input)
  # On redirige vers /jeu
  return redirect("/jeu")



# On lance l'application

app.run("0.0.0.0",3904, debug=True)
