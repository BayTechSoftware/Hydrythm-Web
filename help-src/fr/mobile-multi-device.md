---
title: Plus d’un appareil Cora
description: Choisissez l’appareil qui répond à la voix et celui qui interroge chaque aquarium.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Un foyer peut avoir plusieurs Cora Max. Deux réglages répartissent le travail entre eux, pour qu’ils ne fassent pas deux fois la même chose. Il est aussi utile de savoir ce qu’ils partagent, et ce qu’ils ne partagent pas.

## Ce qui est partagé, et ce qui ne l’est pas

| Partagé par tous les appareils | Propre à chaque écran |
|---|---|
| Aquariums, mesures et historique | Sa mise en page de tableau de bord |
| Appareils et leurs réglages | Wi-Fi, luminosité, son |
| Journal, population, entretien | Mot d’activation et verrouillage enfant |
| Alertes, seuils, automatisations | Les aquariums affichés sur cet écran |
| Forfaits et utilisation | |

Un seuil changé sur un appareil change partout. Un tableau de bord réorganisé, non. Chaque écran garde sa propre mise en page, et le téléphone et le Cora Max n’en partagent jamais.

## Cora Assistant : Appareil répondant

**Réglages → Cora Assistant → Appareil répondant** choisit l’**appareil Cora** qui répond quand vous parlez dans la pièce. Un seul répond, même si plusieurs vous entendent. Choisissez celui qui est le plus près de l’endroit où vous vous tenez d’habitude.

Ce choix est différent de Cora Max principal, décrit plus bas. Appareil répondant décide quel appareil répond à votre voix. Cora Max principal décide quel appareil interroge l’équipement d’un aquarium. Avec deux Cora Max, vous voudrez peut-être régler ces deux choix différemment.

![Le sélecteur de répondeur vocal](img/mobile-voice-responder.webp "Chaque appareil montre ce qu’il écoute, et s’il est en ligne.")

Chaque appareil de la liste indique le mot d’activation qu’il attend, et s’il est en ligne. **Ce mot n’est pas le même partout.** Le mot d’activation est appris par l’appareil lui-même, et des modèles de Cora différents peuvent attendre des mots différents. Lisez-le sur la ligne de chaque appareil, sans supposer que tout le foyer utilise le même.

:::note Votre téléphone n’apparaît pas dans cette liste
Le téléphone n’attend pas de mot d’activation. Vous lancez une conversation en touchant l’écran. Cela marche toujours, quel que soit ce réglage. La liste ne montre que le matériel Cora doté de la voix.
:::

## Cora Max principal

L’équipement de votre réseau est lu par un Cora Max. Si plusieurs Cora Max peuvent lire le même contrôleur, ils l’interrogent tous en parallèle, sauf si vous en désignez un.

**Cora Max principal** se règle pour chaque aquarium. Il désigne l’appareil qui lit le contrôleur de cet aquarium. Dans Cora Mobile, ouvrez l’aquarium et touchez **Cora Max principal**.

| Réglage | Fonctionnement |
|---|---|
| Un appareil précis | Il devient le seul appareil Cora à interroger le contrôleur. Il reste le principal même s’il est hors ligne, et les autres appareils Cora ne prennent pas le relais. Cora Mobile n’interroge le contrôleur que pendant que cet appareil est hors ligne. |
| **Tout appareil actif (automatique)** | Cora Mobile et tous les appareils Cora en ligne se partagent le travail (la dernière écriture l’emporte). Si l’un se déconnecte, un autre continue. Convient à un foyer avec un seul appareil, et c’est le choix le plus sûr si vous hésitez. |

Tant que l’appareil choisi est hors ligne, une commande qui doit passer par lui ne s’exécute pas. Cora vous indique que l’aquarium utilise cet appareil, qu’il est hors ligne et que rien ne s’est exécuté. Vous pouvez réessayer quand il est de retour. S’il doit rester hors ligne un moment, choisissez un autre appareil ou **Tout appareil actif (automatique)**.

:::note Choisissez un principal quand deux appareils suivent un même aquarium
Avec un principal, le contrôleur est moins sollicité, et vous n’avez plus de mesures en double pour la même source.
:::

:::note Ce réglage vaut pour tout le compte, aquarium par aquarium
Cora Max principal appartient à l’aquarium, pas au téléphone ni au Cora Max que vous avez en main. Si vous le changez depuis un appareil, il change pour tout le foyer.
:::

## Ce qui marche quand vous n’êtes pas chez vous

Loin du Wi-Fi de votre aquarium, votre téléphone ne parle pas directement à votre équipement. La commande passe par Cora Cloud, qui la transmet à un Cora Max installé près de l’aquarium. C’est ce Cora Max qui agit sur l’équipement.

En pratique :

- **Les mesures et l’historique** sont toujours disponibles, où que vous soyez, car ils sont déjà stockés dans Cora Cloud.
- **Le pilotage de l’équipement** (allumer ou éteindre une prise, lancer un nourrissage, doser avec une tête, mettre une pompe en pause) marche aussi à distance, tant qu’un Cora Max près de l’aquarium est en ligne et peut joindre l’équipement. Sinon, la commande ne peut pas arriver.
- **Les réglages internes d’un appareil** (pas ses mesures) demandent parfois un téléphone sur le *même* réseau que l’appareil. Un Cora Max près de l’aquarium ne suffit pas toujours. Dans ce cas, la page le précise.

Deux messages signalent qu’une commande n’a pas abouti normalement.

- **« Rien n’a été envoyé »** : la commande n’est jamais partie de votre téléphone, ou aucun Cora Max près de l’aquarium n’a pu la prendre. Rien ne s’est exécuté. Vous verrez ce message si le Cora Max principal de l’aquarium est hors ligne et qu’aucun autre appareil de cet aquarium ne peut prendre le relais.
- **« Cela a peut-être déjà été exécuté »** : la commande est partie, mais aucun Cora Max n’a confirmé à temps. Cora ne sait vraiment pas si elle s’est exécutée. Regardez l’état de l’équipement avant de réessayer, pour ne pas l’envoyer deux fois.

Si l’un de ces messages revient souvent, vérifiez qu’un Cora Max près de l’aquarium est en ligne. Vous pouvez aussi régler **Cora Max principal** sur **Tout appareil actif (automatique)**, pour que n’importe quel appareil en ligne puisse prendre la commande. Tous les résultats possibles d’une commande sont décrits dans [Contrôler votre équipement](/help/mobile-device-control).

## Où voir l’état de chaque appareil

Cora Max indique l’état d’interrogation de chaque aquarium dans **Réglages → Réglages Cora Max → État**. Voir [Appareils et état des appareils](/help/max-devices).
