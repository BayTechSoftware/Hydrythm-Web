---
title: Examiner un paramètre
description: Touchez un widget pour voir tout l’historique d’un paramètre, comparer des sources et des paramètres, exclure une mesure erronée et noter l’entretien d’une sonde.
section: Cora Mobile
reviewed: 2026-10-13
order: 7
group: Your dashboard
---

Un widget vous montre un chiffre. Touchez-le pour voir l’histoire derrière ce chiffre.

Il y a deux façons d’y accéder. Touchez un widget sur le tableau de bord, ou touchez **Historique des paramètres** dans la rangée de boutons sous les widgets et choisissez un paramètre. **Historique des paramètres** liste tous les paramètres qui ont des données, même ceux qui n’ont pas de widget sur le tableau de bord.

## Ce que vous obtenez {#what-you-get}

![Examiner un paramètre](img/mobile-metric-detail.webp "Les listes déroulantes en haut, puis le graphique avec votre plage d’alerte en couleur.")

- Un graphique d’historique. La rangée au-dessus définit ce qu’il affiche. **Paramètre** passe à n’importe quel autre paramètre qui a des données, en gardant votre période. **Période** va de 1 h à Tout, en passant par 6 h, 12 h, 24 h, 3 j, 7 j, 15 j, 30 j, 90 j, 180 j et 360 j. **Source** démarre sur **Toutes les sources** et liste les sources qui signalent ce paramètre sur cet aquarium, comme *Apex*, *Cora*, *Red Sea* ou *Manuel*. Choisissez-en une pour ne voir que ses mesures.
- **Comparer**, au bout de la même rangée, trace un deuxième paramètre sur le graphique, comme l’alcalinité avec le calcium ou le pH avec la température. Le bouton affiche alors **vs** suivi du nom de l’autre paramètre. Touchez-le à nouveau pour retirer la deuxième courbe.
- Une rangée avec **Dernière**, **Min**, **Moy** et **Max** pour la période affichée.
- Des icônes dans la barre du haut : **Mesures** ouvre la liste brute des mesures, et **Enregistrer l’entretien de la sonde** note un étalonnage ou un nettoyage. Pour l’alcalinité, le calcium et le magnésium, il y a aussi le calculateur de dose, qui utilise le volume de l’aquarium de votre [profil d’aquarium](/help/mobile-tank-profile) et les concentrations de [Dosage](/help/mobile-dosing).

L’écran s’ouvre toujours sur 24 h et **Toutes les sources**. Il ne retient pas ce que vous avez choisi la dernière fois.

## Lire le graphique {#reading-the-chart}

- La bande verte est votre plage d’alerte : vous voyez chaque mesure par rapport à elle. Pour changer la plage, faites un appui long sur le widget dans le tableau de bord. Plus de détails dans [Alertes et seuils](/help/mobile-alerts).
- Une ligne pointillée marque une dose notée, pour que vous puissiez rapprocher un changement de ce que vous avez dosé.
- **Max. 30 j** et **Min. 30 j** sont des lignes pointillées qui montrent les extrêmes des 30 derniers jours.
- Un point creux est une mesure que vous avez exclue.
- Avec **Comparer** activé, le deuxième paramètre utilise l’axe de droite.

## Choisir une période {#choosing-a-range}

Choisissez la période qui correspond à la façon dont le paramètre évolue.

| Paramètre | Période utile |
|---|---|
| pH | 24 heures, car il oscille sur un cycle quotidien |
| Température | 24 heures ou 7 jours |
| Alcalinité | 7 ou 30 jours |
| Oligo-éléments | 30 jours ou un an |

:::note Ligne plate ? Vérifiez l’âge de la mesure
Une ligne qui ne bouge pas peut vouloir dire que le paramètre est stable. Elle peut aussi vouloir dire que la source a cessé de transmettre. L’âge affiché à côté de la valeur sur le widget vous dit lequel des deux.
:::

## Comparer les sources {#comparing-sources}

Quand plusieurs sources signalent un paramètre, Cora les garde séparées et n’en fait pas la moyenne. Utilisez la liste **Source** pour regarder chacune. C’est le moyen le plus rapide de comparer une sonde avec un kit de test.

Celle qui s’affiche sur le tableau de bord est la plus récente. Une valeur en direct n’est remplacée que par une mesure dont l’heure de mesure est plus tardive, quelle que soit la source. Une mesure plus ancienne va dans l’historique et n’écrase pas ce qu’affiche le widget. Si vous avez épinglé une source dans l’**Association des paramètres**, Cora suit cette source à la place.

Si une sonde et vos tests notés à la main restent écartés du même écart, la sonde a en général besoin d’être étalonnée.

Un [résultat ICP](/help/mobile-icp-health) est un troisième avis utile, mais il ne tranche pas la question. Les laboratoires diffèrent entre eux, et la façon dont l’échantillon a été manipulé, conservé et expédié change le résultat. Considérez un ICP comme un indice. Deux tests concordants valent bien plus qu’un seul.

## Choisir la source que suit une mesure {#choosing-which-source-a-widget-trusts}

La source se règle par aquarium et par paramètre, pas par widget. Allez dans **Réglages**, touchez l’aquarium, touchez **Association des paramètres**, puis l’onglet **Sources**. Choisissez une sonde, ou **Automatique (la mesure la plus récente l’emporte)**. Le choix s’applique à ce paramètre partout pour l’aquarium. Plus de détails dans [Association des paramètres](/help/mobile-probes).

## Exclure une mesure erronée {#excluding-a-bad-reading}

Une sonde a peut-être fait un pic, vous avez mal lu un test, ou vous avez prélevé l’échantillon en plein changement d’eau. Une seule mesure fausse fausse le graphique, les moyennes et tout ce qui en est calculé.

![La liste des mesures de pH dans Cora Mobile](img/mobile-readings.webp "Chaque mesure derrière la courbe, avec son heure et sa source. Touchez-en une pour l’exclure.")

Touchez **Mesures** dans la barre du haut, puis touchez une mesure. Cora demande **Exclure cette mesure ?** et explique qu’elle reste dans votre historique mais ne compte plus dans les moyennes, les tendances, les analyses et l’assistant. Touchez **Exclure**. Rien n’est supprimé, et vous pouvez la rétablir de la même façon.

Les mesures de plus de 90 jours ne peuvent être ni exclues ni rétablies.

:::warning Excluez les mesures fausses, pas celles qui dérangent
N’excluez qu’une mesure que vous savez invalide. Si une mesure vous déplaît simplement mais que vous n’y trouvez rien d’anormal, ce sont de vraies données. La retirer rend chaque comparaison ultérieure moins honnête.
:::

## Noter l’entretien des sondes {#recording-probe-care}

Touchez **Enregistrer l’entretien de la sonde** (l’icône de capteur dans la barre du haut) et choisissez ce que vous avez fait : étalonner, nettoyer, remplacer, déplacer ou comparer. Cora date cette source, pour qu’un étalonnage récent ne soit pas pris pour une dérive. Plus tard, si la sonde n’est pas d’accord avec autre chose, vous voyez quand elle a été entretenue pour la dernière fois. Plus de détails dans [Association des paramètres](/help/mobile-probes).

## Noter une mesure à la main {#logging-a-reading-by-hand}

Vous notez les mesures depuis le tableau de bord, pas depuis cet écran. Touchez **Enregistrer les paramètres** sous les widgets et saisissez ce qu’indique votre kit de test. La liste est groupée, et le groupe **Oligo-éléments** couvre l’iode, le fer et le cuivre en µg/L, et le potassium en mg/L. Les mesures notées à la main comptent autant que les autres. Elles ont leur propre source et leur propre heure, s’affichent sur le graphique et alimentent Reef Buddy. C’est aussi à elles que Cora compare votre équipement.

:::note Cora revérifie les saisies qui semblent bizarres
Si une valeur est loin de là où se trouvait l’aquarium, Cora vous demande de la confirmer avant de l’enregistrer. Cela attrape une virgule mal placée, ou une mesure saisie sous le mauvais paramètre. Une fois confirmée, la mesure est enregistrée comme d’habitude.
:::
