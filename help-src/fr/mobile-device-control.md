---
title: Contrôler votre équipement
description: Ouvrez la propre page d’un appareil pour voir son état en direct et le piloter : prises, pompes, têtes de dosage et testeurs.
section: Cora Mobile
reviewed: 2026-09-27
order: 11
group: Equipment
---

L’équipement connecté a sa propre page dans Cora, montrant l’état en direct et proposant les commandes que cet appareil prend en charge. Ouvrez-en une depuis l’onglet **Appareils**.

![Une page d’appareil](img/mobile-device-detail.webp "Mesures en direct en haut, puis les commandes que cet appareil prend en charge.")

Chaque page d’appareil suit la même forme : identification en haut, une ligne de mesures en direct, tout état que l’appareil rapporte, puis ses commandes. La cloche dans la barre de titre règle les seuils d’alerte pour cet appareil ; voir [Consommables](/help/mobile-consumables).

:::warning Ces commandes agissent sur un équipement en direct
Il n’y a pas d’aperçu et pas d’annulation. Certaines commandes vous demandent aussi de confirmer d’abord.
:::

## Ce qui se passe quand vous envoyez une commande

Une commande ne réussit pas toujours, et Cora vous dit laquelle des quatre choses s’est produite plutôt que de le supposer :

| Résultat | Signifie |
|---|---|
| **Confirmé** | L’équipement a accusé réception du changement et a rapporté son nouvel état |
| **Non confirmé** | La commande a été envoyée, mais rien n’a été signalé en retour. **Cela signifie « nous ne savons pas », pas « cela a fonctionné »** ; vérifiez le propre état de l’appareil |
| **Refusé** | Quelque chose l’a refusée (une règle de sécurité, un verrou, ou l’équipement lui-même), ou aucun appareil Cora ne l’a prise à temps, donc elle a été annulée et rien ne s’est exécuté |
| **Aucun changement** | L’équipement était déjà dans l’état que vous demandiez |

Chaque résultat est enregistré dans [Activité](/help/mobile-activity) avec ce qui l’a causé.

## Neptune Apex

La page Apex liste vos sondes et prises.

- **Les sondes** rapportent dans Cora comme des sources et peuvent être placées sur un tableau de bord.
- **Les prises** commutent entre **Auto**, **Éteint** et **Allumé**. Auto redonne le contrôle à votre programmation Apex.
- **Les modules installés** (Trident, DŌS et autres) ont chacun leur propre page.

## Trident

Affiche l’état actuel du test, les niveaux restants de réactif et d’eau de déchet, et vous permet de démarrer un test.

Vous pouvez régler un seuil d’alerte pour les tests restants depuis cette page, pour que Cora vous avertisse avant que le réactif ne s’épuise. Voir [Consommables](/help/mobile-consumables).

## DŌS

Un DŌS QD fonctionne exactement comme un DŌS, et tout ce qui suit s’applique aux deux. Quand un Cora Max lit votre Apex, les têtes de dosage apparaissent sur la page DŌS, jamais dans la liste des prises.

Chaque tête de dosage montre ce qu’elle dose, son programme, ce qu’elle a dosé aujourd’hui, combien il reste dans le contenant et son **autonomie** : combien de jours cela durera au rythme actuel.

Par tête, vous pouvez :

- **Suspendre** et **Reprendre** son programme
- **Remplir** : dire à Cora que le contenant est de nouveau plein, ou régler le volume qu’il contient
- **Doser maintenant** : un dosage manuel mesuré

:::note Les programmes se modifient dans Apex Fusion, pas ici
Cora affiche le programme et suit ce qui a été dosé, mais ne le change pas. Modifier le programme, le débit de dosage ou le nombre de dosages se fait dans l’application Apex Fusion. Suspendre, remplir et doser à la main sont tous pris en charge ici.
:::

:::note Mesurez une tête avant de la doser à la main
Cora ne dosera pas une tête à la main jusqu’à ce qu’elle ait été mesurée. **Mesurer pour doser** et **Remesurer** se trouvent sur le Cora Max qui dose pour l’aquarium : Cora exécute la tête pendant vingt secondes, vous mesurez ce qui en est sorti, et Cora calcule le débit réel de la tête. Une mesure sert chaque Cora Max et Cora Mobile, donc mesurez chaque tête une fois, et à nouveau après avoir changé son tuyau.
:::

:::warning Un DŌS continue de doser quand son contenant est vide
L’unité n’a pas de capteur de niveau et ne s’arrête pas d’elle-même. Réglez une alerte de réapprovisionnement depuis la page de la tête pour que Cora vous avertisse avant que le contenant ne s’assèche.
:::

### À quoi sert chaque tête

Chaque tête est réglée sur un **type d’usage**, pour que Cora sache ce qu’elle fait et puisse en parler correctement : **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture**, **Appoint**, ou **Autre**. Réglez cela sous **Utilisée pour** dans les réglages de la tête.

Les deux types d’usage de changement d’eau sont conçus pour être **associés** : réglez la **Tête associée** d’une tête sur l’autre qui déplace l’eau dans le sens opposé, et Cora les traite comme une paire de changement d’eau plutôt que comme deux têtes sans rapport.

Chaque tête a aussi un plafond de **Dosage manuel maximal**, pour empêcher un dosage manuel mal saisi d’être bien plus important que prévu. Les gros dosages manuels ne deviennent disponibles qu’une fois le débit de la tête mesuré par rapport à un vrai test à l’aquarium.

## Red Sea ReefBeat

Chaque unité a une page adaptée à ce qu’elle est :

| Unité | La page affiche | Vous pouvez |
|---|---|---|
| **ReefDose** | Chaque tête, son contenant et ce qu’elle a dosé | Pour chaque tête : **Dose par jour**, **Restant dans le flacon**, **Doser maintenant** et **Activer le programme**. Réglez des alertes de réapprovisionnement par tête |
| **ReefATO+** | Niveau du réservoir et activité de complément | Réglez une alerte de réservoir |
| **ReefMat** | Rouleau restant, en jours et mètres | Avancez le rouleau, réglez une alerte de réapprovisionnement |
| **ReefRun** | Vitesse et état des pompes de remontée et d’écumeur | Changez la vitesse, commutez une pompe, ajustez les réglages de l’écumeur |

**ReefRun est un contrôleur de pompe de remontée et d’écumeur**, pas une pompe de brassage.

Une unité peut s’arrêter elle-même, par exemple une pompe ReefRun quand le godet de l’écumeur se remplit. Quand cela arrive, sa page dit pourquoi et propose la correction :

| Unité | La page dit | Touchez |
|---|---|---|
| ReefRun | Quelle pompe s’est arrêtée et pourquoi, par exemple *Godet plein. Videz-le, puis reprenez.* | **Reprendre** |
| ReefRun ou ReefMat | **Arrêt d’urgence** | **Effacer l’urgence** |
| ReefMat | **Tapis coincé**, **Erreur d’installation** ou **Erreur de configuration** | **Reprendre** |
| ReefMat | *Chargez un nouveau rouleau, puis confirmez-le dans l’application Red Sea.* | **J’ai déjà chargé un nouveau rouleau** |
| ReefMat | **Le capteur doit être nettoyé** | **Capteur nettoyé** |
| ReefDose | **Dysfonctionnement de la tête**, avec le nom de la tête | **Réinitialiser** |
| ReefATO+ | **Effacer la panne** | **Reprendre** |

Certaines de ces actions vous demandent de confirmer d’abord. Loin du réseau de l’unité, Cora Mobile les envoie via un Cora Max de l’aquarium ; si aucun Cora Max ne peut le faire, la page le précise et rien n’est envoyé.

## Pompes Jecod

La page de la pompe affiche son mode et son intensité actuels, et vous permet de changer les deux.

Vous pouvez aussi :

- **Copier le programme vers…** : mettre le programme de cette pompe sur une autre
- **Enregistrer le programme sous…** et **Programmes enregistrés…** : garder un programme et le réappliquer plus tard
- **Partager ce programme** et **Coller un code de programme…** : déplacer un programme entre systèmes sous forme de code court

## Maxspect

:::note La prise en charge Maxspect est en bêta
La prise en charge des pompes de brassage Maxspect est encore en cours de test et de développement, donc certaines commandes peuvent être limitées, et ce que vous voyez ici peut changer entre les mises à jour. Si quelque chose ne fonctionne pas comme décrit, dites-le-nous depuis [Obtenir de l’aide](/help/mobile-support).
:::

La page de la pompe de brassage montre si elle fonctionne, le motif de vague et la vitesse de **Gyre A** et **Gyre B**, et quand cela a été lu pour la dernière fois. Depuis elle, vous pouvez :

- Allumer ou éteindre la pompe de brassage avec le commutateur à côté de son état. Cora vous demande de confirmer d’abord. Éteindre arrête les deux gyres et laisse le programme tel qu’il est.
- Toucher **Modifier les réglages** pour régler le motif de vague et la vitesse de pompe de chaque gyre (et la durée, pour un motif qui en a une), et si les deux gyres sont liés. Cora liste ce qui va changer et vous demande de confirmer avant de l’appliquer. L’alternance se règle dans l’application Maxspect : une pompe de brassage qui l’exécute garde ses rampes et temps de maintien.
- Toucher **Programme défini** à la place quand le programme enregistré sur la pompe de brassage ne peut pas être lu. Cela règle les deux gyres pour que la pompe de brassage puisse redémarrer.
- Voir le programme journalier de la pompe de brassage sur la carte **Programme**. Il est en lecture seule : réglez le programme dans l’application Maxspect.
- Vérifier l’**État de la pompe** : quand la pompe aura besoin d’être nettoyée la prochaine fois (la pompe compte cela elle-même), le courant tiré par la tête A, quelles têtes sont installées, et le micrologiciel. Touchez **Lire** pour l’obtenir.

:::note Comment Cora Mobile atteint une pompe de brassage
Quand un Cora Max dessert l’aquarium, Cora Mobile fonctionne via ce Cora Max, y compris quand vous êtes loin de chez vous, et **Modifier les réglages** part de la dernière lecture de ce Cora Max. Sinon, votre téléphone parle directement à la pompe de brassage et doit être sur son réseau. Ouvrir la page la lit alors ; si la page affiche à la place une lecture stockée plus ancienne, **Modifier les réglages** reste caché jusqu’à ce que vous touchiez actualiser.
:::

## Ce qui se passe après avoir changé quelque chose

Chaque changement est enregistré dans [Activité](/help/mobile-activity) avec l’interface qui l’a demandé. Si un appareil n’accepte pas un changement, l’échec y est aussi enregistré.
