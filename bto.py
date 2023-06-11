import feedparser
from bs4 import BeautifulSoup
import requests
import openai
from instabot import Bot
import ssl

# Init openAI API
openai.api_key = ['OPEN_KEY']

def init_feed():
# URL du flux RSS que vous souhaitez lire
    url = ['FLUX_RSS']

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    # Lire le flux RSS
    feed = feedparser.parse(url)

    # Afficher les informations du flux RSS
    if 'updated' in feed.feed:
        print("Dernière mise à jour du flux:", feed.feed.updated)
    img_select(feed)

def text_select (url,title):
    # Récupérer le contenu HTML de la page web
    response = requests.get(url)
    html = response.content

    # Analyser le HTML avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    paragraph = soup.find_all('p')
    content = ' '.join([p.get_text() for p in paragraph])
    get_init(content,title)

def img_select (feed):
    if 'entries' in feed:
        # Parcourir les éléments du flux RSS
        for entry in feed.entries:
            # Récupérer le titre de l'article
            if 'title' in entry:
                title = entry.title
                print("Titre de l'article:", title)

            # Récupérer l'URL de l'article
            if 'link' in entry:
                article_url = entry.link

            # Récupérer l'URL de l'image
            if 'enclosures' in entry and len(entry.enclosures) > 0:
                image_url = entry.enclosures[0].href
                print("URL de l'image:", image_url)
            img = image_url
            url = article_url
            save_img (img)
            text_select(url,title)
            break
    else:
        print("Le flux RSS ne contient aucun élément.")

    # init de GPT
def get_init (content,title):
        type_chatbot = "tu vas reformuler ou raccourcir les texte que car sa va etres une description d'un poste instagram et ajoute 15 hashtag a la description en rapport avec le texte"
        messages=[
            {"role": "system", "content": type_chatbot}]
        chatbot(messages,content,title)  
        
    #Création de la conversation avec GPT
def chatbot (messages,content,title):
            user_input = content
            messages.append({"role": "user","content": user_input}) 
            reponse = openai.ChatCompletion.create(
                model= "gpt-3.5-turbo",
                messages = messages
            ).choices[0].message
            
            messages.append(reponse)
            description = reponse.content
            description = title + ":\n " + description
            #print(description)
            insta(description)
        
def save_img (img):
    response = requests.get(img)
    response.raise_for_status()
    image_data = response.content
    # Enregistrer l'image dans un fichier
    with open("image.jpg", "wb") as file:
        file.write(image_data)
    print("L'image a été téléchargée avec succès.")

def insta (description):
    bot = Bot()
    bot.login(username=['USERNAME'], password=['PASSWORD'])
    bot.upload_photo("image.jpg", caption= description)

init_feed()