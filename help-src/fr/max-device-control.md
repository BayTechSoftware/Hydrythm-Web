---
title: Contrôler l’équipement depuis Cora Max
description: Les pages d’appareils sur Cora Max pour Neptune Apex, Trident et DŌS, Red Sea ReefBeat, Jecod et AquaWiz, marque par marque.
section: Cora Max
reviewed: 2026-10-18
order: 6
group: Equipment
twin: mobile-device-control
---

Cette page explique ce que vous pouvez voir et faire sur la page de chaque appareil sur Cora Max, marque par marque. Cora Max joint le même équipement que votre téléphone. Ouvrez la page d’un appareil depuis l’icône des appareils dans la barre du haut, depuis **Réglages → Appareils**, ou en touchant une tuile d’appareil sur le tableau de bord.

![La page d’un Apex sur Cora Max avec ses boutons de nourrissage et ses prises](img/max-device-control.webp "Feed A à D et Annuler, puis les prises, disposés pour un écran mural.")

:::warning Ces commandes agissent sur un équipement en fonctionnement
Il n’y a ni aperçu ni annulation. Une commande part dès que vous touchez, mais l’envoyer ne veut pas dire qu’elle est faite. Elle revient **Confirmé**, **Non confirmé**, **Refusé** ou **Aucun changement**, et vous voyez lequel dans [Activité](/help/max-activity).
:::

Vous ajoutez, attribuez et retirez l’équipement sur votre téléphone. Cora Max l’affiche dès que votre compte l’a. Voir [Connecter votre équipement](/help/mobile-connections).

## Ce qui a une page {#what-has-a-page}

| Appareil | Affiche |
|---|---|
| **Neptune Apex** | Sondes et prises, et vous pouvez commander chaque prise |
| **Trident** | L’état du test, les niveaux de réactifs et de déchets, et un bouton pour lancer un test |
| **DŌS**, y compris le DŌS QD | Le dosage, le programme, l’autonomie et le volume du réservoir de chaque tête (avec pause, remplissage, dose immédiate et une mesure unique de vingt secondes) |
| **Red Sea ReefBeat** | Ce que l’appareil possède : têtes de dosage, réservoir, jours de rouleau, mode de pompe, plus un éditeur complet du plan ReefDose, et les réglages ReefMat |
| **Jecod** | Le mode et l’intensité de la pompe, et son programme journalier |
| **AquaWiz** | Pas de page à lui. Il est listé dans **Appareils**, et ses mesures vont sur le tableau de bord |

La plupart des pages d’appareils ont un crayon pour renommer l’appareil. Le nouveau nom apparaît aussi sur votre téléphone. Plus de détails dans [Appareils et état des appareils](/help/max-devices).

## Neptune Apex {#neptune-apex}

La page de l’Apex liste vos sondes et vos prises, avec vos cycles de nourrissage en haut. Chaque prise passe de **Auto** à **Off** ou **On**, et les prises avec un cadenas demandent une confirmation. Le fonctionnement des trois états et du mode nourrissage est expliqué dans [Prises et commandes](/help/max-controls).

Vous pouvez aussi atteindre les prises depuis le tiroir **Prises et nourrissage** en bas du tableau de bord. Il liste les prises activées pour ce tableau de bord (ou toutes, si vous n’en avez choisi aucune).

Un grand Apex avec plusieurs modules affiche toutes ses prises et sondes. Les têtes DŌS n’apparaissent jamais dans la liste des prises, vous ne pouvez donc pas en allumer une là et la laisser tourner. Dosez depuis la page de la tête.

### Trident {#trident}

La page du Trident affiche l’état du test et les niveaux de réactifs et de déchets. Vous pouvez lancer un test d’ici, et régler une alerte de réapprovisionnement avec **Paramètres d’alerte**.

## Têtes DŌS {#dos-heads}

Vous devez mesurer une tête DŌS une fois avant que Cora ne dose avec elle à la main. **Mesurer pour doser** fait tourner la tête vingt secondes dans un récipient gradué, et vous saisissez la quantité sortie. Cora garde une mesure par tête et utilise la plus récente, quel que soit le Cora Max qui l’a prise. La page de la tête indique où et quand elle a été mesurée.

Après une dose manuelle, une tête que vous aviez mise sur Off dans Apex Fusion reste sur Off. Toute autre tête repasse sur Auto.

Un DŌS n’a pas de capteur de niveau et continue de doser depuis un réservoir vide. Réglez une alerte de réapprovisionnement avec **Paramètres d’alerte** sur la page du DŌS. Plus de détails dans [Alertes des doseurs](/help/mobile-device-control#doser-alerts).

### À quoi sert une tête {#what-a-head-is-used-for}

Dans la feuille de réglages d’une tête, vous pouvez régler son **type d’usage**. Les options sont **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture** ou **Appoint**, et **Autre**. Le type d’usage change deux choses.

- La taille du réservoir qu’elle peut suivre. Chaque type d’usage peut suivre un réservoir jusqu’à 1 000 litres. Au-delà du compteur de 150 litres de l’Apex, Cora suit lui-même le volume, et Cora remet le compteur de l’Apex à zéro tous les 100 litres.
- Si elle peut faire une grosse dose à la main. Les têtes Complément et Nourriture gardent le plafond actuel, petit et prudent. Tout autre type d’usage peut avoir sa propre limite de **Dosage manuel maximal**, jusqu’à un plafond absolu de 10 litres, et sa propre **Limite quotidienne pour les automatisations et l’Assistant**. Une grosse dose à la main demande aussi d’activer **Doses importantes** dans les réglages de la tête, désactivé par défaut. Ne l’activez qu’après avoir regardé la première grosse dose se faire à l’aquarium.

Vous pouvez associer une paire de changement d’eau (entrée d’eau salée neuve, sortie d’eau ancienne) comme **Tête associée** et régler une valeur d’**Alerte d’équilibre au-dessus de**. Si les totaux du jour des deux têtes s’écartent de plus que cette valeur, Cora vous prévient. Une paire déséquilibrée veut en général dire qu’un côté ne pompe pas comme il devrait.

### Si une grosse dose est interrompue {#if-a-large-dose-is-interrupted}

Une grosse dose change pendant un moment ce que fait la tête sur l’Apex, puis remet son programme normal. Si la connexion tombe en cours de route, Cora Max affiche un bandeau sur la page de cette tête : *« Un dosage important sur [tête] ne s’est pas terminé proprement. Cora continue d’essayer de remettre son programme en place ; vérifiez-le dans Apex Fusion. »*

Vérifiez vous-même la tête dans Apex Fusion, puis touchez **J’ai vérifié la tête dans Fusion** pour effacer le bandeau. Ne le faites qu’après avoir confirmé que c’est le programme propre de la tête qui tourne, et non le programme de dosage de Cora.

Si le bandeau ne s’efface pas, ou revient sans cesse, consultez [Résolution de problèmes](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Chaque appareil Red Sea a une page adaptée à ce qu’il fait : têtes et réservoirs ReefDose, réservoir ReefATO+, jours de rouleau ReefMat et vitesses de pompe ReefRun. Les alertes de consommables des têtes ReefDose, du réservoir ReefATO+ et du rouleau ReefMat se règlent avec **Paramètres d’alerte** sur la page de l’appareil.

Si un appareil Red Sea s’arrête de lui-même, sa page vous dit ce qui ne va pas et place la solution juste à côté. C’est **Reprendre**, **Effacer l’urgence**, **Capteur nettoyé**, **J’ai déjà chargé un nouveau rouleau**, ou **Réinitialiser** pour une tête de dosage.

Un plan ReefDose et l’avance programmée, le modèle, la position et Nouveau rouleau du ReefMat fonctionnent ici de la même façon que sur votre téléphone. [Contrôler votre équipement](/help/mobile-device-control) donne les détails.


## Jecod {#jecod}

La page Jecod affiche le mode et l’intensité de la pompe, et vous pouvez changer les deux. Son état s’affiche dans la ligne de titre, à côté du nom de la pompe. La barre du haut contient l’interrupteur, le motif en cours et **Nourrissage** avec quatre pastilles : **5**, **10**, **15** et **30** min. Touchez une pastille pour mettre la pompe en pause pendant ce temps. Sous la barre, deux cartes :

- **Identique toute la journée** : touchez un réglage pour l’exécuter toute la journée.
- **Programme** : le graphique de la journée et la liste des plans, avec **maintenant** sur le plan en cours. **Modifier** ouvre l’éditeur, et le menu ⋮ contient **Copier le programme vers…**, **Enregistrer le programme sous…** et **Programmes enregistrés…**.

La carte en cours a un contour et une pastille **En marche**. Une pompe Jecod n’a pas de bouton **Terminer le nourrissage**. Toute pompe Jecod qui peut se mettre en pause pour le nourrissage affiche les pastilles **5**, **10**, **15** et **30** min. Sur une Jecod Pro, la tuile Nourrissage des types de vague fait la même chose, pour 10 minutes. Par un Cora Max éloigné de l’aquarium, une pompe Jecod ne se nourrit que 10 minutes. Une pompe qui ne peut pas se nourrir pour le moment en donne la raison en une courte ligne sous les pastilles, et un appui long affiche la phrase complète. Un nourrissage lancé depuis le téléphone est aussi terminé par le Cora Max : à la fin du temps, la pompe revient à son programme.

Vous pouvez écrire les programmes journaliers des pompes Jecod au mur comme sur votre téléphone. L’éditeur est le même, avec un graphique de la journée, une liste de périodes et une rangée d’actions. Plus de détails dans [Programmer l’équipement](/help/mobile-schedules).

## AquaWiz {#aquawiz}

Un AquaWiz KH Controller n’a pas de page à lui sur Cora Max. Il est listé dans **Appareils**, où vous pouvez le renommer, et ses mesures s’affichent sur le tableau de bord comme n’importe quelle autre source. Un Cora Max sur le même aquarium peut aussi le lire toutes les heures quand il peut atteindre le contrôleur. Configurez-le et gérez-le sur votre téléphone, voir [Connecter votre équipement](/help/mobile-connections).


## Consommables {#consumables}

Vous réglez ici les seuils de réapprovisionnement (réactif, réservoirs de dosage, réservoirs d’osmolateur) sur la page de l’appareil lui-même, comme sur votre téléphone. Plus de détails dans [Consommables](/help/mobile-consumables).

## Noter et calculer devant l’aquarium {#logging-and-calculating-at-the-tank}

Deux choses sont souvent plus faciles au mur que sur un téléphone.

- **Enregistrer les paramètres** vous permet de taper les résultats de test avec le clavier à l’écran. C’est dans le menu de l’aquarium.
- **Calculateur de dose** calcule une correction à partir du volume de l’aquarium et de la concentration de vos produits. Ouvrez-le depuis la page d’un paramètre. Il utilise le même volume et les mêmes concentrations que votre téléphone : une dose calculée ici correspond donc à une dose calculée là-bas. Plus de détails dans [Dosage](/help/mobile-dosing).

## Sur un deuxième Cora Max {#on-a-second-cora-max}

Quand plusieurs Cora Max affichent un aquarium, l’un d’eux lit l’équipement de cet aquarium. Les pages d’appareils l’appellent le Cora Max de l’aquarium. Les autres peuvent toujours ouvrir les pages d’appareils, et une étiquette d’état **Cloud** veut dire que vous êtes sur l’un d’eux. Ils affichent ce que le Cora Max de l’aquarium a lu en dernier et il y a combien de temps. Chaque commande passe par Cora Cloud jusqu’au Cora Max de l’aquarium, qui l’exécute.

Quelques fonctions ne marchent que sur le Cora Max de l’aquarium.

- **Mesurer pour doser** et **Remesurer** n’apparaissent que là. Une fois une tête mesurée, **Doser maintenant** fonctionne depuis n’importe quel Cora Max.
- Vous ne pouvez changer un programme Jecod depuis un autre Cora Max que si le Cora Max de l’aquarium a lu la pompe dans la dernière heure, et jamais pour une pompe qui ne communique qu’en Bluetooth. Un seul **Appliquer à la pompe** depuis là envoie au plus 12 changements, alors envoyez une grosse modification en plusieurs fois.

## Ce qui a été changé, et par quoi {#what-was-changed-and-by-what}

Chaque action est enregistrée avec ce qui l’a causée. Plus de détails dans [Activité sur Cora Max](/help/max-activity).
