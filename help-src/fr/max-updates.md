---
title: Mises à jour et récupération
description: Comment Cora Max se met à jour tout seul, la plage d’installation et le canal de mise à jour, comment vérifier la version, le code PIN de récupération, et que faire si Cora Max ne démarre pas ou affiche un code d’assistance.
section: Cora Max
reviewed: 2026-10-17
order: 15
group: Settings and account
---

Cora Max se tient à jour tout seul. Cette page explique quand les mises à jour s’installent, comment vérifier votre version, et comment relancer Cora Max s’il ne démarre pas normalement.

## Mises à jour automatiques

Les nouvelles versions se téléchargent en arrière-plan dès leur sortie. Elles s’installent pendant la **Plage d’installation**, de 3 à 5 heures du matin sauf si vous la changez, pour que l’écran ne redémarre pas pendant que vous le regardez. Quand une version a des notes de version, Cora Max les affiche.

Vous n’avez rien à faire pour rester à jour.

## Vérifier la version et les réglages de mise à jour {#checking-the-version-and-update-settings}

![Réseau et mises à jour sur Cora Max](img/max-updates.webp "Mise à jour du micrologiciel, dans la section RÉSEAU ET MISES À JOUR des Réglages Cora Max.")

Votre version figure sur la carte en haut de **Réglages → Réglages Cora Max** (*Cora Max · micrologiciel 0.28.170*), et sous **AIDE ET À PROPOS → À propos**.

**Réglages → Réglages Cora Max → Mise à jour du micrologiciel** (dans **RÉSEAU ET MISES À JOUR**) affiche la version que vous avez et indique si une mise à jour attend. Touchez **Rechercher des mises à jour** pour vérifier maintenant, ou **Télécharger et installer** quand il y en a une.

Sous **Réglages de mise à jour**, sur le même écran :

- **Plage d’installation** définit les heures pendant lesquelles les mises à jour peuvent s’installer, avec une heure de **Début** et de **Fin**, à l’heure locale de cet écran. Le fuseau horaire se règle dans Cora Mobile, sous **Appareils →** votre Cora Max **→ Fuseau horaire**.

Pour voir si cet écran lit vos appareils et enregistre dans Cora Cloud, revenez à **Réglages Cora Max** et faites défiler jusqu’à **ÉTAT**. La section affiche pour chaque aquarium l’**État de l’interrogation**, la **Dernière interrogation**, la **Dernière écriture cloud** et l’**Enregistrement cloud**.

Si une mise à jour se télécharge lentement, vérifiez votre connexion avec le **Test de débit réseau** sur le même écran. **Lancer le test** télécharge jusqu’à 16 Mo du fichier de mise à jour depuis Cora Cloud, pendant 20 secondes au plus, et affiche le débit en Mo/s.

## Quand une mise à jour est disponible

Un message vous dit ce qui est nouveau et vous propose deux choix.

- **Mettre à jour maintenant** installe tout de suite et redémarre. Cela prend environ une minute. Gardez Cora Max alimenté.
- **Reporter de 24 heures** masque le message et vous redemande un jour plus tard.

Tant qu’une mise à jour attend, un petit point s’affiche sur l’icône **Réglages** de la barre du haut et sur la ligne **Mise à jour du micrologiciel**. Le point reste pendant un report, vous voyez donc toujours qu’une mise à jour est là. Il disparaît pendant l’installation.

Si vous ne faites rien, la mise à jour s’installe d’elle-même pendant la **Plage d’installation**.

Vous pouvez aussi la lancer depuis votre téléphone : dans Cora Mobile, ouvrez **Appareils →** votre Cora Max et touchez **Mettre à jour vers v…**.

:::note Vous ne perdez pas de mesures pendant une mise à jour
Vos données sont dans votre compte. Quand Cora Max redémarre, il revient avec les mêmes aquariums, tableaux de bord et historique.
:::

## Récupération {#recovery}

La récupération est un mode de maintenance pour quand Cora Max ne démarre pas normalement, ou quand vous devez réparer sa configuration sans ordinateur.

1. Posez **cinq doigts** en haut à droite de l’écran pendant **dix secondes**.
2. La fenêtre **Code PIN de récupération** s’ouvre. Tapez le code PIN à 6 chiffres et touchez **Entrer**.

Vous avez vu le code PIN lors de l’association de Cora Max. Vous le trouvez aussi dans Cora Mobile sous **Appareils →** votre Cora Max **→ Code PIN de récupération**. Cora Max lui-même ne l’affiche jamais, pour qu’un invité ou un enfant appuyé contre l’écran ne puisse pas entrer en récupération.

Si vous tapez un mauvais code PIN trois fois, la récupération se verrouille pendant 30 secondes, puis plus longtemps après chaque nouvel essai erroné. **Trop de tentatives** vous indique combien de temps attendre. Si Cora Max n’a jamais été en ligne depuis l’association, il n’a pas encore de code PIN et affiche **La récupération n’est pas disponible**. Connectez-le d’abord au Wi-Fi.

Depuis **Récupération**, vous pouvez :

- **Refaire la configuration Wi-Fi** : choisir un nouveau réseau Wi-Fi et son mot de passe
- **Réassocier cet appareil** : effacer l’association et le configurer à nouveau avec Cora Mobile
- **Forcer la vérification OTA** : rechercher des mises à jour maintenant
- **Réinitialisation d’usine** : retirer l’association et tous les réglages de l’écran

Les données d’aquarium déjà enregistrées dans Cora Cloud sont conservées dans tous les cas.

Si Cora Max n’arrive pas à démarrer plusieurs fois de suite, il peut aussi revenir tout seul à la version précédente.

:::note Le même geste déverrouille le verrouillage enfant
Si le [verrouillage enfant](/help/max-settings#child-lock) est activé, poser cinq doigts dans le coin déverrouille aussi l’écran. Touchez **Annuler** dans la fenêtre **Code PIN de récupération** si vous vouliez seulement déverrouiller.
:::

:::warning En récupération, l’écran ne commande rien
Votre contrôleur continue de suivre sa propre programmation. Mais une étape d’[automatisation](/help/mobile-automation) que **ce Cora Max** doit exécuter ne peut pas s’exécuter tant qu’il est en récupération. La règle se déclenche, mais l’étape n’atteint jamais l’équipement.
:::

## Si Cora Max affiche "Cora Max a rencontré un problème"

Cet écran veut dire que quelque chose s’est mal passé pendant le démarrage ou le fonctionnement de Cora Max. Il affiche un **Code d’assistance** (qui commence par *CXB-*).

1. Notez le code d’assistance.
2. Attendez. Cora Max redémarre tout seul au bout d’environ 10 minutes. Pour le redémarrer maintenant, posez cinq doigts en haut à droite pendant 10 secondes.
3. Si cela se reproduit, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le code d’assistance.

## Si un appareil ne redémarre pas

Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant la version affichée à l’écran et le message qu’il affiche. Ne le réappairez pas avant. L’état de l’association aide souvent à comprendre ce qui s’est passé.
