---
title: Connecter votre équipement
description: Connecter à Cora votre équipement Neptune Apex, Red Sea ReefBeat, Jecod, AquaWiz et, en Beta, Maxspect, GHL, HYDROS, Focustronic et Inkbird.
section: Cora Mobile
reviewed: 2026-10-12
order: 10
group: Equipment
---

Cora fonctionne avec l’équipement que vous avez déjà. Cette page indique ce qui est pris en charge et ce qu’il faut pour chaque connexion.

Tout commence de la même façon : **Appareils → Ajouter un appareil**, puis choisissez la marque. Chacune ouvre exactement ce dont elle a besoin pour trouver votre équipement.

Les marques indiquées *(Beta)* ne sont ouvertes qu’aux utilisateurs Beta. Voir [Fonctions Beta](/help/mobile-beta).

| Marque | Ouvre |
|---|---|
| Cora | Une recherche d’un nouveau Cora Max, en Wi-Fi ou en Bluetooth |
| Neptune Apex | Son adresse sur votre réseau, la connexion, puis l’aquarium auquel il appartient |
| Red Sea | Une recherche sur votre réseau, puis l’aquarium de chaque appareil |
| Jecod / Jebao | Une recherche sur votre réseau, ou le Bluetooth |
| Maxspect *(Beta)* | La même recherche que Jecod |
| GHL *(Beta)* | Son adresse, son interface et, pour un mini, ses identifiants |
| HYDROS *(Beta)* | Une clé d’appareil depuis l’application HYDROS |
| Focustronic *(Beta)* | Votre connexion Focustronic, puis l’aquarium de chaque appareil |
| EcoTech *(Beta)* | Une recherche Bluetooth des lampes Radion, pompes VorTech et doseurs Versa. Voir [Lampes, pompes et doseurs EcoTech](/help/mobile-ecotech) |
| Inkbird *(Beta)* | Une recherche Bluetooth de votre moniteur d’air ambiant |
| Caméra *(Beta)* | Wyze, Tapo, Sonoff ou une autre caméra RTSP. Voir [Caméras et surveillance de l’écumeur](/help/mobile-cameras) |
| AquaWiz | Votre connexion AquaWiz |

## Neptune Apex

Cora lit votre Apex par votre réseau local : sondes, prises et modules d’extension installés.

Ajoutez-le depuis **Appareils → Ajouter un appareil → Neptune Apex**. Il vous faut son adresse sur votre réseau et ses identifiants de connexion, puis vous choisissez l’aquarium auquel il appartient. Un Apex peut desservir plusieurs aquariums.

Chaque sonde de votre Apex devient une source que vous pouvez placer sur un tableau de bord. Les prises deviennent des commandes. Chaque module d’extension installé a sa propre tuile d’appareil.

:::note Votre Apex garde sa propre programmation
Cora lit votre Apex, l’affiche avec le reste, et peut allumer ou éteindre des prises quand vous le demandez. Votre programmation continue de tourner exactement comme vous l’avez réglée.
:::

## Red Sea ReefBeat

Cora dialogue avec l’équipement ReefBeat sur votre réseau local. Les appareils pris en charge sont **ReefDose**, **ReefATO+**, **ReefMat**, **ReefRun**, ainsi que, en Beta, **ReefControl**, **ReefControl Power**, **ReefWave** et **ReefLED**.

L’équipement doit déjà être configuré dans ReefBeat et sur le même réseau que votre téléphone au moment de l’ajout. Ajoutez-le depuis **Appareils → Ajouter un appareil → Red Sea**, qui scanne votre réseau et demande l’aquarium de chaque appareil. Un appareil Red Sea dessert un seul aquarium : en choisir un autre l’y déplace.

Chaque appareil a sa page, et ses mesures deviennent des sources. ReefDose indique ses têtes et ses bidons. ReefATO+ indique son réservoir et ses remplissages. ReefMat indique les jours restants. ReefRun indique l’état de la pompe. ReefControl indique ses sondes de la même façon. ReefWave et ReefLED *(Beta)* affichent seulement leur mode pour l’instant, en lecture seule.

## Jecod / Jebao

Cora se connecte aux pompes Jecod, et peut les lire et les piloter. Ajoutez-en une depuis **Appareils → Ajouter un appareil → Jecod**. Une pompe Jecod rejoint Cora de l’une de deux façons. Ce qui est possible dépend de celle qu’utilise votre pompe.

![Trouver une pompe](img/mobile-connections.webp "La recherche explique ce dont elle a besoin et pourquoi une pompe peut ne pas apparaître au premier balayage.")

La première passe par votre réseau. La recherche trouve les pompes qui se signalent d’elles-mêmes, vous n’avez donc aucune adresse à saisir. Une pompe réseau peut être lue et pilotée dès qu’elle est sous tension **et joignable**. Il faut pour cela que votre téléphone soit sur le même réseau, ou qu’un Cora Max sur ce réseau fasse le relais. Loin de chez vous, sans Cora Max sur place, une pompe uniquement réseau reste visible, mais vous ne pouvez pas la piloter.

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

Cora lit l’alcalinité d’un contrôleur KH AquaWiz par votre compte AquaWiz. Ajoutez-le depuis **Appareils → Ajouter un appareil → AquaWiz**.

Il vous faut votre nom d’utilisateur et votre mot de passe AquaWiz. Cora se connecte à votre place et garde cette connexion pour continuer à lire les mesures.

L’alcalinité devient une source, mise à jour à chaque titrage de votre contrôleur. Le pH est disponible en option si votre appareil le mesure.

La fiche de l’appareil affiche aussi votre KH cible, la force de votre dose et, pour un appareil dont le dosage est configuré, sa dose maximale par heure et la quantité de supplément d’alcalinité restante dans le bidon. Ces valeurs viennent directement de vos réglages AquaWiz. Modifiez-les dans l’application AquaWiz. Si votre appareil suit son bidon, Cora vous prévient quand le supplément devient bas, à 100 mL par défaut.

:::warning Une seule connexion, partagée
AquaWiz n’accorde qu’une connexion par compte. Cora utilise donc la même que l’application AquaWiz. Si vous changez votre mot de passe AquaWiz, Cora sera déconnecté. Reconnectez-le ensuite depuis la ligne de l’appareil. Pour retirer complètement l’accès de Cora, supprimez l’appareil dans Cora et changez votre mot de passe AquaWiz.
:::

## Maxspect

:::note Beta
**Beta.** Maxspect est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’en êtes pas un, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines commandes peuvent être limitées, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

Cora se connecte aux pompes Maxspect Gyre, et peut les lire et les piloter. Ajoutez-en une depuis **Appareils → Ajouter un appareil → Maxspect**, la même recherche que pour Jecod. Il faut un Cora Max à l’aquarium. Sans lui, la ligne affiche **Nécessite Cora Max**.

Au moment de l’ajout, la pompe et votre téléphone doivent être sur le même réseau.

Vous obtenez le type de vague et la vitesse pour **Gyre A** et **Gyre B**, le programme de la pompe en lecture seule (il se règle dans l’application Maxspect), **État de la pompe**, et si la pompe tourne, avec l’heure de la dernière lecture. Voir [Contrôler votre équipement](/help/mobile-device-control).

:::note Comment Cora Mobile joint une pompe Gyre
Si un Cora Max gère l’aquarium, Cora Mobile passe par ce Cora Max, même quand vous êtes loin de chez vous. **Modifier les réglages** part alors de la dernière lecture de ce Cora Max. Sinon, votre téléphone parle directement à la pompe et doit être sur le même réseau qu’elle. Ouvrir la page de la pompe lance alors une lecture. Si la page affiche une lecture plus ancienne gardée en mémoire, **Modifier les réglages** reste masqué jusqu’à ce que vous touchiez actualiser.
:::

## GHL ProfiLux et Mitras

:::note Beta
**Beta.** GHL est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’en êtes pas un, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore marcher. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

Cora lit un contrôleur GHL ProfiLux ou Mitras : sondes, prises, doseurs, capteurs de niveau et, sur les modèles Director, les résultats de test KH et ionique.

Ajoutez-le depuis **Appareils → Ajouter un appareil → GHL**. Il faut un Cora Max à l’aquarium, et la ligne affiche **Nécessite Cora Max** sans lui. Votre téléphone ne peut pas le rechercher automatiquement : saisissez son adresse et choisissez vous-même l’interface : **API officielle**, **HTTP**, ou **ProfiLux mini** (qui a aussi besoin de ses identifiants). Choisissez ensuite l’aquarium auquel il appartient. Un contrôleur GHL peut desservir plusieurs aquariums.

Un contrôleur GHL ne communique pas directement avec votre téléphone. Il affiche **En attente de Cora Max** jusqu’à ce qu’un Cora Max sur son réseau l’ait lu, puis ses mesures et ses commandes apparaissent partout.

L’API GHL doit être activée pour que Cora puisse joindre le contrôleur. GHL la désactive après chaque mise à jour du micrologiciel, donc vérifiez cela en premier si rien n’apparaît. [Résolution de problèmes](/help/troubleshooting) explique la suite.

## HYDROS

:::note Beta
**Beta.** HYDROS est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’en êtes pas un, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Certaines mesures ou commandes peuvent ne pas encore marcher. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

HYDROS est la seule intégration qui n’a pas besoin que votre Cora et votre contrôleur soient sur le même réseau. Cora le rejoint par le cloud propre à HYDROS, ce qui le fait continuer à marcher loin de chez vous, et même Cora fermé.

Pour le connecter, ouvrez l’application HYDROS et créez une **clé d’appareil** pour le fournisseur **cora-iq**. Choisissez **Lecture** si vous voulez seulement ses mesures, ou **Écriture** si vous voulez aussi le contrôler depuis Cora. Allez ensuite dans **Appareils → Ajouter un appareil → HYDROS** et collez la clé.

Une fois lié, Cora importe les 33 derniers jours de son historique, puis continue à lire à partir de là. [Contrôler votre équipement](/help/mobile-device-control) explique ce que vous pouvez lire et, avec une clé d’écriture, contrôler.

## Focustronic

:::note Beta
**Beta.** Focustronic est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’en êtes pas un, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

Cora lit les appareils Focustronic Alkatronic, Dosetronic et Mastertronic via votre compte Focustronic. Cela marche donc loin de chez vous et ne demande pas de Cora Max.

Allez dans **Appareils → Ajouter un appareil → Focustronic** et connectez-vous avec le compte que vous utilisez dans l’application Focustronic. Choisissez l’aquarium de chaque appareil, puis touchez **Associer à Cora**. **Rester connecté** permet à Cora de garder votre mot de passe Focustronic, chiffré, et de se reconnecter toute seule. Si vous le désactivez, Cora ne garde qu’une connexion temporaire et vous envoie une notification quand vous devez vous reconnecter.

Chaque appareil affiche son état, son micrologiciel, son dernier test et, pour un Alkatronic, l’alcalinité et le pH mesurés. Vous voyez aussi les pompes avec ce qu’il reste dans chacune, les paramètres, les flacons et les avertissements de réactif ou de tampon. Cora demande de nouvelles mesures à Focustronic toutes les 30 minutes.

Sous **Commandes**, vous pouvez **Mesurer maintenant**, **Doser maintenant** depuis une pompe (jusqu’à 500 mL à la fois) et, sur un Mastertronic, **Tester maintenant**. Chacune vous demande d’abord de confirmer. Cora ne retente jamais un dosage : si le résultat indique qu’il est inconnu, vérifiez l’appareil. Les commandes passent par les serveurs de Focustronic, que Cora ne contrôle pas, et ne sont possibles que lorsque l’appareil est en ligne.

Si Focustronic refuse la connexion, ouvrez **Ajouter Focustronic** et reconnectez-vous.

## Moniteur d’air ambiant Inkbird

:::note Beta
**Beta.** Inkbird est en Beta et n’est ouvert qu’aux utilisateurs Beta. Si vous n’en êtes pas un, vous ne le verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

Cora lit un moniteur d’air ambiant Inkbird IAM-T1 ou IAM-T2. Un Cora Max placé à l’aquarium le lit en Bluetooth, et Cora n’écrit jamais rien sur le moniteur. La ligne affiche **Nécessite Cora Max** tant que l’aquarium n’en a pas.

Allez dans **Appareils → Ajouter un appareil → Inkbird** : Cora recherche les moniteurs à proximité. Choisissez le vôtre et touchez **Associer à un bac**. Si aucun n’apparaît, rapprochez-vous et touchez **Rechercher à nouveau**. Le Bluetooth doit être activé, avec l’autorisation pour Cora.

La page du moniteur affiche sa dernière mesure. **Intervalle de mesure** règle la fréquence à laquelle un Cora Max le lit. Tant qu’aucun Cora Max ne l’a lu, la page indique **En attente de Cora Max**, et s’il devient silencieux elle affiche **Ne répond pas** et Cora vous prévient. Les mesures de la pièce alimentent aussi [Reef Buddy](/help/mobile-reef-buddy). Pour arrêter, touchez **Dissocier**. Cora Max cesse de le lire et l’historique reste.

## Saisir à la main

Certains paramètres viennent d’un test en kit, pas d’un équipement. Pour saisir un résultat, faites défiler jusqu’en bas du tableau de bord et touchez **Enregistrer les paramètres**.

Les mesures saisies à la main comptent autant que les autres. Elles s’affichent sur les widgets avec leur propre source et leur âge, et elles alimentent Reef Buddy. C’est aussi à elles que Cora compare vos sondes quand il vous signale que deux sources ne sont pas d’accord.

## Si une connexion ne marche plus

La ligne de l’appareil indique de quel type de problème il s’agit. Consultez le tableau de la page **[Ajouter, modifier et retirer des appareils](/help/mobile-devices)**. Pour les autres cas, voir **[Résolution de problèmes](/help/troubleshooting)**.
