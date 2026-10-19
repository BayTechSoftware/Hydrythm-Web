---
title: Alertes sur Cora Max
description: Que faire quand une alerte apparaît sur Cora Max, comment la reporter ou l’ignorer, changer les seuils d’alerte au mur et régler le son d’alerte.
section: Cora Max
reviewed: 2026-10-13
order: 8
group: Alerts and automation
twin: mobile-alerts
---

Cette page explique ce que fait Cora Max quand quelque chose demande votre attention, et ce que vous pouvez changer au mur. Le fonctionnement des plages, des règles et des notifications du téléphone est expliqué dans [Alertes et seuils](/help/mobile-alerts).

## Quand une alerte apparaît

Quand une mesure sort de sa plage, qu’un appareil signale une panne, qu’une dose est manquée ou qu’un consommable s’épuise, Cora Max affiche l’alerte au milieu de l’écran. Trois boutons se trouvent en dessous.

1. **Répondre à la voix** lance une conversation avec Cora au sujet de cette alerte, pour que vous n’ayez rien d’autre à toucher. Plus de détails dans [Parler à Cora](/help/max-voice).
2. **Reporter** fait taire l’alerte sur ce Cora Max pendant un moment. Le bouton indique combien de temps, par exemple **Reporter 1 h**. C’est le délai réglé pour cette alerte dans les réglages d’alerte de Cora Mobile, et il peut aller jusqu’à 1 semaine (pratique pour un niveau de réactif bas qui ne changera pas avant des jours).
3. **Ignorer** ferme l’alerte maintenant. Elle reste silencieuse sur cet écran jusqu’à ce que le problème disparaisse. S’il revient plus tard, vous recevez une nouvelle alerte.

Quand l’alerte concerne un doseur, comme une tête DŌS ou ReefDose presque vide ou une dose manquée, la carte a aussi un bouton **Ouvrir DŌS** ou **Ouvrir ReefDose**. Il vous mène à la page de ce doseur, où se règlent ses alertes.


Si Reporter ou Ignorer affiche une erreur, réessayez une fois. Si cela échoue encore, voir [Une alerte ne disparaît pas](/help/troubleshooting#an-alert-is-not-clearing).

:::note Reporter ne concerne que ce Cora Max
Tant qu’une alerte est reportée ou ignorée, ce Cora Max cesse de l’afficher, de la faire sonner et de l’énoncer, et elle quitte la barre du haut. Votre téléphone reçoit toujours ses notifications, les autres écrans Cora Max affichent toujours l’alerte, elle reste dans l’**Historique des notifications**, et vos réglages d’alerte ne changent pas.
:::

## Les alertes dans la barre du haut

Chaque alerte active apparaît aussi sous forme de petite étiquette dans la barre du haut, assez grande pour être repérée depuis l’autre bout de la pièce. S’il y en a plus que la place ne le permet, vous verrez **+2** (ou le nombre qui convient).

- Touchez une étiquette pour ramener cette alerte au milieu de l’écran.
- Touchez **+2** pour ouvrir **Alarmes actives**, la liste de tout ce qui est actif. Touchez-en une dans la liste pour l’ouvrir.

## La boîte de réception des notifications

**Paramètres → Paramètres Cora Max → Historique des notifications** est la boîte de réception de tout votre compte. Elle contient chaque briefing, alarme et avis de compte de votre système, y compris ceux que cet écran n’a pas déclenchés et tout ce que votre téléphone a manqué. Quand une mesure sort de sa plage puis y revient, vous voyez les deux.

## Modifier les seuils {#editing-thresholds}

![Les réglages d’un aquarium sur Cora Max, avec Seuils d’alerte, Unités et Cora Max principal](img/max-tank-settings.webp "Seuils d’alerte et Unités d’abord, puis le Cora Max principal de cet aquarium.")

Touchez le nom de l’aquarium dans la barre du haut et choisissez **Seuils d’alerte**, ou allez dans **Paramètres → [votre aquarium] → Seuils d’alerte**. Les deux ouvrent les mêmes plages que sur votre téléphone, et un changement fait ici s’applique partout.

Vous pouvez aussi changer un seuil par un appui long sur son widget dans le tableau de bord, ou à la voix : *« Hey Cora, règle l’alerte de pH entre 7,9 et 8,4. »* Cora vous indique le changement et attend votre accord.

Chaque paramètre de la liste a son propre interrupteur. Une alerte que vous avez désactivée indique **Alerte désactivée**. Cora garde sa plage, mais n’évalue pas cette mesure tant qu’elle est désactivée. Le widget reste gris neutre et ne déclenche jamais d’alerte. Si un paramètre n’a pas encore d’alerte, il indique **Aucune alerte définie**, et **Ajouter une alerte** en crée une avec la plage affichée.

![La liste des seuils d’alerte sur Cora Max](img/max-alerts.webp "Chaque mesure a son propre interrupteur. Une mesure sans alerte affiche Aucune alerte définie et un bouton Ajouter une alerte.")

La feuille du seuil a le même interrupteur en haut, à côté de **Alerte activée** ou **Alerte désactivée**. Si vous enregistrez une nouvelle plage sur une alerte désactivée, Cora demande **Activer cette alerte ?** Touchez **Activer** pour l’activer avec les nouvelles valeurs, ou **Laisser désactivée** pour les enregistrer en la laissant désactivée.

## Alertes d’appareils et de consommables {#doser-alerts}

Un équipement qui consomme quelque chose a un bouton **Paramètres d’alerte** sur sa page dans Cora Max. C’est le cas d’un Trident (réactifs et déchets), des têtes DŌS, des Red Sea ReefDose, ReefATO+ et ReefMat. Choisissez le niveau dont vous voulez être averti, et vous recevez une seule notification quand il est franchi. Sur une tête DŌS, **Alertes de dose manquée** vous prévient aussi quand la tête manque ses doses programmées.

La signification de chaque alerte de doseur est dans [Alertes des doseurs](/help/mobile-device-control#doser-alerts).


## Son d’alerte, alertes vocales et réveil de l’écran

Ces réglages ne concernent que cet écran. Vous les trouvez dans **Paramètres → Paramètres Cora Max**.

- **Son d’alerte** (sous **SON ET VOIX**) joue un son quand une nouvelle alerte arrive. Son curseur règle le volume.
- **Alertes vocales** (sous **SON ET VOIX**) fait dire l’alerte à voix haute par Cora.
- **Réveiller l’écran en cas d’alarme** (sous **AFFICHAGE**) rallume un écran atténué quand une alerte arrive. Les alertes critiques le réveillent toujours.

Pour qu’un Cora Max n’affiche plus du tout d’alertes à l’écran, ouvrez Cora Mobile, allez dans **Appareils →** votre Cora Max, et désactivez **Alertes**. L’historique des notifications et les notifications de votre téléphone ne changent pas.

:::note Une seule alerte pour tout le compte
Chaque appareil ne déclenche pas sa propre copie d’une alerte. Cora Max, votre téléphone et tout autre écran affichent la même, et elle disparaît de tous quand la mesure revient dans sa plage.
:::
