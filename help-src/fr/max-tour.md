---
title: L’écran d’accueil de Cora Max
description: Ce que signifie tout ce qui se trouve sur l’affichage Cora Max : la barre supérieure, la grille du tableau de bord, et le tiroir des prises.
section: Cora Max
reviewed: 2026-09-27
order: 2
group: Getting started
---

Cora Max affiche un aquarium à la fois, remplissant l’écran de mesures en direct que vous pouvez lire depuis l’autre bout de la pièce.

![L’écran d’accueil de Cora Max](img/max-home.webp "Un aquarium, remplissant l’écran.")

## La barre supérieure

De gauche à droite :

- **L’icône de grille** ouvre la Pièce du récif, la vue d’ensemble de chaque aquarium que cet écran affiche
- **Le nom de l’aquarium**, avec un chevron. Le toucher ouvre le **menu de l’aquarium** : chaque écran pour l’aquarium affiché, de l’enregistrement d’un résultat de test à l’arrangement du tableau de bord. La liste complète est ci-dessous.
- **Pastilles d’alerte** : tout ce qui est actuellement hors plage, avec un **+n** quand il y en a plus que ce qui tient. Touchez pour les voir toutes.
- **L’horloge**
- **La pastille d’état** : ce que cet écran fait actuellement. Vert est en bon état, orange demande attention, rouge est une panne. Le vocabulaire complet est ci-dessous.
- **Batterie et Wi-Fi**
- **L’icône des appareils** : tout ce qui est connecté, et comment cela se comporte
- **L’icône Reef Buddy** : ouvre le briefing d’aujourd’hui. Un point signifie que le briefing n’a pas encore été lu.
- **L’icône Cora Assistant** : démarre une conversation vocale
- **La roue dentée** : réglages

### Ce que signifie la pastille d’état

| Pastille | Signification |
|---|---|
| **En ligne** | Cet écran collecte vos mesures, et elles sont actuelles |
| **Cloud** | Un autre Cora collecte les mesures de cet aquarium et cet écran les affiche. Tout aussi actuel qu’**En ligne** ; avec plus d’un Cora, l’écran qui ne fait pas la collecte affiche ceci |
| **Interrogation de l’Apex**, **Voix active** | Travaille sur quelque chose en ce moment |
| **Interrogation désactivée** | La collecte est désactivée pour cet aquarium. Vous pouvez la réactiver depuis Cora Mobile |
| **Mise à jour** | La collecte est en pause pendant l’installation d’une mise à jour |
| **Obsolète** | Les mesures ont arrêté d’arriver. L’écran affiche la dernière qu’il a reçue |
| **Nouvelle tentative Apex dans 12 s** | Votre Apex n’a pas répondu. Cora Max réessaie quand le compte à rebours se termine |
| **Échec de la synchronisation cloud** | Votre Apex a répondu, mais ses mesures n’ont pas pu être enregistrées sur Cora Cloud, donc le tableau de bord prend du retard. Cora Max continue de réessayer |
| **Hors ligne** | Aucune connexion. L’écran affiche les dernières données qu’il a reçues |
| **Hors ligne, nouvelle tentative dans 45 s** | Votre réseau fonctionne, mais Cora Cloud est inaccessible depuis plus de 30 secondes. Cora Max se reconnecte lui-même ; le compte à rebours est le temps avant sa prochaine tentative |
| **Cora principal hors ligne** | Cet écran est un second Cora Max pour cet aquarium, et le **Cora Max principal** (celui épinglé pour interroger l’équipement de cet aquarium) est passé hors ligne. Cet écran continue d’afficher les dernières données qu’il a jusqu’à ce que le principal revienne, ou jusqu’à ce que vous choisissiez un autre Cora Max principal. Voir [Plus d’un appareil Cora](/help/mobile-multi-device) |
| **Mot de passe Apex** | Votre Apex a rejeté le mot de passe enregistré. Voir [Résolution de problèmes](/help/troubleshooting) |

:::note Comment fonctionne le compte à rebours de nouvelle tentative
Cora Max essaie de se reconnecter à un rythme fixe : environ 15 secondes après la première coupure, 15 secondes après cela, puis deux fois à 30 secondes, puis une fois par minute jusqu’à ce qu’il réussisse. Il ne réessaie pas instantanément et n’abandonne pas ; un écran affichant **Hors ligne, nouvelle tentative dans 45 s** fait exactement ce qu’il devrait.
:::

:::warning Cora Assistant commence à écouter immédiatement
Toucher l’icône Cora Assistant démarre une session vocale en direct. Si vous vouliez ouvrir les réglages, c’est la roue dentée tout à droite.
:::

## Le tableau de bord

Le reste de l’écran est le tableau de bord : une grille fixe de widgets, tous visibles à la fois. Le tableau de bord Cora Max ne défile pas.

Les widgets fonctionnent comme sur votre téléphone, à une taille que vous pouvez lire en vous tenant en retrait. Voir **[Référence des widgets](/help/mobile-widgets)** pour ce que montre chaque forme, et **[Modifier le tableau de bord Cora Max](/help/max-dashboard-editing)** pour changer ce qui s’y trouve.

Chaque widget affichant un paramètre mesuré porte son **ancienneté** et sa **source**, tout comme sur le téléphone. Un chiffre avec `2d` à côté a deux jours, et est affiché comme tel. Les tuiles d’appareil et de commande affichent leur propre état à la place.

## Le menu de l’aquarium

![Le menu de l’aquarium](img/max-menu.webp "Tout pour l’aquarium actuel, depuis le nom de l’aquarium dans la barre supérieure.")

Toucher le nom de l’aquarium ouvre le menu pour l’aquarium actuellement à l’écran :

| Élément | Ouvre |
|---|---|
| **Enregistrer les paramètres** | Saisissez des mesures de test en kit sur le clavier à l’écran |
| **Journal** | [Le journal](/help/mobile-journal) pour cet aquarium |
| **Reef Buddy** | Le [briefing](/help/mobile-reef-buddy) actuel |
| **Rapports de santé** | Les évaluations de santé |
| **Entretien** | La [liste des tâches](/help/mobile-maintenance) |
| **Rapports ICP** | Les [résultats de laboratoire](/help/mobile-icp-health) téléchargés |
| **Alertes** | La bande saine pour chaque mesure de cet aquarium |
| **Population** | L’[inventaire](/help/mobile-livestock) de cet aquarium, en lecture seule sur cet écran |
| **Activité** | [Chaque prise, nourrissage et dosage](/help/max-activity), et ce qui en est résulté |
| **Disposition du tableau de bord** | [Arranger les widgets sur cet écran](/help/max-dashboard-editing) |
| **Réglages de l’aquarium** | L’écran de réglages complet pour cet aquarium |

## Changer d’aquarium

Utilisez l’**icône de grille** tout à gauche de la barre supérieure pour atteindre [la Pièce du récif](/help/max-reef-room), puis ouvrez l’aquarium que vous voulez. Chaque aquarium garde sa propre mise en page de tableau de bord, donc tout l’écran change quand vous passez de l’un à l’autre.

## Le tiroir Prises et nourrissage

L’onglet en bas de l’écran tire un tiroir avec chaque prise du système et les commandes de nourrissage.

- **Prises** : chacune commutable entre Auto, Éteint et Allumé
- **Nourrir** : met en pause l’équipement approprié pour un nourrissage et remet tout en place ensuite

:::warning Ce tiroir contrôle un équipement réel
Tout ce qu’il contient agit sur un équipement réel. Une commande est envoyée au moment où vous touchez, mais *envoyé* n’est pas *fait* ; elle revient Confirmée, Non confirmée, Refusée ou Aucun changement, et [Activité](/help/max-activity) est où vous voyez laquelle. Le mode nourrissage est la façon sûre de mettre le débit en pause pour le nourrissage, car il restaure tout lui-même ; un Éteint manuel reste éteint jusqu’à ce que vous le changiez à nouveau.
:::

## Si quelque chose semble anormal

Si les mesures semblent périmées, ou si la pastille d’état est orange ou rouge, commencez par **[Résolution de problèmes](/help/troubleshooting)**.
