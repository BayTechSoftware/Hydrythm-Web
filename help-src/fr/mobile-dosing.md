---
title: Produits de dosage et calculateur de dose
description: Vérifiez la concentration de vos produits d’alcalinité, de calcium et de magnésium, ajoutez les vôtres et utilisez le calculateur de dose pour savoir combien ajouter.
section: Cora Mobile
reviewed: 2026-10-13
order: 27
group: Records
---

Cora ne peut faire les calculs de dosage que s’il connaît la concentration de vos produits. Cette page explique la liste des produits et le calculateur de dose qui s’en sert.

Allez dans **Réglages → Produits de dosage**.

![Produits de dosage](img/mobile-dosing.webp "Les produits portent la concentration que Cora utilise pour les calculs de dose et de consommation.")

## La bibliothèque de produits {#the-product-library}

L’écran **Produits de dosage** liste déjà des produits courants, regroupés sous **Alcalinité (dKH)**, **Calcium (ppm)** et **Magnésium (ppm)**. Trouvez le vôtre et touchez-le pour vérifier sa concentration.

Chaque concentration indique de combien 1 ml (ou 1 g d’un produit sec) fait monter le paramètre dans un volume d’eau donné. C’est ce chiffre qui transforme « 5 ml » en « +0,2 dKH dans votre aquarium ». Passez de **pour 100 L** à **pour 100 gal** en haut de l’écran.

Ne changez une concentration intégrée que si votre flacon indique autre chose. Touchez le produit pour ouvrir **Ajuster la concentration**. **Réinitialiser par défaut** remet le chiffre de Cora.

## Ajouter votre propre produit {#adding-your-own}

Si votre produit n’est pas dans la liste, touchez **+** (**Ajouter un produit personnalisé**). Donnez-lui un **Nom du produit**, choisissez **Liquide (ml)** ou **Sec (g)**, et remplissez sa concentration pour l’alcalinité, le calcium ou le magnésium. Laissez un champ vide si le produit ne fait pas bouger ce paramètre. Un produit en deux parties en remplit un pour chaque partie, un produit équilibré en remplit plusieurs.

La concentration figure presque toujours sur l’étiquette, par exemple « 1 ml pour 100 litres augmente l’alcalinité de 0,1 dKH ».

:::warning Utilisez la concentration donnée par le fabricant
Si la concentration est fausse, toutes les doses que Cora calcule pour ce produit sont fausses dans la même proportion. Si vous ne trouvez pas le chiffre, n’ajoutez pas le produit. Ne le devinez pas.
:::

Les produits de nitrates et de phosphates viennent de la liste de Cora dans le calculateur. Vous ne pouvez pas les ajouter ici.

Le **Mélange de sel** de votre aquarium n’est pas un produit de dosage. Vous le réglez dans le profil de l’aquarium, et Cora propose un catalogue de sels récifaux courants avec leurs chiffres publiés et leurs sources. Voir [Le profil de votre aquarium](/help/mobile-tank-profile).

## Le calculateur de dose {#the-dose-calculator}

Le calculateur calcule la quantité de produit nécessaire pour amener un paramètre à sa cible. Il est disponible pour l’alcalinité, le calcium, le magnésium, les nitrates et les phosphates.

1. Sur le tableau de bord, touchez le widget du paramètre pour l’ouvrir.
2. Touchez l’icône de calculatrice en haut. Un point dessus veut dire que la mesure est sous la cible.
3. Vérifiez les chiffres que Cora a remplis :
   - Actuel est votre dernière mesure. Mettez-la à jour si vous venez de tester.
   - Cible est le milieu de votre plage d’alerte pour ce paramètre, ou la plage récifale habituelle si vous n’en avez pas réglé.
   - **Volume d’eau net (L)** vaut 90 % du volume de votre aquarium, pour tenir compte des pierres et du sable. Changez-le si vous connaissez le vrai chiffre.
4. Choisissez le **Produit**. Vos propres produits du profil de l’aquarium viennent en premier, puis les préréglages des marques. Vous pouvez aussi saisir une **Concentration personnalisée**.

Cora affiche le total nécessaire pour atteindre la cible.

:::warning Étalez une grosse correction
Le calculateur donne le total, pas une dose journalière. Si le total représente un saut plus grand que ce qui est sûr en une journée, il le dit, et vous le répartissez sur plusieurs jours. **Demander à Cora** ouvre Cora Assistant avec vos chiffres, si vous voulez de l’aide pour planifier la quantité par jour.
:::

Une fois la dose donnée, touchez **Enregistrer la dose donnée**. Cela ajoute une entrée à votre [journal](/help/mobile-journal).

Si vous êtes déjà à la cible ou au-dessus, le calculateur vous dit qu’il n’y a rien à ajouter. On ne peut pas faire baisser un paramètre en dosant. La solution est un changement d’eau, un changement de média ou une modification de ce que vous dosez déjà.

Le volume compte ici. S’il est faux de 20 %, les doses sont fausses de 20 % aussi.

## Consommation {#consumption}

Quand Cora voit à la fois vos doses et vos mesures, il peut calculer ce que votre aquarium consomme et vous prévenir quand cela change.

Quand la consommation change, regardez de plus près avant de conclure. Une hausse de la consommation d’alcalinité vient souvent de la croissance, mais un mouvement brusque dans un sens ou dans l’autre peut aussi venir d’une dose manquée, d’une erreur de test, d’une précipitation, d’un changement d’eau ou d’une modification de l’équipement. Regardez ce qui a changé d’autre autour de cette date.

## Équipement de dosage {#dosing-equipment}

Si vous avez un doseur connecté, comme un Neptune DŌS ou un Red Sea ReefDose, ses têtes apparaissent avec leurs propres mesures, dont ce qui reste dans chaque tête et ce qu’elle a dosé. La façon de les faire fonctionner et de les remplir est dans [Contrôler votre équipement](/help/mobile-device-control), et leurs alertes de récipient bas et de dose manquée sont dans [Alertes des doseurs](/help/mobile-device-control#doser-alerts).

Une automatisation peut aussi doser depuis une tête DŌS, avec un plafond de 10 mL par tête et par jour. Voir [Automatisations et scènes](/help/mobile-automation#actions).
