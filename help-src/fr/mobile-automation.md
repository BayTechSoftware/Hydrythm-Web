---
title: Automatisations et scènes
description: Faites agir Cora tout seul selon une mesure, une alerte, une heure ou un appareil qui se déconnecte, et regroupez des actions en scènes que vous lancez d’un seul appui.
section: Cora Mobile
reviewed: 2026-10-13
order: 22
group: Alerts and automation
twin: max-automation
---

Une automatisation est une règle que Cora exécute pour vous : *quand ceci arrive, vérifie cela, puis fais ceci.* Une scène regroupe plusieurs actions en une seule chose que vous lancez quand vous le voulez.

Allez dans **Réglages → Automatisations**.

![L’écran Automatisation dans Cora Mobile, avec les onglets Automatisations et Scènes](img/mobile-automation.webp "Automatisations et Scènes sont des onglets distincts. Chaque règle a son propre interrupteur.")

L’écran a deux onglets, **Automatisations** et **Scènes**, avec un bouton **Nouvelle automatisation** ou **Nouvelle scène**. Chaque règle affiche un résumé d’une ligne, un interrupteur d’activation et un menu pour la **Modifier** ou la **Supprimer**. Une règle qui ne s’est pas encore exécutée l’indique.

:::warning Les règles agissent sur de vrais équipements
Si une règle commande une pompe, la pompe change d’état même quand vous ne regardez pas. Créez une règle à la fois et vérifiez qu’elle fait ce que vous attendez avant d’ajouter la suivante.
:::

## La structure d’une règle {#shape}

Chaque automatisation a trois parties.

- Le déclencheur la réveille.
- Les conditions doivent aussi être vraies.
- Les actions sont ce qu’elle fait ensuite, dans l’ordre.

![Un formulaire Nouvelle automatisation vide dans Cora Mobile](img/mobile-rule-builder.webp "Une nouvelle automatisation : déclencheurs, conditions Si, actions Alors, Sinon-si et Sinon, puis le délai et la plage horaire.")

## Ce qui peut réveiller une règle {#triggers}

Ajoutez un ou plusieurs déclencheurs sous **Quand : n’importe quel déclencheur**. N’importe lequel d’entre eux lance la règle.

| Déclencheur | Se déclenche quand |
|---|---|
| **Quand une valeur change** | Un paramètre franchit une valeur que vous avez réglée. Choisissez la **Direction** : **En hausse**, **En baisse** ou **Tout changement** |
| **Quand une alerte se déclenche** | Une alerte est **Déclenchée**, **Effacée**, ou l’un ou l’autre. Vous pouvez la limiter aux alertes de **Seuil** ou de **Taux de variation** |
| **À une heure de la journée** | Une heure de la journée, dans votre propre fuseau horaire |
| **Quand un appareil passe hors ligne** | Votre Cora Max passe **Hors ligne**, revient **En ligne**, ou l’un ou l’autre |

:::tip Soyez prévenu quand votre Cora Max décroche
Une règle avec **Quand un appareil passe hors ligne** et **Me notifier** vous prévient quand le Cora Max qui lit votre équipement perd l’alimentation ou le Wi-Fi.
:::

## Conditions {#conditions}

Les conditions décident si les actions s’exécutent. Touchez **Ajouter une condition** et choisissez :

- **Comparaison de valeur**, une mesure au-dessus, en dessous ou égale à une valeur
- **Valeur dans / hors d’une plage**
- **Alerte active**
- **Prise activée / désactivée**, pour une prise Apex
- **Heure de la journée**, une plage comme 22:00 à 06:00
- **Résultat d’une étape précédente**, qui vérifie si une étape précédente s’est terminée **OK** ou a été **Ignoré**. Utilisez-le pour « essaie ceci, et si ça n’a pas marché, fais plutôt cela »

Avec plusieurs conditions, réglez **Correspondance** sur **Toutes (ET)** ou **Au moins une (OU)**.

## Branches et vérifications par étape {#branches}

Une automatisation peut faire des choses différentes selon les cas. Son premier bloc est **Si**. Touchez **Sinon-si** pour ajouter un autre cas, ou ajoutez un bloc **Sinon** pour tout le reste. Cora exécute le premier bloc dont les conditions sont remplies.

Vous pouvez aussi conditionner une seule action. Touchez **Seulement si…** sur cette étape et donnez-lui sa propre condition. Sans condition, l’étape s’exécute toujours.

## Quand elle peut s’exécuter {#when-it-may-run}

- **Délai entre les exécutions** empêche une règle de se redéclencher trop vite. Il démarre à 10 min.
- **N’exécuter qu’entre** limite la règle à une plage horaire, par exemple uniquement en journée.
- **Tester avec les valeurs en direct** vérifie la règle par rapport aux mesures actuelles de votre aquarium, sans rien faire. Il vous dit ce qui *s’exécuterait*, ou pourquoi rien ne s’exécuterait.

## Ce qu’une règle peut faire {#actions}

Une action qui nécessite un équipement n’apparaît que sur un aquarium qui a cet équipement.

| Action | Ce qu’elle fait |
|---|---|
| **Contrôler un équipement Apex** | Commander une prise |
| **Lancer un cycle d’alimentation Apex** | Lancer un nourrissage. L’Apex l’arrête avec sa propre minuterie |
| **Lancer un test Trident** | Lancer un test. Chaque exécution consomme du réactif |
| **Doser une tête DŌS** | Faire une dose mesurée avec une tête DŌS |
| **Contrôler un équipement Red Sea** | Piloter un appareil ReefBeat |
| **Contrôler une pompe de brassage** | Régler le débit, le mode de vague ou l’alimentation d’une pompe Jecod, ou **Mettre en pause pour le nourrissage**. Le Cora Max de l’aquarium remet la pompe en marche à la fin du nourrissage |
| **Contrôler un équipement GHL (bêta)** | Mettre en pause un programme de nourrissage, lancer le mode entretien ou changement d’eau, régler une scène ou une luminosité d’éclairage, et plus |
| **Contrôler un équipement HYDROS (bêta)** | Régler une sortie, la remettre sur son programme, changer de mode, lancer une commande de testeur ou doser avec une tête |
| **Contrôler un appareil EcoTech (bêta)** | Régler l’intensité ou la scène d’une Radion, lancer un nourrissage ou un mode VorTech, doser avec un Versa, ou remettre n’importe lequel sur son programme |
| **Me notifier** | Vous envoyer une notification avec votre propre **Titre** et votre **Message** |
| **Attendre avant l’étape suivante** | Faire une pause avant de continuer |
| **Lancer une scène** | Lancer une scène depuis cette règle |
| **Gérer une automatisation** | Activer ou désactiver une autre règle |
| **Créer une tâche d’entretien** | Ajouter une tâche à la liste d’[entretien](/help/mobile-maintenance) de l’aquarium, par exemple changer le média du filtre à CO2 quand le pH passe sous une valeur |

:::note Beta
GHL, HYDROS et EcoTech sont en Beta et ne sont ouverts qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html). Plus de détails dans [Fonctions Beta](/help/mobile-beta).
:::

:::warning Une dose ne s’annule pas, et elle est plafonnée
On ne peut pas retirer une dose de l’aquarium. Une règle ne peut doser qu’avec une tête mesurée avec **Mesurer pour doser** sur un Cora Max. La dose s’exécute sur un Cora Max à l’aquarium. Le dosage par règle est plafonné à **10 mL par tête et par jour**, quelle que soit la façon dont la règle est écrite.
:::

:::note Ce que fait Créer une tâche d’entretien
Choisissez l’aquarium, puis **Tâche existante** (une tâche existante devient due maintenant) ou **Nouvelle tâche** (donnez-lui un **Nom de la tâche**). Une nouvelle tâche est ponctuelle, due tout de suite, et la règle ne la recrée pas tant qu’elle est encore ouverte. Vous recevez une seule notification, et la tâche ponctuelle quitte la liste quand vous la terminez.
:::

:::note Attendre est court
**Attendre avant l’étape suivante** fait une pause de 60 secondes au plus, et une branche peut attendre 60 secondes au total. Après la pause, l’étape suivante voit des mesures fraîches. Pour un arrêt plus long, comme une pompe de remontée coupée 30 minutes pendant un changement d’eau, utilisez une scène avec **Durée** (voir plus bas).
:::

## Scènes {#scenes}

Une scène est un groupe d’actions qui porte un nom, comme « Changement d’eau », « Mode photo » ou « Nuit ». Touchez **Nouvelle automatisation** ou **Nouvelle scène** et choisissez **Scène** en haut. Une scène n’a pas de déclencheur. Vous la lancez avec **Exécuter maintenant** dans la liste, depuis une règle avec **Lancer une scène**, ou selon un horaire par une règle avec **À une heure de la journée**.

**Durée** définit combien de temps dure une scène : un nombre de minutes ou d’heures, ou **Jusqu’à ce que je la change**. À la fin du temps, Cora remet les prises de la scène comme elles étaient. Les autres équipements restent tels que la scène les a laissés. Pendant qu’une scène minutée tourne, la liste affiche un compte à rebours et un bouton **Arrêter** qui la termine plus tôt.

Si une scène commande une prise importante, comme un chauffage, un groupe froid, une pompe de remontée ou l’osmolateur, Cora demande avant de la lancer et liste ces étapes. Vous pouvez désactiver cela avec **Demander avant d’exécuter** sur la scène.

Une scène peut en appeler une autre, jusqu’à 3 niveaux. Cora ne lance pas une scène qui s’appelle elle-même, car elle pourrait tourner en boucle et continuer d’agir sur l’aquarium.

Après l’exécution d’une scène, vous voyez ce qui s’est passé étape par étape, y compris ce qui a échoué ou ne s’est pas exécuté.

## Scènes créées sur Cora Max {#scenes-on-cora-max}

Vous pouvez aussi créer et modifier des scènes sur un Cora Max. C’est le même ensemble de scènes, partagé sur le compte. Un Cora Max plus ancien peut toujours lancer une scène créée sur le téléphone. La modification sur l’appareil est plus récente, en revanche : un Cora Max plus ancien peut donc afficher une scène sans vous laisser la changer. Modifiez-la plutôt depuis le téléphone.

## Désactiver une règle {#turning-a-rule-off}

Chaque règle a un interrupteur d’activation. Désactiver une règle garde ses réglages, ce qui est pratique quand vous voulez la retrouver la saison suivante.

## Voir ce qu’une règle a fait {#seeing-what-a-rule-did}

Chaque action d’une règle est enregistrée avec **Règle d’automatisation** comme cause. Vous la trouverez dans [Activité](/help/mobile-activity).
