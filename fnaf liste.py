import webbrowser
import os

# Génère le chemin absolu vers index.html
index_path = os.path.abspath("index.html")
url = "file://" + index_path

# Ouvre automatiquement dans le navigateur
webbrowser.open(url)

# Affiche le lien correct dans la console
print("Lien à copier-coller :", url)

# Dictionnaire : jeu -> liste des animatroniques
animatronics_by_game = {
    "FNAF 1": [
        "Freddy Fazbear", "Bonnie", "Chica", "Foxy", "Golden Freddy"
    ],
    "FNAF 2": [
        "Toy Freddy", "Toy Bonnie", "Toy Chica", "Mangle", "Balloon Boy (BB)", "JJ",
        "The Puppet (Marionette)", "Withered Freddy", "Withered Bonnie",
        "Withered Chica", "Withered Foxy", "Withered Golden Freddy"
    ],
    "FNAF 3": [
        "Springtrap", "Phantom Freddy", "Phantom Chica", "Phantom Foxy",
        "Phantom BB", "Phantom Puppet", "Phantom Mangle"
    ],
    "FNAF 4": [
        "Nightmare Freddy", "Nightmare Bonnie", "Nightmare Chica", "Nightmare Foxy",
        "Nightmare Fredbear", "Nightmare", "Nightmarionne", "Nightmare BB", "Plushtrap"
    ],
    "Sister Location": [
        "Circus Baby", "Ballora", "Funtime Freddy", "Bon-Bon", "Funtime Foxy", "Ennard",
        "Bidybab", "Electrobab", "Minireena", "Yenndo", "Bonnet"
    ],
    "FNAF 6 (Pizzeria Simulator)": [
        "Rockstar Freddy", "Rockstar Bonnie", "Rockstar Chica", "Rockstar Foxy",
        "Lefty", "Molten Freddy", "Scraptrap", "Scrap Baby",
        "Funtime Chica", "El Chip", "Mr. Hippo", "Pigpatch", "Nedd Bear",
        "Orville Elephant", "Happy Frog", "Candy Cadet", "Bucket Bob",
        "Number 1 Crate", "Pan Stan", "Mr. Can-Do", "Helpy"
    ],
    "Ultimate Custom Night": [
        "Phone Guy", "Old Man Consequences", "Dee Dee", "XOR (Shadow Dee Dee)", "Trash and the Gang"
    ],
    "Help Wanted (VR)": [
        "Glitchtrap"
    ],
    "Security Breach": [
        "Glamrock Freddy", "Glamrock Chica", "Montgomery Gator", "Roxanne Wolf",
        "DJ Music Man", "Mini Music Man", "Sun (Daycare Attendant)", "Moon (Moondrop)",
        "The Blob", "Burntrap", "Vanny"
    ],
    "Security Breach: Ruin": [
        "The Mimic", "MXES", "Roxy (damaged)", "Chica (damaged)", "Monty (damaged)", "Prototype Blob"
    ],
    "Special Delivery (AR)": [
        "Freddy (AR)", "Chica (AR)", "Bonnie (AR)", "Foxy (AR)", "Balloon Boy (AR)",
        "Springtrap (AR)", "Toy Freddy (AR)", "Toy Bonnie (AR)", "Toy Chica (AR)", "Mangle (AR)"
    ],
    "Autres (ombres/variantes)": [
        "Shadow Freddy", "RWQFSFASXC (Shadow Bonnie)"
    ]
}

# Page d’accueil
index_html = '''
<html>
  <body>
    <h1>Bienvenue</h1>
    <a href="blank.html">Cliquez ici pour voir la liste des animatroniques par jeu</a>
  </body>
</html>
'''

# Page blanche avec la liste
blank_html = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>Animatroniques FNAF par jeu</title>
    <style>
      body { background: white; color: #111; font-family: Arial, sans-serif; }
      h2 { margin-top: 20px; color: #333; }
      li { margin: 4px 0; }
    </style>
  </head>
  <body>
    <h1>Animatroniques officiels de FNAF (hors fan games)</h1>
'''

# Ajout des sections par jeu
for game, names in animatronics_by_game.items():
    blank_html += f"<h2>{game}</h2>\n<ul>\n"
    for name in names:
        blank_html += f"  <li>{name}</li>\n"
    blank_html += "</ul>\n"

blank_html += '''
  </body>
</html>
'''

# Écriture des fichiers
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

with open("blank.html", "w", encoding="utf-8") as f:
    f.write(blank_html)

# Ouvre automatiquement index.html
webbrowser.open("index.html")
