import requests
import argparse

parser = argparse.ArgumentParser(description='Monitoring de board 4chan')
parser.add_argument('-b', '--board', help='3 - 3DCG | a - Anime & Manga | aco - Adult Cartoons | adv - '
                                          'Advice | an - Animals & Nature | asp - Alternative Sports | b - '
                                          'Random | bant - InternationalRandom | biz - Business & Finance | c - '
                                          'AnimeCute | cgl - Cosplay & EGL | ck - Food & Cooking | cm - '
                                          'CuteMale | co - Comics & Cartoons | d - HentaiAlternative | diy - '
                                          'Do-It-Yourself | e - Ecchi | fa - Fashion | fit - Fitness | g - '
                                          'Technology | gd - Graphic Design | gif - Adult GIF | h - Hentai | hc - '
                                          'Hardcore | hm - Handsome Men | hr - High Resolution | i - Oekaki | ic '
                                          '- ArtworkCritique | his - History & Humanities | int - '
                                          'International | jp - Otaku Culture | k - Weapons | lit - '
                                          'Literature | lgbt - LGBT | m - Mecha | mlp - Pony | mu - Music | news '
                                          '- Current News | n - Transportation | o - Auto | out - Outdoors | p - '
                                          'Photography | po - Papercraft & Origami | pol - Politically '
                                          'Incorrect | pw - Professional Wrestling | qst - Quests | r - Adult '
                                          'Requests | r9k - ROBOT9001 | s4s - Shit 4chan Says | s - Sexy Beautiful '
                                          'Women | sci - Science & Math | soc - Cams & Meetups | sp - Sports | t '
                                          '- Torrents | tg - Traditional Games | toy - Toys | trash - '
                                          'Off-topic | trv - Travel | tv - Television & Film | u - Yuri | v - '
                                          'Video Games | vg - Video Game Generals | vm - Video '
                                          'GamesMultiplayer | vmg - Video GamesMobile | vip - Very Important '
                                          'Posts | vp - Pokémon | vr - Retro Games | vrpg - Video GamesRPG | vst '
                                          '- Video GamesStrategy | vt - Virtual YouTubers | w - '
                                          'AnimeWallpapers | wg - WallpapersGeneral | wsg - Worksafe GIF | wsr - '
                                          'Worksafe Requests | x - Paranormal | xs - Extreme Sports | y - Yaoi')
parser.add_argument('-t', '--tag', nargs='+', help='tag to watch')
# Parse les arguments en ligne de commande
args = parser.parse_args()

# Vérifie que les arguments --board et --tag sont présents
if not args.board or not args.tag:
    print('Il est nécessaire de spécifier un board et un tag.')
    exit()

# Prépare l'URL de l'API 4chan
url = f'https://a.4cdn.org/{args.board}/catalog.json'

# Récupère les données du board
try:
    response = requests.get(url)
    response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
    data = response.json()
except requests.exceptions.HTTPError as error:
    print(f'Erreur HTTP : {error}')
    exit()
except Exception as error:
    print(f'Erreur : {error}')
    exit()

# Recherche les tags dans les threads
nb_threads = 0
no_of_thread = 0

for element in data:
    threads = element.get('threads')

    for thread in threads:
        sub = thread.get('sub', '').lower()  # Titre du thread en minuscules
        com = thread.get('com', '').lower()  # Commentaire du thread en minuscules
        filename = thread.get('filename', '').lower()  # Nom du fichier en minuscules

        # Vérifie si un des tags spécifiés est présent dans le titre, le commentaire ou le nom de fichier
        for tag in args.tag:
            if tag.lower() in sub or tag.lower() in com or tag.lower() in filename:
                if no_of_thread != thread.get('no'):
                    print('\n\n---> thread = ', thread)
                    no_of_thread = thread.get('no')
                    nb_threads += 1

# Affiche le nombre de threads trouvés
print("\n----------")
print("nb_thread = ", nb_threads, "")