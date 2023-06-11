# Flux RSS et Publication Instagram

Ce code est conçu pour lire un flux RSS et publier des articles sur Instagram en utilisant l'API OpenAI. Voici comment utiliser ce code :

## Installation des dépendances

Assurez-vous d'avoir les bibliothèques suivantes installées :
- feedparser 
- BeautifulSoup
- requests
- openai
-instabot

Vous pouvez les installer en utilisant pip :

`pip install feedparser beautifulsoup4 requests openai instabot`

## Configuration de l'API OpenAI

Avant d'exécuter le code, vous devez configurer votre clé d'API OpenAI. Remplacez `['OPEN_KEY'] `par votre clé d'API dans le code.

## Configuration du flux RSS

Dans la fonction `init_feed()`, remplacez `['FLUX_RSS']` par l'URL du flux RSS que vous souhaitez lire.

## Configuration d'Instagram

Dans la fonction `insta()`, remplacez `['USERNAME'`] et `['PASSWORD']` par votre nom d'utilisateur et votre mot de passe Instagram.

## Exécution du code
Une fois que vous avez effectué toutes les configurations nécessaires, vous pouvez exécuter le code en lançant la fonction `init_feed()`. Le code récupérera le dernier article du flux RSS, téléchargera l'image associée, extraira le texte de l'article et générera une description avec l'API OpenAI. Ensuite, il publiera l'image et la description sur Instagram.

Assurez-vous d'avoir une connexion Internet active lors de l'exécution du code.

>Note : Ce code utilise la version GPT-3.5 Turbo de l'API OpenAI. Vous devez disposer d'un accès valide à cette version pour l'utiliser.

N'hésitez pas à personnaliser le code selon vos besoins et à l'adapter à d'autres flux RSS ou plateformes de médias sociaux. Bonne utilisation !
