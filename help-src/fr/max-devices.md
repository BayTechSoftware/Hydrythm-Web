---
title: Appareils et état des appareils
description: Voyez et renommez l’équipement que lit Cora Max, choisissez quel Cora Max lit chaque aquarium, réparez un aquarium dont les mesures se sont arrêtées et gérez un Cora Max depuis votre téléphone.
section: Cora Max
reviewed: 2026-10-13
order: 7
group: Equipment
twin: mobile-devices
---

**Réglages → Appareils** sur Cora Max liste l’équipement qu’il voit et l’état de chaque appareil. L’icône des appareils dans la barre du haut ouvre la même liste, filtrée sur l’aquarium affiché.

## La liste des appareils {#the-device-list}

![La liste des appareils sur Cora Max, filtrée par aquarium et regroupée par marque](img/max-devices.webp "Filtrez par aquarium, puis chaque appareil regroupé par marque, avec un résumé d’une ligne et son aquarium.")

Cora Max voit le même équipement que votre téléphone, car ils lisent tous les deux le même compte.

Utilisez les puces de filtre en haut pour afficher **Tous les aquariums** ou un seul. Les appareils sont regroupés par marque. Chaque entrée a un point d’état (gris quand Cora ne sait pas encore, vert quand il fonctionne, orange pour un avertissement ou une panne, rouge quand il est hors ligne), un résumé d’une ligne de ce que contient l’appareil (*21 prises · 4 nourrissages*, *19 tests restants*), l’aquarium auquel il appartient et sa **Dernière connexion**. Les appareils en Beta portent une puce **Bêta**.

Touchez un appareil pour ouvrir sa page. Chaque page d’appareil commence par une section **État**. Ce que chaque page permet de faire est expliqué dans [Contrôler l’équipement depuis Cora Max](/help/max-device-control).

Si la liste indique **Chargement de certains appareils en cours : cette liste peut être incomplète.**, patientez un instant.

:::note Beta
**Beta.** Les lampes, pompes et doseurs EcoTech, les moniteurs d’air ambiant Inkbird et les caméras sont en Beta et ne sont ouverts qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Plus de détails dans [Fonctions Beta](/help/mobile-beta).
:::

### Renommer un appareil {#renaming-a-device}

Touchez le crayon sur la ligne d’un appareil, ou sur sa page, et tapez le nouveau nom. Laissez le nom vide pour revenir au nom propre de l’appareil. Le nom est partagé avec votre téléphone, il change donc là aussi.

### Ajouter et retirer des appareils {#adding-and-removing-devices}

Vous ajoutez, attribuez et retirez des appareils sur votre téléphone. Cora Max les affiche et les commande. Tant qu’il n’y a aucun appareil, cet écran indique **Ajoutez des appareils dans l’application Cora.** Plus de détails dans [Ajouter, modifier et retirer des appareils](/help/mobile-devices).

## Cora Max principal : quel appareil parle à votre équipement {#primary-cora-max}

Le **Cora Max principal** est le Cora Max (ou autre appareil Cora) qui lit le contrôleur et les autres équipements d’un aquarium pour tout le compte. Chaque aquarium n’a besoin que d’un appareil pour cela. Tous les autres écrans affichent ce qu’il lit.

Pour le voir ou le changer, ouvrez **Réglages → [votre aquarium] → Cora Max principal**. Vous avez deux options.

- **Tout appareil actif (automatique)** veut dire que chaque appareil Cora en ligne qui peut joindre l’équipement de cet aquarium partage le travail, et la dernière écriture l’emporte. Utilisez cette option sauf si vous avez une raison d’épingler un appareil.
- Épinglez un appareil, pour que lui seul lise l’équipement. S’il se déconnecte, aucun autre Cora Max ne prend le relais. Seul Cora Mobile, ouvert sur le même Wi-Fi, lit l’équipement jusqu’à ce que vous en épingliez un autre ou que vous repassiez sur **Tout appareil actif (automatique)**.

Vous le réglez une fois pour l’aquarium, et il s’applique à tous les écrans Cora. Vous pouvez le changer depuis n’importe quel Cora Max qui affiche l’aquarium, ou depuis Cora Mobile (**Définir comme Cora Max principal** sur la page du Cora Max). Plus de détails dans [Plus d’un appareil Cora](/help/mobile-multi-device).

:::note Le Cora Max principal et l’appareil répondant sont deux réglages distincts
Le Cora Max principal décide quel appareil **lit votre équipement**. L’**Appareil répondant** dans Cora Mobile décide lequel **répond à "Hey Cora"**. Si vous avez plusieurs Cora Max, vous pouvez les régler séparément. Plus de détails dans [Parler à Cora](/help/max-voice).
:::

## Si les mesures d’un aquarium s’arrêtent {#if-a-tanks-readings-stop}

Si les mesures d’un aquarium s’arrêtent alors qu’un autre aquarium du même écran continue de se mettre à jour, commencez ici.

1. Ouvrez **Réglages → [cet aquarium] → Cora Max principal**. Vérifiez qu’un appareil est attribué et qu’il est en ligne.
2. Si un autre Cora Max de cet aquarium affiche **Cora principal hors ligne** dans sa barre du haut, le principal a perdu sa connexion. La signification de l’étiquette d’état est expliquée dans [L’écran d’accueil de Cora Max](/help/max-tour#what-the-status-pill-means).
3. **Réglages → Réglages Cora Max → Réseau et mises à jour → Interrogation des appareils** indique à quelle fréquence ce Cora Max lit vos appareils. Ici, vous pouvez seulement le consulter. Il se règle depuis Cora Mobile.
4. Vérifiez la section **État** de **Réglages → Réglages Cora Max**. Elle affiche l’état de l’interrogation, l’heure de la dernière interrogation et la dernière écriture cloud pour chaque aquarium, sans rien changer.

Si cela ne suffit pas, consultez [Résolution de problèmes](/help/troubleshooting).

## Gérer un Cora Max depuis votre téléphone {#managing-a-cora-max-from-your-phone}

Ouvrez l’onglet **Appareils** sur votre téléphone et touchez le Cora Max. La carte du haut indique sa variante, son micrologiciel et sa dernière connexion. De là, vous pouvez le renommer, et quand une nouvelle version existe, toucher **Mettre à jour vers v…** pour l’installer maintenant. La carte **Code PIN de récupération** se trouve juste en dessous.

![La page d’un Cora Max dans Cora Mobile, avec Verrouillage enfant, Interrogation de l’appareil, Fuseau horaire et Aquariums attribués](img/max-from-phone.webp "Les réglages propres d’un Cora Max sur votre téléphone : Verrouillage enfant, Interrogation de l’appareil et Fuseau horaire, puis ses aquariums.")

Ces réglages ne concernent que **cet écran-là**, exactement comme si vous les changiez au mur :

| Section | Réglages |
|---|---|
| **Affichage** | **Luminosité**, **Atténuer après** |
| **Son et voix** | **Son d’alerte** active ou désactive le carillon d’alerte sur cet écran, et **Volume des alertes** règle son niveau. Les alertes s’affichent toujours à l’écran, et l’historique des alertes et les notifications push ne changent pas |
| **Verrouillage enfant** | **Verrouillage enfant** verrouille l’écran tactile de cet écran et l’empêche de commander l’équipement à la voix |
| **Réseau et mises à jour** | **Interrogation de l’appareil** (la fréquence à laquelle il lit votre équipement) et **Fuseau horaire** (utilisé pour l’atténuation nocturne et la plage de mise à jour) |

Sous **Aquariums**, chaque aquarium affiché par ce Cora Max a une carte avec **Disposition du tableau de bord**, **Modifier l’aquarium** et son appareil d’interrogation. **Ajouter un aquarium** et l’icône de retrait changent les aquariums qu’il affiche, et ces changements s’appliquent à tout le compte. Vous ne pouvez les faire que sur votre téléphone. Les étapes sont dans [Configurer Cora Max](/help/max-setup#changing-which-tanks-it-shows). Le Cora Max principal d’un aquarium peut se changer depuis votre téléphone comme depuis Cora Max.

Sous **Réinitialisation**, **Réinitialiser l’écran** renvoie l’écran à son écran d’association. Il reste sur votre Wi-Fi, vous pouvez donc l’associer à nouveau en Bluetooth, et les données de vos aquariums sont conservées. **Retirer l’appareil** le retire de votre compte. Les mesures de vos aquariums sont conservées, et vous pourrez l’associer à nouveau plus tard.
