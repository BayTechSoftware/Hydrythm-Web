---
title: Caméras et surveillance de l’écumeur
description: Ajoutez une caméra Wyze, Tapo, Sonoff ou autre caméra RTSP à Cora, regardez votre aquarium sur une tuile ou en plein écran, et laissez la surveillance de l’écumeur vous prévenir avant que le godet de l’écumeur ne déborde.
section: Cora Mobile
reviewed: 2026-10-13
order: 17
group: Equipment
---

:::note Beta
**Beta.** Les caméras sont en Beta et ne sont ouvertes qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Plus de détails dans [Fonctions Beta](/help/mobile-beta).
:::

Ajoutez une caméra pour voir votre aquarium depuis Cora, sur votre téléphone et sur Cora Max, et pour laisser la surveillance de l’écumeur garder un œil sur le godet de l’écumeur. Commencez par **Appareils → Ajouter un appareil → Caméra**. Une caméra a besoin d’un Cora Max à l’aquarium, donc la ligne **Caméra** affiche **Nécessite Cora Max** tant que l’aquarium n’en a pas.

## Ajouter une caméra {#adding-a-camera}

1. Allez dans **Appareils → Ajouter un appareil → Caméra**, puis **Ajouter une caméra**.
2. Choisissez le type : Wyze, Tapo, Sonoff ou **Autre caméra (RTSP)**.
3. Suivez les étapes que Cora affiche pour ce type. Elles vous disent quoi activer d’abord dans l’application de la caméra.
4. Remplissez le nom, l’adresse du flux, le nom d’utilisateur, le mot de passe et l’aquarium, puis touchez **Tester la connexion**. Quand la caméra répond, touchez **Ajouter la caméra**.

Votre téléphone doit être sur le même Wi-Fi que la caméra pendant l’ajout. L’adresse doit être sur votre réseau domestique, et vous saisissez le nom d’utilisateur et le mot de passe dans leurs propres champs, pas dans l’adresse.

Les caméras Wyze, Tapo et Sonoff ont été testées (Wyze Cam v4, Tapo C120 et Sonoff Cam S3W). D’autres caméras qui proposent le RTSP peuvent aussi fonctionner.

| Caméra | Activez d’abord ceci |
|---|---|
| Wyze | Dans l’application Wyze, ouvrez la caméra, puis Settings, Advanced Settings, RTSP. Activez le RTSP, choisissez un nom d’utilisateur et un mot de passe, puis redémarrez la caméra. La caméra doit avoir le micrologiciel 4.52.17 ou plus récent. |
| Tapo | Dans l’application Tapo, ouvrez Paramètres, Paramètres avancés, Compte de la caméra et créez un nom d’utilisateur et un mot de passe. Ce n’est pas votre compte TP-Link. Une caméra Tapo ne peut faire tourner que deux de ces fonctions à la fois : Tapo Care, l’enregistrement sur carte SD et la diffusion vers d’autres applications. |
| Sonoff | Dans eWeLink, activez le RTSP pour la caméra et réglez son compte. Cora remplit pour vous un préréglage **Adresse Sonoff**. |
| Autre caméra (RTSP) | Activez le RTSP ou l’ONVIF dans l’application de la caméra, créez un identifiant pour la caméra, et saisissez l’adresse du flux indiquée dans son manuel. Laissez l’identifiant vide si votre caméra n’en a pas. |

## Modifier une caméra {#changing-a-camera}

Ouvrez la caméra et utilisez son menu : **Renommer**, **Modifier les adresses**, **Changer le mot de passe** ou **Retirer la caméra**. La retirer supprime aussi son mot de passe enregistré.

## La regarder {#watching-it}

![La page d’une caméra](img/mobile-camera.webp "La page de la caméra, avec l’image en haut et la carte Surveillance écumeur en dessous.")

Une caméra peut être une tuile de votre tableau de bord, jusqu’à 3×2. Voir [Modifier votre tableau de bord](/help/mobile-dashboard-editing). Ouvrez-la pour **Plein écran** et **Pivoter**.

À la maison, avec votre téléphone sur le Wi-Fi de la caméra, Cora lit la **Vidéo en direct** directement depuis la caméra. Loin de chez vous, ou quand vous choisissez **Instantanés**, votre Cora Max prend des images fixes de la caméra et Cora les affiche en quasi-direct, mises à jour toutes les quelques secondes. Si Cora Max n’envoie pas d’images, la tuile l’indique.

## Surveillance de l’écumeur {#skimmer-watch}

:::note Beta
**Beta.** La surveillance de l’écumeur est en Beta et n’est ouverte qu’aux utilisateurs Beta. Elle demande aussi un forfait payant. Sans forfait payant, la carte indique **La surveillance de l'écumeur fait partie des forfaits payants.** et propose **Voir les forfaits**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

La surveillance de l’écumeur surveille le godet de l’écumeur grâce à une caméra et vous prévient avant qu’il ne déborde. Elle se trouve sur la page de la caméra, dans la carte **Surveillance écumeur**.

![Marquer le godet](img/mobile-camera-mark-cup.webp "Faites glisser le cadre sur le godet : bord inférieur au fond du godet, bord supérieur juste sous le rebord.")

1. Orientez la caméra vers le godet et activez **Surveiller le godet**.
2. Touchez **Marquer le godet**. Faites glisser le cadre sur le godet et tirez les coins pour l’ajuster : le bord inférieur au fond du godet, le bord supérieur juste sous le rebord, là où le godet est plein. Ensuite, le bouton devient **Déplacer le cadre du godet**.
3. Videz le godet et touchez **Le godet est vide maintenant**. Cora prend une photo du godet vide pour comparer. Cela prend environ 10 secondes. Si vous déplacez la caméra ou le cadre, recommencez.
4. Faites glisser le curseur **Alerte à** jusqu’au niveau de remplissage qui doit vous prévenir. Gardez de la marge, car Cora vérifie toutes les 15 minutes.

![La carte Surveillance écumeur sur la page d’une caméra](img/mobile-skimmer-watch.webp "Le godet est vide maintenant, la dernière mesure, les dernières 24 heures, Vérifier maintenant et les conseils pour la caméra.")

Cora Max vérifie le godet toutes les 15 minutes. La carte affiche la dernière mesure et son ancienneté, et la tuile caméra de votre tableau de bord affiche aussi le niveau du godet. **Vérifier maintenant** vérifie le godet tout de suite, ce qui prend environ 10 secondes. **Dernières 24 heures** montre comment le godet s’est rempli au fil de la journée.

Quand le godet atteint votre niveau **Alerte à**, vous recevez une seule notification. Elle est envoyée sous **Pannes d’équipement**, alors gardez cette catégorie activée dans [Notifications](/help/mobile-notifications). Une fois le godet vidé, l’alerte peut se déclencher à nouveau.

### Si la mesure semble fausse {#skimmer-watch-problems}

| La carte indique | Que faire |
|---|---|
| **Lumière trop forte derrière le godet** | Éteignez ou déplacez la lumière derrière le godet. Voir les conseils pour la caméra plus bas |
| **Pas sûr (faible confiance)** | L’image était difficile à lire. Vérifiez les conseils pour la caméra, puis touchez **Vérifier maintenant** |
| **Marquez d'abord le godet** | Touchez **Marquer le godet** et dessinez le cadre |
| **Non calibré : videz le godet et touchez Le godet est vide maintenant** | Videz le godet, puis touchez **Le godet est vide maintenant** |
| **Cadre déplacé : calibrez à nouveau** | Vous avez déplacé le cadre. Videz le godet et touchez à nouveau **Le godet est vide maintenant** |
| **Cora Max n'a pas pu obtenir d'image de la caméra.** | Vérifiez que la caméra est allumée et que le Cora Max de l’aquarium est en ligne |
| **La dernière vérification a échoué.** | Touchez **Vérifier maintenant**. Si cela échoue encore, voir [Résolution de problèmes](/help/troubleshooting) |
| **Pas encore de mesure. Cora Max vérifie toutes les 15 minutes.** | Attendez la première vérification, ou touchez **Vérifier maintenant** |

### Conseils pour la caméra {#camera-tips}

**Conseils pour la caméra** sur la carte vous donne les mêmes conseils qu’ici.

- Réglez la vision nocturne de la caméra sur Activée (infrarouge en permanence), pas sur Auto, pour que chaque image soit la même de jour comme de nuit.
- Réglez le projecteur de la caméra sur Manuel et laissez-le éteint. Les bulles et l’eau de la décantation comptent comme du mouvement et le rallument sans cesse.
- Évitez que des lumières fortes n’éclairent la caméra de face depuis l’arrière du godet.

### Sur Cora Max {#skimmer-watch-on-cora-max}

![Des tuiles caméra sur Cora Max, l’une affichant le niveau du godet de l’écumeur](img/max-skimmer-watch.webp "Sur Cora Max, la tuile caméra affiche le niveau du godet et l’âge de la mesure.")

Sur Cora Max, la tuile caméra et la caméra en plein écran affichent **Godet** avec le niveau de remplissage et l’âge de la mesure. La puce passe à l’orange quand le godet est à moins de 10 points de votre niveau d’alerte et au rouge quand il l’atteint. Sur la caméra en plein écran, le bouton **Alerte à** ouvre **Alerte du godet de l'écumeur**, où vous pouvez aussi changer le niveau. Pendant une vérification, l’image en direct peut se figer quelques secondes. Plus de détails dans [Contrôler l’équipement depuis Cora Max](/help/max-device-control).

## Ce que deviennent les images {#pictures}

À la maison, la vidéo est lue directement depuis la caméra et n’est pas enregistrée. Loin de chez vous, une seule image fixe par caméra est gardée, et chaque nouvelle remplace la précédente. La surveillance de l’écumeur garde la dernière image du godet marqué, les 24 dernières heures de mesures de remplissage (des nombres uniquement) et une petite image du godet vide. Elles sont supprimées quand vous retirez la caméra ou supprimez votre compte. La [politique de confidentialité](/privacy-policy.html) donne tous les détails.
