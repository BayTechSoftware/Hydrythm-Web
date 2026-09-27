---
title: Examiner un paramètre
description: Touchez n’importe quel widget pour l’historique complet, chaque source qui le rapporte, et où changer sa plage.
section: Cora Mobile
reviewed: 2026-09-09
order: 8
group: Your dashboard
---

Un widget vous montre un chiffre. Le toucher vous montre l’histoire derrière le chiffre.

## Ce que vous obtenez

![Examiner un paramètre](img/mobile-metric-detail.webp "Plages en haut, puis les sources qui rapportent ce paramètre, puis le graphique avec votre bande d’alerte ombrée.")

**Un graphique d’historique**, avec son propre sélecteur de plage : **1h · 6h · 12h · 24h · 3j · 7j** et plus long.

**Un filtre de source.** Sous les plages se trouve une ligne de puces : **Tous**, plus une par source rapportant ce paramètre, comme *Apex*, *Cora*, *Red Sea* ou *Manuel*. Sélectionnez-en une pour ne voir que ses mesures. C’est ainsi que vous comparez directement une sonde à un test en kit : basculez entre elles sur le même graphique.

**Un lien vers le calculateur de dose**, pour les paramètres que vous dosez. Il utilise le volume de l’aquarium tiré de votre [profil d’aquarium](/help/mobile-tank-profile) et les concentrations de [Dosage](/help/mobile-dosing).

**Une superposition de comparaison.** *Comparer avec* trace un second paramètre sur le même graphique (alcalinité contre calcium, pH contre température), pour qu’une relation que vous suspectez devienne visible plutôt que mémorisée.

**Des statistiques récapitulatives** pour la fenêtre affichée : **MIN**, **MOY** et **MAX**, montrées comme une ligne sous la valeur actuelle.

**Des marqueurs de dosage** sur le graphique, pour qu’un mouvement puisse être aligné avec ce que vous avez réellement dosé.

**La liste des mesures brutes** : chaque mesure individuelle derrière la ligne, avec sa source et son horodatage.

**Votre bande d’alerte**, ombrée sur le graphique, pour qu’une mesure soit lue par rapport à sa plage plutôt qu’isolément. Pour changer la plage elle-même, appuyez longuement sur le widget sur le tableau de bord. Voir [Alertes et seuils](/help/mobile-alerts).

**Enregistrer une mesure** à la main.

## Choisir une plage

La bonne plage dépend du rythme du paramètre :

| Paramètre | Fenêtre utile |
|---|---|
| pH | 24 heures ; il varie sur un cycle quotidien |
| Température | 24 heures ou 7 jours |
| Alcalinité | 7 ou 30 jours |
| Oligo-éléments | 30 jours ou un an |

:::note Vérifiez l’ancienneté de la mesure sur une tendance plate
Une ligne qui n’a pas bougé peut indiquer un paramètre stable ou une source qui a arrêté de rapporter. L’ancienneté affichée à côté de la valeur distingue les deux.
:::

## Comparer les sources

Quand plus d’une source rapporte un paramètre, Cora les garde séparées plutôt que de les moyenner. Utilisez les puces de source pour voir chacune à tour de rôle.

Un décalage persistant entre une sonde et un test enregistré à la main indique généralement que la sonde a besoin d’un étalonnage.

Un [résultat ICP](/help/mobile-icp-health) est un troisième avis utile, mais pas un arbitre. Les laboratoires diffèrent les uns des autres, et la manipulation, le stockage et le transport de l’échantillon influencent tous le résultat. Traitez un seul ICP comme une preuve, pas comme la valeur vraie ; deux tests d’accord valent bien plus qu’un seul.

## Choisir quelle source un widget suit

Si vous voulez qu’un widget suive une source particulière, réglez-le dans les réglages du widget. Voir **[Modifier votre tableau de bord](/help/mobile-dashboard-editing)**.

## Exclure une mauvaise mesure

Une sonde qui a eu un pic, un test mal lu, un échantillon pris en plein changement d’eau : une seule mesure erronée déforme le graphique, les moyennes et tout ce qui raisonne à partir d’elles.

![La liste des mesures brutes](img/mobile-readings.webp "Chaque mesure derrière la ligne, avec sa source et son heure.")

Ouvrez la liste des mesures depuis l’icône dans la barre supérieure, puis touchez une mesure pour l’exclure. L’écran le dit clairement : *exclue des moyennes et des observations, mais elle reste dans votre journal.* Rien n’est supprimé, et elle peut être restaurée.

:::warning Excluez une mesure erronée, pas une mesure indésirable
Exclure est pour les mesures que vous savez invalides. Une mesure que vous n’aimez pas mais ne pouvez pas mettre en défaut est une donnée, et la retirer rend chaque comparaison ultérieure moins honnête.
:::

## Enregistrer l’entretien des sondes

Enregistrer un étalonnage ou un nettoyage depuis ici horodate la date pour cette source, pour qu’un désaccord ultérieur puisse être lu par rapport à quand la sonde a été vue pour la dernière fois. Voir [Sondes](/help/mobile-probes).

## Enregistrer une mesure à la main

Saisissez ce que dit votre test en kit. Les mesures enregistrées à la main sont de première classe : elles obtiennent leur propre source et horodatage, elles apparaissent sur le graphique, elles alimentent Reef Buddy, et c’est contre elles que Cora compare votre équipement.

:::note Cora vérifie les entrées qui semblent invraisemblables
Si une valeur est très loin de ce que l’aquarium a connu, on vous demande de la confirmer avant qu’elle ne soit enregistrée. Cela intercepte une décimale mal placée ou une mesure saisie contre le mauvais paramètre. Confirmez-la et la mesure est stockée normalement.
:::
