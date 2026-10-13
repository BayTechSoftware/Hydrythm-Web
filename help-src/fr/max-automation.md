---
title: Scènes sur Cora Max
description: Créez, lancez, modifiez et supprimez des scènes sur Cora Max, depuis Réglages → Automatisations ou une tuile de scène sur le tableau de bord.
section: Cora Max
reviewed: 2026-10-13
order: 9
group: Alerts and automation
twin: mobile-automation
---

Une **scène** est un ensemble enregistré d’actions sur l’équipement qui s’exécutent ensemble, soit pendant une durée fixe, soit jusqu’à ce que vous l’arrêtiez. Vous pouvez créer, lancer et modifier des scènes sur Cora Max. Les scènes créées sur votre téléphone et sur Cora Max sont les mêmes scènes. Les règles d’automatisation (du type « quand ceci arrive, fais cela ») se configurent sur votre téléphone. Plus de détails dans [Scènes et automatisations](/help/mobile-automation).

![La liste des scènes sur Cora Max, avec une puce de filtre par aquarium et un bouton Nouvelle scène](img/max-automation.webp "La liste des scènes, filtrée par aquarium. Tant qu’il n’y a aucune scène, elle l’indique et propose Nouvelle scène.")

## Où trouver les scènes

**Réglages → Automatisations** ouvre **Scènes**, la liste de toutes les scènes de tous vos aquariums. Si vous avez plusieurs aquariums, il y a une puce de filtre pour chacun, plus **Tous les aquariums**.

Touchez une scène pour la modifier, ou touchez **Nouvelle scène** pour en créer une. Si vous avez plusieurs aquariums et qu’aucun filtre n’est choisi, Cora Max demande **Pour quel aquarium est cette scène ?**

## Créer une scène

![Un formulaire Nouvelle scène vide sur Cora Max](img/max-scene-builder.webp "Une nouvelle scène : un nom, Permanente ou Minutée, Demander avant d’exécuter, puis Ajouter une étape.")

1. Tapez un **Nom de la scène**.
2. Touchez **Ajouter une étape** et choisissez ce que fait l’étape. Vous ne voyez que les types d’équipement de cet aquarium :
   - **Prise Apex** : mettre une prise Neptune Apex sur **ON**, **OFF** ou **AUTO**.
   - **Contrôler un équipement Red Sea** : par exemple **ReefDose : doser maintenant**, **ReefDose : définir la dose quotidienne**, **ReefRun : définir la vitesse de la pompe**, **ATO : démarrer un remplissage manuel** ou **ReefMat : avancer le rouleau**.
   - **Contrôler une pompe de brassage** : régler le débit ou le mode de vague d’une pompe Jecod, l’allumer ou l’éteindre, ou **Mettre en pause pour le nourrissage**.
   - **Démarrer une alimentation Gyre** : mettre en pause une Gyre Maxspect pour le nourrissage. Elle redémarre toute seule.
   - **GHL** : une pause nourrissage, l’entretien, un changement d’eau, une scène d’éclairage et d’autres commandes du contrôleur.
   - **HYDROS** : un mode, un niveau de sortie, une dose, ou **HYDROS : retour au programme**.
3. Ajoutez d’autres étapes de la même façon. Vous pouvez les réordonner ou les retirer. Une étape que cet écran ne peut pas modifier indique **Non modifiable ici**. Modifiez-la sur votre téléphone.
4. Choisissez combien de temps elle dure. **Minutée** tourne pendant les minutes réglées dans **Durée (minutes)**. **Permanente** tourne jusqu’à ce que vous l’arrêtiez.
5. Laissez **Demander avant d’exécuter** activé, sauf si vous êtes sûr que la scène ne touche jamais à quelque chose qui mérite une vérification.
6. Touchez **Enregistrer**.

:::note Les doses dans une scène
Une tête Neptune DŌS ne peut jamais être une étape de scène. Une étape **ReefDose : doser maintenant** le peut, et elle a son propre **Max par dose (ml)**. Laissez-le vide pour 10 mL. Une dose au-dessus de ce plafond est refusée, jamais réduite. Gardez **Demander avant d’exécuter** activé pour toute scène qui dose.
:::

:::note Beta
**Beta.** Maxspect, GHL et HYDROS sont en Beta et ne sont ouverts qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le [support](/support.html).
:::

## Lancer une scène

Les scènes apparaissent comme des tuiles sur le tableau de bord. Touchez **Lancer** pour en démarrer une.

Si la scène demande avant de s’exécuter, Cora Max liste d’abord ce qu’elle va faire, une ligne par étape. Lisez la liste, puis lancez la scène ou annulez.

Pendant qu’une scène minutée tourne, sa tuile compte à rebours jusqu’à la fin et affiche **Arrêter** si vous voulez la terminer plus tôt. La tuile d’une scène permanente l’indique en cours jusqu’à ce que vous touchiez **Arrêter**. Quand une scène se termine ou que vous l’arrêtez, la tuile affiche **Restauration…** pendant que Cora remet l’équipement comme avant.

Lancer ou arrêter une scène passe par Cora Cloud, comme toute autre commande. Vous trouverez le résultat dans [Activité](/help/max-activity).

Les scènes ne peuvent pas être lancées à la voix sur Cora Max. Utilisez la tuile, **Réglages → Automatisations**, ou votre téléphone.

Si une scène refuse de se lancer ou de s’arrêter, consultez [Résolution de problèmes](/help/troubleshooting).

:::note Le verrouillage enfant couvre aussi les scènes
Tant que le [verrouillage enfant](/help/max-settings#child-lock) a verrouillé l’écran, vous ne pouvez pas lancer, arrêter ni modifier une scène depuis cet écran, comme pour toutes les autres commandes.
:::

## Modifier ou supprimer une scène

Pour changer une scène, ouvrez-la depuis **Réglages → Automatisations** ou faites un appui long sur sa tuile dans le tableau de bord. Changez ce qu’il faut et touchez **Enregistrer**. Pour la retirer, touchez **Supprimer la scène**. C’est irréversible.

:::note Un Cora Max plus ancien peut lancer une scène mais pas la modifier
Les anciennes versions de Cora Max affichent et lancent toujours toutes les scènes, mais ne peuvent pas en changer une. Mettez Cora Max à jour ([Mises à jour et récupération](/help/max-updates)), ou modifiez la scène sur votre téléphone.
:::
