---
title: Caméras et surveillance de l’écumeur
description: Ajoutez une caméra Wyze, Tapo, Sonoff ou une autre caméra RTSP à Cora, regardez-la en tuile ou en plein écran, et laissez la surveillance de l’écumeur vous prévenir avant que le godet déborde.
section: Cora Mobile
reviewed: 2026-10-12
order: 35
group: Equipment
---

:::note Beta
**Beta.** Les caméras sont en Beta et ne sont ouvertes qu’aux utilisateurs Beta. Si vous n’en êtes pas un, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

Ajoutez une caméra pour voir votre aquarium depuis Cora, sur votre téléphone et sur Cora Max. Une caméra a besoin d’un Cora Max à l’aquarium : la ligne **Caméra** affiche donc **Nécessite Cora Max** tant que l’aquarium n’en a pas.

## Ajouter une caméra

1. Allez dans **Appareils → Ajouter un appareil → Caméra**, puis **Ajouter une caméra**.
2. Choisissez le type : Wyze, Tapo, Sonoff ou **Autre caméra (RTSP)**.
3. Suivez les étapes que Cora affiche pour ce type. Elles vous disent ce qu’il faut activer d’abord dans l’application de la caméra.
4. Renseignez le nom, l’adresse du flux, le nom d’utilisateur, le mot de passe et l’aquarium, puis touchez **Tester la connexion**. Quand la caméra répond, touchez **Ajouter la caméra**.

Votre téléphone doit être sur le même Wi-Fi que la caméra pendant l’ajout. L’adresse doit être sur votre réseau domestique, et vous saisissez le nom d’utilisateur et le mot de passe dans leurs propres champs, pas dans l’adresse.

Les caméras Wyze, Tapo et Sonoff ont été testées (Wyze Cam v4, Tapo C120 et Sonoff Cam S3W). D’autres caméras compatibles RTSP peuvent aussi fonctionner.

| Caméra | À activer d’abord |
|---|---|
| Wyze | Dans l’application Wyze, ouvrez la caméra, puis Paramètres, Paramètres avancés, RTSP. Activez RTSP, choisissez un nom d’utilisateur et un mot de passe, puis redémarrez la caméra. La caméra doit avoir le micrologiciel 4.52.17 ou plus récent. |
| Tapo | Dans l’application Tapo, ouvrez Paramètres, Paramètres avancés, Compte de la caméra et créez un nom d’utilisateur et un mot de passe. Ce n’est pas votre compte TP-Link. Une caméra Tapo ne peut utiliser que deux fonctions à la fois parmi Tapo Care, l’enregistrement sur carte SD et la diffusion vers d’autres applications. |
| Sonoff | Dans eWeLink, activez RTSP pour la caméra et définissez son compte. Cora remplit pour vous un préréglage **Adresse Sonoff**. |
| Autre caméra (RTSP) | Activez RTSP ou ONVIF dans l’application de la caméra, définissez un identifiant de caméra, et saisissez l’adresse du flux indiquée dans son manuel. Laissez l’identifiant vide si votre caméra n’en a pas. |

## Modifier une caméra

Ouvrez la caméra et utilisez son menu : **Renommer**, **Modifier les adresses**, **Changer le mot de passe** ou **Retirer la caméra**. La retirer supprime aussi son mot de passe enregistré.

## La regarder

Une caméra peut être une tuile de votre tableau de bord, jusqu’à 3×2, et vous pouvez l’ouvrir en **Plein écran** et la faire **Pivoter**.

À la maison, avec votre téléphone sur le Wi-Fi de la caméra, Cora lit la **Vidéo en direct** directement depuis la caméra. Loin de chez vous, ou quand vous choisissez **Instantanés**, votre Cora Max prend des images fixes de la caméra et Cora les affiche comme du quasi-direct, actualisées toutes les quelques secondes. Si Cora Max n’envoie pas d’images, la tuile le dit.

## Surveillance de l’écumeur

:::note Beta
**Beta.** La surveillance de l’écumeur est en Beta et n’est ouverte qu’aux utilisateurs Beta. Elle demande aussi un forfait payant : **La surveillance de l’écumeur fait partie des forfaits payants.** Pour demander l’accès Beta, contactez le [support](/support.html).
:::

La surveillance de l’écumeur observe le godet de récupération de l’écumeur avec une caméra et vous prévient avant qu’il déborde. Elle se trouve sur la page de la caméra, dans la carte **Surveillance écumeur**.

1. Pointez la caméra vers le godet et activez **Surveiller le godet**.
2. Touchez **Marquer le godet**. Faites glisser le cadre sur le godet et ajustez les coins : le bord du bas sur le fond du godet, le bord du haut juste sous le bord, là où le godet est plein.
3. Videz le godet et touchez **Le godet est vide maintenant**. Cora prend une image du godet vide pour comparer. Cela prend environ 10 secondes. Si vous déplacez la caméra ou le cadre, refaites cette étape.
4. Réglez **Alerte à** sur le niveau de remplissage qui doit vous prévenir. La carte l’affiche en pourcentage.

Cora Max vérifie le godet toutes les quelques minutes. La carte affiche la dernière mesure et son ancienneté. **Vérifier maintenant** demande une vérification immédiate, qui prend environ 10 secondes. **Dernières 24 heures** montre comment le godet s’est rempli au fil de la journée.

Si l’image est difficile à lire, la carte le dit, par exemple **Lumière trop forte derrière le godet**.

### Conseils pour la caméra

**Conseils pour la caméra**, sur la carte, vous donne les mêmes conseils qu’ici.

- Réglez la vision nocturne de la caméra sur Activée (toujours infrarouge), pas sur Auto, pour que chaque image soit identique de jour comme de nuit.
- Réglez le projecteur de la caméra sur Manuel et laissez-le éteint. Les bulles et l’eau de la décantation comptent comme du mouvement et l’allument sans cesse.
- Évitez qu’une lumière forte éclaire directement la caméra depuis l’arrière du godet.

## Ce qu’il advient des images

À la maison, la vidéo est lue directement depuis la caméra et n’est pas enregistrée. Loin de chez vous, une seule image fixe est conservée par caméra, et chaque nouvelle remplace la précédente. La surveillance de l’écumeur garde la dernière image du godet marqué, les niveaux de remplissage des dernières 24 heures (des chiffres uniquement) et une petite image du godet vide. Tout est supprimé quand vous retirez la caméra, l’aquarium ou votre compte. La [politique de confidentialité](/privacy-policy.html) (en anglais) donne tous les détails.
