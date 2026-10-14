---
title: Lire votre tableau de bord
description: Comment lire le tableau de bord de Cora, des widgets, de l’âge des mesures et des sources à la signification des couleurs et aux cartes qui vont et viennent.
section: Cora Mobile
reviewed: 2026-10-13
order: 6
group: Your dashboard
---

Le tableau de bord est une grille de **widgets** pour un aquarium. Chaque widget affiche une seule chose. C’est vous qui décidez de ce qu’il contient, comme décrit dans [Modifier votre tableau de bord](/help/mobile-dashboard-editing).

![Un tableau de bord Cora Mobile](img/mobile-dashboard.webp "L’en-tête de l’aquarium et la carte Reef Buddy, puis des jauges, des valeurs, des graphiques et des tuiles d’appareils.")

## L’en-tête de l’aquarium {#the-tank-header}

Chaque tableau de bord commence par :

- Le nom de l’aquarium, avec un petit symbole à côté. Touchez le nom pour renommer l’aquarium. C’est tout ce qu’il fait.
- **Nourrir**, uniquement sur un aquarium équipé d’un Neptune Apex. Il ouvre le **Mode nourrissage** avec les cycles **Nourrissage A** à **Nourrissage D** de votre Apex. Votre Apex décide de ce qui se met en pause et du moment où cela repart, selon votre configuration sur l’Apex. Pendant qu’un cycle tourne, le bouton indique lequel, par exemple **Nourrissage A**. Touchez-le et choisissez **Annuler le nourrissage** pour l’arrêter avant la fin. Loin de chez vous, un Cora Max de l’aquarium envoie la commande pour vous.
- L’icône de journal, qui ouvre le dernier briefing **Reef Buddy**.
- L’icône de partage, qui crée un instantané de l’aquarium. Voir [Partager votre aquarium](/help/mobile-sharing).
- La règle, qui ouvre les **Unités** de cet aquarium. Voir [Le profil de votre aquarium](/help/mobile-tank-profile#units).
- Le crayon à droite, qui ouvre [le profil de l’aquarium](/help/mobile-tank-profile).

:::note Trois commandes qui se ressemblent
Le nom de l’aquarium sert à le renommer. Le crayon à droite ouvre le **profil** de l’aquarium. Pour modifier le tableau de bord lui-même, touchez **Modifier le tableau de bord** juste sous les widgets.
:::

Si vous avez plusieurs aquariums, balayez vers la gauche ou la droite pour passer de l’un à l’autre. Voir [Gérer vos aquariums](/help/mobile-tanks).

## La carte Reef Buddy {#the-reef-buddy-card}

Au-dessus des widgets, une carte résume le dernier briefing. Elle affiche le titre, un score sur 100 dès que Cora a assez de données, sa date, et le nombre d’analyses et de mesures en dérive. Touchez-la pour ouvrir le briefing complet, ou fermez-la avec **×**. Une nouvelle carte apparaît avec le briefing suivant. Plus de détails dans [Reef Buddy](/help/mobile-reef-buddy).

## Comment lire un widget de paramètre {#how-to-read-a-parameter-widget}

Un widget de **paramètre mesuré** affiche toujours les trois mêmes choses aux mêmes endroits. Les tuiles d’appareils et de commandes, comme une prise, un doseur ou une pompe, affichent plutôt leur propre état, car il n’y a pas une seule mesure derrière elles.

La valeur est la mesure elle-même, en grand et au milieu.

L’âge se trouve en dessous ou à côté, sous la forme `maintenant`, `1 h` ou `2 j`. C’est le temps écoulé depuis que la source a confirmé cette valeur pour la dernière fois, et non depuis le dernier rafraîchissement de l’écran. Pour une sonde, c’est le dernier contact de son appareil : une mesure stable d’une sonde qui fonctionne reste donc fraîche même si le chiffre ne change pas. Pour un résultat de kit de test ou d’ICP, c’est le moment où vous avez fait le test. Un âge qui ne cesse d’augmenter sur une sonde veut dire que son appareil a cessé de transmettre.

Le badge de source est la petite marque à côté de l’âge. Il indique d’où vient le chiffre : une sonde, un contrôleur, un résultat de laboratoire, ou vous avec un kit de test. Touchez le widget pour voir la source écrite en toutes lettres, avec son historique récent.

:::note Pourquoi l’âge compte
Une mesure d’alcalinité parfaite d’il y a quatre jours n’est pas votre alcalinité d’aujourd’hui. Chaque valeur affiche son âge pour que vous voyiez vite la différence.
:::

## Couleurs {#colours}

Cora utilise peu de couleurs, et chaque couleur veut toujours dire la même chose :

| Couleur | Signification |
|---|---|
| Vert | Bien à l’intérieur de la plage de ce paramètre |
| Orange | Près d’une limite. **En général encore dans la plage**, dans son dernier dixième |
| Rouge | Au-delà de la limite, et il faut agir |
| Gris | Pas de verdict. Il n’y a pas de mesure récente, ou pas de plage utilisable pour juger |

:::note Orange veut en général dire "ça va pour l’instant, mais ça dérive"
L’orange est une marge. Une mesure dans sa plage mais dans ses derniers 10 % passe à l’orange, pour que vous voyiez la dérive tant qu’il est encore temps d’agir.

Il y a deux nuances.

**Une plage que vous avez réglée vous-même est une limite stricte.** Franchissez-la et le widget passe directement au rouge, sans marge orange. Une plage **fournie par Cora** est plus souple. La franchir affiche de l’orange pour les premiers 10 % au-delà de la limite, puis du rouge au-delà.

**Une limite d’un seul côté**, comme un plafond pour un contaminant ou un plancher pour un nutriment, n’est évaluée que sur sa limite haute. Le cuivre à zéro s’affiche donc en vert et ne passe pas à l’orange parce qu’il est près du bas de l’échelle.
:::

Un widget entouré d’orange ou de rouge demande votre attention. Tout le widget est entouré, pour que vous le repériez en faisant défiler.

Pour changer une plage, faites un appui long sur le widget. Plus de détails dans [Alertes et seuils](/help/mobile-alerts).

## Les cartes qui vont et viennent {#cards-that-come-and-go}

Certaines cartes n’apparaissent que quand il y a quelque chose à dire. La plupart se trouvent entre l’en-tête et les widgets.

| Carte | Quand elle apparaît | Que toucher |
|---|---|---|
| **Vous démarrez un nouvel aquarium ?** | Sur un aquarium sans aucune mesure. Une fois lancé, elle devient **Continuer le cyclage** | La carte, pour lancer le cyclage guidé. Voir [Parcours guidés](/help/mobile-journeys) |
| **Paramètres de l’aquarium** avec *Pas encore de mesures* | L’aquarium n’a encore aucune mesure | **Configurer l’aquarium** |
| *Impossible de joindre vos mesures : affichage des données en cache.* | Cora ne peut pas charger les dernières mesures, souvent faute de connexion | **Réessayer** |
| **Un résultat de laboratoire de {lab} vous attend.** | Un laboratoire a envoyé un résultat et Cora doit savoir à quel aquarium il correspond | **Choisir l'aquarium**. Voir [Rapports ICP et de santé](/help/mobile-icp-health) |
| Invitation du profil (**Débloquez des analyses plus fines**) | Le profil de l’aquarium est complet à moins de 80 % | La carte, pour continuer le profil |
| **Essai Cora Pro : 9 jours restants** | Les derniers jours de votre essai | La carte, ou **Garder Pro**. Voir [Forfaits et abonnements](/help/mobile-plans) |
| **Reef Buddy** | Un briefing est prêt | La carte |
| **Comment nourris-tu d'habitude ?** | Vous n’avez pas réglé de routine d’alimentation | **Configurer la routine** |
| *Les relevés Red Sea ne se mettent plus à jour.* | Rien ne lit les appareils Red Sea de cet aquarium | Voir [Alertes et seuils](/help/mobile-alerts) |
| **Enregistrez votre premier test d’eau** | Aucune mesure et aucun équipement associé, sous les widgets | La carte. Voir [Configurer Cora Mobile](/help/mobile-setup#the-first-test-card) |

## Sous les widgets {#below-the-widgets}

![Le bas du tableau de bord dans Cora Mobile](img/mobile-dashboard-foot.webp "Modifier le tableau de bord, les boutons Enregistrer les paramètres, Historique des paramètres et Alimentation, et les raccourcis vers les quatre zones de suivi.")

De haut en bas, vous trouvez :

- Une ligne qui indique quand le tableau de bord a été mis à jour et quelles sources il a utilisées, avec **Modifier le tableau de bord** à côté. Cela ouvre l’[éditeur de tableau de bord](/help/mobile-dashboard-editing).
- La carte **Enregistrez votre premier test d’eau**, sur un aquarium sans mesure et sans équipement associé.
- **Enregistrer les paramètres**, pour saisir à la main les mesures de vos kits de test.
- **Historique des paramètres**, pour ouvrir l’historique de n’importe quel paramètre qui a des données, même sans widget. Voir [Examiner un paramètre](/help/mobile-metric-detail).
- **Alimentation**, pour noter un repas qui sort de votre routine. Voir [Le journal](/help/mobile-journal).
- **Journal · Alertes · Entretien · Population**, des raccourcis vers ces zones pour cet aquarium.

## Toucher et appui long {#tapping-through}

Touchez n’importe quel widget de paramètre pour ouvrir son détail. Vous voyez tout l’historique sous forme de graphique, chaque source qui l’a signalé et votre plage d’alerte. De là, vous pouvez comparer les sources, exclure une mesure erronée ou noter l’entretien d’une sonde. Voir [Examiner un paramètre](/help/mobile-metric-detail).

Faites un **appui long** sur un widget de paramètre pour régler sa plage d’alerte directement depuis le tableau de bord.

## Si un widget n’a pas de valeur {#if-a-widget-has-no-value}

Un widget affiche une valeur dès qu’il en reçoit une. S’il est vide, c’est en général pour l’une de ces raisons :

- L’appareil est hors ligne. Vérifiez l’onglet **Appareils**.
- Le paramètre n’a pas encore de source. Notez-le à la main, ou connectez un équipement qui le mesure.
- Rien n’a jamais été signalé ni noté pour ce paramètre.

Une ancienne mesure ne disparaît pas simplement parce qu’elle est plus ancienne que la période du graphique. Elle reste sur le widget avec son âge : une valeur périmée a donc l’air périmée, pas manquante.

Pour tout le reste, voir [Résolution de problèmes](/help/troubleshooting#a-widget-shows-no-value).
