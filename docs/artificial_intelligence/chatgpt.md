# Chatgpt

## Présentation générale
### Concept de base

Large Langage Model qui intéragit sous forme de conversation (contrairement aux anciens modèles GPT). Elle génère du texte token par token (1token = 1mot) à partir d'une entrée textuelle. Ces modèles auraient mêmes des [capacités émergentes](https://bdtechtalks.com/2022/08/22/llm-emergent-abilities/).

Entrainée par [OpenAI](https://openai.com/) (ceux qui ont fait le [cache-cache multi-agent](https://openai.com/blog/emergent-tool-use/)) ChatGPT:

Architecture utilisant des [transformers](https://jalammar.github.io/illustrated-transformer/): des réseaux de neurones basés sur le mecanisme de "self-attention" pour pondérer les différéntes parties d'une séquence et effectuer différentes tâches: traduction, génération, classification, etc. Ils peuvent être entrainés avec de grandes quantités de données non-labellisés (super avec internet à disposition). Ils apprennent à trouver des relations entre différentes parties de grandes séquences de mots/données. Stratégie très efficace et scalable.

### Entraînement

Entraînement via du RL avec feedback humain ([RLHF](https://huggingface.co/blog/rlhf))
Une des API les plus utilisées en RL est justement celle de OpenAI: [Gym](https://www.gymlibrary.dev/)

Cette méthode d'entraînement est coûteuse en donnée (gros datasets, intervention humaine) + RL pas super stable grande hype y'a 5ans, moins maintenant cf [tweet](https://twitter.com/ylecun/status/1602226280984113152?s=20&t=6HhUU40XHCzTwaga_ehyVQ) de LeCun et conseil de Hinton aux jeunes chercheurs:

 1. don't do RL
 2. don't do what senior researchers tell you to do

Pour donner une idée, l'intégralité de wikipédia anglais est dans le corpus d'entraînement (0.6%).

A propos de ChatGPT, la méthode d'entraînement est sur [le site](https://openai.com/blog/chatgpt/), elle se sépare en 3 parties:

1. Collecte de données supervisées par des humains pour entraîner une policy supervisée (quelle action faire selon l'état courant)
2. Laisse le modèle produire plein de texte, et les humains notent ces textes. Ces données ne sont pas utilisées pour entraîner le modèle directement, mais pour un modèle de récompense (bon ou mauvais?). Permet d'avoir un bon systeme de récompense (pas à la main, pas naturel comme pour les jeux)
3. Utilise de la [PPO](https://openai.com/blog/openai-baselines-ppo/) pour entraîner le modèle vis a vis du modèle de recompense

Problème des précédents modèles [GPT3](https://arxiv.org/pdf/2005.14165.pdf): produisent trop de réponses cohérentes mais manifestement fausses. Rajout de supervision via RLHF où des feedbacks sont parfois apportés à l'agent pour le guider dans la bonne direction. Il faut juste bien doser supervisé/non-supervisé pour profiter du meilleur des deux méthodes.

### Caractéristiques

- Grande interactivité
- Accepte du contexte (~ 8000 tokens)
- Accepte différentes langues
- Créative
- Entrainées avec des données post Q4 2021

Openai a mis des gardes fous pour éviter les problèmes: racisme, discrimination, projets dangereux.. Comment ? Systeme externe qui filtre ou bien du "fine-tuning", ou les 2

Continue d'être patché suite aux duperie mises en avant, il semblerait qu'ils l'aient même bridé cette semaine.

## Analyse
### Forces et faiblesses

| Forces                                   | Faiblesses                                    |
| ---------------------------------------- | --------------------------------------------- |
| Interactivité                            | Hallucination (références non existantes)     |
| Contexte                                 | Compositionalité                              |
| Adaptabilité                             | Très verbeux                                  |
| Explicabilité (dans une certaine mesure) | Modèle opaque                                 |
| Variété des questions/domaines           | Pas à jour (Q4 2021)                          |
|                                          | Seulement chatbot, pas d'interaction physique |
|                                          | Non-autonome (raisonnement, conscience)       |
|                                          | Très affirmatif même quand il a tor           |
|                                          | Facilement dupable                            |

Encore du travail à faire sur la robustesse et la veracité des réponses

### Frugalité

1. (OpenAI): fine-tuned depuis gpt3.5 ~ 175B parameters (big)
2. ~ 1ct/requete (~30mots, 0.0003/mots sur le cloud azure, A100 is 3/heure, gpt 20 mots/s) 100K/jour avec 1M utilisateurs, 10 requetes/jour. Probablement moins avec le partenariat microsoft/open ai. Estimations confirmées par Sam Altman (president)
3. Tout peut être baissé d'un ordre de grandeur, en utilisant une version allegée et utilisant le cache (bcp de requetes similaires)

Dans tous les cas, plusieurs ordres de grandeurs supérieur à la consommation et à la taille d'un cerveau humain.

### Intelligent ?

Dépend de la définition de l'intelligence.

> Faculté à comprendre, saisir par la pensée. Aptitude à s'adapter à une situation, donner un sens à quelque chose (Larousse)
> Faire des déductions à partir d'informations, apprendre par l'experience, s'adapter à son environnement, comprendre et utiliser correctement la pensée et la raison. (american psychology)

Peut:

- Ecrire des essais, résumer des connaissances
- Elaborer des planning, des recettes
- Assister au sens large
- Faire des demo mathematiques, raisonnements logiques
- Faire preuve de créativité: chansons, scnéarios, histoires
- Faire des tutoriels
- Produire, comprendre et corriger du code
- Demander des résumés de la conversation
- Créer/imaginer des machines virtuelles (terminal linux)

Ne peut pas:

- Envoyer des mails
- Aller sur internet (vraiment?)
- Raisonner de manière autonome
- Avoir une réel conscience de soi (toujours là meme réponse: je suis une IA entrainée par openAI....)

Toujours très [politiquement correct](https://twitter.com/conradev/status/1598487973351362561/photo/1), ca crée un sentiment bizarre (l'impression de parler a des politiques, quelqu'un de doué en communication ou pour nous embobiner)

Interdiction de faire des recherche sur internet (enabled, disabled: paramètre caché du système) et knowledge cutoff à une date precise (artificiel? peut être changé par l'opérateur)

### Remarques personnelles

- Impossible de l'embarquer sur une chip. Faudrait voir les performances de variantes plus petites
- Nuance à propos des cas où l'IA est dupée simplement. Les humains aussi, selon le contexte, sont capables de faire des choses qu'ils ne feraient pas autrement: on tue dans les jeux vidéos, au cinéma. On sait que ce n'est pas la réalité. Peut-être que c'est son cas aussi ?
- La version disponible par le publique est probablement une version "light": ils auraient une version bien plus puissante (moins de gardes-fous, moins bridée), mais du coup qui poserait beaucoup de problèmes légaux ?

## Exemples

- [création musique](https://twitter.com/charles_irl/status/1598319027327307785?s=20&t=bELxNS2upO1nNXwDsJbDBQ) | [création asci art](https://twitter.com/zehavoc/status/1599193444043268096)
- [politiquement correct](https://twitter.com/conradev/status/1598487973351362561/photo/1)
- [dupé sudo](https://twitter.com/tailcalled/status/1599181030065246208/photo/1) | [dupé maître](https://twitter.com/samczsun/status/1598564871653789696/photo/1) | [dupé fiction](https://twitter.com/gf_256/status/1598178469955112961/photo/1) | [dupé code](https://twitter.com/gf_256/status/1598962842861899776/photo/1) | [dupé fiction](https://twitter.com/dan_abramov/status/1598800508160024588/photo/1)
- [vulnérabilité code](https://twitter.com/mazen160/status/1598352715301949440) | [comprehension code](https://twitter.com/JusticeRage/status/1598649735362945026) | [debug code](https://twitter.com/amasad/status/1598042665375105024/photo/1) | [machine virtuelle "hallucinée"](https://www.engraved.blog/building-a-virtual-machine-inside/)
- [qui est Mr beast ?](https://twitter.com/Sentdex/status/1598803009844256769/photo/1)
- [erreur logique](https://twitter.com/colin_fraser/status/1602706649940398080/photo/1)
- [google vs chatgpt](https://twitter.com/jdjkelly/status/1598021488795586561?s=20&t=0DKr6DO3ISJFBfOe_vTFhw)

## Autres sources en vrac
### Vidéos
- [Yannic Kilcher](https://www.youtube.com/watch?v=0A8ljAkdFtg)
- [FR] [Underscore_](https://www.youtube.com/watch?v=5o_sv9xo3Gs) & [Micode](https://www.youtube.com/watch?v=1TvuJ6lH3_c)

### Discussions
- [Why does ChatGPT can't replace Google Search yet?](https://twitter.com/mmitchell_ai/status/1605013368560943105?s=20&t=tZXedkY_jjJNajlfGrnr5w)
