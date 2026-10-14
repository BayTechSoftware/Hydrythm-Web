---
title: Rapports ICP et de santé
description: Importez le PDF d’un test ICP ou faites-le envoyer par votre laboratoire, lisez le score, suivez chaque élément dans le temps et lancez un rapport de santé de tout votre système.
section: Cora Mobile
reviewed: 2026-10-13
order: 33
group: Intelligence
twin: max-intelligence
---

L’onglet **Intelligence** est l’endroit où vivent vos résultats de laboratoire et vos rapports de long terme. Choisissez d’abord un aquarium en haut. Tout ce qui est à l’écran concerne cet aquarium.

![L’onglet Intelligence](img/mobile-intelligence.webp "Importer un ICP, lancer un rapport de santé, et voir ce qui a bougé depuis le dernier.")

## Importer un test ICP {#uploading-an-icp-test}

Cora lit le rapport PDF que votre laboratoire vous envoie. Téléchargez-le d’abord depuis l’e-mail ou le site de votre laboratoire. Les photos, scans et captures d’écran ne peuvent pas être lus.

1. Touchez **Téléverser un ICP**.
2. Choisissez votre laboratoire, ou laissez **Auto : détecter le laboratoire**. Cora a des conseils pour ATI, Fauna Marin, Modern Reef, Oceamo, Reef Zlements et Triton.
3. Indiquez ce qu’est l’échantillon : **Eau d’aquarium**, **Eau RO/DI**, **Mélange de sel** ou **Autre**. Seule l’eau d’aquarium met à jour votre tableau de bord et vos alertes.
4. Vérifiez la date de prélèvement de l’échantillon. Les laboratoires impriment la date d’analyse, alors Cora vous demande la vôtre et trace les résultats à cette date.
5. Touchez **Choisir le PDF** et sélectionnez le fichier.

Cela prend en général une à deux minutes. Gardez l’écran ouvert et le rapport s’ouvre dès qu’il est prêt. Vous n’avez rien à taper.

Vous pouvez aussi envoyer le PDF par e-mail à **icp@in.coraiq.tech**. Envoyez-le depuis votre e-mail de connexion ou un e-mail de laboratoire vérifié (voir plus bas), et il arrive comme un résultat envoyé par un laboratoire.

Si vous importez deux fois le même rapport, Cora vous montre celui que vous avez déjà et ne vous le décompte pas une deuxième fois.

:::note Cora a d’abord besoin de votre accord
L’analyse ICP envoie le rapport à l’IA, elle nécessite donc **Autoriser Cora Assistant à utiliser les données d’aquarium enregistrées**. Si c’est désactivé, Cora vous le demande avant l’import. Voir [ce que couvre l’interrupteur](/help/mobile-assistant#what-the-switch-covers).
:::

## Quel e-mail un laboratoire peut utiliser {#which-email-a-lab-can-use}

Un laboratoire ou un résultat envoyé par e-mail retrouve votre compte grâce à l’adresse e-mail qu’il connaît. C’est votre e-mail de connexion, plus tout e-mail de laboratoire que vous ajoutez sous **Réglages → carte de votre compte (Compte et abonnement) → E-mails labo et ICP**.

1. Touchez **Ajouter un e-mail de labo** et tapez l’adresse qu’utilise votre laboratoire.
2. Touchez **Envoyer le code**. Cora envoie un code à 6 chiffres à cette adresse. Il expire au bout de 10 minutes.
3. Saisissez le code et touchez **Vérifier**. Si vous ne l’avez pas reçu, touchez **Renvoyer le code**.

Vous pouvez ajouter jusqu’à 3 e-mails de laboratoire. Chacun indique **Vérifié** ou **En attente du code**, et **Retirer** en supprime un. Ensuite, les résultats envoyés à cette adresse n’arrivent plus sur votre compte. Une adresse qui appartient déjà à un autre compte Cora ne peut pas être ajoutée.

Si vous vous êtes connecté avec une adresse Apple masquée, les laboratoires ne peuvent pas trouver votre compte. L’écran ICP affiche une carte, **Recevoir les résultats de labo automatiquement**, qui vous mène à ce réglage. Quand vous vous connectez avec Apple, choisissez **Partager mon adresse e-mail** pour éviter le problème.

## Envoyer à Cora : les résultats qu’un laboratoire ou un e-mail vous livre {#send-to-cora-results-a-lab-or-an-email-delivers-for-you}

Certains laboratoires peuvent envoyer un résultat directement à Cora, et un PDF ICP que vous envoyez par e-mail arrive de la même façon. Vous n’avez rien à importer vous-même.

Si vous avez un seul aquarium, un résultat d’un laboratoire de confiance, ou un résultat que vous avez envoyé par e-mail, va directement dans cet aquarium. Avec plusieurs aquariums, vous verrez un bandeau : *« Un résultat de laboratoire de {lab} vous attend. »* Touchez **Choisir l'aquarium** et choisissez l’aquarium auquel il appartient. Cora ne peut pas le deviner tout seul.

Le rapport affiche **Envoyé par {lab}** près du haut, ou **Reçu par e-mail**, pour que vous le distinguiez d’un rapport que vous avez importé.

Si **Autoriser Cora Assistant à utiliser les données d’aquarium enregistrées** est désactivé, le résultat attend avec le message *Cora Assistant a besoin de votre accord pour le lire.* Donnez votre accord et il arrive.

:::note La première fois
La première fois qu’un résultat arrive de cette façon, Cora affiche une courte indication sur ce qui se passe, pour que cela ne ressemble pas à une erreur.
:::

### Le premier résultat d’un nouveau laboratoire

La première fois qu’un laboratoire vous envoie un résultat, Cora vous demande de l’approuver avant de l’ajouter où que ce soit, même si vous n’avez qu’un aquarium. Vous voyez qui l’a envoyé et pouvez cocher **Faire confiance à ce laboratoire** pour sauter cette vérification la prochaine fois qu’un résultat vient de lui.

Touchez **Approuver** pour le faire entrer, ou **Refuser** pour le supprimer sans l’ajouter à aucun aquarium.

### Laboratoires de confiance et ce que voient les laboratoires {#trusted-labs}

**Réglages → Cora Assistant → Laboratoires de confiance** liste chaque laboratoire auquel vous avez fait confiance. La liste apparaît dès que vous avez fait confiance à au moins un laboratoire. **Révoquer** retire un laboratoire, et son prochain résultat demandera à nouveau votre approbation.

**Partager l’analyse de Cora avec les laboratoires**, sur le même écran, décide de ce que voit un laboratoire après vous avoir envoyé un résultat. Activé, il peut voir les scores et l’analyse écrite de Cora. Désactivé, il voit seulement que le résultat a été livré. C’est désactivé jusqu’à ce que vous l’activiez. Le même interrupteur apparaît aussi sur un rapport envoyé par un laboratoire.

Si quelque chose ici ne fonctionne pas, voir [Résolution de problèmes](/help/troubleshooting).

## Ce que vous obtenez

![Un rapport ICP](img/mobile-icp-report.webp "Chaque rapport porte un score et un résumé écrit pour votre aquarium.")

Vous obtenez un score sur 100 et un résumé en langage simple de ce que cela signifie pour votre système, en tenant compte du type de votre aquarium, de son âge et de sa population.

Le score compare vos résultats avec leurs plages cibles, y compris les plages que vous avez réglées vous-même. Si un résultat est hors de sa plage, le score ne peut pas dépasser 70, il ne peut donc pas indiquer **Sain**. Si l’un est très hors plage, il ne peut pas dépasser 40, aussi bons que soient les autres. L’étiquette sous le score indique **Sain** de 71 à 100, **Attention requise** de 40 à 70 et **Critique** de 0 à 39. Les rapports de santé sont notés de la même façon.

Chaque élément est suivi, y compris les oligo-éléments et les contaminants en plus des paramètres principaux. Cora enregistre les 71 éléments qu’un laboratoire peut indiquer, et la ligne que certains laboratoires appellent *Acidity* est le pH.

Sur la ligne de chaque élément, vous voyez la plage imprimée par le laboratoire, affichée comme *Plage du laboratoire*, à côté de la plage propre à Cora pour cet élément. Un élément pour lequel Cora n’a pas de plage de référence porte l’étiquette **Pas de plage Cora**. Le rapport indique combien d’éléments ont une plage Cora et évalue les autres à partir des connaissances générales sur le récif. Cora Assistant commente chaque élément testé, et son commentaire vaut même quand il n’y a pas de plage Cora.

Si le laboratoire imprime *n.d.*, ou *non détecté*, pour un élément, Cora l’enregistre à 0 et indique qu’il n’a pas été détecté.

:::note Le CO2 dissous n’est pas le CO2 de la pièce
Le **CO₂ dissous** d’un rapport ICP est le CO2 dans l’eau, en mg/L. C’est une mesure différente du CO2 de l’air de votre pièce. Les deux ont des plages différentes et ne sont jamais mélangés.
:::

La carte **Depuis votre dernier ICP** montre ce qui a le plus changé depuis la dernière fois. C’est en général le moyen le plus rapide d’aborder un nouveau rapport.

Touchez **Tendances** pour voir n’importe quel élément sur tous les tests que vous avez importés. C’est là que l’ICP devient vraiment utile.

:::tip C’est au deuxième test que cela devient intéressant
Un ICP vous dit où vous en êtes. Le deuxième vous dit dans quelle direction vous allez, et c’est sur cela que vous pouvez agir. Testez à un rythme régulier, sans attendre que quelque chose tourne mal.
:::

## Un test d’eau RO/DI ou d’eau de départ

Si vous importez de l’eau RO/DI ou une autre eau de départ, choisissez **Eau RO/DI** à l’import. Cora ne la note pas par rapport aux cibles de votre aquarium. Il donne un verdict simple sur la propreté suffisante de l’eau pour l’utiliser, et garde ces chiffres en dehors des mesures de votre aquarium. Elle est enregistrée comme un rapport séparé. Cora fait de même pour **Mélange de sel** ou **Autre** : il dit à quoi ressemble l’échantillon et ne le note pas comme votre aquarium.

## Rapports de santé {#health-reports}

Un **Rapport de santé** est un bilan plus approfondi de tout le système, à faire de temps en temps. Il examine ensemble chaque paramètre, chaque source, votre dosage, votre historique et vos résultats ICP récents.

Touchez **Rapport de santé**, puis **Générer**. Cela prend en général une vingtaine de secondes. Comme l’analyse ICP, il nécessite **Autoriser Cora Assistant à utiliser les données d’aquarium enregistrées**.

Utilisez-le quand vous voulez un examen attentif de l’aquarium. Les bons moments sont avant un gros changement, après un problème, ou toutes les quelques semaines pour faire le point.

Un rapport ouvert a des boutons en haut pour l’exporter en PDF, partager un instantané de l’aquarium, ou le supprimer.

## L’ICP face à vos sondes

Cora compare vos résultats de laboratoire avec ce que signale votre équipement. Si votre sonde d’alcalinité indique 8,4 et votre ICP 7,6, vous voudrez le savoir, et Cora vous le montre sans choisir l’un des deux en silence.

C’est l’une des choses les plus utiles que fait un ICP dans Cora. Considérez-le comme un **troisième avis**. Ce n’est pas le mot de la fin. Les laboratoires diffèrent, et la façon dont un échantillon est manipulé, conservé et expédié fait bouger le résultat. Un seul ICP est un indice, et deux tests concordants comptent bien plus qu’un seul. Si l’écart persiste, vérifiez la sonde. Cela ne prouve pas que la sonde a tort.

:::tip Changer de laboratoire ou de méthode de test
Si vous changez de laboratoire, ou passez des tests ICP-OES aux tests ICP-MS d’un laboratoire, vos résultats peuvent bouger alors que rien n’a changé dans votre aquarium. Cora le signale quand il les compare. L’ICP-OES ne peut pas mesurer de très faibles quantités de chrome, d’étain, de nickel, de cuivre, de cobalt ou de sélénium. Un résultat **Sous le seuil de détection** pour ces éléments sur un test ICP-OES ne veut donc pas dire que votre aquarium n’en contient pas.
:::

## Votre quota

Votre forfait définit combien d’analyses ICP et de rapports de santé vous avez chaque mois. La ligne sous les boutons montre ce que vous avez utilisé. Les chiffres de chaque forfait sont dans [Forfaits et abonnements](/help/mobile-plans).

Quand vos analyses ICP sont épuisées, Cora vous montre d’abord les forfaits vers lesquels vous pouvez passer. Si vous préférez ne pas changer de forfait, il demande **Enregistrer les résultats sans l’analyse IA ?** Touchez **Enregistrer mes résultats** et Cora lit quand même le rapport et enregistre chaque valeur, donc les tendances, l’historique et vos mesures se mettent à jour normalement. Le score et l’analyse écrite restent verrouillés. Vous pourrez les lancer plus tard depuis le rapport lui-même dès que vous aurez une analyse ICP à utiliser.

En plus de la limite de votre forfait, Cora accepte jusqu’à 10 imports ICP par jour. Un import refusé pour cette raison ne consomme aucune des analyses ICP de votre forfait. Cora Mobile n’affiche toutefois qu’une erreur d’import générale : si les imports commencent à échouer après beaucoup d’imports dans la journée, réessayez demain.

## Où se trouvent les rapports

L’écran Intelligence sépare les deux sortes. Les résultats de laboratoire sont sous **RAPPORTS ICP** et les bilans générés sous **RAPPORTS DE SANTÉ**. Chaque liste affiche les plus récents en premier, avec leur score. Touchez-en un pour le rouvrir en entier.

Vous pouvez aussi y accéder depuis **Réglages** : ouvrez un aquarium, puis **Rapports ICP** ou **Rapports de santé**.
