---
title: Alertes et seuils
description: Réglez la plage saine de chaque mesure, choisissez à quelle fréquence une alerte peut vous prévenir, et découvrez pourquoi un appareil "ne remonte plus de mesures".
section: Cora Mobile
reviewed: 2026-10-17
order: 22
group: Alerts and automation
twin: max-alerts
---

Vous recevez une alerte quand une mesure sort de la plage que vous avez réglée pour elle. Cette page explique comment régler ces plages, ce qui se passe quand une alerte se déclenche, et combien de temps Cora attend avant de dire qu’un appareil ne remonte plus de mesures.

Pour ouvrir le **Centre d’alertes**, touchez **Alertes** dans la rangée de boutons sous le tableau de bord. Vous le trouvez aussi dans Réglages → votre aquarium → **Seuils d’alerte**.

![L’onglet Actives du Centre d’alertes dans Cora Mobile](img/mobile-alerts.webp "Les alertes actives, chacune avec sa gravité, ce qui l’a déclenchée et quand, plus Voir la règle et Expliquer cette alerte.")

## Le Centre d’alertes {#alert-center}

Il a deux onglets. **Actives** liste les alertes en cours, avec un badge de comptage. **Règles** contient les règles qui les déclenchent.

Chaque alerte active affiche le paramètre et l’aquarium, la mesure qui l’a déclenchée, une courte explication, une puce de gravité, le type de règle qui s’est déclenchée (**Seuil** ou **Taux de variation**) et le moment du déclenchement. Elle a deux boutons :

- **Voir la règle** ouvre la règle qui est derrière, pour que vous puissiez ajuster la plage. Sur une alerte de doseur, comme une tête DŌS ou ReefDose presque vide ou une dose manquée, ce bouton devient **Ouvrir le doseur**. Il ouvre la page de ce doseur avec ses alertes.
- **Expliquer cette alerte** ouvre Cora Assistant avec une question sur l’alerte prête à envoyer. Vérifiez-la, modifiez-la si vous voulez, puis envoyez-la.

## L’onglet Règles {#rules}

![L’onglet Règles](img/mobile-alert-rules.webp "Les règles regroupées par paramètre, chacune avec son propre interrupteur.")

Les règles sont regroupées par paramètre. Chaque règle a son propre interrupteur sur sa ligne, pour que vous puissiez en désactiver une sans l’ouvrir. Une ligne indique aussi **Se déclenche maintenant** tant que son alerte est en cours, ou quand elle s’est déclenchée pour la dernière fois (ou **Jamais déclenchée**).

Les règles d’une tête de dosage portent le nom de la tête et de ce qu’elles surveillent, par exemple *Iode · jours restants* ou *Iode · restant*. Une dose manquée apparaît comme *Iode · dose manquée*. Chaque DŌS et chaque ReefDose a ici une seule ligne, et les alertes de ses têtes ne sont pas listées une par une. Touchez la ligne pour ouvrir la page de ce doseur. Voir [Alertes des doseurs](/help/mobile-device-control#doser-alerts).

En bas :

- **Ajouter les règles recommandées** ajoute celles des règles recommandées par Cora qui manquent. Il ignore un paramètre qui a déjà une règle. Sur un aquarium sans aucune règle, ce bouton indique **Ajouter les règles par défaut**.
- **Ajouter une règle personnalisée** crée une règle à vous. Choisissez le paramètre et le **Type de règle**, **Seuil** ou **Taux de variation**. Le bouton **Ajouter une règle** en bas à droite fait la même chose.

### Modifier une règle {#editing-a-rule}

Touchez la ligne d’une règle pour l’ouvrir. Vous y trouvez :

- **Minimum d’alerte** et **Maximum d’alerte**, la plage elle-même. Laissez-en un vide pour un plafond ou un plancher.
- **Recommandé**, qui remet la plage suggérée par Cora.
- **Plage de la jauge (affichage Cora)**, avec **Min. de la jauge** et **Max. de la jauge**. Ils ne règlent que l’échelle de la jauge sur Cora Max. Ils ne déclenchent jamais d’alerte.
- **Délai entre les alertes**, expliqué [plus bas](#cooldowns).
- **Activée**, et un bouton de suppression.

Une règle de panne d’appareil, comme un Trident à court de réactif, n’a pas de plage. Vous choisissez seulement son délai.

## Régler une plage {#setting-a-range}

Les paramètres que Cora peut évaluer ont une plage cible. Les valeurs par défaut viennent du type et de l’âge de votre aquarium lors de sa configuration, et c’est un bon point de départ. Si un paramètre n’a pas de plage utilisable, Cora ne l’évalue pas, et son widget reste gris neutre.

Le plus rapide pour changer une plage est de faire un appui long sur le widget du paramètre dans le tableau de bord. Cela ouvre ses seuils. Un appui normal ouvre plutôt la page du paramètre.

![La feuille de modification du seuil de pH dans Cora Mobile](img/mobile-threshold-sheet.webp "Minimum et maximum d’alerte, la plage de la jauge pour Cora Max, et le délai entre les alertes.")

Si le paramètre n’a pas encore de règle, les champs démarrent sur la valeur par défaut de Cora et une note en dessous l’indique. Changez n’importe quelle valeur pour régler la vôtre.

Vous pouvez régler :

- une plage, avec un bas et un haut, pour des choses comme l’alcalinité ou la température
- un plafond, avec seulement un haut, pour ce qui peut être bas sans problème, comme les nitrates ou les phosphates
- un plancher, avec seulement un bas

:::tip Réglez la plage où votre aquarium tourne vraiment
Les valeurs par défaut ne sont qu’un point de départ. Un aquarium pauvre en nutriments à 6 dKH n’est pas « dans l’erreur » parce qu’un tableau dit 8–9. Réglez la plage où vous tournez, et Cora vous prévient quand *vous* dérivez.
:::

## Ce qui déclenche une alerte {#what-triggers-an-alert}

Une alerte se déclenche quand une mesure franchit un seuil. Cora vérifie chaque mesure à son arrivée, donc une seule mesure hors de votre plage suffit.

Une règle de taux de variation surveille la vitesse à laquelle un paramètre bouge plutôt que sa position. Utilisez-la quand la vitesse d’un changement compte plus que le chiffre.

Une fois qu’une alerte est en cours, elle ne vous prévient pas sans cesse de la même chose. Le [délai](#cooldowns) de la règle décide quand elle peut vous prévenir à nouveau.

## Où apparaissent les alertes

- La cloche, en haut à droite des onglets principaux, garde votre historique. Le chiffre indique combien vous n’en avez pas lu. Plus de détails dans [Notifications](/help/mobile-notifications).
- Une notification push arrive sur votre téléphone si cette catégorie est activée.
- Le widget du tableau de bord passe à l’orange ou au rouge.
- Cora Max affiche les mêmes alertes à l’écran.

## Quand un équipement demande de l’attention {#equipment-faults}

Certaines alertes concernent l’équipement, pas une mesure. Quand un appareil comme un Trident ou une pompe Jecod signale une panne, Cora envoie une notification qui nomme l’aquarium et l’appareil, par exemple *« Aquarium principal : Pompe de remontée demande de l’attention »*. Elle dit aussi ce qui ne va pas, comme un rotor bloqué. Quand la panne disparaît, vous en recevez une deuxième : *« Aquarium principal : Pompe de remontée fonctionne de nouveau »*. Les deux relèvent de **Pannes d’équipement** dans **Réglages → Notifications**.

Un AquaWiz KH Controller lu toutes les heures par votre Cora Max déclenche le même type d’alerte quand :

- sa pompe doseuse signale une panne ;
- sa sonde pH est défaillante ou proche de la fin de sa vie ;
- le niveau de son réservoir d’eau reste bas ou haut pendant plus d’une heure.

Cela demande la lecture horaire par le Cora Max (à partir de la prochaine mise à jour de Cora Max) (voir [Contrôler l’équipement depuis Cora Max](/help/max-device-control#aquawiz-hourly)) : la lecture cloud d’AquaWiz toutes les 12 heures ne les transmet pas.


## Un appareil ne remonte plus de mesures {#stopped-reporting}

Quand un appareil connecté devient silencieux, Cora envoie *« [Appareil] : ne remonte plus de mesures »*. Cela ne veut pas dire que l’appareil est en panne, seulement que Cora n’en a pas eu de nouvelles depuis un moment. Vous recevez une deuxième notification, *« [Appareil] : remonte de nouveau des mesures »*, quand il revient.

Le temps d’attente de Cora dépend de l’appareil :

| Appareil | Cora attend |
|---|---|
| Neptune Apex | Environ 30 minutes sans mise à jour |
| Red Sea ReefBeat | Environ 30 minutes |
| AquaWiz | Environ 25 heures, car AquaWiz ne laisse Cora lire son cloud que toutes les 12 heures |
| Pompes Jecod | Trois lectures manquées d’affilée, à l’intervalle de lecture de la pompe (90 minutes avec les 30 par défaut) |
| Prise Zigbee | N’est pas revenue 30 minutes après le redémarrage du hub. Donnez-lui un nom avec **Renommer** pour que l’alerte la nomme |

Ce qu’il faut vérifier dépend de la façon dont Cora lit l’appareil.

- Apex, ReefBeat et Jecod sont lus par un Cora Max en Wi-Fi. Vérifiez l’alimentation et le Wi-Fi de l’appareil, et que le Cora Max qui le lit est allumé et en ligne.
- AquaWiz est lu par votre compte chez le fabricant. Vérifiez la connexion du compte sur la page de l’appareil dans Cora Mobile.


Ces notifications relèvent de **Pannes d’équipement** dans **Réglages → Notifications**.


Un aquarium Red Sea peut aussi afficher un bandeau, *« Les relevés Red Sea ne se mettent plus à jour »*, quand aucun téléphone ni aucun Cora Max ne lit son équipement ReefBeat. Touchez-le pour choisir un **Cora Max principal**. La solution complète est dans [Résolution de problèmes](/help/troubleshooting#red-sea-readings-have-stopped-updating).

## Choisir ce qui vous parvient {#choosing-what-reaches-you}

Dans **Réglages → Notifications**, vous choisissez quelles catégories peuvent vous envoyer une notification. Voir [Notifications](/help/mobile-notifications), qui explique aussi comment [garder des nuits calmes](/help/mobile-notifications#quiet-at-night).

Reef Buddy n’a pas d’interrupteur à lui. Son horaire est la ligne **Heure du briefing**, juste sous Notifications dans les Réglages. Avec le forfait gratuit, il n’y a pas de notification de briefing.

:::note Cora reste silencieux sauf si quelque chose a changé
Le briefing quotidien est une seule notification par aquarium et par jour. Un jour où rien ne demande votre attention, il reste en général silencieux au lieu de vous dire que tout va bien. Si Cora vous envoie une notification, quelque chose a changé.
:::

## Délais : à quelle fréquence la même alerte peut vous prévenir {#cooldowns}

Chaque règle a son propre **Délai entre les alertes**. Vous le réglez quand vous ajoutez ou modifiez la règle. Une règle qui n’en a jamais eu utilise 1 h.

Le délai ne masque pas l’alerte. Il limite seulement la fréquence des notifications. La mesure est toujours évaluée, et l’alerte reste sur le widget et sous la cloche pendant tout ce temps.

Vous pouvez choisir 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 jour, 3 jours ou 1 semaine.

Un délai court convient à une mesure qui bouge vite, comme la température. Un délai long, jusqu’à une semaine, convient à quelque chose qui reste anormal pendant des jours en attendant une pièce, comme un Trident à court de réactif ou un réservoir de dosage vide.

:::note Reporter se trouve sur Cora Max
Cora Mobile n’a pas de bouton Reporter sur une alerte active. Reporter se trouve sur l’écran Cora Max à l’aquarium, et coupe l’alerte pendant le délai que vous avez choisi ici. Sur votre téléphone, le délai de chaque règle est le moyen de changer la fréquence à laquelle vous entendez parler de quelque chose.
:::

## Effacer une alerte {#clearing-an-alert}

Une alerte s’efface toute seule quand la mesure revient dans la plage. Il n’y a rien à fermer. Vous recevez alors une notification, par exemple *« Aquarium principal : Alcalinité revenue à la normale »*. Si le problème revient plus tard, vous recevez une nouvelle alerte.

:::note Les pics brefs déclenchent aussi des alertes
Une seule mesure hors plage suffit à déclencher une alerte, donc une sonde qui fait un pic en déclenchera une. Si une source n’est pas fiable, réétalonnez-la ou faites suivre au widget une autre source. N’élargissez pas le seuil.
:::

Parfois la mesure est fausse et l’aquarium va bien, par exemple quand une sonde a besoin d’être étalonnée. Dans ce cas, corrigez la source. Si vous élargissez un seuil pour faire taire une mauvaise sonde, vous manquerez aussi le prochain vrai problème.

## Désactiver une alerte {#turning-an-alert-off}

Désactivez l’interrupteur sur la ligne de la règle dans l’onglet **Règles**. Cora garde la règle et sa plage, pour que vous puissiez la réactiver sans tout reconfigurer.

Tant qu’une règle est désactivée, Cora n’évalue pas cette mesure. Son widget reste gris neutre et ne déclenche jamais d’alerte.

:::warning Désactivez un paramètre sans supprimer sa plage
Supprimer une règle n’empêche pas toujours Cora d’évaluer cette mesure. Les plages de référence par défaut colorent toujours la valeur et peuvent toujours alimenter le briefing. Utilisez l’interrupteur de la règle.
:::
