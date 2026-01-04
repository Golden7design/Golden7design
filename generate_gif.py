import gifos
from dotenv import load_dotenv
import os

load_dotenv()

# Création du terminal virtuel
t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)

# Texte initial
t.gen_text(text="Hello, I'm Nassir", row_num=1)
t.gen_text(text="FullStack Web Developer & DevOps", row_num=2)

# Récupération des stats GitHub
github_stats = gifos.utils.fetch_github_stats(
    user_name="Golden7design"
)

# Suppression de la première ligne
t.delete_row(row_num=1)

# Affichage des infos disponibles
t.gen_text(text=f"GitHub Name: {github_stats.account_name}", row_num=1, contin=True)

if getattr(github_stats, "name", None):
    t.gen_text(text=f"Name: {github_stats.name}", row_num=2)

if getattr(github_stats, "bio", None):
    t.gen_text(text=f"Bio: {github_stats.bio}", row_num=3)

if getattr(github_stats, "email", None):
    t.gen_text(text=f"Email: {github_stats.email}", row_num=4)

# Génération du GIF
t.gen_gif()  # PAS d'argument ici

# Upload optionnel sur IMGBB
if os.getenv("IMGBB_API_KEY"):
    image = gifos.utils.upload_imgbb(file_name="output.gif", expiration=60)
    print("Image URL:", image.url)
else:
    print("GIF généré localement : output.gif")
