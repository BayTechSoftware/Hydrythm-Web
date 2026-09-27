---
title: Plus d’un appareil Cora
description: Choisissez quel appareil répond à la voix et lequel interroge chaque aquarium.
section: Cora Mobile
reviewed: 2026-09-27
order: 29
group: Account
---

Un foyer peut avoir plus d’un Cora Max. Deux réglages déterminent lequel fait quoi, pour qu’ils ne dupliquent pas le travail l’un de l’autre, et une troisième chose qui vaut la peine d’être connue est ce qui est partagé entre eux, ou pas.

## Ce qui est partagé, et ce qui ne l’est pas

| Partagé sur chaque appareil | Appartient à un seul écran |
|---|---|
| Aquariums, mesures et historique | Sa mise en page de tableau de bord |
| Appareils et leurs réglages | Wi-Fi, luminosité, audio |
| Journal, population, entretien | Mot d’activation et verrouillage enfant |
| Alertes, seuils, automatisations | Quels aquariums cet écran affiche |
| Forfaits et utilisation | |

Changer un seuil sur un appareil le change partout. Réarranger un tableau de bord ne le fait pas ; chaque écran garde sa propre mise en page, et le téléphone et le Cora Max n’en partagent jamais une.

## Cora Assistant : appareil répondant

**Réglages → Cora Assistant → Appareil répondant** choisit quel **appareil Cora** répond quand vous parlez à la pièce. Un seul répond, quel que soit le nombre qui peut vous entendre ; réglez-le sur l’unité la plus proche de l’endroit où vous vous tenez habituellement.

C’est un choix différent de Cora Max principal ci-dessous : Appareil répondant détermine quel appareil répond à votre voix, et Cora Max principal détermine quel appareil interroge l’équipement d’un aquarium. Un foyer avec deux tablettes peut vouloir régler chacun différemment.

![Le sélecteur de répondeur vocal](img/mobile-voice-responder.webp "Chaque appareil montre ce qu’il écoute, et s’il est en ligne.")

Chaque appareil de la liste montre le mot d’activation qu’il écoute, ainsi que s’il est en ligne. **Ce ne sont pas tous les mêmes.** Un mot d’activation est entraîné dans l’appareil lui-même, donc différents modèles de Cora peuvent en écouter des différents. Lisez le mot d’activation sur la propre ligne de l’appareil plutôt que de supposer que le foyer en partage un seul.

:::note Votre téléphone n’est pas dans ce sélecteur
Le téléphone n’écoute pas de mot d’activation. Vous démarrez une conversation en le touchant, ce qui fonctionne toujours et n’est pas affecté par ce réglage. Le sélecteur ne liste que le matériel Cora capable de voix.
:::

## Cora Max principal

L’équipement de votre réseau est lu par un Cora Max. Quand plus d’un pourrait lire le même contrôleur, ils l’interrogeraient sinon en parallèle.

**Cora Max principal** est un choix par aquarium de quel appareil lit le contrôleur de cet aquarium. Dans Cora Mobile, ouvrez l’aquarium et touchez **Cora Max principal**.

| Réglage | Comportement |
|---|---|
| Un appareil nommé | Il devient le seul appareil Cora qui interroge le contrôleur, et il reste le principal même quand il est hors ligne : les autres appareils Cora ne prennent pas le relais. Cora Mobile interroge seulement quand il est hors ligne. |
| **Tout appareil actif (automatique)** | L’application et tout appareil Cora en ligne partagent le travail (la dernière écriture l’emporte), donc si l’un passe hors ligne, un autre continue. Convient à un foyer à un seul appareil, et le choix par défaut plus sûr quand vous n’êtes pas sûr de quel appareil devrait le posséder. |

Tant qu’un appareil que vous avez nommé est hors ligne, une commande qui doit passer par lui ne s’exécute pas : Cora vous dit que l’aquarium est réglé pour utiliser cet appareil, qu’il est hors ligne, et que rien ne s’est exécuté, pour que vous puissiez réessayer une fois qu’il est de retour. S’il doit rester hors ligne un moment, choisissez un autre appareil ou **Tout appareil actif (automatique)**.

:::note Réglez un principal quand deux appareils surveillent un aquarium
Nommer un principal réduit la charge sur le contrôleur et retire les mesures dupliquées de la même source.
:::

:::note C’est un réglage à l’échelle du compte, par aquarium, pas par appareil
Cora Max principal appartient à l’aquarium, pas au téléphone ou à la tablette que vous regardez. Le changer depuis n’importe quel appareil le change pour tout le foyer.
:::

## Ce qui fonctionne loin de chez vous

Votre téléphone ne parle pas directement à votre équipement quand vous êtes loin du Wi-Fi de votre aquarium. Au lieu de cela, une commande voyage jusqu’à Cora Cloud, qui la transmet à un Cora Max présent à l’aquarium ; c’est ce Cora Max qui atteint réellement l’équipement.

Cela signifie :

- **Les mesures et l’historique** sont toujours disponibles, où que vous soyez, car ils sont déjà stockés dans Cora Cloud.
- **Contrôler l’équipement** (commuter une prise, démarrer un nourrissage, doser une tête, mettre une pompe en pause) fonctionne aussi loin de chez vous, tant qu’un Cora Max à l’aquarium est en ligne et peut atteindre cet équipement. S’il n’y en a aucun, la commande ne peut pas être délivrée.
- **Les réglages propres à un appareil** (par opposition à ses mesures) ont parfois besoin d’un téléphone sur le *même* réseau que l’appareil lui-même, pas seulement d’un Cora Max à l’aquarium. Là où cela s’applique, la page le précise.

Deux messages vous disent que la commande n’a pas simplement réussi :

- **« Rien n’a été envoyé »** : la commande n’a jamais quitté votre téléphone, ou aucun Cora Max à l’aquarium n’a pu la prendre. Rien ne s’est exécuté. C’est ce que vous verrez si le Cora Max principal de l’aquarium est hors ligne et qu’aucun autre appareil sur cet aquarium ne peut prendre le relais.
- **« Cela a peut-être déjà été exécuté »** : la commande a été envoyée, mais aucun Cora Max n’a répondu à temps pour la confirmer. Cora ne sait réellement pas si elle s’est exécutée. Vérifiez l’état propre de l’équipement avant de réessayer, pour ne pas l’envoyer deux fois.

Si l’un des deux messages continue d’apparaître, vérifiez qu’un Cora Max à l’aquarium est en ligne, ou réglez **Cora Max principal** sur **Tout appareil actif (automatique)** pour que tout appareil en ligne puisse prendre la commande. Voir [Contrôler votre équipement](/help/mobile-device-control) pour tous les résultats qu’une commande peut avoir.

## Où l’état de chaque appareil est affiché

Cora Max signale son propre état d’interrogation et de voix sous **Réglages → Cora Max → Micrologiciel → État et commandes de l’appareil**. Voir [Appareils et état des appareils](/help/max-devices).
