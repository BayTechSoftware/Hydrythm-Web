---
title: Examiner un paramètre
description: Touchez un widget pour voir tout l’historique, chaque source qui mesure ce paramètre et l’endroit où changer sa plage.
section: Cora Mobile
reviewed: 2026-10-12
order: 8
group: Your dashboard
---

Un widget vous donne un chiffre. Touchez-le, et vous voyez l’histoire qui se cache derrière.

Il y a deux façons d’y accéder. Touchez un widget du tableau de bord, ou touchez **Historique des paramètres** dans la rangée de boutons sous les widgets et choisissez un paramètre. **Historique des paramètres** liste tous les paramètres qui ont des données, même sans widget sur le tableau de bord.

## Ce que vous trouvez

![Examiner un paramètre](img/mobile-metric-detail.webp "Les listes déroulantes en haut, puis le graphique avec votre bande d’alerte ombrée.")

**Un graphique de l’historique.** Trois listes déroulantes au-dessus règlent ce qu’il affiche. **Paramètre** passe à n’importe quel autre paramètre qui a des données, en gardant votre période. **Période** va de 1h à 6h, 12h, 24h, 3d, 7d, 15d, 30d, 90d, 180d et 360d jusqu’à Tout. **Source** commence sur **Toutes les sources** et liste les sources qui rapportent ce paramètre sur cet aquarium, par exemple *Apex*, *Cora*, *Red Sea* ou *Manuel*. Choisissez-en une pour ne voir que ses mesures. C’est comme cela que vous comparez une sonde et un test en kit : passez de l’une à l’autre sur le même graphique.

L’écran s’ouvre toujours sur 24h et **Toutes les sources**. Il ne retient pas ce que vous avez choisi la fois précédente.

**Une ligne** avec **Dernière**, **Min**, **Moy** et **Max** pour la période affichée.

**Un lien vers le calculateur de dose**, pour les paramètres que vous dosez. Il se sert du volume indiqué dans le [profil de l’aquarium](/help/mobile-tank-profile) et des concentrations réglées dans [Dosage](/help/mobile-dosing).

**Comparer** trace un deuxième paramètre sur le même graphique (alcalinité et calcium, pH et température). La liste contient tous les paramètres de l’aquarium. Un lien que vous soupçonnez devient visible, sans avoir à vous en souvenir. Touchez de nouveau la pastille pour retirer la deuxième ligne.

**Des repères de dosage** sur le graphique, pour mettre un mouvement en regard de ce que vous avez vraiment dosé.

**La liste des mesures brutes** : toutes les mesures derrière la courbe, avec leur source, leur date et leur heure.

**Votre bande d’alerte**, en grisé sur le graphique. Vous lisez ainsi chaque mesure par rapport à sa plage. Pour changer la plage elle-même, appuyez longuement sur le widget dans le tableau de bord. Voir [Alertes et seuils](/help/mobile-alerts).

**La saisie d’une mesure** à la main.

## Choisir une période

La bonne période dépend du rythme du paramètre.

| Paramètre | Période utile |
|---|---|
| pH | 24 heures. Il varie au fil de la journée |
| Température | 24 heures ou 7 jours |
| Alcalinité | 7 ou 30 jours |
| Oligo-éléments | 30 jours ou un an |

:::note Courbe plate ? Vérifiez l’âge de la mesure
Une courbe qui ne bouge pas peut vouloir dire un paramètre stable, ou une source qui n’envoie plus rien. L’âge affiché à côté de la valeur fait la différence.
:::

## Comparer les sources

Quand plusieurs sources mesurent un même paramètre, Cora les garde séparées et n’en fait pas la moyenne. Utilisez la liste déroulante **Source** pour les voir l’une après l’autre.

Le paramètre affiché sur le tableau de bord est le plus récent. Une valeur en direct n’est remplacée que par une mesure dont l’heure de mesure est plus tardive, quelle que soit la source. Une mesure plus ancienne va dans l’historique et n’écrase pas ce que le widget affiche. Si vous avez épinglé une source pour le widget, Cora suit cette source à la place.

Un écart constant entre une sonde et un test saisi à la main veut souvent dire que la sonde doit être étalonnée.

Un [résultat ICP](/help/mobile-icp-health) est un troisième avis utile, mais pas un arbitre. Les laboratoires ne donnent pas tous les mêmes résultats, et la manipulation, la conservation et le transport de l’échantillon jouent sur la mesure. Voyez un ICP comme un indice, pas comme la vraie valeur. Deux tests qui concordent valent bien plus qu’un seul.

## Choisir la source suivie par un widget

Pour qu’un widget suive une source précise, réglez-la dans les réglages du widget. Voir **[Modifier votre tableau de bord](/help/mobile-dashboard-editing)**.

## Écarter une mauvaise mesure

Un pic de sonde, un test mal lu, un échantillon pris pendant un changement d’eau… Une seule mesure fausse suffit à déformer le graphique, les moyennes et tout ce qui en découle.

![La liste des mesures brutes](img/mobile-readings.webp "Chaque mesure derrière la ligne, avec sa source et son heure.")

Ouvrez la liste des mesures avec l’icône de la barre du haut, puis touchez une mesure pour l’exclure. L’écran le dit clairement : *exclue des moyennes et des observations, mais elle reste dans votre journal.* Rien n’est supprimé, et vous pouvez la rétablir.

:::warning Écartez une mesure fausse, pas une mesure qui vous déplaît
L’exclusion sert aux mesures dont vous savez qu’elles sont fausses. Une mesure qui vous déplaît mais que vous ne pouvez pas mettre en cause reste une donnée. La retirer fausse toutes les comparaisons suivantes.
:::

## Noter l’entretien d’une sonde

Si vous notez ici un étalonnage ou un nettoyage, la date est enregistrée pour cette source. Plus tard, en cas de désaccord, vous saurez quand la sonde a été entretenue pour la dernière fois. Voir [Sondes](/help/mobile-probes).

## Saisir une mesure à la main

Saisissez le résultat de votre test en kit. La liste est regroupée, et le groupe **Oligo-éléments** couvre l’iode, le fer et le cuivre en µg/L, et le potassium en mg/L. Les mesures saisies à la main comptent autant que les autres. Elles ont leur propre source, leur date et leur heure, elles apparaissent sur le graphique et alimentent Reef Buddy. C’est aussi à elles que Cora compare votre équipement.

:::note Cora vérifie les valeurs étonnantes
Si une valeur est très éloignée de ce que l’aquarium affiche d’habitude, Cora vous demande de la confirmer avant de l’enregistrer. Cela évite une virgule mal placée ou une mesure saisie sur le mauvais paramètre. Une fois confirmée, la mesure est enregistrée normalement.
:::
