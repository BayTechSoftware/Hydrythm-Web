---
title: Activité et chronologie
description: Tout ce qui est arrivé à votre équipement, et ce qui l’a causé.
section: Cora Mobile
reviewed: 2026-09-09
order: 22
group: Records
---

Activité enregistre chaque **demande d’action** (chaque tentative de changer quelque chose) avec ce qui l’a demandée et ce qu’il en est advenu.

Une demande n’est pas la même chose qu’un changement. Les demandes refusées ne se sont pas exécutées, à une exception : une entrée disant *Aucun appareil n’a répondu à temps* peut malgré tout s’être exécutée, vérifiez donc l’équipement avant de la répéter. Les demandes sans changement ont trouvé l’équipement déjà comme demandé, et une demande non confirmée peut avoir atteint l’appareil ou non. Toutes sont enregistrées.

**Réglages → Activité.**

![Le journal d’activité](img/mobile-activity.webp "Chaque action, avec l’interface qui l’a demandée.")

## Ce qui est enregistré

Chaque **demande**, pas seulement celles qui ont fonctionné : commutations de prises, cycles de nourrissage, dosages, changements de fiches, et tout ce qu’une scène ou une automatisation a fait.

Une demande qui a été **refusée**, qui n’a fait **aucun changement**, ou qui est partie et est revenue **non confirmée** est enregistrée exactement comme une demande exécutée. C’est bien le but : une commande qui n’a discrètement rien fait est exactement ce que vous voulez trouver ici.

## Ce qui l’a causée

Chaque entrée nomme sa cause :

| Cause | Signifie |
|---|---|
| **Cette application** | Vous l’avez touchée ici |
| **Voix dans cette application** | Vous l’avez demandée, sur ce téléphone |
| **Appui sur un Cora** | Quelqu’un a utilisé un écran Cora ; la ligne indique lequel |
| **Voix sur un Cora Max** | Quelqu’un a parlé à un écran |
| **Cora Assistant** | Vous avez demandé à Cora de le faire |
| **Règle d’automatisation** | Une règle s’est déclenchée |
| **Bouton intelligent** | Un bouton physique a été pressé |
| **Envoyé depuis Cora Cloud** | Émis par votre compte plutôt que par un appareil devant vous |
| **Source inconnue** | Enregistré avant que la source ne puisse être identifiée |

## Comment elle a voyagé

Chaque ligne porte aussi une puce d’itinéraire, car *comment* une demande a atteint votre équipement explique beaucoup de ce qui a mal tourné quand quelque chose l’a fait :

| Puce | Signifie |
|---|---|
| **LAN** | Envoyé via votre propre réseau, directement à l’équipement |
| **VIA LE CLOUD** | Envoyé via votre compte, pour un équipement non accessible directement |
| **ROUTE ?** | Enregistré avant que les itinéraires ne soient suivis : réellement inconnu, pas supposé |

Sur un système avec plus d’un Cora, la ligne nomme aussi lequel a exécuté la demande.

## La chronologie de l’aquarium

Séparément des actions sur l’équipement, chaque aquarium a une **chronologie** : mesures, alertes, entrées de journal, résultats ICP et changements de population disposés en ordre.

Utilisez Activité quand vous demandez *« qu’est-ce que quelque chose a fait ? »* et la chronologie quand vous demandez *« que se passait-il autour de cette date ? »*

:::note La chronologie et le journal sont complémentaires
La chronologie contient ce que Cora a enregistré ; le [journal](/help/mobile-journal) contient ce que vous avez fait. Lus ensemble, ils établissent la cause et l’effet autour d’une date donnée.
:::
