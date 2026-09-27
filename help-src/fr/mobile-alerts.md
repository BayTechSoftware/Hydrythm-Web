---
title: Alertes et seuils
description: Réglez la plage de chaque paramètre, choisissez les alertes que vous recevez et comprenez pourquoi une alerte s’est déclenchée.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Une alerte se déclenche quand une mesure sort de la plage que vous avez réglée. C’est vous qui réglez les plages, et c’est vous qui choisissez les alertes qui arrivent sur votre téléphone.

Ouvrez le **Centre d’alertes** depuis la ligne de raccourcis en bas du tableau de bord.

![Le Centre d’alertes](img/mobile-alerts.webp "Alertes actives, chacune avec sa gravité, ce qui l’a déclenchée, et quand.")

## Le Centre d’alertes

Il a deux onglets.

- **Actives** : les alertes en cours, avec un badge qui les compte
- **Règles** : les seuils et les règles de taux de variation qui produisent ces alertes

Chaque alerte active indique le paramètre et l’aquarium, la mesure en cause, une explication simple, une étiquette de gravité, le type de règle (**Seuil** ou **Taux de variation**) et l’heure du déclenchement.

Chaque alerte a deux boutons.

- **Voir la règle** ouvre la règle à l’origine de l’alerte. Vous pouvez y ajuster la plage.
- **Expliquer cette alerte** demande à l’Assistant de l’interpréter à la lumière de l’historique de votre aquarium.

## Régler une plage

Les paramètres que Cora sait évaluer ont une plage cible. Les valeurs par défaut dépendent du type et de l’âge de l’aquarium indiqués à sa création. C’est en général un bon point de départ. Un paramètre sans plage utilisable n’est pas évalué du tout. Il reste en gris neutre, et Cora ne devine rien.

Pour changer une plage, **appuyez longuement sur le widget** du paramètre dans le tableau de bord. Les seuils de ce paramètre s’ouvrent directement. Un appui simple ouvre la page du paramètre. Les deux gestes ne mènent pas au même endroit, et c’est l’appui long qu’il faut retenir.

Si le paramètre n’a pas encore de règle, les champs affichent la valeur par défaut de Cora, et une note en dessous le signale. Modifiez une valeur pour définir la vôtre.

Pour voir toutes les règles à la fois, touchez **Alertes** dans la rangée de boutons sous le tableau de bord.

Vous pouvez régler :

- **Une plage** : une limite basse et une limite haute, par exemple pour l’alcalinité ou la température
- **Un plafond** : une limite haute seulement, quand une valeur basse ne pose pas de problème, comme pour les nitrates ou les phosphates
- **Un plancher** : une limite basse seulement

:::tip Réglez la plage où tourne vraiment votre aquarium
Les valeurs par défaut sont un point de départ, pas un jugement. Un aquarium pauvre en nutriments à 6 dKH n’a pas « tort » parce qu’un tableau indique 8–9. Réglez la plage où vous tournez réellement, et Cora vous préviendra quand *votre* aquarium s’en écarte.
:::

## Ce qui déclenche une alerte

Une alerte se déclenche quand une mesure franchit un seuil. Cora vérifie chaque mesure dès qu’elle arrive. Une seule mesure hors de votre plage suffit donc.

Une fois l’alerte déclenchée, Cora ne vous relance pas sans arrêt pour la même chose. Un délai doit passer avant qu’elle puisse se déclencher de nouveau. L’alerte **se ferme toute seule** dès qu’une mesure revient dans la plage. Vous n’avez rien à valider.

Vous pouvez aussi créer une règle de **taux de variation**. Elle surveille la vitesse à laquelle un paramètre bouge, pas sa valeur du moment. Choisissez-la quand la vitesse du changement compte plus que le chiffre.

## Où apparaissent les alertes

- **La cloche**, en haut à droite de chaque écran, garde l’historique. Le chiffre indique le nombre d’alertes non lues.
- **Les notifications push** arrivent sur votre téléphone si vous les autorisez.
- **Le widget** passe à l’orange ou au rouge dans le tableau de bord.
- **Cora Max** affiche les mêmes alertes sur le grand écran.

## Quand l’équipement a besoin d’attention

Certaines alertes portent sur l’équipement et non sur une mesure. Quand un appareil comme un Trident ou une pompe Jecod signale une panne, Cora envoie une notification avec le nom de l’aquarium et de l’appareil, par exemple *« Aquarium Display : la pompe de remontée a besoin d’attention »*. Elle précise le problème, comme un rotor bloqué. Quand la panne disparaît, une deuxième notification suit : *« Aquarium Display : la pompe de remontée est de nouveau OK »*. Les deux dépendent de **Pannes d’équipement** dans **Réglages → Notifications**.

Une pompe de brassage Maxspect (bêta) peut déclencher la même alerte. Cela arrive quand un Cora Max sur le même réseau trouve les deux têtes réglées à 0 %, ou quand la pompe ne répond pas deux fois de suite. Voyez-y un avertissement, pas une sécurité. Le Cora Max vérifie de temps en temps, pas en continu, et seulement s’il est allumé et peut joindre la pompe.

## « Les mesures Red Sea ont arrêté de se mettre à jour »

Cette bannière peut apparaître sur la page d’un paramètre :

> Les mesures Red Sea ont arrêté de se mettre à jour. Aucun appareil ne lit actuellement les appareils Red Sea de cet aquarium : vérifiez Cora Max principal dans Réglages, ou ouvrez cet aquarium sur un appareil sur le même Wi-Fi.

Aucun téléphone ni Cora Max n’interroge en ce moment l’équipement ReefBeat de cet aquarium. Les mesures affichées sont donc anciennes, mais pas forcément fausses. Touchez la bannière pour ouvrir **Cora Max principal**. Choisissez alors un appareil allumé, ou réglez l’option sur **Tout appareil actif (automatique)**. Plus de détails dans [Plus d’un appareil Cora](/help/mobile-multi-device). Si la bannière reste, consultez la page [Résolution de problèmes](/help/troubleshooting).

## Choisir ce que vous recevez

Dans **Réglages → Notifications**, vous choisissez :

- les catégories de notifications autorisées à vous être envoyées

Reef Buddy n’a pas d’interrupteur à lui. Il envoie un briefing quand il y a quelque chose à faire, et il se tait sinon.

:::note Cora sait se taire
Le briefing quotidien, c’est une notification par aquarium et par jour. Les jours où rien ne demande votre attention, il reste en général silencieux. Il ne vous écrit pas juste pour dire que tout va bien. Si Cora vous envoie une notification, c’est que quelque chose a changé.
:::

## Délais : à quelle fréquence une même alerte vous prévient

Chaque règle a son propre **Délai entre les alertes**. Vous le réglez quand vous ajoutez ou modifiez la règle, dans l’onglet **Règles** du Centre d’alertes. Ce délai ne cache pas l’alerte. Il limite seulement le nombre de notifications que Cora vous envoie à son sujet. La mesure reste évaluée, et l’alerte reste visible sur le widget et dans la cloche pendant tout ce temps.

Les choix possibles sont 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 jour, 3 jours ou **1 semaine**.

Un délai court convient à une mesure qui bouge vite, comme la température. Un délai long, jusqu’à une semaine, convient à un problème qui dure plusieurs jours le temps de recevoir une pièce, comme un Trident sans réactif ou un bidon de dosage vide. Sans ce long délai, Cora vous enverrait plusieurs notifications par jour pour un problème que vous connaissez déjà.

:::note Le report d’une alerte se fait sur Cora Max
Cora Mobile n’a pas de bouton pour reporter une alerte active. Ce bouton se trouve sur l’écran Cora Max près de l’aquarium. Il coupe l’alerte pendant le délai que vous avez choisi ici. Depuis le téléphone, pour être prévenu moins souvent, réglez ce délai dans la règle.
:::

## Fermer une alerte

Une alerte se ferme quand la mesure revient dans la plage. Il n’y a rien à ignorer. L’alerte décrit l’état de l’aquarium, ce n’est pas une tâche.

:::note Une mesure passagère déclenche aussi une alerte
Une seule mesure hors plage suffit. Une sonde qui fait un pic déclenchera donc une alerte. Si une source n’est pas fiable, réétalonnez-la ou choisissez une autre source pour le widget. N’élargissez pas le seuil.
:::

Si c’est la mesure qui est fausse et non l’aquarium (une sonde à étalonner, par exemple), corrigez la source. Élargir un seuil pour faire taire une mauvaise sonde cache aussi le prochain vrai problème.

## Désactiver les alertes d’un paramètre

Ouvrez la règle dans l’onglet **Règles** du Centre d’alertes et coupez son **interrupteur d’activation**. La règle et sa plage sont gardées. Vous pourrez la réactiver sans tout refaire.

:::warning Faire taire un paramètre sans supprimer sa plage
Retirer un seuil n’arrête pas forcément toute évaluation de la mesure. Les plages de référence par défaut colorent toujours la valeur et peuvent toujours alimenter le briefing. Utilisez plutôt l’interrupteur d’activation de la règle.
:::
