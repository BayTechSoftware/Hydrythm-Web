---
title: Rapports ICP et de santé
description: Importez un test ICP, suivez chaque élément dans le temps et lancez un bilan complet de votre système.
section: Cora Mobile
reviewed: 2026-10-12
order: 26
group: Intelligence
---

L’onglet **Intelligence** rassemble vos analyses de laboratoire et le suivi de votre aquarium sur la durée.

![L’onglet Intelligence](img/mobile-intelligence.webp "Téléchargez un ICP, exécutez un rapport de santé, et voyez ce qui a changé depuis le dernier.")

## Importer un test ICP

Touchez **Téléverser un ICP**, choisissez votre aquarium et ajoutez le résultat du laboratoire. Cora lit le rapport, enregistre chaque élément et le compare à vos tests précédents.

Vous n’avez rien à taper. Cora reconnaît les formats de laboratoire courants.

## Quelle adresse e-mail un laboratoire peut utiliser

Un laboratoire ou un résultat envoyé par e-mail retrouve votre compte grâce à l’adresse e-mail qu’il connaît. C’est l’e-mail de votre connexion, plus tout e-mail de labo que vous ajoutez dans **Réglages → la carte de votre compte → E-mails labo et ICP**.

1. Touchez **Ajouter un e-mail de labo** et saisissez l’adresse utilisée par votre laboratoire.
2. Touchez **Envoyer le code**. Cora envoie un code à 6 chiffres à cette adresse. Il expire au bout de 10 minutes.
3. Saisissez le code et touchez **Vérifier**. S’il n’est pas arrivé, touchez **Renvoyer le code**.

Vous pouvez ajouter jusqu’à 3 e-mails de labo. Chacun affiche **Vérifié** ou **En attente du code**, et **Supprimer** en retire un. Ensuite, les résultats envoyés à cette adresse n’arrivent plus sur votre compte. Une adresse qui appartient déjà à un autre compte Cora ne peut pas être ajoutée.

Si vous vous êtes connecté avec un e-mail Apple masqué, les laboratoires ne peuvent pas trouver votre compte. L’écran ICP affiche alors une carte, **Recevoir les résultats de labo automatiquement**, qui mène à ce réglage. Quand vous vous connectez avec Apple, choisissez **Partager mon e-mail** pour éviter le problème.

## Envoyer à Cora : les résultats transmis par un laboratoire ou par e-mail

Certains laboratoires peuvent envoyer un résultat directement à Cora. Un résultat ICP reçu par e-mail peut aussi arriver de cette façon. Vous n’avez alors rien à importer vous-même.

Quand un résultat arrive, une bannière s’affiche : *« Un résultat de laboratoire de {lab} est en attente. »* Touchez **Choisir un bac** et indiquez l’aquarium concerné. Cora ne peut pas le deviner. Une fois l’aquarium choisi, Cora y ajoute le rapport comme s’il avait été importé.

Le rapport affiche **Envoyé par {lab}** près de son en-tête. Vous le distinguez ainsi d’un rapport que vous avez importé vous-même.

:::note La première fois
La première fois qu’un résultat arrive par ce chemin, Cora affiche une courte explication, pour que vous ne le preniez pas pour une erreur.
:::

### Le premier résultat d’un nouveau laboratoire

La première fois qu’un laboratoire vous envoie un résultat, Cora vous demande de l’approuver avant de l’ajouter où que ce soit, même si vous n’avez qu’un seul aquarium. Vous voyez qui l’a envoyé et pouvez cocher **Faire confiance à ce laboratoire** pour sauter cette vérification la prochaine fois qu’un résultat viendra de lui.

Touchez **Approuver** pour le faire entrer, ou **Refuser** pour le supprimer sans l’ajouter à aucun aquarium. **Réglages → Laboratoires de confiance** liste chaque laboratoire auquel vous avez fait confiance de cette façon, et **Révoquer** en retire un, pour que son prochain résultat demande de nouveau votre approbation.

En cas de problème, consultez la page [Résolution de problèmes](/help/troubleshooting).

![Un rapport ICP](img/mobile-icp-report.webp "Chaque rapport porte un score et un résumé rédigé pour votre aquarium.")

## Ce que vous obtenez

D’abord, **un score** sur 100, avec un résumé en langage simple de ce qu’il veut dire pour votre système : votre type d’aquarium, son âge, votre population.

Le score compare vos résultats à leurs plages cibles, y compris les plages que vous avez réglées vous-même. Un seul résultat hors de sa plage bloque le score à 70 au plus. Il ne peut donc pas afficher **Sain**. Un résultat très hors plage le bloque à 40 au plus, même si tout le reste est bon. Sous le score, l’étiquette indique **Sain** de 71 à 100, **Attention requise** de 40 à 70 et **Critique** de 0 à 39. Les rapports de santé sont notés de la même façon.

Ensuite, **tous les éléments suivis** : les paramètres principaux, mais aussi les oligo-éléments et les contaminants. Cora enregistre les 71 éléments qu’un laboratoire peut rapporter, et la ligne que certains laboratoires appellent *Acidity* est le pH.

Sur chaque ligne d’élément, vous voyez la plage imprimée par le laboratoire, affichée comme *Plage du laboratoire*, à côté de la plage propre à Cora pour cet élément. Un élément pour lequel Cora n’a pas de plage de référence porte l’étiquette **Pas de plage Cora**. Le rapport indique combien d’éléments ont une plage Cora et évalue le reste d’après les connaissances générales en récif. Cora Assistant commente chaque élément testé, et son commentaire reste valable même sans plage Cora.

Si le laboratoire imprime *n.d.*, ou *non détecté*, pour un élément, Cora l’enregistre comme 0 et indique qu’il n’a pas été détecté.

:::note Le CO2 dissous n’est pas le CO2 de la pièce
Le **CO₂ dissous** d’un rapport ICP est le CO2 présent dans l’eau, en mg/L. C’est une mesure différente du CO2 de l’air de votre pièce, que mesure un moniteur d’air ambiant Inkbird en Beta. Les deux ont des plages différentes et ne sont jamais mélangés. Voir [Fonctions Beta](/help/mobile-beta).
:::

La carte « Depuis votre dernier ICP » montre **les plus gros changements** depuis le test précédent. C’est souvent le moyen le plus rapide de comprendre un nouveau rapport.

Enfin, touchez **Tendances** pour suivre un élément sur tous les tests que vous avez importés. C’est là que l’ICP devient vraiment utile, au-delà d’une simple photo à un instant donné.

:::tip Tout devient intéressant au deuxième test
Un ICP vous dit où vous en êtes. Le deuxième vous dit dans quelle direction vous allez, et c’est ce qui vous aide le plus à agir. Faites vos tests à un rythme régulier, et pas uniquement quand quelque chose ne va pas.
:::

## Un test d’eau osmosée ou d’eau source

Si vous importez un échantillon d’eau osmosée (RO/DI) ou d’une autre eau source, dites-le lors de l’import. Cora ne la note pas par rapport aux cibles de votre aquarium. Elle rend un verdict simple : l’eau est-elle assez propre pour servir ? Et elle garde ces chiffres hors des mesures de votre aquarium. Le rapport indique combien de résultats sont de l’eau source. Cora fait de même pour un sel fraîchement mélangé ou tout autre échantillon qui n’est pas de l’eau d’aquarium : elle dit à quoi l’échantillon ressemble et ne le note pas comme votre aquarium.

## Rapports de santé

Un **Rapport de santé** est un bilan plus complet de tout le système, à faire de temps en temps. Il examine ensemble tous les paramètres, toutes les sources, votre dosage, votre historique et vos derniers résultats ICP.

Touchez **Rapport de santé** et choisissez un aquarium. Le rapport met un moment à se préparer.

Lancez-en un quand le titre du jour ne suffit pas et que vous voulez un avis réfléchi : avant un gros changement, après un problème, ou toutes les quelques semaines pour faire le point.

## L’ICP face à vos sondes

Cora compare vos résultats de laboratoire avec ce que mesure votre équipement. Si votre sonde d’alcalinité indique 8,4 et votre ICP 7,6, c’est bon à savoir. Cora vous le montre, sans choisir l’un des deux en silence.

C’est l’un des grands intérêts d’un ICP dans Cora. Voyez-le comme **un troisième avis, pas un arbitre**. Les laboratoires ne donnent pas tous les mêmes résultats, et la manipulation, la conservation et le transport de l’échantillon jouent tous sur la mesure. Un ICP est un indice. Deux tests qui concordent valent bien plus qu’un seul. Si l’écart persiste, vérifiez la sonde, sans conclure pour autant qu’elle se trompe.

:::tip Changer de laboratoire ou de méthode
Changer de laboratoire, ou passer de l’ICP-OES à l’ICP-MS dans un même laboratoire, peut faire bouger vos résultats sans que rien ne change dans l’aquarium. Cora le signale quand il compare les tests. L’ICP-OES ne mesure pas les très faibles taux de chrome, d’étain, de nickel, de cuivre, de cobalt ou de sélénium. Un résultat **Sous le seuil de détection** pour ces éléments sur un test ICP-OES ne veut donc pas dire que votre aquarium n’en contient pas.
:::

## Votre quota

Les ICP et les rapports de santé sont décomptés selon votre forfait. La ligne sous les boutons montre ce que vous avez utilisé ce mois-ci.

En plus de votre forfait, Cora accepte au maximum 10 imports ICP par jour. Un import refusé pour cette raison ne compte pas dans les analyses ICP de votre forfait. Mais Cora Mobile n’affiche alors qu’une erreur d’import générale. Si vos imports échouent après en avoir fait beaucoup dans la journée, réessayez le lendemain.

## Où trouver vos rapports

L’écran Intelligence range les deux types à part : les résultats de laboratoire dans **Rapports ICP**, les bilans générés dans **Rapports de santé**. Chaque liste commence par le plus récent et affiche son score. Touchez un rapport pour le rouvrir en entier.
