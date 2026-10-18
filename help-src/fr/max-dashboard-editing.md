---
title: Modifier le tableau de bord Cora Max
description: Ajoutez, déplacez et retirez des tuiles sur le tableau de bord Cora Max, choisissez une grille, utilisez les modèles ou Concevoir avec l’IA, et enregistrez des dispositions à réutiliser sur n’importe quel Cora Max.
section: Cora Max
reviewed: 2026-10-17
order: 4
group: Your dashboard
twin: mobile-dashboard-editing
---

Cette page explique comment disposer les tuiles d’un tableau de bord Cora Max. Il utilise une **grille fixe** : l’affichage ne défile pas, donc toutes les tuiles doivent tenir sur un seul écran. C’est la grande différence avec le tableau de bord du téléphone.

Ouvrez l’éditeur depuis le **menu de l’aquarium** : touchez le nom de l’aquarium dans la barre du haut, puis **Disposition du tableau de bord**. Vous le trouvez aussi dans **Réglages → [votre aquarium] → Disposition du tableau de bord**.

![L’éditeur de tableau de bord sur Cora Max](img/max-dashboard-editor.webp "Les tailles de grille en haut, puis les tuiles. C’est un écran de mise en page, donc chaque tuile montre son type et sa source au lieu d’une mesure. Rien n’est enregistré tant que vous n’appuyez pas sur Enregistrer.")

:::tip Vous pouvez aussi le modifier depuis votre téléphone
Dans Cora Mobile, ouvrez l’onglet **Appareils**, touchez votre Cora Max, puis touchez **Disposition du tableau de bord** sur la carte de l’aquarium. C’est plus rapide que de disposer les tuiles à la main sur un écran mural, et le résultat apparaît sur Cora Max dès que vous enregistrez.
:::

## Choisir une grille {#choosing-a-grid}

Choisissez d’abord la taille de la grille. La changer plus tard déplace toutes les tuiles.

| Grille | Tuiles | Rendu |
|---|---|---|
| 2×2, 3×2, 3×3 | 4–9 | Grand. Facile à lire depuis l’autre bout de la pièce. |
| 4×4, 5×3, 6×4 | 16–24 | Le choix habituel pour un système complet. |
| 6×5, 8×4, 8×5 | 30–40 | Dense. Toute une pièce de récif sur un seul écran. |
| 9×5, 10×5 | 45–50 | Très dense. Idéal sur les plus grands écrans. |
| **Auto** | jusqu’à 32 | Cora choisit une forme adaptée au nombre de tuiles ajoutées. |

Une grille fixe contient autant de tuiles qu’elle a de cases, jusqu’à 50 en 10×5. **Auto** a sa propre limite de 32 tuiles. Au-delà, le texte devient trop petit pour être lu de loin.

:::note Dans le doute, commencez par Auto
Ajoutez les tuiles que vous voulez et laissez la grille sur **Auto**. Cora choisit une forme qui leur convient. Si elle vous plaît, vous pourrez ensuite passer à cette forme fixe.
:::

:::warning Changer de grille ne retire des tuiles que si elles ne tiennent pas
Quand vous changez de grille, Cora ne jette pas les tuiles selon leur position. Les tuiles qui ont encore une case valide restent en place, et les autres sont replacées dans l’ordre. Vous ne perdez des tuiles que si la nouvelle grille a **moins de cases que vous n’avez de tuiles**, et Cora vous dit combien ont disparu. Passer de 10×5 (50 cases) à 3×3 (9) en retire la plupart.
:::

## Ajouter et disposer les tuiles {#adding-and-arranging}

1. Touchez une case vide (elle affiche un **+**) pour ouvrir **Ajouter un widget**.
2. Sous **TYPE**, choisissez le genre de tuile, puis ce qu’elle affiche (une mesure, une prise, un appareil ou une scène).
3. Sous **TAILLE**, choisissez sa taille. Une tuile peut faire une ou deux cases de large et une ou deux cases de haut. Un graphique a aussi une **PLAGE DE TEMPS**. Une tuile de doseur a **Afficher le reste en**, en **Jours** ou **Millilitres (mL)**.
4. Touchez **Ajouter**.

Les gestes sont rappelés en haut de l’éditeur : **Touchez une tuile pour modifier**, **appui long pour déplacer** et **✕ pour retirer**. **Tout effacer** vide la grille pour repartir de zéro.

Les types de tuiles sont Valeur, Jauge, Graphique, État, Prise, Scène, ReefBeat, Module Apex et Jecod. Vous les trouverez dans la [Référence des widgets](/help/mobile-widgets). La tuile **Scène** n’existe que sur Cora Max. Elle lance une [scène](/help/max-automation) d’un seul appui.


## Prises et nourrissage {#outlets-feed}

**Prises et nourrissage**, dans l’éditeur, choisit quelles prises et quels cycles de nourrissage apparaissent dans **Commandes**, le tiroir que vous faites glisser vers le haut depuis le bas du tableau de bord. Cela n’ajoute pas de tuiles. Si vous n’en choisissez aucun, Commandes les liste tous. Pour mettre une prise sur la grille elle-même, ajoutez une tuile **Prise**. Plus de détails dans [Prises et commandes](/help/max-controls).

Quand vous retirez un appareil d’un aquarium, ses tuiles quittent le tableau de bord toutes seules, sur votre téléphone et sur chaque Cora Max de cet aquarium. Une tuile dont l’appareil a disparu affiche **Cet appareil n'est plus dans cet aquarium** et n’ouvre rien.

## Modèles {#templates}

**Modèles** se trouve en haut de l’éditeur, à côté de **Mes tableaux de bord** et **Concevoir avec l'IA**. C’est ouvert avec tous les forfaits et n’utilise jamais l’IA, donc cela fonctionne aussi sans partage de données avec l’IA.

Cela ouvre **Modèles de tableau de bord**, quelques dispositions toutes prêtes construites à partir de ce que cet aquarium remonte et a associé :

- **Vue d'ensemble** : peu de tuiles, en grand, avec les paramètres clés en jauges et vos appareils principaux
- **Équipement** : d’abord une tuile par appareil, puis les prises et les paramètres clés
- **Paramètres** : graphiques et mesures d’abord, appareils et prises en dernier

Chacun affiche un aperçu et indique combien de tuiles il contient et sur quelle grille. Touchez **Utiliser**. Cora demande d’abord **Remplacer votre tableau de bord ?** Touchez **Enregistrer l'actuel comme préréglage d'abord** si vous voulez garder votre disposition actuelle, ou **Remplacer**. Rien n’est enregistré tant que vous n’appuyez pas sur **Enregistrer**.

## Concevoir avec l’IA {#design-with-ai}

L’éditeur a un bouton **Concevoir avec l'IA**. Il fonctionne avec un forfait payant et pendant l’essai. Cora propose une disposition complète à partir de ce que cet aquarium remonte et a associé, et indique combien de tuiles elle contient et sur quelle grille. Touchez **Utiliser** pour la placer dans l’éditeur, ou **Réessayer** pour en obtenir une autre. Vous pouvez créer 5 designs par aquarium et par jour.

Un design de l’IA remplace ce qui se trouve actuellement sur ce tableau de bord. Rien n’est enregistré tant que vous n’appuyez pas sur **Enregistrer**, et vous pouvez d’abord garder votre disposition actuelle en l’enregistrant dans **Mes tableaux de bord**. Avec le forfait gratuit, **Concevoir avec l'IA** vous renvoie vers les forfaits. Il faut aussi que le partage de données avec l’IA soit activé dans Cora Mobile. Plus de détails dans [Interroger Cora](/help/mobile-assistant).

## Penser à la distance {#designing-for-distance}

On lit un écran mural de plus loin qu’un téléphone, et le plus souvent d’un simple coup d’œil.

- Mettez vos paramètres clés en deux par deux. L’alcalinité, la température et le pH sont des valeurs que vous voudrez lire sans vous approcher.
- Placez les commandes sur les bords. Les tuiles de prises sont celles que vous touchez, et elles sont plus faciles à atteindre sur les côtés.
- Regroupez les tuiles par sujet. Gardez tout le dosage ensemble et tout le brassage ensemble, car on parcourt un écran mural par zones.
- Gardez les oligoéléments en petit. Ces valeurs et les autres valeurs lentes servent de repère, donc une tuile Valeur d’une case suffit largement.

## Enregistrer et réutiliser des dispositions {#saving-layouts}

Rien de ce que vous faites dans l’éditeur ne prend effet tant que vous n’appuyez pas sur **Enregistrer**. Si vous quittez avec des changements non enregistrés, Cora demande d’abord **Abandonner les modifications ?**

**Mes tableaux de bord** garde les designs auxquels vous voulez revenir. Ils sont enregistrés sur votre compte, pas sur cet écran : n’importe quel Cora Max de votre compte peut donc les charger, pour un autre aquarium ou pour un écran de remplacement.

- **Enregistrer ce design** garde ce qui est dans l’éditeur. Vous pouvez en garder jusqu’à 30.
- **Charger** place un design enregistré dans l’éditeur. Les designs enregistrés depuis votre téléphone sont marqués **Téléphone**.
- Avant le chargement, Cora vous dit combien de tuiles seront reprises. Ce qui ne peut pas l’être, comme une mesure que cet aquarium ne remonte pas ou un appareil qui n’est pas sur cet aquarium, est listé sous **Laissées de côté :** avec la raison.

Par exemple, vous pouvez garder une disposition dense pour tous les jours et une disposition à grandes tuiles pour quand vous travaillez dans l’aquarium.

## Plusieurs aquariums {#multiple-tanks}

Chaque aquarium a sa propre disposition. Passez sur cet aquarium et ouvrez **Disposition du tableau de bord** depuis son menu d’aquarium, ou utilisez **Réglages → [cet aquarium] → Disposition du tableau de bord**.
