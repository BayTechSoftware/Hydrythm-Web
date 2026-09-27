---
title: Automatisations et scènes
description: Créez des règles qui tournent toutes seules (déclencheurs, conditions, actions) et regroupez des actions en scènes.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Une automatisation est une règle que Cora applique à votre place : *quand ceci arrive, vérifie cela, puis fais ceci.* Une scène regroupe plusieurs actions que vous lancez d’un coup, à la main ou selon un programme.

**Réglages → Automatisation.**

![La liste des automatisations](img/mobile-automation.webp "Automatisations et Scènes sont des onglets séparés. Chaque règle a un commutateur d’activation.")

L’écran a deux onglets, **Automatisations** et **Scènes**, et un bouton **Nouvelle automatisation**. Chaque règle affiche un résumé d’une ligne, un interrupteur d’activation et un menu pour la modifier ou la supprimer. Une règle qui n’a encore jamais tourné est signalée.

:::warning Les règles agissent sur du vrai matériel
Une règle qui coupe une pompe la coupe, que vous soyez là ou non. Créez une règle à la fois et vérifiez qu’elle fait ce que vous attendez avant de passer à la suivante.
:::

## Comment se construit une règle

Chaque règle a trois parties.

**Déclencheur** : ce qui la réveille
**Conditions** : ce qui doit aussi être vrai
**Actions** : ce qu’elle fait ensuite, dans l’ordre

## Ce qui réveille une règle

Il y a quatre déclencheurs.

| Déclencheur | Se déclenche quand |
|---|---|
| **Quand une valeur change** | Un paramètre franchit une valeur que vous avez fixée, dans le sens que vous avez choisi |
| **Quand une alerte se déclenche** | Une alerte se déclenche, se ferme, ou les deux |
| **À une heure de la journée** | Il est une certaine heure, dans votre propre fuseau horaire |
| **Quand un appareil passe hors ligne** | Un appareil se déconnecte ou revient en ligne |

## Conditions

Les conditions décident si les actions s’exécutent vraiment. Vous avez les comparaisons habituelles (égal, différent, supérieur à, inférieur à, etc.), que vous pouvez combiner avec **et**, **ou** et **non**.

Il existe aussi une condition d’**étape**. Elle regarde comment s’est passée l’étape *précédente*. Vous pouvez ainsi écrire « essaie ceci, et si ça n’a pas marché, fais cela ».

## Ce qu’une règle peut faire

Une action qui demande un équipement n’apparaît que sur un aquarium équipé.

| Action | Ce qu’elle fait |
|---|---|
| **Contrôler un équipement Apex** | Allumer ou éteindre une prise |
| **Contrôler un équipement Red Sea** | Piloter un appareil ReefBeat |
| **Contrôler une pompe de brassage** | Régler le débit, le mode de vague ou la puissance d’une pompe Jecod, ou **Mettre en pause pour le nourrissage**. Dans ce cas, le Cora Max de l’aquarium relance la pompe à la fin du nourrissage |
| **Contrôler un équipement Cora** | Allumer ou éteindre une prise connectée |
| **Contrôler un appareil IR** | Envoyer une commande infrarouge |
| **Lancer un cycle d’alimentation Apex** | Démarrer un nourrissage |
| **Lancer un test Trident** | Lancer un test |
| **Me notifier** | Vous envoyer une notification push |
| **Attendre avant l’étape suivante** | Faire une pause avant de continuer |
| **Lancer une scène** | Lancer une autre scène depuis cette règle |
| **Gérer une automatisation** | Activer ou désactiver une autre règle |
| **Doser une tête DŌS** | Envoyer une dose précise avec une tête DŌS |

:::warning Un dosage par règle est irréversible et plafonné
On ne peut pas retirer une dose de l’aquarium. Une règle ne peut doser avec une tête que si cette tête est **étalonnée**. Le dosage sans surveillance est plafonné à **10 mL par tête et par jour**, et aucune règle ne peut dépasser ce plafond, quelle que soit sa rédaction. Les actions de dosage n’apparaissent qu’une fois vos têtes reconnues comme têtes de dosage.
:::

:::note Utilisez Attendre pour enchaîner des étapes
Avec une pause, une seule règle peut suivre une procédure dans l’ordre. Par exemple, éteindre une prise, attendre, puis la rallumer. Pas besoin d’une deuxième règle ni d’un programme.
:::

## Scènes

Une scène est un groupe d’actions portant un nom, comme « Changement d’eau », « Mode photo » ou « Nuit ». Vous pouvez la lancer quand vous voulez, depuis un programme ou depuis une autre règle.

Une scène peut en appeler une autre. Cora refuse de lancer une scène imbriquée trop profondément, et refuse une scène qui s’appellerait elle-même. Cela évite une boucle qui agirait sans fin sur l’aquarium.

Après une scène, Cora vous montre ce qui s’est passé, étape par étape, y compris ce qui a échoué.

Quand vous lancez une scène à la main, Cora vous demande d’abord de confirmer. Une scène peut en effet actionner plusieurs équipements à la fois.

## Scènes créées sur Cora Max

Vous pouvez aussi créer et modifier des scènes directement sur un Cora Max. Ce sont les mêmes scènes que sur le téléphone, partagées dans tout le compte. Un Cora Max plus ancien peut lancer une scène créée sur le téléphone. La modification sur l’appareil est plus récente. Un ancien Cora Max peut donc afficher une scène sans vous laisser la modifier. Dans ce cas, modifiez-la depuis le téléphone.

## Désactiver une règle

Chaque règle a un interrupteur d’activation. Une règle désactivée garde ses réglages. C’est pratique si vous voulez la retrouver à la saison prochaine sans la recréer.

## Voir ce qu’une règle a fait

Chaque action d’une règle est enregistrée avec la règle comme source. Tout est dans **[Activité](/help/mobile-activity)**.
