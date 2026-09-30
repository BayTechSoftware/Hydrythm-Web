---
title: Connecter votre équipement
description: Connecter à Cora votre équipement Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz, GHL et HYDROS.
section: Cora Mobile
reviewed: 2026-09-30
order: 10
group: Equipment
---

Cora fonctionne avec l’équipement que vous avez déjà. Cette page indique ce qui est pris en charge et ce qu’il faut pour chaque connexion.

Chaque marque se connecte à sa façon. Commencez par le bon point d’entrée :

| Marque | Point de départ |
|---|---|
| Neptune Apex | L’aquarium. La connexion Apex se trouve dans son profil |
| Red Sea ReefBeat | L’aquarium |
| Jecod / Jebao | **Appareils → Trouver une pompe sur votre réseau**, ou Bluetooth |
| AquaWiz | **Appareils → Ajouter AquaWiz** |
| Maxspect *(bêta)* | **Appareils → Trouver une pompe sur votre réseau** |
| GHL ProfiLux / Mitras *(bêta)* | Cora Max, depuis les réglages de l’aquarium |
| HYDROS *(bêta)* | **Appareils → Ajouter HYDROS (bêta)** |
| Cora Max | **Appareils → Ajouter un appareil** |

## Neptune Apex

Cora lit votre Apex par votre réseau local : sondes, prises et modules d’extension installés.

Il vous faut l’adresse de votre Apex sur votre réseau, ainsi que ses identifiants de connexion.

Chaque sonde de votre Apex devient une source que vous pouvez placer sur un tableau de bord. Les prises deviennent des commandes. Chaque module d’extension installé a sa propre tuile d’appareil.

:::note Votre Apex garde sa propre programmation
Cora lit votre Apex, l’affiche avec le reste, et peut allumer ou éteindre des prises quand vous le demandez. Votre programmation continue de tourner exactement comme vous l’avez réglée.
:::

## Red Sea ReefBeat

Cora dialogue avec l’équipement ReefBeat sur votre réseau local. Les appareils pris en charge sont **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun**, ainsi que, en bêta, **ReefControl**, **ReefControl Power**, **ReefWave** et **ReefLED**.

L’équipement doit déjà être configuré dans ReefBeat. Au moment de l’ajout, il doit être sur le même réseau que votre téléphone.

Chaque appareil a sa page, et ses mesures deviennent des sources. ReefDose indique ses têtes et ses bidons. ReefATO+ indique son réservoir et ses remplissages. ReefMat indique les jours restants. ReefRun indique l’état de la pompe. ReefControl indique ses sondes de la même façon. ReefWave et ReefLED *(bêta)* affichent seulement leur mode pour l’instant, en lecture seule.

## Jecod / Jebao

Cora se connecte aux pompes Jecod, et peut les lire et les piloter. Une pompe Jecod rejoint Cora de l’une de deux façons. Ce qui est possible dépend de celle qu’utilise votre pompe.

![Trouver une pompe](img/mobile-connections.webp "La recherche explique ce dont elle a besoin et pourquoi une pompe peut ne pas apparaître au premier balayage.")

La première passe par votre réseau. Touchez **Trouver une pompe sur votre réseau**. La recherche trouve les pompes qui se signalent d’elles-mêmes, vous n’avez donc aucune adresse à saisir. Une pompe réseau peut être lue et pilotée dès qu’elle est sous tension **et joignable**. Il faut pour cela que votre téléphone soit sur le même réseau, ou qu’un Cora Max sur ce réseau fasse le relais. Loin de chez vous, sans Cora Max sur place, une pompe uniquement réseau reste visible, mais vous ne pouvez pas la piloter.

:::note Une pompe rate souvent le premier balayage
Une pompe répond à un balayage et rate le suivant. Si la vôtre n’apparaît pas, relancez la recherche avant de conclure qu’elle est injoignable.
:::

Si la recherche ne trouve rien, le résultat affiche les adresses examinées sur le Wi-Fi. Si l’application Jebao donne une autre adresse à votre pompe, votre téléphone est sur un autre réseau. Un réseau invité ou IoT, ou une bande 5 GHz seule, ne voit pas ces pompes. Sur iPhone, Cora a aussi besoin de l’accès au réseau local pour voir les pompes de votre Wi-Fi. Si cet accès est coupé, la liste reste vide, sans message d’erreur. Le résultat l’explique alors et propose **Ouvrir les Réglages** pour le réactiver. Vous pouvez aussi ouvrir le même endroit à tout moment par **Réglages → Accès aux appareils**. Voir [Réglages](/help/mobile-settings).

La seconde passe par Bluetooth. Certaines pompes ne sont joignables que depuis un téléphone posé à côté. La page de la pompe l’indique. Elle montre aussi les derniers réglages lus, et leur âge.

Cora a besoin pour cela de l’autorisation Bluetooth. Donnez-la avant d’ajouter une pompe Bluetooth. Sans elle, la pompe reste introuvable, même en attendant.

Vous obtenez l’état en direct, le mode et l’intensité, la pause nourrissage et un programme journalier. Voir [Programmer l’équipement](/help/mobile-schedules).

:::warning Une pompe Bluetooth n’est joignable que si vous êtes à côté
Sa page montre les derniers réglages lus par Cora et leur âge. Pour changer quoi que ce soit, y compris lancer une pause nourrissage, la pompe doit être à portée. Approchez-vous et rouvrez la page.
:::

## Contrôleur KH AquaWiz

Cora lit l’alcalinité d’un contrôleur KH AquaWiz par votre compte AquaWiz.

Il vous faut votre nom d’utilisateur et votre mot de passe AquaWiz. Cora se connecte à votre place et garde cette connexion pour continuer à lire les mesures.

L’alcalinité devient une source, mise à jour à chaque titrage de votre contrôleur. Le pH est disponible en option si votre appareil le mesure.

La fiche de l’appareil affiche aussi votre KH cible, la force de votre dose et, pour un appareil dont le dosage est configuré, sa dose maximale par heure et la quantité de supplément d’alcalinité restante dans le bidon. Ces valeurs viennent directement de vos réglages AquaWiz. Modifiez-les dans l’application AquaWiz. Si votre appareil suit son bidon, Cora vous prévient quand le supplément devient bas, à 100 mL par défaut.

:::warning Une seule connexion, partagée
AquaWiz n’accorde qu’une connexion par compte. Cora utilise donc la même que l’application AquaWiz. Si vous changez votre mot de passe AquaWiz, Cora sera déconnecté. Reconnectez-le ensuite depuis la ligne de l’appareil. Pour retirer complètement l’accès de Cora, supprimez l’appareil dans Cora et changez votre mot de passe AquaWiz.
:::

## Maxspect

:::note La prise en charge Maxspect est en bêta
La prise en charge des pompes de brassage Maxspect est encore en test et en développement. Certaines commandes peuvent être limitées, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

Cora se connecte aux pompes Maxspect Gyre, et peut les lire et les piloter.

Au moment de l’ajout, la pompe et votre téléphone doivent être sur le même réseau. Touchez **Appareils → Trouver une pompe sur votre réseau**.

Vous obtenez le type de vague et la vitesse pour **Gyre A** et **Gyre B**, le programme de la pompe en lecture seule (il se règle dans l’application Maxspect), **État de la pompe**, et si la pompe tourne, avec l’heure de la dernière lecture. Voir [Contrôler votre équipement](/help/mobile-device-control).

:::note Comment Cora Mobile joint une pompe Gyre
Si un Cora Max gère l’aquarium, Cora Mobile passe par ce Cora Max, même quand vous êtes loin de chez vous. **Modifier les réglages** part alors de la dernière lecture de ce Cora Max. Sinon, votre téléphone parle directement à la pompe et doit être sur le même réseau qu’elle. Ouvrir la page de la pompe lance alors une lecture. Si la page affiche une lecture plus ancienne gardée en mémoire, **Modifier les réglages** reste masqué jusqu’à ce que vous touchiez actualiser.
:::

## GHL ProfiLux et Mitras

:::note La prise en charge GHL est en bêta
Nous testons et développons encore la prise en charge GHL. Certaines mesures ou commandes peuvent ne pas encore marcher, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

Cora lit un contrôleur GHL ProfiLux ou Mitras par votre réseau local : sondes, prises, doseurs, capteurs de niveau et, sur les modèles Director, les résultats de test KH et ionique.

Vous le connectez depuis **Cora Max**, pas depuis votre téléphone : ouvrez les réglages de l’aquarium et ajoutez son adresse IP là-bas. [Contrôler l’équipement depuis Cora Max](/help/max-device-control) donne les étapes. Une fois connecté, ses mesures et ses commandes apparaissent aussi sur votre téléphone.

L’API GHL doit être activée pour que Cora puisse joindre le contrôleur. GHL la désactive après chaque mise à jour du micrologiciel, donc vérifiez cela en premier si rien n’apparaît. [Résolution de problèmes](/help/troubleshooting) explique la suite.

## HYDROS

:::note La prise en charge HYDROS est en bêta
Nous testons et développons encore la prise en charge HYDROS. Certaines mesures ou commandes peuvent ne pas encore marcher, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

HYDROS est la seule intégration qui n’a pas besoin que votre Cora et votre contrôleur soient sur le même réseau. Cora le rejoint par le cloud propre à HYDROS, ce qui le fait continuer à marcher loin de chez vous, et même Cora fermé.

Pour le connecter, ouvrez l’application HYDROS et créez une **clé d’appareil** pour le fournisseur **cora-iq**. Choisissez **Lecture** si vous voulez seulement ses mesures, ou **Écriture** si vous voulez aussi le contrôler depuis Cora. Allez ensuite dans **Appareils → Ajouter HYDROS (bêta)** et collez la clé.

Une fois lié, Cora importe les 33 derniers jours de son historique, puis continue à lire à partir de là. [Contrôler votre équipement](/help/mobile-device-control) explique ce que vous pouvez lire et, avec une clé d’écriture, contrôler.

## Saisir à la main

Certains paramètres viennent d’un test en kit, pas d’un équipement. Pour saisir un résultat, faites défiler jusqu’en bas du tableau de bord et touchez **Enregistrer les paramètres**.

Les mesures saisies à la main comptent autant que les autres. Elles s’affichent sur les widgets avec leur propre source et leur âge, et elles alimentent Reef Buddy. C’est aussi à elles que Cora compare vos sondes quand il vous signale que deux sources ne sont pas d’accord.

## Si une connexion ne marche plus

La ligne de l’appareil indique de quel type de problème il s’agit. Consultez le tableau de la page **[Ajouter, modifier et retirer des appareils](/help/mobile-devices)**. Pour les autres cas, voir **[Résolution de problèmes](/help/troubleshooting)**.
