---
title: Contrôler l’équipement depuis Cora Max
description: Les pages d’appareils sur Cora Max pour Neptune Apex, Trident et DŌS, Red Sea ReefBeat, Jecod, AquaWiz et les marques en Beta, marque par marque.
section: Cora Max
reviewed: 2026-10-13
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
| **DŌS**, y compris le DŌS QD | Le dosage, le programme, l’autonomie et le volume du récipient de chaque tête (avec pause, remplissage, dose immédiate et une mesure unique de vingt secondes) |
| **Red Sea ReefBeat** | Ce que l’appareil possède : têtes de dosage, réservoir, jours de rouleau, mode de pompe, plus un éditeur complet du plan ReefDose et du programme ReefRun, et les réglages ReefMat *(Beta)* |
| **Red Sea ReefControl**, **ReefControl Power**, **ReefWave**, **ReefLED** *(Beta)* | Les sondes de ReefControl. Les prises de ReefControl Power comme des prises, allumées ou éteintes, sans mode automatique pour l’instant. ReefWave et ReefLED, en lecture seule |
| **Jecod** | Le mode et l’intensité de la pompe, et son programme journalier |
| **AquaWiz** | Pas de page à lui. Il est listé dans **Appareils**, et ses mesures vont sur le tableau de bord |
| **Maxspect** *(Beta)* | Le mode et la vitesse de **Gyre A** et **Gyre B**, l’**État de la pompe** (compte à rebours de nettoyage, courant de la tête A, têtes installées, micrologiciel), et son programme, en lecture seule |
| **GHL ProfiLux / Mitras** *(Beta)* | Sondes, prises, doseurs, capteurs de niveau et, sur les modèles Director, résultats de tests KH et d’ions |
| **HYDROS** *(Beta)* | Ce que signale sa clé d’appareil : entrées et, avec une clé d’écriture, sorties, modes, têtes de dosage et commandes de testeur |
| **Focustronic** *(Beta)* | État, dernier test, pompes et flacons, plus **Mesurer maintenant**, **Doser maintenant** ou **Tester maintenant** selon l’appareil |
| **EcoTech** *(Beta)* | Lampes Radion, pompes VorTech et doseurs Versa, chacun avec sa propre page. Les commandes vers VorTech et Versa ne sont pas encore prouvées sur du matériel |
| **Inkbird** *(Beta)* | Mesures de l’air ambiant, en lecture seule |
| **Caméra** *(Beta)* | Une image de votre caméra, en tuile sur le tableau de bord ou sur sa propre page, avec la surveillance de l’écumeur dans les forfaits payants |

:::note Beta
**Beta.** Maxspect, GHL, HYDROS, Focustronic, EcoTech, Inkbird et les caméras sont en Beta et ne sont ouverts qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore fonctionner.
:::

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

Un DŌS n’a pas de capteur de niveau et continue de doser depuis un récipient vide. Réglez une alerte de réapprovisionnement avec **Paramètres d’alerte** sur la page du DŌS. Plus de détails dans [Alertes des doseurs](/help/mobile-device-control#doser-alerts).

### À quoi sert une tête {#what-a-head-is-used-for}

Dans la feuille de réglages d’une tête, vous pouvez régler son **type d’usage**. Les options sont **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture** ou **Appoint**, et **Autre**. Le type d’usage change deux choses.

- La taille du récipient qu’elle peut suivre. Chaque type d’usage peut suivre un récipient jusqu’à 1 000 litres. Au-delà du compteur de 150 litres de l’Apex, Cora suit lui-même le volume, et Cora remet le compteur de l’Apex à zéro tous les 100 litres.
- Si elle peut faire une grosse dose à la main. Les têtes Complément et Nourriture gardent le plafond actuel, petit et prudent. Tout autre type d’usage peut avoir sa propre limite de **Dosage manuel maximal**, jusqu’à un plafond absolu de 10 litres, et sa propre **Limite quotidienne pour les automatisations et l’Assistant**. Une grosse dose à la main demande aussi d’activer **Doses importantes (bêta)** dans les réglages de la tête, désactivé par défaut. Ne l’activez qu’après avoir regardé la première grosse dose se faire à l’aquarium.

Vous pouvez relier une paire de changement d’eau (entrée d’eau salée neuve, sortie d’eau ancienne) comme **Tête associée** et régler une valeur d’**Alerte d’équilibre au-dessus de**. Si les totaux du jour des deux têtes s’écartent de plus que cette valeur, Cora vous prévient. Une paire déséquilibrée veut en général dire qu’un côté ne pompe pas comme il devrait.

### Si une grosse dose est interrompue {#if-a-large-dose-is-interrupted}

Une grosse dose change pendant un moment ce que fait la tête sur l’Apex, puis remet son programme normal. Si la connexion tombe en cours de route, Cora Max affiche un bandeau sur la page de cette tête : *« Un dosage important sur [tête] ne s’est pas terminé proprement. Cora continue d’essayer de remettre son programme en place ; vérifiez-le dans Apex Fusion. »*

Vérifiez vous-même la tête dans Apex Fusion, puis touchez **J’ai vérifié la tête dans Fusion** pour effacer le bandeau. Ne le faites qu’après avoir confirmé que c’est le programme propre de la tête qui tourne, et non le programme de dosage de Cora.

Si le bandeau ne s’efface pas, ou revient sans cesse, consultez [Résolution de problèmes](/help/troubleshooting).

## Red Sea ReefBeat {#red-sea}

Chaque appareil Red Sea a une page adaptée à ce qu’il fait : têtes et récipients ReefDose, réservoir ReefATO+, jours de rouleau ReefMat et vitesses de pompe ReefRun. Les alertes de consommables des têtes ReefDose, du réservoir ReefATO+ et du rouleau ReefMat se règlent avec **Paramètres d’alerte** sur la page de l’appareil.

Si un appareil Red Sea s’arrête de lui-même, sa page vous dit ce qui ne va pas et place la solution juste à côté. C’est **Reprendre**, **Effacer l’urgence**, **Capteur nettoyé**, **J’ai déjà chargé un nouveau rouleau**, ou **Réinitialiser** pour une tête de dosage.

Un plan ReefDose, un programme de vitesse ReefRun et l’avance programmée, le modèle, la position et Nouveau rouleau du ReefMat fonctionnent ici de la même façon que sur votre téléphone. [Contrôler votre équipement](/help/mobile-device-control) donne les détails.

ReefControl, ReefControl Power, ReefWave et ReefLED portent *(Beta)* dans leur nom mais sont ouverts à tous. ReefControl affiche ses sondes. Les prises de ReefControl Power apparaissent comme des prises, allumées ou éteintes uniquement. ReefWave et ReefLED sont en lecture seule pour l’instant.

## Jecod {#jecod}

La page Jecod affiche le mode et l’intensité de la pompe, et vous pouvez changer les deux.

Vous pouvez écrire les programmes journaliers des pompes Jecod au mur comme sur votre téléphone. L’éditeur est le même, avec un graphique de la journée, une liste de périodes et une rangée d’actions. Plus de détails dans [Programmer l’équipement](/help/mobile-schedules).

## AquaWiz {#aquawiz}

Un AquaWiz KH Controller n’a pas de page à lui sur Cora Max. Il est listé dans **Appareils**, où vous pouvez le renommer, et ses mesures s’affichent sur le tableau de bord comme n’importe quelle autre source. Configurez-le et gérez-le sur votre téléphone, voir [Connecter votre équipement](/help/mobile-connections).

## Maxspect {#maxspect}

:::note Beta
**Beta.** Maxspect est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore fonctionner.
:::

La page Maxspect affiche le mode et la vitesse de **Gyre A** et **Gyre B** et son **État de la pompe**. Vous pouvez consulter ici le programme d’une Gyre, mais pas l’enregistrer. Réglez-le dans l’application Maxspect.

## GHL ProfiLux et Mitras {#ghl}

:::note Beta
**Beta.** GHL est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore fonctionner.
:::

Connectez un contrôleur GHL depuis votre téléphone : **Appareils → Ajouter un appareil → GHL**. [Connecter votre équipement](/help/mobile-connections) donne les étapes. Cora Max l’affiche et le commande dès qu’un Cora Max de son réseau l’a lu, mais la configuration elle-même se fait sur le téléphone.

Un ProfiLux mini lit ses sondes, ses prises, ses doseurs et ses capteurs de niveau. Avec **Autoriser le contrôle depuis Cora (bêta)** activé, un mini peut aussi commander ses prises, comme n’importe quel autre contrôleur GHL. Tout le reste, comme les consignes et la pause nourrissage, nécessite un ProfiLux 3, 4 ou un Mitras.

Les commandes restent désactivées tant que vous n’activez pas **Autoriser le contrôle depuis Cora (bêta)** sur la page de l’appareil. C’est désactivé par défaut. Une fois activé, une prise peut être réglée sur **Toujours allumé**, **Toujours éteint** ou **Retour à automatique**, et une consigne comme la température ou le pH affiche sa plage autorisée et refuse une valeur en dehors. Les deux sortes de changements sont enregistrées sur le contrôleur lui-même et y restent même si Cora perd ensuite le contact avec lui. Un changement qui semble toucher un chauffage ou une pompe de remontée vous demande de confirmer deux fois.

Si le récipient d’un doseur se vide, Cora vous prévient comme pour les autres consommables. La valeur par défaut est 20 % de remplissage, et vous pouvez la changer depuis la règle du doseur dans le [Centre d’alertes](/help/mobile-alerts).

Si le contrôleur n’accepte pas un changement, son API GHL est probablement désactivée. GHL la désactive après chaque mise à jour du micrologiciel. Réactivez-la depuis **System → GHL API** dans GHL Control Center ou GHL Connect. [Résolution de problèmes](/help/troubleshooting) donne la suite.

## HYDROS {#hydros}

:::note Beta
**Beta.** HYDROS est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore fonctionner.
:::

HYDROS joint son contrôleur par le cloud HYDROS, il fonctionne donc même quand Cora Max est sur un autre réseau que le contrôleur. Il se configure uniquement depuis votre téléphone : **Appareils → Ajouter un appareil → HYDROS**. [Connecter votre équipement](/help/mobile-connections) donne les étapes.

La lecture et la commande fonctionnent comme sur votre téléphone. Voir [Contrôler votre équipement](/help/mobile-device-control) pour les sorties, les modes, les têtes de dosage et les commandes de testeur, et pour les limites de dose par tête.

## Focustronic {#focustronic}

:::note Beta
**Beta.** Focustronic est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore fonctionner.
:::

La page Focustronic affiche l’état de l’appareil, son dernier test, et ses pompes et flacons. Sous **Commandes** :

- Un Alkatronic a **Mesurer maintenant**.
- Un Dosetronic a **Doser maintenant** pour chaque pompe. Saisissez la quantité, jusqu’à 500 mL à la fois, touchez **Vérifier**, puis confirmez. Une dose ne peut pas être annulée, et Cora ne la relance jamais.
- Un Mastertronic a un profil de test à choisir et **Tester maintenant**.

Ces commandes passent par les serveurs de Focustronic, que Cora ne contrôle pas. Configurez l’appareil sur votre téléphone, voir [Connecter votre équipement](/help/mobile-connections).

## EcoTech, Inkbird et caméras {#ecotech-inkbird-and-cameras}

:::note Beta
**Beta.** EcoTech, Inkbird et les caméras sont en Beta et ne sont ouverts qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

Vous les associez depuis votre téléphone, et un Cora Max de l’aquarium fait la lecture.

### EcoTech {#ecotech}

Les lampes Radion, les pompes VorTech et les doseurs Versa ont chacun leur propre page, avec un bouton **Paramètres d’alerte** pour leurs consommables. [Lampes, pompes et doseurs EcoTech](/help/mobile-ecotech) donne les détails.

### Inkbird {#inkbird}

Un moniteur d’air ambiant Inkbird affiche ses mesures et rien de plus.

### Caméras et surveillance de l’écumeur {#cameras}

Pour afficher une caméra au mur, ajoutez une tuile **Caméra** dans l’[éditeur du tableau de bord](/help/max-dashboard-editing). Touchez la tuile pour ouvrir la caméra en plein écran. Ses boutons s’estompent au bout de quelques secondes, et un appui les fait revenir.

Avec la surveillance de l’écumeur activée (forfaits payants), la tuile caméra et la vue plein écran affichent le niveau du godet et l’âge de la mesure, par exemple *Godet 42 % · il y a 5 min*. La puce passe à l’orange à moins de 10 points de votre niveau d’alerte et au rouge quand il est atteint. Sur la caméra en plein écran, **Alerte à 80 %** (ou votre niveau) ouvre **Alerte du godet de l'écumeur**, où vous réglez le niveau. Vous recevez une seule notification quand le godet l’atteint.

La configuration d’une caméra et de la surveillance de l’écumeur est expliquée dans [Caméras et surveillance de l’écumeur](/help/mobile-cameras).

## Consommables {#consumables}

Vous réglez ici les seuils de réapprovisionnement (réactif, récipients, réservoirs) sur la page de l’appareil lui-même, comme sur votre téléphone. Plus de détails dans [Consommables](/help/mobile-consumables).

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
