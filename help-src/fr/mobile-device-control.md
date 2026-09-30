---
title: Contrôler votre équipement
description: La page de chaque appareil montre son état en direct et ses commandes, pour les prises, les pompes, les têtes de dosage et les testeurs.
section: Cora Mobile
reviewed: 2026-09-30
order: 11
group: Equipment
---

Chaque équipement connecté a sa page dans Cora. Vous y voyez son état en direct et les commandes qu’il accepte. Ouvrez-la depuis l’onglet **Appareils**.

![Une page d’appareil](img/mobile-device-detail.webp "Mesures en direct en haut, puis les commandes que cet appareil prend en charge.")

Toutes les pages d’appareil sont construites pareil. En haut, le nom de l’appareil, puis une ligne de mesures en direct, l’état indiqué par l’appareil et enfin ses commandes. La cloche dans la barre de titre règle les seuils d’alerte de l’appareil, comme expliqué dans [Consommables](/help/mobile-consumables).

:::warning Ces commandes agissent sur l’équipement en direct
Il n’y a ni aperçu ni annulation. Certaines commandes demandent aussi une confirmation.
:::

## Après l’envoi d’une commande

Une commande ne réussit pas toujours. Cora ne fait pas de supposition et vous indique lequel de ces quatre résultats s’est produit.

| Résultat | Signification |
|---|---|
| **Confirmé** | L’équipement a accepté le changement et a indiqué son nouvel état |
| **Non confirmé** | La commande est partie, mais aucune réponse n’est revenue. **Cela veut dire « on ne sait pas », et non « ça a marché »**. Vérifiez l’état affiché par l’appareil lui-même |
| **Refusé** | Quelque chose a bloqué la commande (une règle de sécurité, un verrou ou l’équipement lui-même), ou aucun appareil Cora ne l’a prise en charge à temps. Elle a été annulée et rien ne s’est exécuté |
| **Aucun changement** | L’équipement était déjà dans l’état demandé |

Chaque résultat est enregistré dans [Activité](/help/mobile-activity), avec sa source.

## Neptune Apex

La page Apex liste vos sondes et vos prises.

- **Les sondes** deviennent des sources dans Cora, que vous pouvez placer sur un tableau de bord.
- **Les prises** passent de **Auto** à **Éteint** ou **Allumé**. Auto rend la main à votre programmation Apex.
- **Les modules installés** (Trident, DŌS et autres) ont chacun leur page.

## Trident

La page indique où en est le test, ce qui reste de réactif et le niveau d’eau usée. Vous pouvez aussi y lancer un test.

Depuis cette page, vous pouvez régler un seuil d’alerte sur les tests restants. Cora vous préviendra avant la fin du réactif. Voir [Consommables](/help/mobile-consumables).

## DŌS

Un DŌS QD fonctionne exactement comme un DŌS, et tout ce qui suit vaut pour les deux. Quand un Cora Max lit votre Apex, les têtes de dosage apparaissent sur la page DŌS, jamais dans la liste des prises.

Pour chaque tête de dosage, vous voyez le produit dosé, le programme, la quantité dosée aujourd’hui, ce qui reste dans le bidon et son **autonomie**, c’est-à-dire le nombre de jours restants au rythme actuel.

Pour chaque tête, vous pouvez :

- **Suspendre** et **Reprendre** son programme
- **Remplir**, pour indiquer à Cora que le bidon est de nouveau plein, ou saisir le volume qu’il contient
- **Doser maintenant**, pour envoyer une dose précise à la main

:::note Les programmes se modifient dans Apex Fusion
Cora affiche le programme et suit ce qui a été dosé, mais ne le modifie pas. Le programme, le débit et le nombre de doses se changent dans l’application Apex Fusion. Ici, vous pouvez suspendre, remplir et doser à la main.
:::

:::note Mesurez une tête avant de doser à la main
Cora ne dose pas à la main avec une tête qui n’a pas été mesurée. **Mesurer pour doser** et **Remesurer** se trouvent sur le Cora Max qui gère le dosage de l’aquarium. Cora fait tourner la tête pendant vingt secondes, vous mesurez ce qui est sorti, et Cora calcule le vrai débit de la tête. Une seule mesure sert pour tous les Cora Max et Cora Mobile. Mesurez donc chaque tête une fois, puis de nouveau après un changement de tuyau.
:::

:::warning Un DŌS continue à doser avec un bidon vide
L’appareil n’a pas de capteur de niveau et ne s’arrête pas tout seul. Réglez une alerte de réapprovisionnement depuis la page de la tête. Cora vous préviendra avant que le bidon soit vide.
:::

### L’usage de chaque tête

Chaque tête a un **type d’usage**. Cora sait ainsi à quoi elle sert et peut en parler correctement. Les choix sont **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture**, **Appoint** et **Autre**. Le type se règle sous **Utilisée pour**, dans les réglages de la tête.

Les deux types de changement d’eau vont **par paire**. Dans **Tête associée**, choisissez la tête qui déplace l’eau dans l’autre sens. Cora traite alors les deux têtes comme une seule paire de changement d’eau.

Chaque tête a aussi une limite de **Dosage manuel maximal**. Elle évite qu’une faute de frappe envoie une dose bien plus grosse que prévu. Les grosses doses manuelles ne sont possibles qu’une fois le débit de la tête mesuré avec un vrai test à l’aquarium, et une fois **Doses importantes (bêta)** activé dans les réglages de la tête. C’est désactivé par défaut. Activez ceci seulement après avoir observé la première dose importante s’exécuter devant l’aquarium.

## Red Sea ReefBeat

Chaque appareil a une page adaptée à ce qu’il fait.

| Appareil | La page affiche | Vous pouvez |
|---|---|---|
| **ReefDose** | Chaque tête, son bidon et ce qu’elle a dosé | Pour chaque tête : **Dose par jour**, **Restant dans le flacon**, **Doser maintenant** et **Activer le programme**, plus un éditeur complet **Programme de dosage (bêta)**. Régler des alertes de réapprovisionnement par tête |
| **ReefATO+** | Niveau du réservoir et activité de l’osmolateur | Régler une alerte de réservoir. Demander à l’Assistant combien de jours il reste à son réservoir |
| **ReefMat** | Rouleau restant, en jours et en mètres | Faire avancer le rouleau, régler une alerte de réapprovisionnement, et, en bêta, activer une avance programmée, régler son modèle et la position du moteur, et enregistrer un nouveau rouleau |
| **ReefRun** | Vitesse et état de la pompe de remontée et de la pompe d’écumeur | Changer la vitesse, allumer ou éteindre une pompe, ajuster les réglages de l’écumeur, et modifier un programme de vitesse complet *(bêta)* |
| **ReefControl** *(bêta)* | Ses sondes de température, pH, salinité et ORP | Voir ses mesures |
| **ReefWave**, **ReefLED** *(bêta)* | Son mode actuel | Lecture seule pour l’instant |

**ReefRun pilote la pompe de remontée et la pompe d’écumeur.** Ce n’est pas une pompe de brassage. Les prises **ReefControl Power** *(bêta)* apparaissent comme des prises, pilotées depuis la même commande de prise qu’une prise Apex, seulement allumé ou éteint. Il n’y a pas encore de mode automatique pour elles.

## Modifier un programme ReefDose ou ReefRun *(bêta)*

Touchez l’icône de calendrier sur une page ReefDose ou ReefRun pour ouvrir son programme.

Un programme ReefDose est un total quotidien, réparti en jusqu’à quatre plages horaires. Chaque plage a une heure de début et de fin, un nombre de doses à délivrer, et une vitesse : **Silencieux**, **Normal** ou **Rapide**. Ajoutez et retirez des plages, puis enregistrez. Cora vous montre ce que vous êtes sur le point d’envoyer et vous demande de confirmer avant de remplacer tout le programme de la tête.

Un programme ReefRun compte jusqu’à six segments sur un seul port de pompe. Chaque segment a une heure de début et une vitesse, et peut ajouter une courte impulsion. La vitesse est soit 0, soit à partir de 5 %. Enregistrer demande aussi une confirmation, et remplace tout le programme de la pompe.

Les deux éditeurs lisent d’abord le programme déjà présent sur l’appareil : vous modifiez donc le programme réel, pas un formulaire vide.

## Paramètres ReefMat *(bêta)*

Touchez l’icône d’engrenage sur une page ReefMat pour trois réglages de plus.

- **Avance programmée** active une avance à heure fixe, séparée du capteur d’avance automatique déjà présent sur la page. Activez-la et réglez la fréquence, ainsi que la distance parcourue par le tapis à chaque avance.
- **Modèle ReefMat** et **Position du moteur** (**Gauche** ou **Droite**) indiquent à Cora quel appareil et quelle orientation vous avez.

Après avoir chargé un nouveau rouleau, informez-en Cora avec **Nouveau rouleau (bêta)** : son épaisseur, et son diamètre extérieur si vous le connaissez. C’est différent de **Faire avancer le rouleau**, qui se contente de déplacer le tapis déjà chargé.

Un appareil peut s’arrêter de lui-même. Par exemple, une pompe ReefRun s’arrête quand le godet de l’écumeur est plein. Dans ce cas, sa page explique pourquoi et propose la solution.

| Appareil | La page affiche | Touchez |
|---|---|---|
| ReefRun | La pompe arrêtée et la raison, par exemple *Godet plein. Videz-le, puis reprenez.* | **Reprendre** |
| ReefRun ou ReefMat | **Arrêt d’urgence** | **Effacer l’urgence** |
| ReefMat | **Tapis coincé**, **Erreur d’installation** ou **Erreur de configuration** | **Reprendre** |
| ReefMat | *Chargez un nouveau rouleau, puis confirmez-le dans l’application Red Sea.* | **J’ai déjà chargé un nouveau rouleau** |
| ReefMat | **Le capteur doit être nettoyé** | **Capteur nettoyé** |
| ReefDose | **Dysfonctionnement de la tête**, avec le nom de la tête | **Réinitialiser** |
| ReefATO+ | **Effacer la panne** | **Reprendre** |

Certaines de ces actions demandent une confirmation. Si vous n’êtes pas sur le réseau de l’appareil, Cora Mobile les envoie par un Cora Max de l’aquarium. Si aucun Cora Max ne peut s’en charger, la page le signale et rien n’est envoyé.

## Pompes Jecod

La page de la pompe affiche son mode et son intensité, et vous pouvez changer les deux.

Vous pouvez aussi :

- **Copier le programme vers…** pour mettre le programme de cette pompe sur une autre
- **Enregistrer le programme sous…** et **Programmes enregistrés…** pour garder un programme et le réappliquer plus tard
- **Partager ce programme** et **Coller un code de programme…** pour passer un programme d’un système à l’autre sous forme de code court

## Maxspect

:::note La prise en charge Maxspect est en bêta
La prise en charge des pompes de brassage Maxspect est encore en test et en développement. Certaines commandes peuvent être limitées, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

La page de la pompe indique si elle tourne, le type de vague et la vitesse de **Gyre A** et **Gyre B**, et l’heure de la dernière lecture. Depuis cette page, vous pouvez :

- allumer ou éteindre la pompe avec l’interrupteur à côté de son état. Cora vous demande d’abord de confirmer. L’arrêt coupe les deux gyres et ne touche pas au programme.
- toucher **Modifier les réglages** pour régler le type de vague et la vitesse de chaque gyre (et la durée, pour les types de vague qui en ont une), et choisir si les deux gyres sont liés. Cora liste les changements et vous demande de confirmer avant de les appliquer. Le mode alterné se règle dans l’application Maxspect. Une pompe qui l’utilise garde ses rampes et ses temps de maintien.
- toucher **Programme défini** quand le programme enregistré dans la pompe est illisible. Cette commande règle les deux gyres pour que la pompe puisse redémarrer.
- voir le programme journalier de la pompe sur la carte **Programme**. Il est en lecture seule. Le programme se règle dans l’application Maxspect.
- consulter l’**État de la pompe** : la date du prochain nettoyage (la pompe fait elle-même le décompte), le courant consommé par la tête A, les têtes installées et le micrologiciel. Touchez **Lire** pour récupérer ces informations.

:::note Comment Cora Mobile joint une pompe Gyre
Si un Cora Max gère l’aquarium, Cora Mobile passe par ce Cora Max, même quand vous êtes loin de chez vous. **Modifier les réglages** part alors de la dernière lecture de ce Cora Max. Sinon, votre téléphone parle directement à la pompe et doit être sur le même réseau qu’elle. Ouvrir la page lance alors une lecture de la pompe. Si la page affiche une lecture plus ancienne gardée en mémoire, **Modifier les réglages** reste masqué jusqu’à ce que vous touchiez actualiser.
:::

## GHL ProfiLux et Mitras

:::note La prise en charge GHL est en bêta
Nous testons et développons encore la prise en charge GHL. Certaines mesures ou commandes peuvent ne pas encore marcher, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

La page du contrôleur affiche ses sondes, ses prises, ses doseurs et ses capteurs de niveau, et sur les modèles Director, ses résultats de test KH et ionique.

Les commandes restent désactivées tant que vous n’activez pas **Autoriser le contrôle depuis Cora (bêta)** sur la page de l’appareil. C’est désactivé par défaut, et l’activer permet à Cora d’envoyer des commandes de pause d’alimentation, entretien, changement d’eau, orage, éclairage, consigne et prise à ce contrôleur.

Une fois activé :

- Une prise peut être réglée sur **Toujours activé**, **Toujours désactivé**, ou **Revenir en mode automatique** pour la rendre à la programmation du contrôleur.
- Une consigne, comme la température ou le pH, affiche sa plage autorisée et refuse une valeur en dehors.

:::warning Un changement de prise ou de consigne est enregistré sur le contrôleur lui-même
Ce réglage reste enregistré là même si Cora perd ensuite le contact avec le contrôleur. Régler une prise sur Toujours activé ou Toujours désactivé prend le pas sur la programmation du contrôleur pour elle, jusqu’à ce que vous choisissiez Revenir en mode automatique.
:::

Si une prise ou une consigne ressemble à un chauffage ou une pompe de remontée, Cora vous demande de confirmer deux fois avant de l’envoyer.

Si le bidon d’un doseur devient bas, Cora vous prévient de la même façon que pour les autres consommables. La valeur par défaut est 20 % plein, et vous pouvez la changer depuis la règle du doseur dans le [Centre d’alertes](/help/mobile-alerts).

:::note ProfiLux mini
Un mini peut seulement commuter ses prises. Tout le reste ici, comme les consignes et la pause nourrissage, nécessite un ProfiLux 3, 4 ou Mitras.
:::

Si le contrôleur refuse le changement, vérifiez que son API GHL est activée avec un accès complet. GHL la désactive après chaque mise à jour du micrologiciel. [Résolution de problèmes](/help/troubleshooting) donne la suite.

## HYDROS

:::note La prise en charge HYDROS est en bêta
Nous testons et développons encore la prise en charge HYDROS. Certaines mesures ou commandes peuvent ne pas encore marcher, et ce que vous voyez ici peut changer d’une mise à jour à l’autre. Si quelque chose ne marche pas comme décrit, prévenez-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

Ce que vous voyez ici dépend de la clé avec laquelle vous l’avez lié. Une clé **Lecture** vous donne seulement ses entrées. Une clé **Écriture** ajoute les sorties, les modes, le dosage et les commandes de testeur, ainsi qu’une bannière en haut de page qui rappelle quel type de clé vous avez.

Avec une clé d’écriture, les commandes restent aussi désactivées tant que vous n’activez pas **Autoriser le contrôle depuis Cora (bêta)** sur la page de l’appareil. C’est désactivé par défaut.

Une fois activé, la page peut afficher :

- Les **sorties**, sous forme d’interrupteur pour une sortie tout ou rien, de curseur pour un niveau comme une pompe ou un éclairage, ou de bouton pour un indicateur. Une sortie forcée affiche **Forcé** avec un bouton **Retour au programme** pour la rendre à son propre programme.
- Les **modes**, comme Nourrissage ou Changement d’eau, sous forme d’une ligne de choix. Toucher l’un d’eux vous demande de confirmer.
- Les **têtes de dosage**, chacune avec un bouton **Doser** et une entrée **Réglages de la tête** où vous fixez ses propres limites : une plus grosse dose à la main et un plafond quotidien. Demander plus que la limite d’une tête, ou plus que ce que son propre plafond quotidien a encore laissé pour la journée, est refusé avec les chiffres dans le message.
- Les **commandes de testeur**, pour un iV ou un Maven connecté, se lancent depuis un bouton et sont confirmées d’abord.

Si le contrôleur n’a pas donné de nouvelles depuis un moment, la page le signale et les mesures peuvent être périmées. Une commande envoyée pendant qu’il semble hors ligne n’est pas envoyée du tout, et la page vous le dit aussi.

## Après un changement

Chaque changement est enregistré dans [Activité](/help/mobile-activity), avec l’interface qui l’a demandé. Si un appareil refuse un changement, l’échec y est aussi enregistré.
