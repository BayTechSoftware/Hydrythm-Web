---
title: Automatisations et scènes
description: Créez des règles qui s’exécutent seules (déclencheurs, conditions, actions) et regroupez-les en scènes.
section: Cora Mobile
reviewed: 2026-09-27
order: 17
group: Alerts and automation
---

Une automatisation est une règle que Cora exécute pour vous : *quand ceci arrive, vérifie cela, puis fais ceci.* Les scènes regroupent plusieurs actions en une seule chose que vous pouvez exécuter ou programmer.

**Réglages → Automatisation.**

![La liste des automatisations](img/mobile-automation.webp "Automatisations et Scènes sont des onglets séparés. Chaque règle a un commutateur d’activation.")

L’écran a deux onglets (**Automatisations** et **Scènes**) et un bouton **Nouvelle automatisation**. Chaque règle affiche un résumé en une ligne de ce qu’elle fait, un commutateur d’activation, et un menu pour la modifier ou la supprimer. Une règle qui ne s’est pas encore exécutée est marquée comme telle.

:::warning Elles agissent sur un équipement réel
Une règle qui commute une pompe la commute que vous regardiez ou non. Créez-en une à la fois et vérifiez que chacune fait ce que vous attendez avant d’ajouter la suivante.
:::

## La forme d’une règle

Chaque règle a les mêmes trois parties :

**Déclencheur** : ce qui la réveille
**Conditions** : ce qui doit aussi être vrai
**Actions** : ce qu’elle fait ensuite, dans l’ordre

## Ce qui peut réveiller une règle

Quatre choses :

| Déclencheur | Se déclenche quand |
|---|---|
| **Paramètre** | Un paramètre franchit une valeur que vous avez définie, dans une direction que vous choisissez |
| **Alerte** | Une alerte est déclenchée, fermée, ou l’un ou l’autre |
| **Programme** | Une heure du jour, dans votre propre fuseau horaire |
| **État de l’appareil** | Un appareil passe hors ligne ou revient |

## Conditions

Les conditions déterminent si les actions s’exécutent réellement. Vous disposez des comparaisons habituelles (égal, différent, supérieur à, inférieur à, et ainsi de suite) et vous pouvez les combiner avec **et**, **ou** et **non**.

Il existe aussi une condition d’**étape**, qui vérifie comment l’étape *précédente* s’est déroulée. C’est ce qui vous permet d’écrire « essaie ceci ; si ça n’a pas fonctionné, fais plutôt cela ».

## Ce qu’une règle peut faire

Une action qui nécessite un équipement n’est proposée que sur un aquarium qui a cet équipement :

| Action | Ce qu’elle fait |
|---|---|
| **Contrôler un équipement Apex** | Commuter une prise |
| **Contrôler un équipement Red Sea** | Piloter une unité ReefBeat |
| **Contrôler une pompe de brassage** | Régler le débit, le mode vague ou la puissance d’une pompe Jecod, ou **Mettre en pause pour le nourrissage** : le Cora Max de l’aquarium remet la pompe en place quand le nourrissage se termine |
| **Contrôler un équipement Cora** | Commuter une fiche intelligente |
| **Contrôler un appareil IR** | Envoyer une commande infrarouge |
| **Lancer un cycle d’alimentation Apex** | Démarrer un nourrissage |
| **Lancer un test Trident** | Déclencher un test |
| **Me notifier** | Vous envoyer une notification push |
| **Attendre avant l’étape suivante** | Mettre en pause avant de continuer |
| **Lancer une scène** | Exécuter une autre scène depuis l’intérieur de cette règle |
| **Gérer une automatisation** | Activer ou désactiver une autre règle |
| **Doser une tête DŌS** | Exécuter un dosage mesuré sur une tête DŌS |

:::warning Doser depuis une règle est irréversible et plafonné
Un dosage ne peut pas être retiré de l’aquarium. La tête doit être **étalonnée** avant qu’une règle ne puisse doser depuis elle, et le dosage sans surveillance est plafonné à **10 mL par tête par jour** ; une règle ne peut pas dépasser cela quelle que soit la façon dont elle est écrite. Les actions de dosage n’apparaissent qu’une fois vos têtes reconnues comme têtes de dosage.
:::

:::note Utilisez Attendre pour séquencer des étapes dans une règle
Une pause permet à une seule règle d’exécuter une procédure ordonnée (par exemple éteindre une prise, attendre, puis la rallumer) sans une seconde règle et un programme.
:::

## Scènes

Une scène est un groupe nommé d’actions que vous pouvez exécuter à la demande, depuis un programme, ou depuis l’intérieur d’une autre règle : « Changement d’eau », « Mode photo », « Nuit ».

Une scène peut appeler une autre scène. Cora refuse d’exécuter une scène imbriquée au-delà de sa limite de profondeur, et refuse une scène qui s’appellerait elle-même, pour éviter une boucle qui continuerait d’agir sur l’aquarium indéfiniment.

Après l’exécution d’une scène, on vous dit ce qui s’est passé, étape par étape, y compris tout ce qui a échoué.

Exécuter une scène à la main vous demande de confirmer d’abord, car une scène peut commuter plusieurs équipements à la fois.

## Scènes créées sur Cora Max

Les scènes peuvent aussi être créées et modifiées directement sur une tablette Cora Max, pas seulement sur le téléphone : c’est le même ensemble de scènes dans les deux cas, partagé à travers le compte. Si un foyer a un Cora Max plus ancien, il peut tout de même exécuter une scène créée sur le téléphone ; seule la modification sur l’appareil est une capacité plus récente, donc une tablette plus ancienne peut afficher une scène sans vous laisser la changer là. Modifiez-la plutôt depuis le téléphone.

## Désactiver une règle

Chaque règle a un commutateur d’activation. En désactiver une garde sa définition, utile quand vous voulez retrouver une règle la saison prochaine plutôt que de la reconstruire.

## Voir ce qu’une règle a fait

Chaque action qu’une règle entreprend est enregistrée avec la règle comme cause. Voir **[Activité](/help/mobile-activity)**.
