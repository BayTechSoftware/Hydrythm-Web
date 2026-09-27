---
title: Contrôler l’équipement depuis Cora Max
description: Les pages d’appareils sur le grand écran : sondes, prises, têtes de dosage, testeurs et pompes.
section: Cora Max
reviewed: 2026-09-27
order: 6
group: Equipment
---

Cora Max accède au même équipement que votre téléphone, avec une page par appareil. Ouvrez-les depuis **Réglages → Appareils**, ou en touchant une tuile d’appareil sur le tableau de bord.

![Une page Apex sur Cora Max](img/max-device-control.webp "Cycles de nourrissage et chaque prise, disposés pour un écran mural.")

:::warning Ces commandes agissent sur un équipement en direct
Il n’y a pas d’aperçu et pas d’annulation. Une commande part au moment où vous touchez, mais *envoyé* n’est pas *fait* : elle revient **Confirmée**, **Non confirmée**, **Refusée** ou **Aucun changement**, et [Activité](/help/max-activity) est où vous voyez laquelle c’était.
:::

## Ce qui a une page

| Appareil | Affiche |
|---|---|
| **Neptune Apex** | Sondes et prises, chaque prise étant commutable |
| **Trident** | État du test, niveaux de réactif et de déchets, et la possibilité de démarrer un test |
| **DŌS**, y compris le DŌS QD | Le dosage, le programme, l’autonomie et le volume du contenant de chaque tête (avec pause, remplissage, doser maintenant et une mesure unique de vingt secondes) |
| **Red Sea ReefBeat** | Ce que l’unité est : têtes de dosage, réservoir, jours de rouleau, mode de pompe |
| **Jecod** | Mode et intensité de la pompe, et son programme journalier |
| **Maxspect** *(bêta)* | Mode et vitesse pour **Gyre A** et **Gyre B**, **État de la pompe** (compte à rebours de nettoyage, courant de la tête A, têtes installées, micrologiciel), et son programme, lecture seule |

Si une unité Red Sea s’arrête elle-même, sa page indique ce qui ne va pas et place la correction à côté : **Reprendre**, **Effacer l’urgence**, **Capteur nettoyé**, **J’ai déjà chargé un nouveau rouleau**, ou **Réinitialiser** pour une tête de dosage.

## Têtes DŌS

Une tête DŌS doit être mesurée une fois avant que Cora ne la dose à la main. **Mesurer pour doser** exécute la tête pendant vingt secondes dans un contenant de mesure, et vous saisissez combien en est sorti. Cora garde une mesure par tête et utilise la plus récente, quel que soit le Cora Max qui l’a prise ; la page de la tête montre où et quand elle a été mesurée.

Après un dosage manuel, une tête que vous aviez réglée sur Éteint dans Apex Fusion reste Éteinte. Toute autre tête revient sur Auto.

### À quoi une tête sert

Chaque tête peut être réglée sur un **type d’usage**, depuis sa fiche de réglages : **Complément**, **Changement d’eau : entrée d’eau salée neuve**, **Changement d’eau : sortie d’eau ancienne**, **Kalkwasser**, **Réacteur à calcium**, **Nourriture** ou **Appoint**, ou **Autre**. Le type d’usage change deux choses :

- **La taille de contenant qu’elle peut suivre.** Une tête Complément suit jusqu’à 20 litres ; tout autre type d’usage peut suivre un contenant bien plus grand, jusqu’à 500 litres, pour qu’une tête gérant un changement d’eau ou un réacteur à calcium ne soit pas traitée comme une petite bouteille de dosage.
- **Si elle peut recevoir un gros dosage à la main.** Les têtes Complément et Nourriture gardent le plafond petit et prudent d’aujourd’hui. Tout autre type d’usage peut recevoir sa propre limite de **Dosage manuel maximal**, jusqu’à un plafond absolu de 10 litres, et sa propre **limite quotidienne pour les automatisations et l’Assistant**.

Une paire de changement d’eau (entrée d’eau salée neuve, sortie d’eau ancienne) peut être liée comme **Tête associée**, avec un montant d’**Alerte d’équilibre au-dessus de** : si les totaux du jour des deux têtes s’écartent de plus que ce montant, Cora vous avertit, car une paire déséquilibrée signifie généralement qu’un côté ne pompe pas comme prévu.

### Si un gros dosage est interrompu

Un gros dosage change temporairement ce que fait la tête sur l’Apex, puis remet son programme normal en place ensuite. Si la connexion se rompt en cours de route, Cora Max affiche une bannière sur la page de cette tête : *« Un gros dosage sur [tête] ne s’est pas terminé proprement. Cora continue d’essayer de remettre son programme en place ; vérifiez-le dans Apex Fusion. »*

Vérifiez la tête vous-même dans Apex Fusion, puis touchez **J’ai vérifié la tête dans Fusion** pour effacer la bannière. Faites cela seulement après avoir confirmé que c’est le propre programme de la tête, pas le programme de dosage de Cora, qui s’exécute réellement.

**Si cela ne fonctionne pas :** si la bannière ne veut pas s’effacer, ou revient sans cesse, voir [Résolution de problèmes](/help/troubleshooting).

## Programmes

Les programmes journaliers des pompes Jecod peuvent être créés au mur comme sur le téléphone. L’éditeur est le même : un graphique journalier, une liste de périodes, et une ligne d’action. Voir [Programmer l’équipement](/help/mobile-schedules).

Le programme d’une pompe de brassage Maxspect *(bêta)* peut être consulté ici mais pas enregistré. Réglez-le dans l’application Maxspect.

## Prises

Les prises sont aussi accessibles depuis le tiroir **Prises et nourrissage** en bas du tableau de bord, qui liste les prises activées pour ce tableau de bord au même endroit (toutes, si aucune n’a été choisie). Voir [Prises et commandes](/help/max-controls).

Les têtes DŌS n’apparaissent jamais dans la liste des prises, pour qu’une tête ne puisse pas être allumée là et laissée en marche ; dosez depuis sa propre page. Un grand Apex avec plusieurs modules affiche toutes ses prises et sondes.

## Consommables

Les seuils de réapprovisionnement (réactif, contenants, réservoirs) se règlent depuis la propre page de l’appareil ici, exactement comme sur le téléphone. Voir [Consommables](/help/mobile-consumables).

## Enregistrer et calculer à l’aquarium

Deux choses sont souvent plus pratiques au mur que sur un téléphone :

- **Enregistrer les paramètres** : saisissez les résultats de test sur le clavier à l’écran, depuis le menu de l’aquarium
- **Calculateur de dose** : déterminez une correction en utilisant le volume de l’aquarium et les concentrations de vos produits, depuis la page d’un paramètre. Il utilise le même volume et les mêmes concentrations de produits que le téléphone, donc un dosage calculé ici correspond à un calculé là. Voir [Dosage](/help/mobile-dosing).

## Sur un second Cora Max

Quand plus d’un Cora Max affiche un aquarium, l’un d’eux lit l’équipement de cet aquarium ; les pages d’appareils l’appellent le Cora Max de l’aquarium. Les autres ouvrent tout de même les pages d’appareils (une pastille d’état indiquant **Cloud** signifie que cet écran en fait partie). Elles montrent ce que le Cora Max de l’aquarium a lu en dernier, et depuis combien de temps, et transmettent chaque commande via Cora Cloud à ce Cora Max pour qu’il l’exécute.

Quelques choses restent avec le Cora Max de l’aquarium :

- **Mesurer pour doser** et **Remesurer** apparaissent seulement là. Une fois qu’une tête est mesurée, **Doser maintenant** fonctionne depuis n’importe quel Cora Max.
- Un programme Jecod peut être changé depuis un autre Cora Max seulement si le Cora Max de l’aquarium a lu la pompe dans la dernière heure, et jamais pour une pompe qui ne communique que par Bluetooth. Un **Appliquer à la pompe** depuis là envoie au maximum 12 changements, donc envoyez une modification plus importante en plusieurs fois.

## Ce qui a été changé, et par quoi

Chaque action est enregistrée avec sa cause. Voir [Activité et chronologie](/help/mobile-activity).
