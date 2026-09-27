---
title: Résolution de problèmes
description: Les mesures ne bougent plus, un appareil est hors ligne, une alerte ne se ferme pas, ou quelque chose semble anormal. Commencez ici.
section: Help
reviewed: 2026-09-27
order: 1
---

Cherchez ce que vous constatez dans la liste ci-dessous.

## Un widget n’affiche aucune valeur

Vérifiez dans cet ordre :

1. **Regardez l’âge des mesures sur les widgets voisins.** Si tout est ancien, c’est la connexion qui pose problème, pas le paramètre.
2. **Ouvrez l’onglet Appareils.** Un appareil injoignable le signale sur sa ligne.
3. **Vérifiez l’aquarium de l’appareil.** Un appareil qui envoie ses mesures au mauvais aquarium ressemble en tout point à un appareil qui n’envoie rien. Ouvrez l’appareil et vérifiez son aquarium.
4. **Vérifiez que la source existe.** Le phosphate, par exemple, ne s’affiche que si un équipement le mesure ou si vous le saisissez à la main.

## Une mesure est ancienne

L’âge affiché est exact : rien de nouveau n’est arrivé.

- **Un paramètre saisi à la main** vieillit si vous n’avez pas saisi de nouvelle mesure. Saisissez-en une.
- **Une mesure d’équipement** qui vieillit veut dire que l’appareil n’envoie plus rien. Regardez sa ligne dans **Appareils**.
- **Certains équipements sont lents par nature.** Un titrateur qui mesure toutes les heures affiche normalement `1h`. Ce n’est pas une panne.

## Un appareil est injoignable

C’est en général le réseau.

1. L’équipement est-il allumé, et fonctionne-t-il dans sa propre application ?
2. Est-il toujours sur le réseau où vous l’avez ajouté ?
3. Votre box a-t-elle changé (nouveau matériel, nouveau nom de réseau, isolation du réseau invité) ?

Un équipement qui passe par votre réseau local doit être joignable sur ce réseau. Un équipement qui passe par un compte du fabricant n’en a pas besoin, mais ce compte doit rester valide.

## Un appareil indique que la connexion a été refusée

Le fabricant a refusé la connexion enregistrée. C’est presque toujours parce que vous avez changé votre mot de passe chez lui.

Ouvrez la ligne de l’appareil et reconnectez-vous.

## L’appairage d’un Cora Max échoue

Si l’ajout d’un Cora Max s’arrête en cours de route, Cora Mobile indique l’étape qui a échoué et pourquoi, avec **Annuler** et **Réessayer** en dessous.

- *« Votre téléphone n’a pas pu atteindre le Cora Max sur votre Wi-Fi. »* Mettez votre téléphone et Cora Max sur le même Wi-Fi. Sur iPhone, vérifiez aussi que Cora a accès au réseau local. **Réglages → Accès aux appareils** vous y amène (voir [Réglages](/help/mobile-settings)). Touchez ensuite **Réessayer**.
- *« Le Cora Max n’a pas accepté cette session d’appairage. »* Réessayer ne servira à rien. Fermez l’écran et recommencez depuis **Appareils → Ajouter un appareil**.

Pour tout autre message, touchez **Réessayer**.

## Cora Max affiche des données anciennes

Regardez l’étiquette d’état dans la barre du haut. **En ligne** et **Cloud** veulent dire que tout va bien. Si vous avez plusieurs Cora, l’écran qui ne récupère pas les mesures affiche **Cloud**, et ses mesures sont tout aussi à jour. **Obsolète** ou **Hors ligne** veut dire que l’écran a perdu sa source et affiche les dernières données reçues. C’est le comportement prévu, mais ces données ne sont pas à jour.

- Vérifiez le Wi-Fi dans **Réglages → Réglages Cora Max → Wi-Fi**
- Vérifiez que le réseau lui-même fonctionne
- Si l’étiquette affiche **En ligne** ou **Cloud** et que les données restent anciennes, le problème vient d’avant Cora Max. Regardez le même aquarium sur votre téléphone

## Une alerte ne se ferme pas

Une alerte se ferme quand la mesure revient dans sa plage. Si elle ne se ferme pas :

- **La mesure est vraiment hors plage.** Regardez l’historique du widget.
- **Le seuil ne convient pas à votre aquarium.** Voir [Alertes et seuils](/help/mobile-alerts).
- **La source est en cause.** Une sonde à étalonner envoie un chiffre qui est bien hors plage. Corrigez la sonde, pas le seuil.

## Deux sources ne sont pas d’accord

Cora fait son travail en vous le signalant. Quand votre sonde et votre test en kit ne sont pas d’accord, c’est un vrai constat sur votre système.

Un résultat ICP donne un troisième avis utile, mais il ne tranche pas tout. Les laboratoires ne donnent pas tous les mêmes résultats, et la manipulation et le transport de l’échantillon jouent sur le résultat. Deux tests qui concordent valent bien plus qu’un seul.

Le plus souvent, la sonde a besoin d’un étalonnage. Parfois, c’est le test en kit qui est trop vieux. Étalonnez la sonde, refaites le test avec un réactif neuf et comparez les deux dans les mêmes conditions. Un [résultat ICP](/help/mobile-icp-health) apporte un troisième point de comparaison.

## Je ne reçois pas de notifications

1. Dans **Réglages → Notifications**, vérifiez que cette catégorie a le droit d’envoyer des notifications
2. Vérifiez l’autorisation des notifications de votre téléphone pour Cora
3. Le briefing du jour reste volontairement silencieux quand rien n’a changé

## Comprendre pourquoi quelque chose a changé

**Réglages → Activité** liste chaque changement de prise, nourrissage, dosage et prise connectée, avec son origine : Cora Mobile, un écran Cora, la voix, l’Assistant, une règle d’automatisation, un bouton intelligent ou votre compte.

## Mon tableau de bord semble anormal après une modification

Chargez une disposition enregistrée : ouvrez **Mes tableaux de bord** et choisissez-en une.

Si vous n’en avez pas, refaites la disposition, puis enregistrez-la. Ensuite, un seul geste suffira pour y revenir.

Dans tous les cas, les mesures, l’historique et le journal sont stockés à part de la disposition. Vous ne perdez donc rien de ce qu’affiche le tableau de bord.

## « Les mesures Red Sea ont arrêté de se mettre à jour »

Aucun appareil sur le réseau de cet aquarium n’interroge votre équipement Red Sea en ce moment. Les mesures affichées ne sont donc plus mises à jour.

1. Ouvrez **Réglages → Cora Max principal** et vérifiez qu’un Cora Max est choisi, ou que **Tout appareil actif (automatique)** est sélectionné.
2. Ouvrez l’aquarium sur un appareil connecté au même Wi-Fi que le matériel Red Sea.
3. Vérifiez dans l’application Red Sea que l’équipement est allumé et en ligne.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe : rien n’a été envoyé »

Une commande pour une pompe Jecod ou Jebao n’est jamais partie de votre appareil. En général, la pompe est éteinte ou hors de son réseau.

1. Vérifiez que la pompe est allumée.
2. Vérifiez qu’elle est toujours sur le réseau où vous l’avez ajoutée.
3. Touchez **Réessayer**.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe par Bluetooth. Approchez-vous et réessayez. »

Une pompe Jecod uniquement Bluetooth est hors de portée de votre téléphone.

1. Rapprochez-vous de la pompe.
2. Touchez **Réessayer**.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe de brassage. Aucun nourrissage n’a été démarré. »

Une pompe de brassage Maxspect (intégration en bêta) n’a pas répondu quand Cora a voulu y lancer le mode nourrissage.

1. Vérifiez que la pompe de brassage est allumée et connectée à son réseau.
2. Touchez **Réessayer**.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe de brassage. Son programme n’a pas été modifié. »

Le programme envoyé à une pompe de brassage Maxspect (intégration en bêta) n’a pas pu l’atteindre.

1. Vérifiez que votre téléphone ou Cora Max est sur le même réseau que la pompe de brassage.
2. Touchez **Réessayer** depuis l’écran du programme.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre l’Apex : rien n’a changé » / « rien n’a été dosé »

Un Neptune Apex, un Trident ou une tête DŌS n’a pas répondu à une commande ou à une demande de dosage.

1. Ouvrez l’application de l’Apex et vérifiez qu’il est en ligne.
2. Vérifiez la connexion réseau de l’appareil que vous utilisez.
3. Touchez **Réessayer**.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Ceci n’a pas pu être envoyé : aucun appareil sur cet aquarium ne peut l’envoyer »

Aucun appareil Cora de cet aquarium n’a les identifiants Apex nécessaires pour exécuter la commande, ou celui qui les a est hors ligne.

1. Ajoutez les informations de l’Apex dans **Réglages** sur un appareil en ligne.
2. Ou choisissez un autre Cora Max qui fonctionne comme **Cora Max principal** de cet aquarium.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## Un Cora Max secondaire affiche « Cora principal hors ligne »

Le Cora Max principal de cet aquarium est hors ligne. L’écran secondaire affiche donc les dernières données reçues, et non des données en direct.

1. Vérifiez l’alimentation et le Wi-Fi du Cora Max principal.
2. Attendez qu’elle se reconnecte, ou choisissez comme **Cora Max principal** un appareil en ligne.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## « Appareil hors ligne. Affichage du dernier état connu. »

C’est le comportement normal hors ligne. L’appareil n’envoie plus rien, et Cora affiche ses dernières valeurs sans les faire passer pour actuelles.

1. Vérifiez la connexion réseau de l’appareil.
2. Considérez que les valeurs affichées ne sont pas à jour tant que la ligne indique hors ligne.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## Certains réglages ReefBeat sont grisés ou absents

C’est normal. Les réglages propres à l’appareil (à la différence des mesures) ne s’ouvrent que si votre téléphone est sur le même réseau que l’appareil. Loin de ce réseau, seules les mesures s’affichent.

1. Connectez-vous au Wi-Fi de l’aquarium pour changer ces réglages.
2. Loin de l’aquarium, les mesures et l’historique fonctionnent toujours normalement.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## « Impossible d’atteindre Cora. Vérifiez votre Wi-Fi ou vos données mobiles, puis réessayez. »

Au moment de la connexion, votre téléphone n’a aucun accès utilisable à Cora Cloud. Le problème vient de la connexion de votre téléphone, pas de l’équipement de votre aquarium.

1. Vérifiez que votre téléphone a une connexion Wi-Fi ou données mobiles qui fonctionne.
2. Essayez un autre réseau si vous en avez un.
3. Touchez **Réessayer**.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Tout est soudain dans une autre langue

Quelqu’un a changé la langue du compte depuis un appareil. La langue est un seul réglage pour tout le compte, pas un réglage par appareil.

1. Ouvrez **Réglages → Langue**, sur Cora Mobile ou sur Cora Max.
2. Remettez la bonne langue si elle a été changée par erreur. Le changement s’applique partout en quelques instants.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une ancienne alerte ou un ancien rapport reste dans l’autre langue

C’est normal. Cora ne retraduit pas ce qui existe déjà. Seuls les nouvelles alertes, les nouveaux rapports et les briefings suivants sont dans la nouvelle langue.

1. Il n’y a rien à corriger. Le nouveau contenu sera dans la langue actuelle.

Si vous avez encore une question, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une alerte continue de vous notifier après que vous l’avez traitée

**Reporter** et **Ignorer** sur Cora Max ne font taire que ce Cora Max. Votre téléphone continue de recevoir des notifications tant que la mesure reste hors plage.

1. Pour être prévenu moins souvent sur votre téléphone, ouvrez la règle d’alerte dans Cora Mobile et choisissez un **Délai entre les alertes** plus long (jusqu’à 1 semaine).
2. Si le seuil ne convient pas à votre aquarium, modifiez le seuil lui-même.

Si le problème continue, lisez [Alertes et seuils](/help/mobile-alerts) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un dosage s’est arrêté en cours de route et une alerte de reprise est apparue

La tête DŌS a perdu le contact pendant le dosage. Cora vous prévient, sans supposer que tout a été versé.

1. Ouvrez l’alerte et regardez la quantité réellement dosée avant l’arrêt.
2. Reprenez ou ajustez le dosage à partir de cette quantité, et non de la quantité prévue au départ.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’aquarium et de l’appareil.

## Une scène créée sur le téléphone ne se modifie pas sur Cora Max

La modification des scènes sur Cora Max est arrivée dans une version récente. Avec un micrologiciel plus ancien, Cora Max peut lancer les scènes créées sur le téléphone, mais pas les modifier.

1. Mettez Cora Max à jour.
2. Ou continuez de modifier cette scène sur le téléphone. Elle se lancera sur Cora Max dans les deux cas.

Si le problème continue, lisez [Mises à jour et récupération](/help/max-updates) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant parle du mauvais aquarium

Aucun aquarium n’était choisi quand vous avez posé la question, ou le mauvais aquarium était sélectionné.

1. Choisissez d’abord l’aquarium qui vous intéresse.
2. Reposez votre question.

Si le problème continue, lisez [L’Assistant](/help/mobile-assistant) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant refuse de répondre, ou affiche de nouveau un écran d’accord

L’option « Autoriser Cora Assistant à utiliser les données de l’aquarium enregistrées » a été désactivée. L’Assistant n’a donc aucune donnée pour vous répondre.

1. Touchez **Accepter et continuer** sur l’écran d’accord pour la réactiver.

Si le problème continue, lisez [L’Assistant](/help/mobile-assistant) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un résultat ICP de laboratoire ou envoyé par e-mail n’apparaît pas

Pour qu’un résultat arrive dans Cora, il faut lui choisir un aquarium, et parfois que l’expéditeur soit reconnu.

1. Relisez l’aide qui s’affiche la première fois que vous envoyez un résultat à Cora.
2. Quand Cora vous le demande, indiquez à quel aquarium rattacher le résultat.
3. Si vous avez déjà envoyé un résultat par e-mail, envoyez le nouveau depuis la même adresse.

Si le problème continue, lisez [Rapports ICP et de santé](/help/mobile-icp-health) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une notification ICP reçue par e-mail ne donne pas le nom du laboratoire

C’est un problème connu : la notification push « choisir l’aquarium » n’indiquait pas le nom du laboratoire. Il est corrigé dans les versions actuelles.

1. Mettez Cora Mobile à jour vers la dernière version.
2. Le résultat lui-même n’est pas touché. Seul le nom manquait dans le texte de la notification.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un widget affiche les mauvaises unités

Ce n’est pas un problème de données, mais le réglage des unités d’affichage de l’aquarium. Les valeurs sont stockées de la même façon, quelle que soit l’unité affichée.

1. Ouvrez les **Réglages** de cet aquarium et vérifiez ses unités d’affichage.
2. Changez-les à cet endroit. Tous les téléphones et Cora Max qui affichent cet aquarium suivent.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une jauge ou un seuil a changé d’aspect après un changement d’unités

C’est normal. Les jauges, les tuiles et l’historique se redessinent dans l’unité choisie. Les valeurs elles-mêmes n’ont pas changé.

1. Il n’y a rien à corriger. Seul l’affichage change.

Si vous avez encore une question, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max ne se reconnecte pas tout de suite après une coupure Wi-Fi

Après une coupure, Cora Max attend un peu plus longtemps entre chaque essai pour ne pas saturer le réseau, jusqu’à environ une minute entre deux essais.

1. Attendez environ une minute après le retour du réseau.
2. S’il n’est toujours pas reconnecté, vérifiez le Wi-Fi dans **Réglages → Réglages Cora Max → Wi-Fi**.

Si le problème continue, lisez [L’écran d’accueil de Cora Max](/help/max-tour) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Renommer un Cora Max depuis le téléphone ne change pas le nom affiché sur Cora Max

Le nom que vous donnez depuis le téléphone est le nom de l’appareil sur votre compte. Le nom affiché par Cora Max pendant l’appairage peut être différent.

1. Vérifiez de quel nom il s’agit : celui de la liste des appareils sur le téléphone, ou celui de l’écran d’appairage de Cora Max.
2. Pour changer le nom sur votre compte, renommez l’appareil depuis la liste des appareils du téléphone.

Si le problème continue, écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** en indiquant le nom de l’appareil.

## Je ne trouve pas comment couper le mot d’activation sur Cora Max

Le réglage du mot d’activation se trouve dans la section **Son et voix**, et non dans les réglages de Cora Assistant, où la plupart des gens le cherchent d’abord.

1. Allez dans **Réglages → Réglages Cora Max → Son et voix → Écoute du mot d’activation**.
2. Désactivez-le. Vous pourrez toujours toucher l’icône Cora pour lancer une session vocale.

Si le problème continue, lisez [Réglages sur Cora Max](/help/max-settings) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Le verrouillage enfant bloque l’accès aux réglages

C’est prévu. Après un certain temps sans contact, le verrouillage enfant empêche quiconque de commander l’équipement depuis cet écran, au toucher comme à la voix. Les mesures continuent de se mettre à jour, et vous pouvez toujours poser des questions à Cora. Pour déverrouiller :

1. Appuyez trois fois sur **Volume haut** ou **Volume bas** en moins de deux secondes.
2. Ou posez cinq doigts dans le coin en haut à droite de l’écran pendant dix secondes.

Si le problème continue, lisez [La voix sur Cora Max](/help/max-voice) ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Toujours bloqué

Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Dites-nous quel aquarium et quel écran sont concernés, et ce que vous vous attendiez à voir. Vous aurez une réponse utile plus vite.
