---
title: Connecter votre équipement
description: Comment connecter à Cora un Neptune Apex, un Red Sea ReefBeat, un Jecod ou un AquaWiz.
section: Cora Mobile
reviewed: 2026-10-17
order: 12
group: Equipment
---

Cette page montre comment connecter chaque marque d’équipement à Cora et ce dont chaque connexion a besoin. Toutes commencent de la même façon : **Appareils → Ajouter un appareil**, puis choisissez la marque.

![La liste des marques dans Ajouter un appareil](img/mobile-add-device-brands.webp "La liste des marques.")


| Marque | Ouvre | Sans Cora Max |
|---|---|---|
| Cora | Une recherche de nouveau Cora Max, en Wi-Fi ou en Bluetooth | |
| Neptune Apex | Une recherche sur le réseau ou son adresse IP, puis les aquariums qu’il dessert | Local uniquement |
| Red Sea | Une recherche sur votre réseau, puis l’aquarium de chaque appareil | Local uniquement |
| Jecod / Jebao | Une recherche sur votre réseau, ou en Bluetooth | Local uniquement |
| AquaWiz | Vos identifiants AquaWiz | Fonctionne |

## Sans Cora Max : local uniquement {#local-only}

Les équipements Neptune Apex, Red Sea et Jecod sont sur votre réseau domestique (ou en Bluetooth). Si vous n’avez pas de Cora Max (ou aucun sur l’aquarium auquel vous ajoutez l’équipement), l’écran d’ajout de ces marques indique *Sans Cora Max, cette intégration fonctionne uniquement en local dans l'application Mobile.* Cela veut dire :

- Votre téléphone lit et commande l’équipement tant que Cora Mobile est ouvert sur le même réseau, ou à portée Bluetooth.
- Loin de chez vous, vous voyez les dernières mesures enregistrées par votre téléphone, et vous ne pouvez pas le commander.

Un Cora Max à l’aquarium lit cet équipement jour et nuit et transmet vos commandes quand vous êtes absent. AquaWiz est joint par le service du fabricant, il fonctionne donc de partout sans Cora Max. Plus de détails dans [Plus d’un appareil Cora](/help/mobile-multi-device).

## Neptune Apex {#neptune-apex}

Cora lit votre Apex sur votre réseau local, y compris les sondes, les prises et les modules d’extension que vous avez installés.

1. Allez dans **Appareils → Ajouter un appareil → Neptune Apex**.
2. Touchez **Rechercher un APEX sur le réseau** et choisissez votre Apex, ou tapez son adresse sous **Ou saisissez l’IP manuellement :**.
3. Remplissez **Connexion Apex (seulement si vous en avez défini une sur l’Apex) :**. Laissez le mot de passe vide si vous n’en avez pas défini.
4. Touchez **Charger les mesures depuis l’APEX** et cochez celles que vous voulez sous **Mesures à suivre**.
5. Réglez la **Fréquence d’interrogation**. Ne la laissez pas désactivée : sans interrogation, rien ne lit l’Apex et ses mesures deviennent périmées.
6. Touchez **Continuer**, cochez chaque aquarium sous **Quels aquariums cet Apex dessert-il ?**, puis touchez **Enregistrer**. Un Apex peut desservir plusieurs aquariums.

Si la recherche ne trouve rien, vérifiez que votre téléphone est sur le même Wi-Fi que l’Apex, ou saisissez vous-même l’adresse IP.

Une fois connecté, chaque sonde que signale votre Apex devient une source que vous pouvez mettre sur un tableau de bord. Les prises apparaissent comme des commandes, et chaque module d’extension installé a sa propre tuile d’appareil. Votre propre programmation Apex continue de tourner exactement comme vous l’avez configurée. Ce que vous pouvez commander est dans [Contrôler votre équipement](/help/mobile-device-control#neptune-apex).

## Red Sea ReefBeat {#red-sea-reefbeat}

Cora communique avec l’équipement ReefBeat sur votre réseau local. Il prend en charge **ReefDose**, **ReefATO+**, **ReefMat** et **ReefRun**.

1. Configurez d’abord l’appareil dans l’application ReefBeat de Red Sea, et vérifiez qu’il est sur le même réseau que votre téléphone.
2. Allez dans **Appareils → Ajouter un appareil → Red Sea**. Cora recherche sur votre réseau.
3. Choisissez l’aquarium auquel appartient chaque appareil.

Un appareil Red Sea dessert un seul aquarium. En choisir un autre l’y déplace.

Chaque appareil a sa propre page, et ses mesures deviennent des sources. ReefDose signale ses têtes et ses réservoirs, ReefATO+ son réservoir et ses remplissages, ReefMat les jours qui lui restent, et ReefRun l’état de ses pompes. Ce que chaque page vous permet de faire est dans [Contrôler votre équipement](/help/mobile-device-control#red-sea).

## Jecod / Jebao {#jecod}

Cora se connecte aux pompes Jecod et peut les lire et les commander. Ajoutez-en une depuis **Appareils → Ajouter un appareil → Jecod**. Une pompe Jecod rejoint Cora de l’une de deux façons, et cela décide de ce que vous pouvez en faire.

![L’écran d’ajout d’une pompe dans Cora Mobile, sans pompe trouvée pour l’instant](img/mobile-connections.webp "Aucune pompe vue pour l’instant : la recherche explique ce dont elle a besoin et pourquoi une pompe peut manquer un passage.")

**Par votre réseau.** La recherche trouve les pompes qui s’annoncent, vous n’avez donc pas à taper d’adresse. Vous pouvez lire et piloter une pompe réseau tant qu’elle est alimentée et joignable. Cela veut dire que votre téléphone est sur le même réseau, ou qu’un Cora Max sur ce réseau transmet vos commandes. Si vous êtes loin de chez vous et qu’il n’y a pas de Cora Max sur place, vous voyez une pompe réseau mais vous ne pouvez pas la commander.

:::note Une pompe manque souvent la première recherche
Les pompes répondent à une recherche et manquent la suivante. Si la vôtre n’est pas listée, relancez la recherche avant de conclure qu’elle est injoignable.
:::

Si une recherche ne trouve rien, le résultat montre les adresses vérifiées en Wi-Fi. Si l’application Jebao affiche une autre adresse pour votre pompe, votre téléphone est sur un autre réseau. Un réseau invité ou IoT, ou une bande 5 GHz uniquement, ne voit pas ces pompes. Sur iPhone, Cora a aussi besoin de l’accès au réseau local pour voir les pompes sur votre Wi-Fi. Sans lui, la liste reste vide et aucune erreur n’apparaît : le résultat l’explique donc et propose **Ouvrir les Réglages** pour le réactiver. Vous pouvez aussi y accéder à tout moment depuis **Réglages → Accès aux appareils**, décrit dans [Réglages](/help/mobile-settings).

**En Bluetooth.** Certaines pompes ne sont joignables que depuis un téléphone qui se trouve près d’elles. La page de la pompe l’indique, et affiche les derniers réglages lus et leur ancienneté. Cora a besoin de l’autorisation Bluetooth pour cela. Accordez-la avant d’ajouter une pompe Bluetooth, sinon Cora ne peut pas du tout trouver la pompe.

:::warning Vous devez être près d’une pompe Bluetooth
Sa page affiche les derniers réglages lus par Cora et il y a combien de temps. Changer quoi que ce soit, même lancer une pause nourrissage, demande que la pompe soit à portée. Placez-vous près d’elle et rouvrez la page.
:::

Avec l’une ou l’autre connexion, vous avez l’état en direct, le mode et l’intensité, une pause nourrissage et un programme journalier. Une pause nourrissage lancée depuis votre téléphone demande, sur certaines pompes, que la page de la pompe reste ouverte. Les détails sont dans [Contrôler votre équipement](/help/mobile-device-control#jecod), et [Programmer l’équipement](/help/mobile-schedules) explique le programme journalier.

## AquaWiz KH Controller {#aquawiz-kh-controller}

Cora lit l’alcalinité d’un contrôleur KH AquaWiz par votre compte AquaWiz : cela fonctionne donc loin de chez vous et ne nécessite pas de Cora Max.

1. Allez dans **Appareils → Ajouter un appareil → AquaWiz**.
2. Saisissez votre nom d’utilisateur et votre mot de passe AquaWiz et touchez **Connecter**.
3. Choisissez l’aquarium, vérifiez **Lire aussi son pH** (il est activé au départ pour un appareil qui signale le pH), et touchez **Lier à Cora**.

Avec **Rester connecté automatiquement** activé, Cora garde votre mot de passe AquaWiz et renouvelle la connexion tout seul. Désactivé, Cora ne garde qu’un jeton de connexion, qu’AquaWiz fait expirer environ tous les 30 jours, et vous envoie une notification quand il est temps de vous reconnecter.

Vous obtenez l’alcalinité comme source, et aussi le pH si votre appareil le signale et que **Lire aussi son pH** est activé. Votre première mesure arrive dès que vous liez l’appareil. Ensuite, AquaWiz ne laisse Cora lire son cloud automatiquement que toutes les 12 heures : une mesure venue de là peut avoir jusqu’à une demi-journée. Un Cora Max à l’aquarium peut aussi lire lui-même le contrôleur toutes les heures quand il peut l’atteindre. Ouvrez la page de l’appareil pour voir quand chaque mesure a été prise et d’où elle vient, et touchez **Lire maintenant** pour en avoir une fraîche (au plus une fois toutes les 15 minutes). Ce qu’affiche la carte AquaWiz, et ses alertes, sont dans [Contrôler votre équipement](/help/mobile-device-control#aquawiz).

:::warning Cora partage votre connexion AquaWiz
AquaWiz donne une seule connexion par compte, donc Cora utilise la même que l’application AquaWiz. Si vous changez votre mot de passe AquaWiz, Cora se déconnecte. Reconnectez-le ensuite depuis la ligne de l’appareil. Pour retirer complètement l’accès de Cora, retirez l’appareil dans Cora et changez votre mot de passe AquaWiz.
:::


## Saisie manuelle {#logging-by-hand}

Certains paramètres viennent d’un kit de test, pas d’un équipement. Pour saisir un résultat, faites défiler jusqu’en bas du tableau de bord et touchez **Enregistrer les paramètres**.

Les mesures que vous notez à la main comptent autant que les autres. Elles s’affichent sur les widgets avec leur propre source et leur âge, et elles alimentent Reef Buddy. Cora compare aussi vos sondes avec elles quand il vous dit que deux sources ne sont pas d’accord.

## Si une connexion cesse de fonctionner {#if-a-connection-stops-working}

La ligne de l’appareil vous dit de quel genre de problème il s’agit. Cherchez-le dans le tableau de [Ajouter, modifier et retirer des appareils](/help/mobile-devices#health). Pour tout ce qu’il ne couvre pas, voir [Résolution de problèmes](/help/troubleshooting).
