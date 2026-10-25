---
title: Plus d’un appareil Cora
description: Avec plusieurs appareils Cora, choisissez lequel répond à votre voix et lequel interroge chaque aquarium, et voyez ce qui fonctionne loin de chez vous.
section: Cora Mobile
reviewed: 2026-10-13
order: 37
group: Settings and account
twin: max-reef-room
---

Cette page concerne un foyer avec plusieurs Cora Max, ou un Cora Max et plusieurs téléphones. Deux réglages décident quel appareil fait quoi, pour qu’ils ne fassent pas deux fois le même travail. Il est aussi utile de savoir ce qu’ils partagent.

## Ce qui est partagé, et ce qui ne l’est pas

| Partagé entre tous les appareils | Propre à un Cora Max |
|---|---|
| Aquariums, mesures et historique | Sa disposition de tableau de bord |
| Appareils et leurs réglages | Wi-Fi, luminosité, son |
| Journal, population, entretien | Mot d’activation et verrouillage enfant |
| Alertes, seuils, automatisations | Les aquariums que cet écran affiche |
| Forfaits et consommation | |

Si vous changez un seuil sur un appareil, il change partout. Les dispositions de tableau de bord sont différentes. La disposition du téléphone suit votre compte, donc tous les téléphones sur lesquels vous vous connectez affichent la même. Chaque Cora Max garde sa propre disposition, et le téléphone et Cora Max n’en partagent jamais une.

## Cora Assistant : Appareil répondant {#cora-assistant-answering-device}

**Paramètres → Cora Assistant → Appareil répondant** choisit l’**appareil Cora** qui répond quand vous parlez dans la pièce. Peu importe combien d’appareils vous entendent, un seul répond. Choisissez celui qui est le plus proche de l’endroit où vous vous tenez d’habitude.

Seul l’appareil répondant écoute la phrase d’activation. Un autre Cora Max prend le relais de l’écoute tant qu’il est hors ligne, ou qu’on ne l’a pas vu depuis plus de 15 minutes, et s’arrête dès qu’il revient. Plus de détails dans [Parler à Cora](/help/max-voice).

C’est indépendant du Cora Max principal, plus bas. L’appareil répondant décide qui répond à votre voix. Le Cora Max principal décide qui interroge l’équipement d’un aquarium. Avec deux Cora Max à la maison, vous pouvez les régler différemment.

![Le choix de l’appareil répondant](img/mobile-voice-responder.webp "Chaque appareil indique ce qu’il écoute, et s’il est en ligne.")

Chaque appareil de la liste indique sa phrase d’activation et s’il est en ligne. **Les phrases d’activation ne sont pas toujours les mêmes.** La phrase est intégrée à l’appareil, donc différents modèles Cora peuvent écouter des phrases différentes. Vérifiez la ligne de chaque appareil. Ne supposez pas que tout le foyer utilise la même phrase.

:::note Votre téléphone n’est pas dans cette liste
Le téléphone n’écoute pas de phrase d’activation. Vous y lancez une conversation en touchant l’écran, et cela fonctionne toujours, quel que soit ce réglage. La liste ne montre que le matériel Cora doté de la voix.
:::

## Cora Max principal {#primary-cora-max}

Un Cora Max lit l’équipement de votre réseau. Si plusieurs peuvent joindre le même contrôleur, ils l’interrogeraient tous en parallèle.

**Cora Max principal** vous permet de choisir, pour chaque aquarium, quel appareil lit le contrôleur de cet aquarium. Dans Cora Mobile, ouvrez l’aquarium et touchez **Cora Max principal**.

| Réglage | Comportement |
|---|---|
| Un appareil nommé | C’est le seul appareil Cora qui interroge le contrôleur. Il reste principal même hors ligne, et les autres appareils Cora ne prennent pas le relais. Cora Mobile ne lit le contrôleur que tant que cet appareil est hors ligne. |
| **Tout appareil actif (automatique)** | Cora Mobile et tout appareil Cora en ligne se partagent le travail (la dernière écriture l’emporte). Si l’un se déconnecte, un autre continue. Bien pour un foyer avec un seul appareil, et le choix le plus sûr si vous ne savez pas quel appareil doit gérer l’aquarium. |

Tant que l’appareil que vous avez nommé est hors ligne, une commande qui doit passer par lui ne s’exécute pas. Cora vous dit que l’aquarium est réglé pour utiliser cet appareil, qu’il est hors ligne et que rien ne s’est exécuté. Réessayez quand il est revenu. S’il doit rester hors ligne un moment, choisissez un autre appareil ou **Tout appareil actif (automatique)**.

:::note Deux appareils surveillent un aquarium ? Choisissez un principal
Nommer un principal soulage le contrôleur et supprime les mesures en double d’une même source.
:::

:::note Ce réglage appartient à l’aquarium
Le Cora Max principal se règle par aquarium pour tout le compte. Il n’appartient pas au téléphone ou au Cora Max que vous avez en main. Changez-le depuis n’importe quel appareil, et il change pour tout le foyer.
:::

## Ce qui fonctionne loin de chez vous {#what-works-away-from-home}

Quand vous êtes loin du Wi-Fi de votre aquarium, votre téléphone ne parle pas directement à votre équipement. Une commande part vers Cora Cloud, qui la transmet à un Cora Max à l’aquarium. C’est ce Cora Max qui atteint l’équipement.

Voici ce que cela signifie pour vous.

- **Les mesures et l’historique** sont toujours là, où que vous soyez. Ils sont déjà stockés dans Cora Cloud.
- **La commande de l’équipement** fonctionne aussi loin de chez vous, tant qu’un Cora Max à l’aquarium est en ligne et peut joindre cet équipement. Cela couvre par exemple commander une prise, lancer un nourrissage, doser avec une tête ou mettre une pompe en pause. Si aucun Cora Max ne peut le joindre, la commande ne passe pas.
- **Les réglages propres d’un appareil** (ses réglages natifs, pas ses mesures) demandent parfois un téléphone sur le *même* réseau que l’appareil. Un Cora Max à l’aquarium ne suffit pas pour ceux-là. La page de cet appareil indique quand c’est le cas.

Deux messages vous disent qu’une commande n’est pas passée proprement.

- **"Rien n’a été envoyé"** veut dire que la commande n’a jamais quitté votre téléphone, ou qu’aucun Cora Max à l’aquarium n’a pu la prendre. Rien ne s’est exécuté. Vous le verrez si le Cora Max principal de l’aquarium est hors ligne et qu’aucun autre appareil de cet aquarium ne peut prendre le relais.
- **"Elle a peut-être déjà été exécutée"** veut dire que la commande est partie, mais qu’aucun Cora Max ne l’a confirmée à temps. Cora ne sait vraiment pas si elle s’est exécutée. Vérifiez l’équipement lui-même avant de réessayer, pour ne pas l’envoyer deux fois.

Si l’un de ces messages revient sans cesse, vérifiez qu’un Cora Max à l’aquarium est en ligne. Vous pouvez aussi régler le **Cora Max principal** sur **Tout appareil actif (automatique)** pour que n’importe quel appareil en ligne puisse prendre la commande. Tous les résultats possibles d’une commande sont listés dans [Contrôler votre équipement](/help/mobile-device-control).

## Où voir l’état de chaque appareil

Cora Max affiche l’état d’interrogation de chaque aquarium sous **Paramètres → Paramètres Cora Max → État**. Plus de détails dans [Appareils et état des appareils](/help/max-devices).
