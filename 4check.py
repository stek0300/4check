import requests
import argparse
import os
import time
from bs4 import BeautifulSoup
from tqdm import tqdm


# Vérifie si le dossier "threads" existe. S'il n'existe pas, le crée.
def path_change(path_):
    new_path = path_.replace('\\', '/')
    new_path += "/"
    print("path parsé")
    return new_path


def check_create_folder(path_):
    if os.path.exists(path_ + 'threads/'):
        print(path_ + 'threads/ existe')
        pass
    else:
        os.mkdir(path_ + 'threads/')
        print(path_ + 'threads/ créé')


def create_thread_folder(path_, no_thread):
    if os.path.exists(path_ + 'threads/' + no_thread):
        print(path_ + 'threads/' + no_thread + ' existe')
        pass
    else:
        os.mkdir(path_ + 'threads/' + no_thread)
        print(path_ + 'threads/' + no_thread + ' créé')


def create_thread_txt_file(path_, no_thread):
    with open(path_ + 'threads/' + no_thread + '/' + no_thread + '.txt', "w", encoding='utf-8') as f:
        f.write(str(thread))
    print(path_ + 'threads/' + no_thread + '/' + no_thread + '.txt créé')


def create_thread_html_file(path_, no_thread, key_board):
    url_thread = "https://boards.4channel.org/" + key_board + "/thread/" + no_thread
    r = requests.get(url_thread)
    html_thread = r.text
    soup = BeautifulSoup(html_thread, 'html.parser')
    with open(path_ + 'threads/' + no_thread + '/index.html', "w", encoding='utf-8') as f:
        f.write(str(soup))
    print(path_ + 'threads/' + no_thread + '/index.html créé')


def parse_html_file(path_, no_thread):
    with open(path_ + 'threads/' + no_thread + '/index.html', "r", encoding='utf-8') as f:
        file = f.read()
        new_file = file.replace("//", "https://")

    with open(path_ + 'threads/' + no_thread + '/index.html', "w", encoding='utf-8') as f:
        f.write(new_file)
    print(path_ + 'threads/' + no_thread + '/index.html parsé')


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
parser.add_argument('-p', '--path', type=str, help='chemin pour le depot des threads (full path)', required=False)
# Parse les arguments en ligne de commande
args = parser.parse_args()

# Vérifie que les arguments --board et --tag sont présents
if not args.board or not args.tag:
    print('Il est nécessaire de spécifier un board et un tag.')
    exit()

path = ""
if args.path:
    path = path_change(str(args.path))



nb_mj = 0

OS = os.name

while True:

    if OS == 'nt':
        os.system('cls')
    elif OS == 'posix':
        os.system('clear')

    print("\n---------- logs ----------")
    print("path : " + path)

    check_create_folder(path)

    # Prépare l'URL de l'API 4chan
    url_api = f'https://a.4cdn.org/{args.board}/catalog.json'


    # Récupère les données du board
    try:
        response = requests.get(url_api)
        print(response)
        response.raise_for_status()  # Lève une exception en cas d'erreur HTTP
        data = response.json()
        print("api trouvée : ", url_api)
        print("JSON récupéré")
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
                        no_of_thread = thread.get('no')
                        # print('\n\n---> thread = ', thread)
                        print("threads " + str(thread.get('no')) + " récupéré")
                        create_thread_folder(path, str(thread.get('no')))
                        create_thread_txt_file(path, str(thread.get('no')))
                        create_thread_html_file(path, str(thread.get('no')), args.board)
                        parse_html_file(path, str(thread.get('no')))
                        nb_threads += 1

    nb_mj += 1
    print("nombre de thread(s) trouvés : ", nb_threads)
    print("nombre de mise à jour : ", nb_mj)
    print("Ctrl+C pour stopper le programme")

    for i in tqdm(range(0, 120), desc="next update (120s) : "):
        time.sleep(1)
