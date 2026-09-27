---
title: Alertes et seuils
description: Réglez la plage de chaque paramètre, choisissez ce dont vous êtes informé, et comprenez pourquoi une alerte s’est déclenchée.
section: Cora Mobile
reviewed: 2026-09-27
order: 15
group: Alerts and automation
---

Une alerte se déclenche quand une mesure sort de la plage que vous avez réglée pour elle. Vous réglez les plages, et vous contrôlez quelles alertes atteignent votre téléphone.

Ouvrez le **Centre d’alertes** depuis la ligne de raccourcis en bas du tableau de bord.

![Le Centre d’alertes](img/mobile-alerts.webp "Alertes actives, chacune avec sa gravité, ce qui l’a déclenchée, et quand.")

## Le Centre d’alertes

Deux onglets :

- **Actives** : les alertes actuellement déclenchées, avec un badge de compte
- **Règles** : les seuils et règles de taux de variation qui les produisent

Chaque alerte active affiche le paramètre et l’aquarium, la mesure qui l’a déclenchée, une explication simple, une puce de gravité, le type de règle qui s’est déclenché (**Seuil** ou **Taux de variation**), et l’heure du déclenchement.

Deux actions sur chacune :

- **Voir la règle** : ouvre la règle qui l’a déclenchée, pour que vous puissiez ajuster la plage
- **Expliquer cette alerte** : demande à l’Assistant de l’interpréter par rapport à l’historique de votre aquarium

## Régler une plage

Les paramètres que Cora peut évaluer ont une plage cible, et les valeurs par défaut viennent du type et de l’âge de votre aquarium quand vous l’avez configuré, généralement un point de départ raisonnable. Un paramètre sans plage utilisable n’est pas évalué du tout : il reste gris neutre plutôt que d’être deviné.

Pour en changer une : **appuyez longuement sur son widget** sur le tableau de bord, ce qui ouvre directement les seuils de ce paramètre. Un simple appui ouvre la vue du paramètre à la place ; les deux gestes vont à des endroits différents, et l’appui long est le raccourci à retenir.

Si le paramètre n’a pas encore de règle, les champs démarrent sur la valeur par défaut de Cora, et une note en dessous le précise. Changez n’importe quelle valeur pour définir la vôtre.

Pour les voir toutes ensemble, utilisez **Alertes** dans la ligne de boutons sous le tableau de bord.

Vous pouvez régler :

- **Une plage** : un bas et un haut, pour des choses comme l’alcalinité ou la température
- **Un plafond** : un haut seulement, pour des choses où bas est correct, comme le nitrate ou le phosphate
- **Un plancher** : un bas seulement

:::tip Réglez la plage à laquelle votre aquarium fonctionne réellement
Les valeurs par défaut sont un point de départ, pas un verdict. Un aquarium à faible teneur en nutriments à 6 dKH n’est pas « faux » parce qu’un graphique disait 8–9. Réglez la plage à laquelle vous fonctionnez réellement, et Cora vous le dira quand *vous* dérivez.
:::

## Ce qui déclenche une alerte

Une alerte se déclenche quand une mesure franchit un seuil. Cora vérifie chaque mesure à son arrivée, donc une seule mesure hors de votre plage suffit à en déclencher une.

Une fois une alerte levée, elle ne continuera pas à vous notifier à répétition pour la même chose ; il y a un délai de repos avant qu’elle ne puisse se déclencher à nouveau. Et elle **se ferme d’elle-même** au moment où une mesure revient dans la plage ; il n’y a rien à accuser réception.

Vous pouvez aussi régler une règle de **taux de variation**, qui surveille à quelle vitesse un paramètre évolue plutôt qu’où il se trouve actuellement. C’est celle à utiliser pour les choses où la vitesse d’un changement compte plus que le chiffre.

## Où les alertes apparaissent

- **La cloche**, en haut à droite de chaque écran, garde votre historique. Le chiffre indique combien vous n’avez pas lu.
- **Les notifications push** atteignent votre téléphone quand vous les autorisez.
- **Le widget** passe à l’orange ou au rouge sur le tableau de bord.
- **Cora Max** affiche les mêmes alertes sur le grand écran.

## Quand l’équipement a besoin d’attention

Certaines alertes concernent l’équipement plutôt qu’une mesure. Quand un appareil comme un Trident ou une pompe Jecod signale une panne, Cora envoie une notification qui nomme l’aquarium et l’appareil, par exemple *« Aquarium Display : la pompe de remontée a besoin d’attention »*, et dit ce qui ne va pas, comme un rotor bloqué. Quand la panne se résorbe, une seconde suit : *« Aquarium Display : la pompe de remontée est de nouveau OK »*. Les deux relèvent de **Pannes d’équipement** dans **Réglages → Notifications**.

Une pompe de brassage Maxspect (bêta) peut déclencher la même alerte quand un Cora Max sur son réseau trouve les deux têtes réglées à 0 %, ou n’obtient aucune réponse de la pompe de brassage deux fois de suite. Traitez cela comme un avertissement, pas une sauvegarde : le Cora Max vérifie de temps en temps plutôt que continuellement, et seulement pendant qu’il fonctionne et peut atteindre la pompe de brassage.

## « Les mesures Red Sea ont arrêté de se mettre à jour »

Vous pouvez voir cette bannière sur la page d’un paramètre d’un aquarium :

> Les mesures Red Sea ont arrêté de se mettre à jour. Aucun appareil ne lit actuellement les appareils Red Sea de cet aquarium : vérifiez Cora Max principal dans Réglages, ou ouvrez cet aquarium sur un appareil sur le même Wi-Fi.

Cela signifie qu’aucun téléphone ni Cora Max n’interroge actuellement l’équipement ReefBeat de cet aquarium, donc les mesures affichées sont anciennes, pas nécessairement fausses. Touchez la bannière pour ouvrir **Cora Max principal** et soit choisissez un appareil qui est en ligne, soit réglez-le sur **Tout appareil actif (automatique)**. Voir [Plus d’un appareil Cora](/help/mobile-multi-device). Si cela ne se résorbe pas, voir [Résolution de problèmes](/help/troubleshooting).

## Choisir ce qui vous atteint

**Réglages → Notifications.** Vous pouvez contrôler :

- Quelles catégories de notifications peuvent être envoyées

Reef Buddy n’a pas de commutateur propre : il envoie un briefing quand il y a quelque chose sur lequel agir et reste silencieux quand ce n’est pas le cas.

:::note Cora est conçu pour rester silencieux
Le briefing quotidien est une notification par aquarium par jour, et un jour où rien n’a besoin de votre attention, il reste généralement silencieux plutôt que de vous dire que tout va bien. Si Cora envoie une notification, quelque chose a changé.
:::

## Délais de repos : à quelle fréquence la même alerte peut vous notifier

Chaque règle a son propre **Délai entre les alertes**, réglé quand vous ajoutez ou modifiez la règle (dans l’onglet **Règles** du Centre d’alertes). Le délai de repos ne masque pas l’alerte elle-même : il limite seulement la fréquence à laquelle Cora vous envoie une notification à son sujet. La mesure reste évaluée et l’alerte reste visible sur le widget et dans la cloche pendant tout ce temps.

Vous pouvez choisir parmi : 15 min, 30 min, 1 h, 2 h, 4 h, 8 h, 1 jour, 3 jours, ou **1 semaine**.

Un délai court convient à une mesure qui évolue vite comme la température. Un délai long, jusqu’à une semaine, convient à quelque chose qui reste faux pendant des jours en attendant une pièce, comme un Trident à court de réactif ou un contenant de dosage vide : sans un long délai, Cora enverrait une notification pour le même problème connu plusieurs fois par jour.

:::note Reporter une alerte active se fait sur Cora Max
Cora Mobile n’a pas de bouton Reporter propre sur une alerte active ; ce contrôle se trouve sur l’écran Cora Max à l’aquarium, et il met en sourdine la même alerte pour la durée de repos que vous avez choisie ici. Depuis le téléphone, la façon de changer la fréquence à laquelle vous entendez parler de quelque chose est ce délai de repos par règle, pas un report par alerte.
:::

## Fermer une alerte

Une alerte se ferme quand la mesure revient dans la plage. Il n’y a rien à ignorer ; c’est une constatation sur l’aquarium, pas une tâche.

:::note Les mesures transitoires déclenchent des alertes
Une seule mesure hors plage suffit à déclencher une alerte, donc une sonde qui a un pic en déclenchera une. Si une source est peu fiable, réétalonnez-la ou pointez le widget vers une source différente plutôt que d’élargir le seuil.
:::

Si une mesure est fausse plutôt que l’aquarium étant en tort (une sonde qui a besoin d’un étalonnage, par exemple), corrigez la source. Élargir un seuil pour faire taire une mauvaise sonde masque aussi le prochain vrai problème.

## Désactiver les alertes pour un paramètre

Ouvrez la règle dans l’onglet **Règles** du Centre d’alertes et désactivez son **commutateur d’activation**. La règle et sa plage sont conservées, donc vous pouvez la réactiver sans la reconstruire.

:::warning Faire taire un paramètre sans supprimer sa plage
Retirer un seuil n’arrête pas nécessairement toute évaluation de cette mesure ; les bandes de référence par défaut colorent toujours la valeur et peuvent toujours alimenter le briefing. Utilisez le commutateur d’activation de la règle.
:::
