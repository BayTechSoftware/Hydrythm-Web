---
title: Association des paramètres et sondes
description: Voyez les mesures de chaque appareil dans une seule liste, choisissez le paramètre affiché et l’appareil qui l’alimente, et notez l’étalonnage et le nettoyage des sondes.
section: Cora Mobile
reviewed: 2026-11-03
order: 15
group: Equipment
---

Utilisez **Association des paramètres** pour dire à Cora sous quel paramètre s’affiche chaque mesure et, quand deux appareils mesurent la même chose, auquel faire confiance. Allez dans **Paramètres**, ouvrez l’aquarium et touchez **Association des paramètres**.

Elle se trouve entre **Modifier l’aquarium** et **Seuils d’alerte**. Le crayon en haut du tableau de bord ouvre **Modifier l’aquarium**, qui ne la contient pas. Vous pouvez aussi y accéder depuis les pages d’appareil Neptune Apex.

L’écran est une seule liste d’appareils, avec un champ de recherche (**Rechercher un paramètre**) au-dessus. La recherche porte sur les noms de paramètres, les noms de mesures, les appareils et les marques. Le même champ de recherche se trouve dans chaque sélecteur de paramètre.

## Une seule liste d’appareils {#mapping}

Sous le champ de recherche, Cora résume l’écran en une ligne : les mesures de chaque appareil et le paramètre de l’aquarium sous lequel elles s’affichent. Touchez une mesure pour la modifier.

- **Chaque appareil apparaît sous le nom que vous lui avez donné.** Un appareil sans nom apparaît sous sa marque, et deux appareils de même marque sans nom sont numérotés (« AquaWiz 1 », « AquaWiz 2 »). Les numéros de série et identifiants d’appareil ne servent jamais de noms ; ils se trouvent derrière **Afficher les détails** sur la page de l’appareil. Voir [La page d’un appareil](/help/mobile-devices#a-devices-page).
- **Chaque mesure est listée sous l’appareil qui la signale réellement.** Chaque ligne montre le nom que l’appareil donne à la mesure, sa dernière valeur et **S’affiche comme**, le paramètre de l’aquarium qu’elle alimente. Une mesure que vous avez masquée indique **Non affichée**.
- **Un aquarium n’a qu’un seul Neptune Apex**, quel que soit le nombre d’appareils Cora qui le lisent. Ses sondes forment une seule liste dans une seule section **Apex** (ou sous le nom que vous lui avez donné). Un module d’extension Apex, comme un DŌS ou un Trident, est listé sous son propre nom. Ses mesures ne peuvent pas être réorientées ; en toucher une vous permet de renommer le paramètre à la place.
- **Un appareil partagé avec d’autres aquariums apparaît dans la liste de chaque aquarium auquel il est lié.** Sa section indique *Aussi sur* et les noms des autres aquariums, suivis de *Les changements ici ne s’appliquent qu’à cet aquarium.*
- **Un appareil de deux mesures ou moins est ouvert d’emblée** ; un appareil plus long est fermé au départ et affiche son nombre de mesures, sauf si l’une de ses mesures partage un paramètre avec un autre appareil. Touchez le nom d’un appareil pour l’ouvrir ou le fermer. Pendant une recherche, tous les résultats sont ouverts.

Cora reconnaît toute seule les noms de mesure standard, donc la plupart des lignes affichent déjà le bon paramètre. Ne corrigez que les quelques-unes qu’elle n’a pas su placer.

Un changement est enregistré dès que vous le choisissez, et il n’y a pas de bouton d’enregistrement. Il prend effet à l’arrivée des mesures suivantes. En corriger un ici ne réécrit pas l’historique : les mesures passées restent où elles sont, et seul ce qui est enregistré à partir de là change. Les associations faites avant cette présentation sont conservées telles quelles.

:::warning Cora ne voit pas une mesure masquée
Si un paramètre n’affiche aucune mesure alors que l’appareil fonctionne, vérifiez si sa mesure indique **Non affichée**.
:::

:::note Un capteur de fuite ne peut pas être réaffecté ici
L’alarme d’un capteur de fuite dépend de son propre nom, donc sa ligne indique *L’alarme de fuite dépend de ce nom, il ne peut donc pas être modifié ici.* Il fonctionne comme d’habitude.
:::

:::note Appareils qui attendent encore une mise à jour
Un appareil qui attend une mise à jour de son firmware indique *Les changements ici s’appliquent après la mise à jour du firmware de cet appareil.* Votre choix est enregistré et s’applique dès que la mise à jour est installée.
:::

## Choisir sous quel paramètre s’affiche une mesure {#shows-as}

Touchez une mesure pour ouvrir **Afficher cette mesure comme**. En haut figure la mesure elle-même : l’appareil, le nom de la mesure et sa valeur. En dessous :

- **Vos paramètres** liste chaque paramètre de cet aquarium. Chaque option indique d’où viennent ses mesures, pour que vous n’ayez jamais à hésiter entre deux noms proches :
  - *Vient de* et le nom de l’appareil qui l’alimente, ou *Vient aussi de* et le nom d’un autre appareil quand cette mesure s’affiche déjà sous ce paramètre.
  - *Aucun appareil ne l’alimente actuellement. Dernière valeur …* avec l’ancienneté, pour un paramètre dont l’appareil s’est tu.
  - *Issu de vos résultats de tests* ou *Issu de résultats d’ICP*, avec la dernière valeur, pour un paramètre qui n’a que vos propres résultats.

  Le crayon (**Renommer**) à côté d’un paramètre lui donne votre propre nom. C’est ce nom qui apparaît sur votre tableau de bord, dans les alertes et dans Reef Buddy. Laissez le nom vide pour le réinitialiser.
- **Plus de paramètres** est replié. Il contient les paramètres standard que cet aquarium n’a pas encore.
- **Nouveau paramètre…** crée un paramètre à part, à part de vos autres paramètres. Voir ci-dessous.
- **Ne pas afficher cette mesure** (*Cora l’ignore*) empêche la mesure d’être enregistrée sous un paramètre. Une mesure masquée n’apparaît sur aucun tableau de bord et ne déclenche aucune alerte.

La feuille se termine par *Enregistré dès que vous choisissez. Les mesures passées restent où elles sont.*

### Nouveau paramètre {#new-parameter}

Utilisez **Nouveau paramètre…** quand une mesure ne doit pas être mélangée avec une autre de même nom, par exemple une deuxième sonde de pH dans la décantation. Cora ouvre **Nouveau paramètre** et explique que la mesure de cet appareil s’affichera comme un paramètre à part et que son unité vient de l’appareil.

1. Saisissez un **Nom**. Le nom de votre choix, par exemple *pH décantation* ou *pH 2*, jusqu’à 32 caractères.
2. Touchez **Créer**. **Créer** reste grisé tant que le nom est vide. **Annuler** ferme la fenêtre et ne change rien.

La mesure alimente maintenant le nouveau paramètre. Le nom garde l’orthographe que vous avez saisie. Si vous saisissez le nom d’un paramètre que vous avez déjà, la mesure le rejoint et son nom n’est pas modifié. Aucune plage d’alerte n’est copiée depuis un autre paramètre.

## Tests et résultats de laboratoire {#tests-and-lab-results}

Les résultats de vos propres kits de test et vos résultats d’ICP sont listés tout en bas, dans **Tests et résultats de laboratoire**. La section est fermée au départ, car un seul rapport d’ICP compte des dizaines d’éléments. Touchez-la pour l’ouvrir. Les résultats sont regroupés sous **Résultats d’ICP** et **Vos résultats de tests**.

Chaque résultat s’associe à un paramètre comme la mesure d’un appareil. Touchez-en un pour ouvrir **Afficher cette mesure comme** et choisir le paramètre sous lequel il s’affiche, par exemple pour garder le pH d’un kit de test séparé de celui d’une sonde. Cora le dit dans la section : les nouveaux résultats suivent votre choix, et les anciens restent où ils sont. Un résultat de test ou d’ICP n’est jamais écarté, donc **Ne pas afficher cette mesure** ne lui est pas proposé.

Les paramètres qu’aucune mesure ci-dessus n’alimente, et qui ne sont pas des tests, sont listés sous **Autres paramètres**. Touchez-en un pour le renommer.

## Plusieurs sondes pour un même paramètre {#multiple-probes}

Si deux mesures s’affichent sous le même paramètre, qu’elles viennent de deux sondes d’un même appareil ou de deux appareils différents, une bannière apparaît en haut de la liste. Elle indique par exemple *pH reçoit des mesures de 2 appareils* (ou *2 sondes*), suivi de ce que fait Cora : *La plus récente est affichée.* ou *Utilise* l’appareil que vous avez choisi. Touchez-la, ou touchez **En choisir une**, pour ouvrir la feuille.

- **Mesure la plus récente** (*L’appareil qui a envoyé en dernier*) laisse Cora utiliser l’appareil qui a transmis en dernier. Les autres restent dans l’historique.
- Choisissez un appareil ou une sonde pour suivre seulement celui-là. Chacun affiche sa valeur et il y a combien de minutes il a transmis. Votre choix s’applique à ce paramètre partout dans l’aquarium : sa tuile, son graphique et ses alertes, pas un seul widget.
- **En afficher une séparément** (*Par exemple une deuxième sonde dans la décantation*) demande **Laquelle afficher séparément ?** puis ouvre **Afficher cette mesure comme** pour celle que vous choisissez.

Si un appareil choisi arrête de transmettre, la bannière indique *Ne signale plus depuis* et l’heure, et propose **Utiliser la plus récente**, pour qu’une sonde morte ne puisse pas bloquer une mesure.

Vous pouvez comparer les sources dans [la page du paramètre](/help/mobile-metric-detail).

Quand deux sources signalent le même paramètre, la mesure la plus récente l’emporte. Une valeur à l’écran n’est remplacée que par une mesure dont l’heure de mesure est plus tardive, quel que soit l’appareil d’où elle vient. Une mesure plus ancienne, ou un appareil qui renvoie une ancienne mesure, va dans l’historique et n’écrase pas la valeur actuelle. Si vous avez choisi un appareil, Cora suit cet appareil à la place.

Le profil de l’aquarium a aussi une section **Sources des paramètres** (elle est masquée pendant la création d’un nouvel aquarium). Elle règle la même chose sous une forme plus courte. Utilisez l’Association des paramètres quand vous voulez voir tous les appareils et toutes les mesures au même endroit.

## Noter l’entretien des sondes {#recording-probe-care}

Les sondes dérivent. Quand vous étalonnez, nettoyez ou remplacez une sonde, dites-le à Cora, pour qu’il ne prenne pas le saut de la mesure pour un vrai changement dans l’aquarium.

1. Touchez le widget du paramètre sur le tableau de bord, par exemple le pH, la température, la salinité ou l’ORP.
2. Touchez **Enregistrer l’entretien de la sonde** (l’icône de capteur) dans la barre du haut.
3. Choisissez ce que vous avez fait : **Étalonnée**, **Nettoyée**, **Remplacée**, **Repositionnée** ou **Comparée à une référence**. Vous pouvez ajouter une **Mesure de référence** et une note.
4. Touchez **Enregistrer l’entretien de la sonde**.

La page du paramètre indique ensuite depuis combien de temps cette sonde a été étalonnée. L’entretien des sondes fait aussi une bonne [tâche d’entretien](/help/mobile-maintenance) régulière.

:::note Les dates d’étalonnage expliquent les désaccords
Quand une sonde et un kit de test ne sont pas d’accord, regardez quand vous avez étalonné la sonde pour la dernière fois. C’est en général la réponse.
:::
