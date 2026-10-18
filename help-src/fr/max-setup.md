---
title: Configurer Cora Max
description: Associez un nouveau Cora Max à Cora Mobile en Bluetooth, connectez-le au Wi-Fi, choisissez ses aquariums, et déplacez-le plus tard vers un autre aquarium.
section: Cora Max
reviewed: 2026-10-13
order: 1
group: Getting started
twin: mobile-setup
---

Cette page vous mène d’un Cora Max neuf à un écran mural qui fonctionne. Vous l’associez depuis votre téléphone en Bluetooth, et vous ne tapez rien sur l’écran lui-même.

:::tip Configurez d’abord vos aquariums sur votre téléphone
Cora Max affiche les aquariums et les appareils de votre compte, et il ne peut pas créer d’aquarium lui-même. [Configurez-les d’abord dans Cora Mobile](/help/mobile-setup). Cora Max les récupère dès que vous l’associez.
:::

## Ce qu’il vous faut {#what-you-need}

- Cora Max, branché et allumé. Il est fait pour rester branché.
- Cora Mobile sur votre téléphone, connecté, avec **au moins un aquarium** déjà créé.
- Le Bluetooth activé sur votre téléphone, et le téléphone près de Cora Max.
- Le nom et le mot de passe de votre réseau Wi-Fi.

Placez Cora Max là où vous le voyez depuis l’autre bout de la pièce et où vous pouvez lui parler, à l’abri des éclaboussures et des dépôts de sel.

## Ce que l’écran affiche d’abord {#what-the-screen-shows-first}

Allumez Cora Max. Il affiche un écran d’association qui indique **Ouvrez l’application Cora sur votre téléphone**, puis **Touchez Ajouter un appareil.** et **Choisissez ce Cora Max dans la liste des appareils.** En dessous, il affiche **Détectable sous le nom** suivi de son nom, qui se termine par un code court. Si vous en associez plusieurs, ce code permet de les distinguer sur votre téléphone.

![L’écran d’association de Cora Max, en attente de votre téléphone](img/max-pairing-screen.webp "En attente de votre téléphone. La ligne du bas montre le nom que votre téléphone affichera.")

Le même écran affiche un court avis sur les intégrations avec l’équipement d’autres fabricants. Les Conditions que vous avez acceptées dans Cora Mobile couvrent aussi Cora Max.

## Associer depuis votre téléphone {#pairing}

Tout le reste se passe dans Cora Mobile. Une feuille vous guide en cinq étapes, affichées en haut : **Connecter · Wi-Fi · Connexion · Aquariums · Terminé**.

1. **Le trouver.** Ouvrez l’onglet **Appareils**, touchez **Ajouter un appareil**, puis **Cora**. L’écran **Ajoutez votre Cora** liste les appareils Cora de votre réseau et les appareils de configuration proches trouvés en Bluetooth. Touchez **Analyser** si le vôtre n’apparaît pas encore, puis touchez votre Cora Max.

   ![L’écran Ajoutez votre Cora dans Cora Mobile, en recherche d’appareils](img/mobile-add-device.webp "Ajouter un appareil, puis Cora. Cora Mobile cherche sur votre Wi-Fi et en Bluetooth, avec la saisie manuelle de l’adresse IP en dessous.")

2. **Connecter.** Votre téléphone se connecte à Cora Max en Bluetooth et affiche son adresse MAC, son micrologiciel, sa variante et sa révision matérielle. Vérifiez que c’est le bon, puis touchez **Continuer**.

3. **Wi-Fi.** Choisissez votre réseau dans la liste, ou touchez **Rechercher à nouveau**, et tapez le mot de passe sur votre téléphone. À partir de là, votre téléphone parle à Cora Max en Wi-Fi, gardez donc le téléphone sur le même réseau.

4. **Connexion.** Votre téléphone associe Cora Max à votre compte. Cela se fait tout seul, et Cora Max affiche sa propre progression, comme **Vérification de votre compte…** et **Configuration de votre aquarium…**.

   ![L’écran d’association de Cora Max affichant Vérification de votre compte](img/max-pairing-verifying.webp "Cora Max affiche chaque étape pendant que votre téléphone l’associe à votre compte.")

5. **Aquariums.** Sous **Attribuer des aquariums**, choisissez les aquariums que ce Cora Max va gérer, **jusqu’à quatre**.

6. **Terminé.** Votre téléphone indique que Cora Max est configuré et affiche un **Code PIN de récupération**. Touchez le bouton qui ouvre le tableau de bord de votre aquarium, ou **Aller aux appareils**. Cora Max affiche **Associé**, puis **Ouverture du tableau de bord…**.

:::warning Notez le code PIN de récupération
Le **Code PIN de récupération** a six chiffres et c’est le seul moyen d’entrer en récupération sur ce Cora Max. Pour l’utiliser, posez cinq doigts en haut à droite de l’écran pendant dix secondes, puis saisissez le code PIN. La récupération vous permet de refaire le Wi-Fi, d’associer à nouveau, de rechercher une mise à jour ou de faire une réinitialisation d’usine. Vous retrouvez le code PIN sur votre téléphone sous **Appareils → votre Cora Max → Code PIN de récupération**, mais jamais sur Cora Max lui-même.
:::

### Si l’association bloque {#if-pairing-gets-stuck}

- **Le Bluetooth est désactivé. Activez-le, puis appuyez à nouveau sur Rechercher.** Activez le Bluetooth et relancez la recherche.
- **L’autorisation Bluetooth est désactivée pour Cora.** Autorisez le Bluetooth pour Cora dans les réglages de votre téléphone, puis touchez **Analyser**. Un iPhone peut aussi demander l’accès au réseau local. Autorisez-le aussi.
- **Aucun appareil de configuration Cora à proximité n’a été trouvé via Bluetooth.** Placez-vous à côté de Cora Max, vérifiez qu’il affiche toujours l’écran d’association, et relancez la recherche.
- **Aucun aquarium trouvé** à l’étape Aquariums. Votre compte n’a pas encore d’aquarium. Créez-en un dans Cora Mobile, puis refaites l’étape.
- **Pas encore associé à votre aquarium** à la fin. Cora Max est associé, mais le lien avec l’aquarium n’a pas abouti. Touchez **Réessayer maintenant**. Tant que ce n’est pas fini, les alertes de cet écran utilisent les plages par défaut.

D’autres solutions dans [Résolution de problèmes](/help/troubleshooting#pairing-a-cora-max-fails).

## Après l’association {#after-pairing}

Cora Max voit maintenant les mêmes aquariums, appareils, mesures et suivis que votre téléphone.

- Si l’un de vos aquariums avait déjà un Cora Max, Cora Max demande **Restaurer la disposition précédente pour cet aquarium ?** **Restaurer** remet les réglages d’affichage, de son et d’alerte que l’ancien avait enregistrés. **Repartir de zéro** les ignore.
- Un aquarium sans mesure affiche **Pas encore de mesures** et un bouton **Enregistrer votre premier test**.
- Cora Max construit un tableau de bord de départ à partir du profil de votre aquarium. Il ne copie pas celui de votre téléphone.

Vous pouvez associer plusieurs Cora Max au même compte, par exemple un dans la pièce technique et un dans le salon. Chacun peut afficher des aquariums différents et a sa propre disposition. Si deux affichent le même aquarium, [Plus d’un appareil Cora](/help/mobile-multi-device) explique lequel lit l’équipement.

## Construire le tableau de bord {#building-the-dashboard}

Le tableau de bord grand écran est une grille fixe, et tout doit tenir sur un seul écran. Le plus rapide est de le disposer depuis votre téléphone : ouvrez l’onglet **Appareils**, touchez votre Cora Max, puis touchez **Disposition du tableau de bord** sur la carte de l’aquarium. Vous pouvez aussi le faire au mur depuis le menu de l’aquarium.

Pour réutiliser la disposition d’un autre Cora Max ou d’un autre aquarium, chargez-la depuis **Mes tableaux de bord** dans l’éditeur. Plus de détails dans [Modifier le tableau de bord Cora Max](/help/max-dashboard-editing).

## Déplacer Cora Max vers un autre aquarium {#changing-which-tanks-it-shows}

Vous changez les aquariums qu’affiche un Cora Max sur votre téléphone. Les réglages de Cora Max lui-même ne le permettent pas.

1. Dans Cora Mobile, ouvrez l’onglet **Appareils** et touchez votre Cora Max.
2. Sous **Aquariums**, touchez **Ajouter un aquarium** et choisissez l’aquarium. Un Cora Max en accepte jusqu’à quatre. Quand il en a déjà quatre, le bouton disparaît : retirez-en d’abord un.
3. Pour retirer un aquarium de cet écran, touchez l’icône rouge de retrait (**Retirer l’aquarium**) sur la carte de cet aquarium, puis touchez **Retirer**.

Pour déplacer Cora Max d’un aquarium à un autre, ajoutez le nouvel aquarium, puis retirez l’ancien. Le nouvel aquarium reçoit un tableau de bord de départ construit à partir de son profil. Disposez-le avec **Disposition du tableau de bord**.

Si ce Cora Max était le Cora Max principal épinglé de l’aquarium retiré, cet épinglage est effacé et l’aquarium repasse sur **Tout appareil actif (automatique)**. Plus de détails dans [Appareils et état des appareils](/help/max-devices).

## Mises à jour {#updates}

Cora Max se met à jour tout seul. Une nouvelle version se télécharge en arrière-plan et s’installe la nuit. Votre version est affichée en haut de **Réglages → Réglages Cora Max**. Plus de détails dans [Mises à jour et récupération](/help/max-updates).

## Le passer sur un autre réseau Wi-Fi {#moving-it-to-a-different-network}

Allez dans **Réglages → Réglages Cora Max → Wi-Fi**, choisissez le nouveau réseau et saisissez le mot de passe. Cora Max reste associé, vous n’avez donc pas à le configurer à nouveau.
