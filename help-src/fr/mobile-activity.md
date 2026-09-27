---
title: Activité et chronologie
description: Tout ce qui est arrivé à votre équipement, et ce qui l’a déclenché.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Activité enregistre chaque **demande d’action**, c’est-à-dire chaque tentative de changer quelque chose. Pour chacune, vous voyez qui l’a demandée et ce qu’elle est devenue.

Une demande n’est pas forcément un changement. Une demande refusée ne s’est pas exécutée, avec une exception. Si l’entrée dit *Aucun appareil n’a répondu à temps*, l’action a pu s’exécuter quand même. Vérifiez l’équipement avant de la relancer. Une demande sans changement a trouvé l’équipement déjà dans l’état voulu. Une demande non confirmée a pu atteindre l’appareil, ou pas. Toutes sont enregistrées.

**Réglages → Activité.**

![Le journal d’activité](img/mobile-activity.webp "Chaque action, avec l’interface qui l’a demandée.")

## Ce qui est enregistré

Toutes les **demandes**, y compris celles qui n’ont pas marché : prises allumées ou éteintes, cycles de nourrissage, dosages, changements de prises connectées, et tout ce qu’une scène ou une automatisation a fait.

Une demande **refusée**, sans **aucun changement** ou revenue **non confirmée** est enregistrée comme une demande exécutée. C’est voulu. Une commande qui n’a rien fait sans le dire, c’est justement ce que vous cherchez ici.

## Qui l’a déclenchée

Chaque entrée indique sa source.

| Source | Signification |
|---|---|
| **Cette application** | Vous avez touché le bouton ici |
| **Voix dans cette application** | Vous l’avez demandé à voix haute sur ce téléphone |
| **Appui sur un Cora** | Quelqu’un a utilisé un écran Cora. La ligne indique lequel |
| **Voix sur un Cora Max** | Quelqu’un a parlé à un écran |
| **Cora Assistant** | Vous avez demandé à Cora de le faire |
| **Règle d’automatisation** | Une règle s’est déclenchée |
| **Bouton intelligent** | Quelqu’un a appuyé sur un bouton physique |
| **Envoyé depuis Cora Cloud** | Envoyé par votre compte, pas par un appareil devant vous |
| **Source inconnue** | Enregistré avant que Cora sache identifier la source |

## Par quel chemin

Chaque ligne porte aussi une étiquette de trajet. Quand quelque chose a mal tourné, savoir *comment* la demande est arrivée à l’équipement explique souvent beaucoup.

| Étiquette | Signification |
|---|---|
| **LAN** | Envoyé par votre propre réseau, directement à l’équipement |
| **VIA LE CLOUD** | Envoyé par votre compte, pour un équipement qu’on ne peut pas joindre directement |
| **ROUTE ?** | Enregistré avant le suivi des trajets. Le trajet est vraiment inconnu, Cora ne le devine pas |

Si vous avez plusieurs Cora, la ligne indique aussi celui qui a exécuté la demande.

## La chronologie de l’aquarium

À côté des actions sur l’équipement, chaque aquarium a sa **chronologie** : mesures, alertes, entrées du journal, résultats ICP et changements de population, dans l’ordre.

Ouvrez Activité pour savoir *« qu’a fait cet équipement ? »*. Ouvrez la chronologie pour savoir *« que se passait-il autour de cette date ? »*.

:::note Chronologie et journal vont ensemble
La chronologie contient ce que Cora a enregistré. Le [journal](/help/mobile-journal) contient ce que vous avez fait. En lisant les deux, vous retrouvez les causes et les effets autour d’une date.
:::
