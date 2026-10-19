---
title: L’écran d’accueil de Cora Max
description: Ce que veulent dire la barre du haut, l’étiquette d’état, les étiquettes d’alerte, le menu de l’aquarium et le tableau de bord sur Cora Max, et comment changer d’aquarium et ouvrir Prises et nourrissage.
section: Cora Max
reviewed: 2026-10-13
order: 2
group: Getting started
twin: mobile-tour
---

Cette page explique ce que vous voyez sur Cora Max. Il affiche un aquarium à la fois, avec les mesures en direct sur tout l’écran pour que vous puissiez les lire depuis l’autre bout de la pièce.

![L’écran d’accueil de Cora Max avec les jauges, valeurs, graphiques et tuiles d’appareils d’un aquarium sous la barre du haut](img/max-home.webp "Le tableau de bord d’un aquarium remplit l’écran, avec la barre du haut au-dessus.")

## La barre du haut {#the-top-bar}

![La barre du haut de Cora Max](img/max-topbar.webp "La barre du haut, numérotée de gauche à droite comme la liste ci-dessous.")

De gauche à droite :

1. **L’icône de grille** ouvre [la Pièce du récif](/help/max-reef-room), la vue d’ensemble de tous les aquariums affichés par cet écran.
2. **Le nom de l’aquarium**, avec une petite flèche. Touchez-le pour ouvrir le **menu de l’aquarium**, qui contient tous les écrans de l’aquarium affiché. La liste complète est plus bas.
3. **Les étiquettes d’alerte** montrent ce qui demande votre attention en ce moment : mesures hors plage, pannes d’appareils, doses manquées ou consommables bas. Touchez une étiquette pour ramener cette alerte au milieu de l’écran. S’il y en a plus que la place ne le permet, vous verrez **+2** (ou le nombre qui convient). Touchez-le pour voir toutes les alarmes actives.
4. **L’horloge**. Vous pouvez la masquer avec **Afficher l’horloge** dans **Paramètres → Paramètres Cora Max**.
5. **L’étiquette d’état** indique ce que fait cet écran en ce moment. Vert veut dire que tout va bien, bleu qu’il est occupé, orange qu’il faut regarder, et rouge signale une panne. Tous les états sont listés plus bas.
6. **La batterie et le Wi-Fi**.
7. **L’icône des appareils** ouvre **Appareils**, filtré sur cet aquarium. Un aquarium sans appareil ne l’affiche pas.
8. **L’icône Reef Buddy** ouvre le briefing du jour. Un point veut dire que vous ne l’avez pas encore lu.
9. **L’icône Cora Assistant** lance une conversation vocale.
10. **La roue dentée** ouvre les réglages.

:::warning Cora Assistant commence à écouter tout de suite
Toucher l’icône Cora Assistant lance une session vocale en direct. Si vous vouliez les réglages, c’est la roue dentée tout à droite.
:::

### Ce que veut dire l’étiquette d’état {#what-the-status-pill-means}

| Étiquette | Signification |
|---|---|
| **En ligne** | Cet écran collecte vos mesures, et elles sont à jour |
| **Cloud** | Un autre Cora collecte les mesures de cet aquarium et cet écran les affiche. Elles sont tout aussi à jour qu’avec **En ligne**. Si vous avez plusieurs Cora, celui qui ne collecte pas affiche ceci |
| **Interrogation de l’Apex**, **Voix active** | Occupé à quelque chose en ce moment (bleu) |
| **Interrogation désactivée** | La collecte est désactivée pour cet aquarium. Vous pouvez la réactiver dans Cora Mobile |
| **Mise à jour** | La collecte est en pause pendant l’installation d’une mise à jour |
| **Obsolète** | Les mesures n’arrivent plus. L’écran affiche les dernières reçues |
| **Nouvelle tentative Apex dans 12 s** | Votre Apex n’a pas répondu. Cora Max réessaie à la fin du compte à rebours |
| **Échec de la synchronisation cloud** | Votre Apex a répondu, mais ses mesures n’ont pas pu être enregistrées dans Cora Cloud, donc le tableau de bord prend du retard. Cora Max continue d’essayer |
| **Enregistrement cloud refusé** | Cora Cloud refuse d’enregistrer une partie des données de cet écran. Rien ne va mal avec votre aquarium ni avec Cora Max, et rien n’est à changer sur cet écran. La solution est une mise à jour de Cora Cloud. Ouvrez **Paramètres → Paramètres Cora Max** et faites défiler jusqu’à la section **État**, où la ligne **Enregistrement cloud** indique quelles données sont concernées. Puis [contactez l’assistance](/support.html) |
| **Hors ligne** | Pas de connexion. L’écran affiche les dernières données reçues |
| **Hors ligne, nouvelle tentative dans 45 s** | Votre réseau fonctionne, mais Cora Cloud est injoignable depuis plus de 30 secondes. Cora Max se reconnecte tout seul, et le compte à rebours indique quand il réessaie |
| **Cora principal hors ligne** | Cet écran est un deuxième Cora Max pour cet aquarium, et le **Cora Max principal** (celui épinglé pour lire l’équipement de cet aquarium) s’est déconnecté. Cet écran continue d’afficher les dernières données qu’il a jusqu’au retour du principal ou jusqu’à ce que vous choisissiez un autre Cora Max principal. Plus de détails dans [Plus d’un appareil Cora](/help/mobile-multi-device) |
| **Mot de passe Apex** | Votre Apex a refusé le mot de passe enregistré. Consultez [Résolution de problèmes](/help/troubleshooting) |

:::note Comment fonctionne le compte à rebours
Cora Max essaie de se reconnecter à un rythme régulier. Il attend environ 15 secondes après la première coupure, puis encore 15 secondes, puis 30 secondes deux fois, puis une fois par minute jusqu’à ce que cela passe. Il n’abandonne jamais. **Hors ligne, nouvelle tentative dans 45 s** est normal.
:::

## Le tableau de bord {#the-dashboard}

Le reste de l’écran est le tableau de bord, une grille fixe qui garde chaque widget visible. Il ne défile pas.

Les widgets fonctionnent comme sur votre téléphone, mais assez grands pour être lus à quelques pas. Ce que montre chaque forme est dans la [Référence des widgets](/help/mobile-widgets). Pour changer ce qu’il y a sur le tableau de bord, voir [Modifier le tableau de bord Cora Max](/help/max-dashboard-editing).

Chaque widget avec un paramètre mesuré affiche son **âge** et sa **source**, comme sur votre téléphone. Un nombre avec `2 j` à côté a deux jours. Les tuiles d’appareils et de commandes affichent plutôt leur propre état.

### Quand l’écran est atténué {#when-the-screen-is-dimmed}

Après le délai **Atténuer après** sans contact, l’écran s’atténue. Votre premier appui ne fait que le réveiller, pour qu’il ne puisse pas actionner une commande par accident. Touchez à nouveau pour utiliser l’écran.

## Le menu de l’aquarium {#the-tank-menu}

![Le menu de l’aquarium ouvert par-dessus le tableau de bord, avec Enregistrer les paramètres, Journal, Reef Buddy et les autres écrans de l’aquarium](img/max-menu.webp "Le menu de l’aquarium, ouvert depuis le nom de l’aquarium dans la barre du haut.")

Touchez le nom de l’aquarium pour ouvrir le menu de l’aquarium affiché.

| Élément | Ouvre |
|---|---|
| **Enregistrer les paramètres** | Saisir des mesures de kits de test avec le clavier à l’écran |
| **Journal** | [Le journal](/help/max-records) de cet aquarium |
| **Reef Buddy** | Le dernier [briefing](/help/max-intelligence) |
| **Rapports de santé** | Les bilans de santé |
| **Entretien** | La [liste des tâches](/help/max-records) |
| **Rapports ICP** | Les [résultats de laboratoire](/help/max-intelligence) importés |
| **Historique des paramètres** | Choisir n’importe quel paramètre qui a des données et ouvrir son [graphique](/help/max-intelligence) |
| **Seuils d’alerte** | La [plage saine](/help/max-alerts) de chaque paramètre de cet aquarium |
| **Population** | L’inventaire de cet aquarium, en lecture seule sur cet écran |
| **Activité** | [Chaque prise, nourrissage et dosage](/help/max-activity), et ce qui s’est passé |
| **Disposition du tableau de bord** | [Disposer les widgets de cet écran](/help/max-dashboard-editing) |
| **Unités** | Les unités d’affichage des mesures de cet aquarium |
| **Paramètres de l’aquarium** | L’écran complet des réglages de cet aquarium |

## Changer d’aquarium {#switching-tanks}

Touchez l’**icône de grille** tout à gauche de la barre du haut pour aller à [la Pièce du récif](/help/max-reef-room), puis ouvrez l’aquarium voulu. Vous pouvez aussi balayer vers la gauche ou la droite sur le tableau de bord. Chaque aquarium a sa propre disposition, donc tout l’écran change quand vous passez de l’un à l’autre.

## Le tiroir Prises et nourrissage {#the-outlets-feed-drawer}

Sur un aquarium équipé d’un Neptune Apex, une petite étiquette **Prises et nourrissage** se trouve en bas du tableau de bord. Touchez-la, ou balayez vers le haut n’importe où sur le tableau de bord, pour ouvrir **Commandes**.

- **NOURRISSAGE** lance l’un des cycles de nourrissage de votre Apex avec **A**, **B**, **C** ou **D**. **Annuler** l’arrête avant la fin.
- Les **PRISES** peuvent chacune passer de Auto à Off ou On.

Il liste les prises et les cycles de nourrissage que vous avez choisis pour ce tableau de bord, ou tous si vous n’en avez choisi aucun. Plus de détails dans [Prises et commandes](/help/max-controls).

:::warning Ce tiroir commande de vrais équipements
Une commande part dès que vous touchez, mais l’envoyer ne veut pas dire qu’elle est faite. Elle revient Confirmé, Non confirmé, Refusé ou Aucun changement, et vous voyez lequel dans [Activité](/help/max-activity). Le mode nourrissage est la façon sûre de couper le brassage pour nourrir, car il remet tout en marche tout seul. Un Off manuel reste éteint jusqu’à ce que vous le changiez.
:::

## Si quelque chose semble anormal {#if-something-looks-out-of-place}

Si les mesures semblent périmées, ou si l’étiquette d’état est orange ou rouge, commencez par [Résolution de problèmes](/help/troubleshooting).
