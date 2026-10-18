---
title: Entretien
description: Ajoutez des tâches régulières comme le nettoyage de l’écumeur ou le changement des chaussettes filtrantes, recevez un rappel à l’échéance, et marquez-les comme faites ou reportez-les.
section: Cora Mobile
reviewed: 2026-10-17
order: 28
group: Records
twin: max-records
---

Entretien garde les tâches régulières dont votre aquarium a besoin, avec un rappel pour chacune.

Touchez **Entretien** dans la rangée de boutons sous le tableau de bord. Vous le trouvez aussi dans Réglages → votre aquarium → **Entretien**.

![La liste d’entretien](img/mobile-maintenance.webp "Le taux de conformité, le nombre de tâches en retard, et chaque tâche avec sa dernière réalisation et sa prochaine échéance.")

## Le résumé {#summary}

En haut, vous voyez la **Conformité de l’entretien**, la part des tâches à jour en ce moment, et le nombre de tâches en retard.

Chaque tâche de la liste a une couleur selon qu’elle est en retard, bientôt due ou programmée. Elle indique aussi quand vous l’avez faite pour la dernière fois et quand elle est due la prochaine fois.

## Ajouter une tâche {#adding-a-task}

Touchez **Ajouter une tâche**, puis choisissez :

- **Depuis un modèle** pour une tâche courante dont l’intervalle est déjà rempli. Choisissez-la, réglez sa prochaine échéance et l’heure du rappel, puis touchez **Confirmer**.
- **Tâche personnalisée** pour la vôtre. Donnez-lui un **Nom de la tâche**, un **Intervalle (jours)**, une **Catégorie** et une **Prochaine échéance**. Activez **Rappel** et choisissez **Me le rappeler à** si vous voulez une notification.

Quelques modèles, avec l’intervalle de départ :

| Tâche | Intervalle |
|---|---|
| Changer les chaussettes filtrantes | 3 jours |
| Nettoyer le godet de l’écumeur | 7 jours |
| Changement d’eau | 7 jours |
| Tester les paramètres de l’eau | 7 jours |
| Remplacer le charbon | 30 jours |
| Étalonner la sonde pH | 30 jours |
| Nettoyer les pompes de brassage | 90 jours |
| Téléverser les résultats ICP | 90 jours |

Vous pouvez changer l’intervalle de n’importe quelle tâche plus tard.

### Tâches que Cora ajoute pour l’équipement Red Sea {#red-sea-tasks}

Quand vous connectez un Red Sea ReefDose, ReefATO+, ReefMat ou ReefRun, Cora ajoute l’entretien dont cet appareil a besoin, déjà au bon intervalle :

| Appareil | Tâche | Intervalle |
|---|---|---|
| ReefATO+ | Remplacer le capteur EC du ReefATO+ | 42 jours |
| ReefATO+ | Remplacer la pompe de remontée du ReefATO+ | 135 jours |
| ReefMat | Remplacer le charbon du ReefMat | 25 jours |
| ReefRun | Vérifier le venturi de l’écumeur ReefRun | 35 jours |
| ReefRun | Remplacer le rotor de l’écumeur ReefRun | 135 jours |
| ReefRun | Étalonner le capteur de godet plein du ReefRun | 28 jours |
| ReefRun | Étalonner le capteur de sur-écumage du ReefRun | 28 jours |
| ReefRun, par pompe | Entretenir le moteur de pompe ReefRun | 135 jours |
| ReefRun, par pompe | Nettoyer la crépine de pompe ReefRun | 42 jours |
| ReefDose, par tête | Étalonner la tête ReefDose | 90 jours |
| ReefDose, par tête | Remplacer le tuyau de la tête ReefDose | 450 jours |

Elles fonctionnent comme les tâches que vous ajoutez vous-même. Vous pouvez les renommer, changer l’intervalle, les reporter ou les supprimer. Si vous en supprimez une, Cora ne la rajoute pas pour cet appareil.

### Tester l’eau {#test-water}

Si vous touchez **Me rappeler de tester chaque semaine** sur la carte du premier test, Cora ajoute une tâche hebdomadaire appelée **Tester l’eau**, due le **Jour du test** que vous choisissez. Elle fonctionne comme n’importe quelle autre tâche. Voir [Configurer Cora Mobile](/help/mobile-setup). Vous pouvez aussi ajouter à tout moment un rappel de test avec le modèle **Tester les paramètres de l’eau**.

### Depuis une automatisation {#from-an-automation}

Une [automatisation](/help/mobile-automation) avec l’action **Créer une tâche d’entretien** peut ajouter une tâche à cette liste quand sa règle se déclenche, ou rendre une tâche existante due maintenant. Une nouvelle tâche est une **Tâche ponctuelle**, due maintenant, et elle affiche *Créée par une automatisation* avec la raison. Elle quitte la liste quand vous la terminez. Tant qu’elle est ouverte, la même automatisation n’en ajoute pas d’autre. Vous recevez une seule notification.

## Rappels {#reminders}

Ouvrez une tâche et activez **Rappel**, puis choisissez **Me le rappeler à**. Vous recevez une notification la veille de l’échéance et une le jour même. Tant qu’elle est en retard, vous recevez un rappel tous les quelques jours. Si plusieurs tâches d’un aquarium arrivent à échéance ensemble, elles arrivent en une seule notification.

Les rappels relèvent de **Rappels d’entretien** dans [Réglages → Notifications](/help/mobile-notifications). Si vous préférez simplement voir une tâche dans la liste, désactivez son **Rappel**.

## Marquer une tâche comme faite {#marking-done}

Balayez la tâche vers la droite, ou ouvrez-la et touchez **Terminer**. Si vous avez balayé par erreur, touchez **Annuler** dans le message qui apparaît.

Cora enregistre l’heure à laquelle vous avez fini et calcule la prochaine échéance à partir de là. Si vous faites une tâche avec trois jours de retard, la suivante est donc décalée de trois jours aussi. Si la tâche est en retard, Cora demande d’abord **Quand l’avez-vous fait ?** Choisissez **À l’instant**, ou **Choisir la date et l’heure** si vous l’avez fait plus tôt (voir plus bas).

La fiche de la tâche affiche son **Historique des validations**, avec le retard de chacune.

:::note Terminer une tâche écrit aussi une entrée de journal
Cora ajoute pour vous une courte entrée à votre [journal](/help/mobile-journal), en précisant si la tâche était en retard. Ajoutez votre propre entrée quand il y a plus à dire, par exemple quand la pompe était pleine de sable ou que les chaussettes étaient noires au bout d’un jour.
:::

## Marquer une tâche comme faite plus tôt {#done-earlier}

Vous avez fait le travail hier et oublié de le cocher ? Ouvrez la tâche, touchez **Fait plus tôt…**, puis choisissez la date et l’heure. Cora date la validation, l’entrée de journal et la prochaine échéance à partir de cette heure : la prochaine échéance est donc l’heure choisie plus l’intervalle.

Vous pouvez remonter jusqu’à un an, mais pas avant la dernière validation de la tâche. Si vous choisissez une heure qui n’est pas encore passée, ou antérieure à la dernière validation, Cora le dit et n’enregistre rien.

## Modifier une tâche {#editing}

Touchez une tâche pour l’ouvrir. Vous pouvez changer le **Nom de la tâche**, l’**Intervalle (jours)**, les **Notes (facultatif)**, la **Prochaine échéance** et le rappel, puis touchez **Enregistrer**. **Supprimer** la retire.

## Reporter {#snoozing}

Vous ne pouvez pas faire une tâche maintenant ? Ouvrez-la, touchez **Reporter** et choisissez **1 jour**, **3 jours**, **1 semaine**, **2 semaines** ou **1 mois**. Elle reste dans la liste comme **Reportée** avec sa nouvelle date, et vous n’êtes pas rappelé avant.

:::warning Ne marquez une tâche comme faite que si vous l’avez faite
La prochaine échéance est calculée à partir de l’heure à laquelle vous avez fait la tâche. Si vous marquez comme faite une tâche encore à faire, toutes les échéances suivantes se décalent. Si vous l’avez faite plus tôt, utilisez **Fait plus tôt…** et choisissez l’heure réelle. Si vous ne l’avez pas faite, reportez-la plutôt.
:::

Il n’est pas possible de mettre une tâche en pause. Pour une tâche qui ne s’applique pas cette saison, reportez-la de **1 mois**, ou supprimez-la et ajoutez-la à nouveau plus tard.
