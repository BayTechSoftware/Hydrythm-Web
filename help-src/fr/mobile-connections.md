---
title: Connecter votre équipement
description: Comment connecter à Cora l’équipement Neptune Apex, Red Sea ReefBeat, Jecod et AquaWiz.
section: Cora Mobile
reviewed: 2026-09-17
order: 10
group: Equipment
---

Cora fonctionne avec l’équipement que vous possédez déjà. Cette page couvre ce qui est pris en charge et ce dont chaque connexion a besoin.

Chaque marque se connecte de la façon qui lui convient le mieux, donc commencez par le point d’entrée de votre équipement :

| Marque | Commencer par |
|---|---|
| Neptune Apex | L’aquarium ; son profil contient la connexion Apex |
| Red Sea ReefBeat | L’aquarium |
| Jecod / Jebao | **Appareils → Trouver une pompe sur votre réseau**, ou Bluetooth |
| AquaWiz | **Appareils → Ajouter AquaWiz** |
| Maxspect *(bêta)* | **Appareils → Trouver une pompe sur votre réseau** |
| Cora Max | **Appareils → Ajouter un appareil** |

## Neptune Apex

Cora lit votre Apex via votre réseau local : sondes, prises et tout module d’extension que vous avez installé.

**Il vous faudra :** l’adresse de votre Apex sur votre réseau, et sa connexion.

**Ce que vous obtenez :** chaque sonde rapportée par votre Apex apparaît comme une source que vous pouvez placer sur un tableau de bord. Les prises apparaissent comme des commandes. Les modules d’extension installés obtiennent leurs propres tuiles d’appareil.

:::note Votre Apex garde sa propre programmation
Cora lit votre Apex, l’affiche avec tout le reste, et peut commuter des prises quand vous le demandez. Votre propre programmation continue de s’exécuter exactement comme vous l’avez configurée.
:::

## Red Sea ReefBeat

Cora communique avec l’équipement ReefBeat sur votre réseau local. Les unités prises en charge sont **ReefDose**, **ReefATO+**, **ReefMat** et **ReefRun**.

**Il vous faudra :** l’équipement déjà configuré dans ReefBeat et sur le même réseau que votre téléphone quand vous l’ajoutez.

**Ce que vous obtenez :** une page d’appareil par unité, plus les mesures de chaque unité comme sources. ReefDose rapporte ses têtes et contenants ; ReefATO+ rapporte son réservoir et ses remplissages ; ReefMat rapporte les jours restants ; ReefRun rapporte l’état de la pompe.

## Jecod / Jebao

Cora se connecte aux pompes Jecod, et peut les lire et les contrôler. Les unités Jecod atteignent Cora de deux façons, et celle utilisée par la vôtre déterminera ce qui est possible.

![Trouver une pompe](img/mobile-connections.webp "La recherche explique ce dont elle a besoin et pourquoi une pompe peut ne pas apparaître au premier balayage.")

**Via votre réseau.** Utilisez **Trouver une pompe sur votre réseau** ; elle trouve les unités qui s’annoncent elles-mêmes, donc aucune adresse n’a besoin d’être saisie. Une pompe réseau peut être lue et pilotée dès qu’elle est alimentée **et accessible** : soit votre téléphone est sur le même réseau, soit un Cora Max sur ce réseau relaie pour vous. Loin de chez vous sans Cora Max sur les lieux, une pompe uniquement réseau est visible mais pas contrôlable.

:::note Une pompe manque souvent le premier balayage
Les pompes répondent à un balayage et manquent le suivant. Si la vôtre n’est pas listée, recherchez à nouveau plutôt que de supposer qu’elle est inaccessible.
:::

Si une recherche ne trouve rien, le résultat affiche les adresses qu’elle a examinées sur le Wi-Fi. Si votre pompe a une adresse différente dans l’application Jebao, votre téléphone est sur un autre réseau. Un réseau invité ou IoT, ou une bande uniquement 5 GHz, ne verra pas ces pompes. Sur iPhone, Cora a aussi besoin de l’accès au réseau local pour voir les pompes sur votre Wi-Fi. S’il est désactivé, la liste reste vide et aucune erreur n’apparaît, donc le résultat l’explique et propose **Ouvrir les Réglages** pour le réactiver. **Réglages → Accès aux appareils** ouvre le même endroit à tout moment ; voir [Réglages](/help/mobile-settings).

**Via Bluetooth.** Certaines pompes ne sont accessibles que depuis un téléphone se tenant à proximité. La page de la pompe le précise, et montre les derniers réglages qu’elle a réussi à lire ainsi que leur ancienneté.

Cora a besoin de la permission Bluetooth pour cela. Accordez-la avant d’ajouter une pompe Bluetooth : sans permission, la pompe ne peut pas être découverte du tout, plutôt que de simplement prendre plus de temps à apparaître.

**Ce que vous obtenez :** état en direct, mode et intensité, pause de nourrissage, et un programme journalier. Voir [Programmer l’équipement](/help/mobile-schedules).

:::warning Une pompe Bluetooth n’est accessible que quand vous êtes près d’elle
Sa page montre les derniers réglages que Cora a lus et depuis combien de temps. Changer quoi que ce soit, y compris démarrer une pause de nourrissage, nécessite que la pompe soit à portée. Restez près d’elle et rouvrez la page.
:::

## Contrôleur KH AquaWiz

Cora lit l’alcalinité depuis un contrôleur KH AquaWiz via votre compte AquaWiz.

**Il vous faudra :** votre nom d’utilisateur et mot de passe AquaWiz. Cora se connecte en votre nom et garde la connexion pour continuer à lire.

**Ce que vous obtenez :** l’alcalinité comme source, mise à jour aussi souvent que votre contrôleur titre. Le pH est disponible en option si votre unité le rapporte.

:::warning Une connexion, partagée
AquaWiz délivre une seule connexion par compte, donc celle que Cora détient est la même que celle utilisée par leur propre application. Changer votre mot de passe AquaWiz déconnectera Cora ; reconnectez-le depuis la ligne de l’appareil ensuite. Pour révoquer entièrement l’accès de Cora, retirez l’appareil dans Cora et changez votre mot de passe AquaWiz.
:::

## Maxspect

:::note La prise en charge Maxspect est en bêta
La prise en charge des pompes de brassage Maxspect est encore en cours de test et de développement, donc certaines commandes peuvent être limitées, et ce que vous voyez ici peut changer entre les mises à jour. Si quelque chose ne fonctionne pas comme décrit, dites-le-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

Cora se connecte aux pompes Maxspect Gyre, et peut les lire et les piloter.

**Il vous faudra :** au moment de l’ajout, la pompe de brassage et votre téléphone sur le même réseau. Utilisez **Appareils → Trouver une pompe sur votre réseau**.

**Ce que vous obtenez :** motif de vague et vitesse pour **Gyre A** et **Gyre B**, le programme de la pompe de brassage à consulter (réglez-le dans l’application Maxspect), **État de la pompe**, et si elle fonctionne, avec quand elle a été lue pour la dernière fois. Voir [Contrôler votre équipement](/help/mobile-device-control).

:::note Comment Cora Mobile atteint une pompe de brassage
Quand un Cora Max dessert l’aquarium, Cora Mobile fonctionne via ce Cora Max, y compris quand vous êtes loin de chez vous, et **Modifier les réglages** part de la dernière lecture de ce Cora Max. Sinon, votre téléphone parle directement à la pompe de brassage et doit être sur son réseau. Ouvrir la page de la pompe de brassage la lit alors ; si la page affiche à la place une lecture stockée plus ancienne, **Modifier les réglages** reste caché jusqu’à ce que vous touchiez actualiser.
:::

## Enregistrer à la main

Certains paramètres viennent d’un test en kit plutôt que de l’équipement. Pour saisir un résultat, faites défiler jusqu’en bas du tableau de bord et touchez **Enregistrer les paramètres**.

Les mesures enregistrées à la main sont de première classe : elles apparaissent sur les widgets, portent leur propre source et ancienneté, alimentent Reef Buddy, et c’est contre elles que Cora compare vos sondes quand il vous dit que deux sources ne sont pas d’accord.

## Si une connexion arrête de fonctionner

La ligne de l’appareil vous dit de quel type de problème il s’agit. Voir le tableau dans **[Ajouter, modifier et retirer des appareils](/help/mobile-devices)**, et **[Résolution de problèmes](/help/troubleshooting)** pour tout ce qu’il ne couvre pas.
