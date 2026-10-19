---
title: Contrôler votre équipement
description: Ouvrez la page d’un appareil pour voir son état en direct et commander prises, pompes, têtes de dosage et testeurs, marque par marque.
section: Cora Mobile
reviewed: 2026-10-18
order: 13
group: Equipment
twin: max-device-control
---

Utilisez la page d’un appareil pour voir son état en direct et changer ce qu’il fait. Ouvrez-la depuis **Appareils** → touchez l’appareil, ou touchez sa tuile sur le tableau de bord.

![La page d’un ReefATO+ dans Cora Mobile](img/mobile-device-detail.webp "L’état, les mesures du jour et le niveau d’eau, puis les fuites, les remplissages et l’étalonnage de la sonde.")

Toutes les pages d’appareils sont organisées de la même façon. Le nom et les détails sont en haut, puis une rangée de mesures en direct, l’état que l’appareil signale, et ses commandes. La cloche de la barre de titre règle les seuils d’alerte de cet appareil, comme décrit dans [Consommables](/help/mobile-consumables). La façon d’ajouter un appareil au départ est dans [Connecter votre équipement](/help/mobile-connections).

Aller directement à votre équipement : [Neptune Apex](#neptune-apex) · [Trident](#trident) · [DŌS](#dos) · [Red Sea](#red-sea) · [ReefDose](#reefdose) · [ReefRun](#reefrun) · [ReefMat](#reefmat) · [ReefATO+](#reefato) · [Alertes des doseurs](#doser-alerts) · [Jecod](#jecod) · [AquaWiz](#aquawiz)

:::warning Ces commandes agissent sur un équipement en fonctionnement
Il n’y a ni aperçu ni annulation. Certaines commandes vous demandent d’abord de confirmer.
:::

## Ce qui se passe quand vous envoyez une commande {#what-happens-when-you-send-a-command}

Une commande ne passe pas toujours. Cora vous dit laquelle de ces quatre choses s’est produite :

| Résultat | Signification |
|---|---|
| **Confirmé** | L’équipement a accepté le changement et a signalé son nouvel état |
| **Non confirmé** | La commande est partie, mais rien n’est revenu. **Cela veut dire "on ne sait pas". Cela ne veut pas dire que cela a marché.** Vérifiez l’état de l’appareil lui-même |
| **Refusé** | Quelque chose l’a refusée (une règle de sécurité, un verrou ou l’équipement lui-même), ou aucun appareil Cora ne l’a prise à temps. Elle a été annulée et rien ne s’est exécuté |
| **Aucun changement** | L’équipement était déjà réglé comme vous le demandiez |

Chaque résultat est enregistré dans [Activité](/help/mobile-activity), avec ce qui l’a causé.

Sans Cora Max à l’aquarium, l’équipement Neptune Apex, Red Sea et Jecod ne fonctionne qu’en local : votre téléphone doit être sur le même réseau (ou à portée Bluetooth) pour envoyer une commande. Avec un Cora Max à l’aquarium, Cora Mobile l’envoie par ce Cora Max, même quand vous êtes loin de chez vous.

## Neptune Apex {#neptune-apex}

![La page d’un Apex dans Cora Mobile, avec son état, ses modules Trident et DŌS, l’association des paramètres et l’aquarium qu’il dessert](img/mobile-apex.webp "La page de l’Apex : État, Modules, Association des paramètres et Aquariums.")

La page de l’Apex affiche l’état du contrôleur, puis **Modules**, **Association des paramètres** et **Aquariums**.

- **Modules** liste chaque Trident et chaque DŌS installés. Touchez-en un pour ouvrir sa propre page.
- **Association des paramètres** est l’endroit où vous choisissez ce qu’alimente chaque sonde. Les sondes arrivent dans Cora comme des sources, et vous pouvez les mettre sur un tableau de bord. Voir [Association des paramètres et sondes](/help/mobile-probes).
- **Aquariums** indique les aquariums que dessert l’Apex. Touchez **Modifier** pour les changer.
- Les **prises** passent de **Auto** à **Off** ou **On** depuis un widget **Prise** sur le tableau de bord. Auto rend le contrôle à votre programmation Apex. Voir [Référence des widgets](/help/mobile-widgets#outlet).

Votre Apex continue de suivre sa propre programmation. Cora ne change une prise que quand vous le demandez.

## Trident {#trident}

La page du Trident affiche l’état actuel du test et les niveaux de réactifs et d’eau usée. Vous pouvez lancer un test d’ici.

Vous pouvez aussi régler une alerte pour les tests restants et pour le flacon de déchets, pour que Cora vous prévienne avant que le réactif s’épuise ou que la bouteille se remplisse. Voir [Consommables](/help/mobile-consumables).

## DŌS {#dos}

![La page d’un DŌS qui indique que le DŌS ne répond pas sur l’AquaBus, avec sa dernière autonomie, la dose du jour et le plan quotidien, puis la ligne Alertes](img/mobile-dos.webp "Un DŌS hors de l’AquaBus : la page affiche ses derniers chiffres connus, une carte Attention requise et la ligne Alertes.")

Un DŌS QD fonctionne exactement comme un DŌS, et tout ce qui suit s’applique aux deux. Quand un Cora Max lit votre Apex, les têtes de dosage apparaissent sur la page du DŌS. Elles n’apparaissent jamais dans la liste des prises.

Chaque tête de dosage affiche ce qu’elle dose, son programme, ce qu’elle a dosé aujourd’hui et ce qui reste dans le réservoir. Elle affiche aussi l’**autonomie**, c’est-à-dire le nombre de jours que cela durera au rythme actuel.

Si le DŌS cesse de répondre sur l’AquaBus, sa page affiche **Hors du bus** et une carte **Attention requise**. Les chiffres de la page sont alors les derniers qu’il a signalés, pas ce qu’il fait maintenant. Vérifiez le câble AquaBus du module et l’Apex.

Pour chaque tête, vous pouvez :

- **Pause** et **Reprendre** son programme
- **Remplir**, pour dire à Cora que le réservoir est de nouveau plein ou régler ce qu’il contient (**Volume total** est la taille du réservoir, **Volume restant** est ce qu’il contient maintenant, et **Plein** règle l’un sur l’autre)
- **Doser maintenant**, pour une dose mesurée à la main

:::note Modifiez les programmes dans Apex Fusion
Cora affiche le programme et suit ce qui a été dosé, mais il ne change pas le programme. Vous modifiez le programme, le débit et le nombre de doses dans l’application Apex Fusion. La pause, le remplissage et le dosage à la main fonctionnent tous ici.
:::

:::note Mesurez une tête avant de doser à la main
Cora ne dose pas à la main avec une tête tant qu’elle n’a pas été mesurée. **Mesurer pour doser** et **Remesurer** se trouvent sur le Cora Max qui dose pour l’aquarium. Cora fait tourner la tête vingt secondes, vous mesurez ce qui est sorti, et Cora en déduit le vrai débit de la tête. Une seule mesure vaut pour tous les Cora Max et pour Cora Mobile. Mesurez chaque tête une fois, et à nouveau après avoir changé son tuyau.
:::

:::warning Un DŌS continue de doser quand son réservoir est vide
L’appareil n’a pas de capteur de niveau et ne s’arrête pas tout seul. Réglez une alerte de réapprovisionnement pour chaque tête sous **Alertes** sur la page du DŌS, pour que Cora vous prévienne avant que le réservoir soit à sec. Voir [Alertes des doseurs](#doser-alerts).
:::

### À quoi sert chaque tête {#dos-head-use}

Donnez à chaque tête un **type d’usage** pour que Cora sache ce qu’elle fait et en parle correctement. Les choix sont **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture**, **Appoint** et **Autre**. Réglez-le sous **Utilisée pour** dans les paramètres de la tête.

Les deux types d’usage de changement d’eau vont par **paires**. Réglez la **Tête associée** d’une tête sur la tête qui déplace l’eau dans l’autre sens, et Cora traite les deux comme une seule paire de changement d’eau.

Un réservoir peut faire jusqu’à 1 000 L, pour tous les types d’usage. L’Apex lui-même ne compte que jusqu’à 150 L, donc au-delà, Cora suit lui-même le réservoir d’après ce que dose la tête. Saisissez le **Volume total** lors de la configuration. Cora remet aussi de temps en temps à zéro le compteur propre de l’Apex, et Activité l’affiche comme *Compteur propre de l'Apex remis à 150 L*.

Chaque tête a aussi une limite de **Dosage manuel maximal**, pour qu’une faute de frappe ne puisse pas transformer une dose manuelle en quelque chose de bien plus gros que prévu. Les grosses doses à la main ne deviennent disponibles qu’après que le débit de la tête a été mesuré par un vrai test à l’aquarium, et après que vous avez activé **Doses importantes** dans les paramètres de la tête. C’est désactivé par défaut. Ne l’activez qu’après avoir regardé la première grosse dose se faire à l’aquarium.

## Red Sea ReefBeat {#red-sea}

Chaque appareil Red Sea a une page adaptée à ce qu’il fait :

| Appareil | La page affiche | Vous pouvez |
|---|---|---|
| [ReefDose](#reefdose) | Chaque tête, son réservoir et ce qu’elle a dosé | Doser, changer la dose quotidienne, modifier le **Programme de dosage** |
| [ReefRun](#reefrun) | La vitesse et l’état des pompes de remontée et d’écumeur | Changer la vitesse, allumer ou éteindre une pompe |
| [ReefMat](#reefmat) | Le rouleau restant, en jours et en mètres | Faire avancer le tapis, régler les **Paramètres ReefMat**, enregistrer un nouveau rouleau |
| [ReefATO+](#reefato) | Le niveau du réservoir et l’activité de l’osmolateur | Régler une alerte de réservoir |



Quand vous êtes loin du réseau de l’appareil, Cora Mobile envoie les commandes Red Sea par un Cora Max de l’aquarium. Si aucun Cora Max ne peut le faire, la page l’indique et rien n’est envoyé.

## ReefDose {#reefdose}

![La page d’un ReefDose 4 dans Cora Mobile](img/mobile-reefdose.webp "L’état, les têtes et le total du jour, l’utilisation du doseur pour la consommation, puis chaque tête de dosage.")

Pour chaque tête, vous pouvez régler la **Dose par jour** et le **Restant dans le flacon**, lancer **Doser maintenant**, et **Activer le programme**. Les alertes de réapprovisionnement se règlent par tête avec la cloche, comme décrit dans [Alertes des doseurs](#doser-alerts).

La section **Dosage** affiche les **Prochaines doses**, ce que chaque tête a dosé aujourd’hui (**Dosé aujourd'hui jusqu'ici**), et **Dosé par tête** sur les **7 derniers jours** ou au **Total**. Cora lit ces données tant qu’un Cora Max ou votre téléphone est sur votre réseau domestique.

### Modifier un programme de dosage {#reefdose-plan}

Touchez l’icône de calendrier sur la page d’un ReefDose pour ouvrir le **Programme de dosage**.

Un programme est un total quotidien, réparti sur quatre plages horaires au plus. Chaque plage a une heure de début et de fin, le nombre de doses à délivrer et une vitesse : **Silencieux**, **Normal** ou **Rapide**. Ajoutez et retirez des plages, puis enregistrez. Cora vous montre ce que vous allez envoyer et vous demande de confirmer avant de remplacer tout le programme de la tête.

L’éditeur lit d’abord le programme qui se trouve déjà sur l’appareil : vous modifiez donc le vrai programme, pas un formulaire vierge.

## ReefRun {#reefrun}

ReefRun commande les pompes de remontée et d’écumeur. Ce n’est pas une pompe de brassage. Vous pouvez changer la vitesse d’une pompe, l’allumer ou l’éteindre, et ajuster les réglages de l’écumeur.


## ReefMat {#reefmat}

La page du ReefMat affiche le rouleau restant, en jours et en mètres. Touchez **Avancer maintenant** pour faire avancer le tapis à la main. Cora demande d’abord **Avancer le tapis maintenant ?** Vous pouvez aussi régler une alerte de réapprovisionnement pour le rouleau.

Touchez la roue dentée pour les **Paramètres ReefMat** :

- **Avance programmée** active une avance à heure fixe, indépendante du capteur d’avance automatique déjà présent sur la page. Activez-la et réglez la fréquence, et la distance de chaque avance.
- **Modèle ReefMat** et **Position du moteur** (**Gauche** ou **Droite**) indiquent à Cora quel appareil et quelle orientation vous avez.

Après avoir mis un nouveau rouleau, indiquez-le à Cora avec **Nouveau rouleau** : son épaisseur, et son diamètre extérieur si vous le connaissez. **Avancer maintenant** ne fait que déplacer le tapis déjà chargé.

## ReefATO+ {#reefato}

La page du ReefATO+ affiche le niveau du réservoir et les appoints récents. Réglez une alerte de réservoir avec la cloche. Cora estime combien de jours il reste au réservoir d’après la consommation récente de l’osmolateur, et vous pouvez aussi interroger l’Assistant à ce sujet.

## Quand un appareil Red Sea s’arrête de lui-même {#red-sea-stops}

Un appareil peut s’arrêter de lui-même. Une pompe ReefRun le fait par exemple quand le godet de l’écumeur est pleine. Dans ce cas, la page dit pourquoi et propose la solution :

| Appareil | La page indique | Touchez |
|---|---|---|
| ReefRun | Quelle pompe s’est arrêtée et pourquoi, par exemple *Godet plein. Videz-le, puis reprenez.* | **Reprendre** |
| ReefRun ou ReefMat | **Arrêt d’urgence** | **Effacer l’urgence** |
| ReefMat | **Tapis coincé**, **Erreur d’installation** ou **Erreur de configuration** | **Reprendre** |
| ReefMat | *Chargez un nouveau rouleau, puis confirmez-le dans l’application Red Sea.* | **J’ai déjà chargé un nouveau rouleau** |
| ReefMat | **Le capteur doit être nettoyé** | **Capteur nettoyé** |
| ReefDose | **Dysfonctionnement de la tête**, avec le nom de la tête | **Réinitialiser** |
| ReefATO+ | **Effacer la panne** | **Reprendre** |

Certaines de ces actions vous demandent d’abord de confirmer. Loin du réseau de l’appareil, elles passent par un Cora Max de l’aquarium, comme décrit dans [Red Sea ReefBeat](#red-sea).

## Alertes des doseurs {#doser-alerts}

Un DŌS et un ReefDose gardent leurs alertes sur leur propre page. L’onglet **Règles** du [Centre d’alertes](/help/mobile-alerts) a une ligne par doseur qui l’ouvre, et le bouton **Ouvrir le doseur** d’une alerte de doseur vous amène aussi ici.

Sur la page d’un DŌS, touchez la carte **Alertes** (ou la cloche de la barre de titre). La feuille liste chaque tête, et pour chacune vous pouvez régler :

- *[tête] · jours restants*, par exemple *Iode · jours restants* : vous recevez une alerte en dessous de ce nombre de jours de réserve
- *[tête] · restant* : vous recevez une alerte en dessous de cette quantité restante dans le réservoir
- **Espace restant dans le réservoir d’eau usée**, pour une tête qui retire l’eau usée : vous recevez une alerte quand le réservoir d’eau usée se remplit
- **Alertes de dose manquée** : un interrupteur qui vous prévient quand la tête manque une dose programmée

Chaque seuil a son propre interrupteur, pour que vous puissiez en désactiver un en gardant sa valeur. Touchez **Enregistrer** quand vous avez fini.

Sur la page d’un ReefDose, touchez la cloche de la barre de titre. Chaque tête a son propre seuil en jours restants et son interrupteur.

Les valeurs par défaut et les autres consommables sont dans [Consommables](/help/mobile-consumables).

## Pompes Jecod / Jebao {#jecod}

La page de la pompe affiche le type de vague actuel (le mode) et l’intensité, et vous pouvez changer les deux. Son état s’affiche dans la ligne de titre, à côté du nom de la pompe. Un sélecteur **Identique toute la journée** / **Programme** marque celui qui fonctionne avec *· en cours*, et la page s’ouvre dessus. La création d’un programme journalier, et sa copie, son enregistrement ou son partage, sont dans [Programmer l’équipement](/help/mobile-schedules).

Si la pompe fait partie d’un groupe, la page affiche son rôle, comme **Mène le groupe**, **Suit : en phase** ou **Suit : en alternance**.

### Pause nourrissage {#jecod-feeding}

Lancez une pause nourrissage depuis **Nourrissage** sur la page de la pompe : touchez **5**, **10**, **15** ou **30** min. Certaines pompes terminent la pause d’elles-mêmes, et la page indique *La pompe met fin à cela elle-même.*

:::warning Gardez la page de la pompe ouverte pendant une pause nourrissage
Certaines pompes ne terminent pas un nourrissage d’elles-mêmes, et la page l’indique. Pour celles-là, et pour toute pompe sur un programme, Cora Mobile ne rétablit le type de vague et le programme que tant que la page de la pompe reste ouverte. Si vous quittez la page, la pompe reste arrêtée en mode nourrissage, ou reste hors de son programme, jusqu’à ce que vous la changiez à nouveau ou que vous touchiez **Programme**.
:::

Si votre foyer a un Cora Max, il met fin au nourrissage et remet la pompe sur son programme à la fin du temps, même si Cora Mobile est fermé. L’avertissement ci-dessus ne compte alors que s’il n’y a pas de Cora Max.

Une pompe Bluetooth doit être à portée de votre téléphone pour lancer un nourrissage, et une pompe réseau doit être sur votre réseau.

### Vérifications de pannes {#jecod-fault-checks}

**Vérifications de pannes** règle la fréquence à laquelle Cora relit la pompe pour vous prévenir d’une panne, comme une pompe bloquée ou qui tourne à sec. Si vous le désactivez, ces avertissements s’arrêtent pour cette pompe. Les vérifications de pannes nécessitent un Cora Max à l’aquarium. Votre choix est enregistré et les vérifications démarrent dès qu’un Cora Max est ajouté. **Utiliser ceci pour toutes les pompes de cet aquarium** copie le réglage sur toutes.

## AquaWiz {#aquawiz}

La carte AquaWiz affiche vos mesures d’alcalinité, et le pH si votre appareil le signale. Elle affiche aussi votre KH cible, la concentration de votre dose et, pour un appareil avec le dosage configuré, sa dose maximale par heure et la quantité de produit d’alcalinité restant dans le réservoir. Ces valeurs viennent directement de vos réglages AquaWiz : changez-les donc dans l’application AquaWiz. Cora ne peut pas commander un AquaWiz.

Sous les mesures, la carte indique quand la dernière a été prise (par exemple *Mesuré 14:00*) et d’où elle vient : **Toutes les heures depuis votre Cora Max** ou **Depuis le cloud AquaWiz, toutes les 12 heures**. Elle affiche aussi la **variation du pH**. L’ouverture de la page demande une mesure fraîche, et **Lire maintenant** la redemande, au plus une fois toutes les 15 minutes. Si une mesure n’a pas changé, c’est normal : l’appareil ne mesure que de temps en temps.

Quand un Cora Max lit l’appareil toutes les heures, la carte affiche aussi sa pompe, sa sonde de pH et le niveau du réservoir d’eau, et Cora vous alerte quand la pompe signale un défaut, quand la sonde de pH est en panne ou presque en fin de vie, ou quand le niveau du réservoir d’eau reste bas ou haut plus d’une heure.

Si votre appareil suit son réservoir, Cora vous prévient quand le produit s’épuise, à 100 mL par défaut. Changez-le depuis sa règle dans le [Centre d’alertes](/help/mobile-alerts).


## Ce qui se passe après un changement {#what-happens-after-you-change-something}

Chaque changement est enregistré dans [Activité](/help/mobile-activity), avec l’interface d’où il vient. Si un appareil n’accepte pas un changement, c’est aussi enregistré là.
