import gifos

# Création du terminal virtuel
t = gifos.Terminal(
    width=320,
    height=240,
    xpad=5,
    ypad=5
)

# Texte initial
t.gen_text(
    text="👋 Hello, I'm Nassir",
    row_num=1
)

t.gen_text(
    text="FullStack Web Developer & \x1b[32mDevOps\x1b[0m",
    row_num=2
)

# Récupération des stats GitHub (nécessite un token)
github_stats = gifos.utils.fetch_github_stats(
    user_name="Golden7design"
)

# Suppression de la première ligne
t.delete_row(row_num=1)

# Affichage dynamique avec les données GitHub
t.gen_text(
    text=f"GitHub Name: \x1b[36m{github_stats.account_name}\x1b[0m",
    row_num=1,    contin=True
)

t.gen_text(
    text=f"Public Repos: {github_stats.public_repos}",
    row_num=3
)

t.gen_text(
    text=f"Followers: {github_stats.followers}",
    row_num=4
)

# Génération du GIF
t.gen_gif()

# Upload automatique (OPTIONNEL)
image = gifos.utils.upload_imgbb(
    file_name="output.gif",
    expiration=60
)

print("Image URL:", image.url)
