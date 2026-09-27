---
title: Contrôler l’équipement depuis Cora Max
description: Les pages d’appareils sur Cora Max : sondes, prises, têtes de dosage, testeurs et pompes.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max accède au même équipement que votre téléphone, avec une page par appareil. Ouvrez-les depuis **Réglages → Appareils**, ou touchez une tuile d’appareil sur le tableau de bord.

![Une page Apex sur Cora Max](img/max-device-control.webp "Cycles de nourrissage et chaque prise, disposés pour un écran mural.")

:::warning Ces commandes agissent sur l’équipement en direct
Il n’y a ni aperçu ni annulation. La commande part dès que vous touchez. Mais *envoyée* ne veut pas dire *faite*. Le résultat affiché peut être **Confirmé**, **Non confirmé**, **Refusé** ou **Aucun changement**, et vous le voyez dans [Activité](/help/max-activity).
:::

## Les appareils qui ont une page

| Appareil | Contenu |
|---|---|
| **Neptune Apex** | Sondes et prises. Chaque prise peut être allumée ou éteinte |
| **Trident** | État du test, niveaux de réactif et de déchets, et lancement d’un test |
| **DŌS**, y compris le DŌS QD | Pour chaque tête : dosage, programme, autonomie et volume du contenant (avec pause, remplissage, dosage immédiat et mesure unique de vingt secondes) |
| **Red Sea ReefBeat** | Selon l’appareil : têtes de dosage, réservoir, jours de rouleau restants, mode de pompe |
| **Jecod** | Mode et intensité de la pompe, et son programme de la journée |
| **Maxspect** *(bêta)* | Mode et vitesse pour **Gyre A** et **Gyre B**, **État de la pompe** (compte à rebours du nettoyage, courant de la tête A, têtes installées, micrologiciel), et son programme en lecture seule |

Si un appareil Red Sea s’arrête de lui-même, sa page dit ce qui ne va pas et affiche la solution juste à côté : **Reprendre**, **Effacer l’urgence**, **Capteur nettoyé**, **J’ai déjà chargé un nouveau rouleau**, ou **Réinitialiser** pour une tête de dosage.

## Têtes DŌS

Avant que Cora puisse doser à la main avec une tête DŌS, il faut la mesurer une fois. **Mesurer pour doser** fait tourner la tête vingt secondes dans un récipient gradué, puis vous saisissez la quantité obtenue. Cora garde une mesure par tête et utilise la plus récente, quel que soit le Cora Max qui l’a faite. La page de la tête indique où et quand elle a été mesurée.

Après un dosage manuel, une tête que vous aviez mise sur Éteint dans Apex Fusion reste sur Éteint. Les autres têtes reviennent sur Auto.

### L’usage d’une tête

Dans la fiche de réglages de chaque tête, vous pouvez choisir un **type d’usage** : **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture** ou **Appoint**, ou **Autre**. Le type d’usage change deux choses :

- **La taille du contenant suivi.** Une tête Complément suit un contenant de 20 litres au plus. Avec les autres types d’usage, le contenant peut aller jusqu’à 500 litres. Une tête qui gère un changement d’eau ou un réacteur à calcium n’est donc pas traitée comme un petit flacon de dosage.
- **La possibilité de faire un gros dosage à la main.** Les têtes Complément et Nourriture gardent la petite limite prudente habituelle. Pour les autres types d’usage, vous pouvez fixer un **Dosage manuel maximal**, avec un plafond absolu de 10 litres, et une **limite quotidienne pour les automatisations et l’Assistant**.

Les deux têtes d’un changement d’eau (entrée d’eau salée neuve et sortie d’eau ancienne) peuvent être reliées comme **Tête associée**, avec un seuil d’**Alerte d’équilibre au-dessus de**. Si les totaux du jour des deux têtes s’écartent de plus que ce seuil, Cora vous prévient. Un tel écart veut souvent dire qu’un des deux côtés ne pompe pas comme prévu.

### Si un gros dosage est interrompu

Pendant un gros dosage, Cora modifie temporairement le fonctionnement de la tête sur l’Apex, puis remet son programme normal. Si la connexion coupe en cours de route, Cora Max affiche une bannière sur la page de la tête : *« Un gros dosage sur [tête] ne s’est pas terminé proprement. Cora continue d’essayer de remettre son programme en place ; vérifiez-le dans Apex Fusion. »*

Vérifiez vous-même la tête dans Apex Fusion, puis touchez **J’ai vérifié la tête dans Fusion** pour faire disparaître la bannière. Ne le faites qu’après avoir constaté que c’est bien le programme habituel de la tête qui tourne, et non le programme de dosage de Cora.

Si la bannière ne disparaît pas ou revient sans cesse, consultez la page [Résolution de problèmes](/help/troubleshooting).

## Programmes

Vous pouvez créer les programmes journaliers des pompes Jecod sur Cora Max comme sur le téléphone. L’éditeur est le même : un graphique de la journée, une liste de plages horaires et une ligne d’action. Plus de détails dans [Programmer l’équipement](/help/mobile-schedules).

Le programme d’une pompe de brassage Maxspect *(bêta)* se consulte ici mais ne s’enregistre pas. Réglez-le dans l’application Maxspect.

## Prises

Vous trouvez aussi les prises dans le tiroir **Prises et nourrissage**, en bas du tableau de bord. Il regroupe les prises activées pour ce tableau de bord (ou toutes, si vous n’en avez choisi aucune). Plus de détails dans [Prises et commandes](/help/max-controls).

Les têtes DŌS n’apparaissent jamais dans la liste des prises. On ne peut donc pas en allumer une par là et l’oublier en marche. Pour doser, passez par la page de la tête. Un grand Apex avec plusieurs modules affiche toutes ses prises et sondes.

## Consommables

Les seuils de réapprovisionnement (réactif, contenants, réservoirs) se règlent sur la page de l’appareil, comme sur le téléphone. Plus de détails dans [Consommables](/help/mobile-consumables).

## Saisir et calculer à l’aquarium

Deux choses sont souvent plus pratiques sur Cora Max que sur le téléphone :

- **Enregistrer les paramètres** : saisissez vos résultats de test avec le clavier à l’écran, depuis le menu de l’aquarium
- **Calculateur de dose** : calculez une correction à partir du volume de l’aquarium et de la concentration de vos produits, depuis la page d’un paramètre. Il utilise le même volume et les mêmes concentrations que le téléphone, et trouve donc le même résultat. Plus de détails dans [Dosage](/help/mobile-dosing).

## Sur un deuxième Cora Max

Quand plusieurs Cora Max affichent le même aquarium, un seul lit son équipement. Les pages d’appareils l’appellent le Cora Max de l’aquarium. Les autres ouvrent quand même les pages d’appareils (une étiquette d’état **Cloud** vous indique que cet écran en fait partie). Ils affichent ce que le Cora Max de l’aquarium a lu en dernier, et il y a combien de temps. Chaque commande passe par Cora Cloud jusqu’au Cora Max de l’aquarium, qui l’exécute.

Certaines choses restent réservées au Cora Max de l’aquarium :

- **Mesurer pour doser** et **Remesurer** n’apparaissent que sur lui. Une fois la tête mesurée, **Doser maintenant** marche depuis n’importe quel Cora Max.
- Un autre Cora Max ne peut changer un programme Jecod que si le Cora Max de l’aquarium a lu la pompe dans l’heure. Jamais pour une pompe qui ne communique qu’en Bluetooth. Depuis un autre écran, **Appliquer à la pompe** envoie 12 changements au maximum. Envoyez une grosse modification en plusieurs fois.

## Ce qui a été changé, et par quoi

Chaque action est enregistrée avec son origine. Plus de détails dans [Activité et chronologie](/help/mobile-activity).
