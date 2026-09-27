---
title: Résolution de problèmes
description: Les mesures se sont arrêtées, un appareil est hors ligne, les alertes ne se ferment pas, ou quelque chose semble anormal. Commencez ici.
section: Help
reviewed: 2026-09-27
order: 1
---

Commencez par le symptôme.

## Un widget n’affiche aucune valeur

Parcourez cette liste :

1. **Vérifiez l’ancienneté sur les widgets voisins.** Si tout est périmé, le problème vient de la connexion, pas du paramètre.
2. **Ouvrez l’onglet Appareils.** Un appareil inaccessible l’indique sur sa ligne.
3. **Vérifiez l’attribution de l’aquarium.** Un appareil qui rapporte sur le mauvais aquarium ressemble exactement à un appareil qui ne rapporte pas. Ouvrez l’appareil et confirmez son aquarium.
4. **Vérifiez que la source existe.** Rien ne rapporte le phosphate à moins que vous ayez un équipement qui le mesure ou que vous ne le saisissiez à la main.

## Une mesure est périmée

Le badge d’ancienneté vous dit la vérité : rien de nouveau n’est arrivé.

- **Les paramètres saisis à la main** deviennent périmés quand aucune mesure n’a été entrée. Saisissez-en une.
- **Les mesures d’équipement** qui deviennent périmées signifient que l’appareil a arrêté de rapporter ; vérifiez sa ligne dans **Appareils**.
- **Certains équipements sont censés être lents.** Un titrateur qui mesure toutes les heures affichera normalement `1h`. Ce n’est pas un défaut.

## Un appareil est inaccessible

Généralement le réseau.

1. L’équipement est-il alimenté et fonctionne-t-il dans sa propre application ?
2. Est-il sur le même réseau sur lequel il a été ajouté ?
3. Votre routeur a-t-il changé (nouveau matériel, nouveau nom de réseau, isolation du réseau invité) ?

L’équipement qui se connecte via votre réseau local doit être accessible sur ce réseau. L’équipement qui se connecte via un compte du fabricant n’en a pas besoin, mais a besoin que ce compte reste valide.

## Un appareil indique que la connexion a été refusée

Le fabricant a rejeté la connexion enregistrée. Presque toujours parce que vous avez changé votre mot de passe chez lui.

Ouvrez la ligne de l’appareil et reconnectez-vous.

## L’appairage d’un Cora Max échoue

Si l’ajout d’un Cora Max s’arrête en cours de route, Cora Mobile indique quelle étape a échoué et pourquoi, avec **Annuler** et **Réessayer** en dessous.

- *« Votre téléphone n’a pas pu atteindre le Cora Max sur votre Wi-Fi. »* Mettez votre téléphone et le Cora Max sur le même réseau Wi-Fi. Sur iPhone, vérifiez aussi que Cora a l’accès au réseau local : **Réglages → Accès aux appareils** vous y amène (voir [Réglages](/help/mobile-settings)). Puis touchez **Réessayer**.
- *« Le Cora Max n’a pas accepté cette session d’appairage. »* Réessayer n’aidera pas. Fermez l’écran et recommencez depuis **Appareils → Ajouter un appareil**.

Pour tout autre message, touchez **Réessayer**.

## Cora Max affiche des données anciennes

Vérifiez la pastille d’état dans la barre supérieure. **En ligne** et **Cloud** sont tous deux en bon état : avec plus d’un Cora, l’écran qui ne fait pas la collecte affiche **Cloud**, et ses mesures sont tout aussi actuelles. **Obsolète** ou **Hors ligne** signifie que l’écran a perdu sa source et affiche les dernières données qu’il a reçues (comportement correct, mais pas actuel).

- Vérifiez le Wi-Fi sous **Réglages → Cora Max → Réseau**
- Vérifiez que le réseau lui-même fonctionne
- Si la pastille affiche **En ligne** ou **Cloud** et que les données sont toujours anciennes, le problème est en amont : vérifiez le même aquarium sur votre téléphone

## Une alerte ne se ferme pas

Une alerte se ferme quand la mesure revient dans la plage. Si elle ne se ferme pas :

- **La mesure est réellement hors plage.** Regardez l’historique du widget.
- **Le seuil est incorrect pour votre aquarium.** Voir [Alertes et seuils](/help/mobile-alerts).
- **La source est en cause.** Une sonde qui a besoin d’un étalonnage rapporte un chiffre qui est réellement hors plage. Corrigez la sonde plutôt que le seuil.

## Deux sources ne sont pas d’accord

C’est Cora qui fonctionne, pas Cora qui échoue. Quand votre sonde et votre test en kit ne sont pas d’accord, c’est un fait réel sur votre système.

Un résultat ICP est un troisième avis utile ici, mais il ne règle pas le débat : les laboratoires diffèrent les uns des autres, et la manipulation et le transport d’un échantillon influencent le résultat. Deux tests d’accord valent bien plus qu’un seul.

Généralement la sonde a besoin d’un étalonnage ; parfois le test en kit est ancien. Étalonnez la sonde, refaites le test avec du réactif frais, et comparez les deux dans les mêmes conditions. Un [résultat ICP](/help/mobile-icp-health) ajoute un troisième point de données à cette comparaison.

## Je ne reçois pas de notifications

1. **Réglages → Notifications** : vérifiez que cette catégorie est autorisée à envoyer des notifications
2. Vérifiez les permissions de notification de votre téléphone pour Cora
3. Rappelez-vous que le briefing quotidien est délibérément silencieux les jours où rien n’a changé

## Établir pourquoi quelque chose a changé

**Réglages → Activité** liste chaque changement de prise, nourrissage, dosage et fiche, avec ce qui l’a demandé : Cora Mobile, un écran Cora, la voix, l’Assistant, une règle d’automatisation, un bouton intelligent ou votre compte.

## Mon tableau de bord semble anormal après une modification

Chargez une mise en page enregistrée : **Mes tableaux de bord**, puis choisissez-en une.

Si vous n’en avez pas enregistré, reconstruisez la mise en page puis enregistrez-la comme mise en page. À partir de ce moment, y revenir tient en un seul geste.

Dans les deux cas, les mesures, l’historique et les entrées de journal sont stockés séparément de la mise en page, donc rien derrière le tableau de bord n’est perdu.

## « Les mesures Red Sea ont arrêté de se mettre à jour »

**Ce que cela signifie :** Aucun appareil sur le réseau de cet aquarium n’interroge actuellement votre équipement Red Sea, donc les mesures à l’écran n’ont pas été actualisées.

**Que faire :**
1. Ouvrez **Réglages → Cora Max principal** et vérifiez qu’un Cora Max est réglé (ou que **Tout appareil actif (automatique)** est choisi).
2. Ouvrez l’aquarium sur un appareil qui est sur le même Wi-Fi que le matériel Red Sea.
3. Confirmez que l’équipement Red Sea est alimenté et en ligne dans sa propre application.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe : rien n’a été envoyé »

**Ce que cela signifie :** Une commande vers une pompe Jecod ou Jebao n’a jamais quitté l’application, généralement parce que la pompe est éteinte ou hors de son réseau.

**Que faire :**
1. Vérifiez que la pompe est allumée.
2. Vérifiez qu’elle est sur le même réseau sur lequel elle a été ajoutée.
3. Touchez **Réessayer**.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe par Bluetooth. Approchez-vous et réessayez. »

**Ce que cela signifie :** Un appareil Jecod uniquement Bluetooth est hors de portée de votre téléphone.

**Que faire :**
1. Rapprochez-vous de la pompe.
2. Touchez **Réessayer**.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe de brassage. Aucun nourrissage n’a été démarré. »

**Ce que cela signifie :** Une pompe de brassage Maxspect (intégration bêta) n’a pas répondu quand Cora a essayé d’y démarrer le mode nourrissage.

**Que faire :**
1. Vérifiez que la pompe de brassage est allumée et sur son réseau.
2. Touchez **Réessayer**.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre cette pompe de brassage. Son programme n’a pas été modifié. »

**Ce que cela signifie :** L’envoi d’un programme à une pompe de brassage Maxspect (intégration bêta) n’a pas réussi à l’atteindre.

**Que faire :**
1. Vérifiez que votre téléphone ou Cora Max est sur le réseau de la pompe de brassage.
2. Touchez **Réessayer** depuis l’écran de programmation.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Impossible d’atteindre l’Apex : rien n’a changé » / « rien n’a été dosé »

**Ce que cela signifie :** Un Neptune Apex, Trident, ou une tête DŌS n’a pas répondu à une commande ou une demande de dosage.

**Que faire :**
1. Ouvrez la propre application de l’Apex et confirmez qu’il est en ligne.
2. Vérifiez la connectivité réseau sur l’appareil que vous utilisez.
3. Touchez **Réessayer**.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Ceci n’a pas pu être envoyé : aucun appareil sur cet aquarium ne peut l’envoyer »

**Ce que cela signifie :** Aucun appareil Cora sur cet aquarium n’a les informations de connexion Apex nécessaires pour exécuter la commande, ou celui qui les a est hors ligne.

**Que faire :**
1. Ajoutez les informations de l’Apex dans **Réglages** sur un appareil actuellement en ligne, ou
2. Réglez un autre Cora Max fonctionnel comme **Cora Max principal** pour cet aquarium.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## Un Cora Max secondaire affiche « Cora principal hors ligne »

**Ce que cela signifie :** La tablette principale de cet aquarium est passée hors ligne, donc cet écran secondaire affiche les dernières données qu’il a reçues plutôt que des données en direct.

**Que faire :**
1. Vérifiez l’alimentation et le Wi-Fi de la tablette principale.
2. Attendez qu’elle se reconnecte, ou changez le **Cora Max principal** pour un appareil actuellement en ligne.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## « Appareil hors ligne. Affichage du dernier état connu. »

**Ce que cela signifie :** Gestion normale du hors ligne : l’appareil a arrêté de rapporter, et Cora affiche les dernières valeurs qu’il avait plutôt que de prétendre qu’elles sont actuelles.

**Que faire :**
1. Vérifiez la propre connexion réseau de l’appareil.
2. Traitez les valeurs affichées comme non actuelles jusqu’à ce que la ligne n’indique plus hors ligne.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## Certains réglages ReefBeat sont grisés ou absents

**Ce que cela signifie :** C’est voulu, pas un défaut. Les réglages propres à l’appareil (par opposition aux mesures) ne s’ouvrent que quand votre téléphone est sur le même réseau que l’appareil lui-même ; loin de ce réseau, seules les mesures s’affichent.

**Que faire :**
1. Rendez-vous sur le Wi-Fi de l’aquarium pour changer ces réglages.
2. Les mesures et l’historique fonctionnent toujours normalement loin de l’aquarium.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## « Impossible d’atteindre Cora. Vérifiez votre Wi-Fi ou vos données mobiles, puis réessayez. »

**Ce que cela signifie :** Votre téléphone n’a aucune connexion utilisable à Cora Cloud lors de la connexion. Cela concerne la propre connectivité de votre téléphone, pas votre équipement d’aquarium.

**Que faire :**
1. Vérifiez que votre téléphone a une connexion Wi-Fi ou données mobiles qui fonctionne.
2. Essayez un autre réseau si disponible.
3. **Réessayer**.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Tout est soudainement dans la mauvaise langue

**Ce que cela signifie :** La langue du compte a été changée depuis n’importe quel appareil. La langue est un réglage unique pour tout le compte, pas par appareil.

**Que faire :**
1. Ouvrez **Réglages → Langue** sur l’une des deux applications.
2. Remettez-la si elle a été changée par erreur ; le changement s’applique partout instantanément.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une alerte ou un rapport ancien est toujours dans une autre langue après le changement

**Ce que cela signifie :** C’est normal, pas un bug. Cora ne retraduit pas le contenu déjà généré ; seules les nouvelles alertes, rapports et briefings suivent la nouvelle langue.

**Que faire :**
1. Rien à corriger. Attendez le nouveau contenu, qui utilisera la langue actuelle.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une alerte ne cesse pas de notifier même après l’avoir acquittée

**Ce que cela signifie :** Confusion entre **Ignorer** (ferme l’alerte définitivement) et **Reporter** (la met en sourdine temporairement, jusqu’à une semaine).

**Que faire :**
1. Si vous comprenez et acceptez la condition, utilisez **Ignorer**.
2. Si vous voulez seulement du calme pour un temps, utilisez **Reporter** et choisissez une durée.

**Toujours pas de solution ?** Voir [Alertes et seuils](/help/mobile-alerts), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un dosage s’est arrêté en cours de route et une alerte « reprise » est apparue

**Ce que cela signifie :** La tête DŌS a perdu le contact en cours de dosage, donc Cora vous le dit délibérément plutôt que de supposer que le dosage complet a été versé.

**Que faire :**
1. Ouvrez l’alerte et vérifiez combien a réellement été dosé avant l’arrêt.
2. Reprenez ou ajustez le dosage selon cette quantité, pas la quantité initialement programmée.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’aquarium et de l’appareil.

## Une scène créée sur le téléphone n’apparaît pas comme modifiable sur Cora Max

**Ce que cela signifie :** Modifier des scènes directement sur la tablette est une capacité plus récente de Cora Max. Un micrologiciel plus ancien peut encore exécuter des scènes créées sur le téléphone, mais pas les modifier là.

**Que faire :**
1. Mettez à jour Cora Max, ou
2. Continuez à modifier cette scène depuis le téléphone ; elle continuera de s’exécuter sur la tablette dans les deux cas.

**Toujours pas de solution ?** Voir [Mises à jour et récupération](/help/max-updates), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant répond à propos du mauvais aquarium

**Ce que cela signifie :** Aucun aquarium n’a été choisi avant de poser la question, ou le mauvais aquarium est actuellement actif.

**Que faire :**
1. Choisissez d’abord l’aquarium que vous voulez dire.
2. Posez la question à nouveau.

**Toujours pas de solution ?** Voir [L’Assistant](/help/mobile-assistant), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Assistant refuse de répondre, ou affiche à nouveau un écran de consentement

**Ce que cela signifie :** « Autoriser Cora Assistant à utiliser les données de l’aquarium enregistrées » a été désactivé, donc il n’a rien à partir de quoi répondre.

**Que faire :**
1. Touchez **Accepter et continuer** sur l’écran de consentement pour le réactiver.

**Toujours pas de solution ?** Voir [L’Assistant](/help/mobile-assistant), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un résultat ICP de laboratoire ou envoyé par e-mail n’est jamais apparu

**Ce que cela signifie :** Faire entrer un résultat dans Cora nécessite un aquarium choisi pour lui, et parfois un expéditeur reconnu, avant qu’il ne s’attache où que ce soit.

**Que faire :**
1. Vérifiez l’indice d’intégration affiché la première fois que vous envoyez un résultat à Cora.
2. Confirmez à quel aquarium le résultat doit s’attacher quand on vous le demande.
3. Assurez-vous que l’e-mail a été envoyé depuis l’adresse que vous avez utilisée pour l’envoyer auparavant, si vous en avez déjà envoyé un.

**Toujours pas de solution ?** Voir [Rapports ICP et de santé](/help/mobile-icp-health), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une notification ICP envoyée par e-mail ne nomme aucun laboratoire

**Ce que cela signifie :** Un problème connu où la notification push « choisir l’aquarium » manque le nom du laboratoire. Cela a été corrigé dans les versions actuelles.

**Que faire :**
1. Assurez-vous que Cora Mobile est mis à jour vers la dernière version.
2. Le résultat lui-même n’est pas affecté ; seul le texte de la notification manquait un nom.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Un widget affiche les mauvaises unités

**Ce que cela signifie :** C’est le réglage des unités d’affichage de l’aquarium, pas un problème de données. Les valeurs sont stockées de la même façon quelle que soit la façon dont elles sont affichées.

**Que faire :**
1. Ouvrez **Réglages** pour cet aquarium et vérifiez ses unités d’affichage.
2. Changez-les là ; chaque téléphone et Cora Max affichant cet aquarium se met à jour pour correspondre.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Une jauge ou un seuil semble différent après un changement d’unités d’affichage

**Ce que cela signifie :** C’est normal. Les jauges, tuiles et historiques se redessinent dans l’unité que vous avez choisie ; les valeurs sous-jacentes n’ont pas changé.

**Que faire :**
1. Rien à corriger ; c’est purement cosmétique.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Cora Max ne se reconnecte pas immédiatement après une coupure Wi-Fi

**Ce que cela signifie :** Après avoir perdu sa connexion, Cora Max attend un peu plus longtemps avant chaque nouvelle tentative plutôt que de marteler le réseau, ralentissant jusqu’à environ une minute avant de réessayer.

**Que faire :**
1. Attendez environ une minute après le retour de votre réseau.
2. S’il ne s’est toujours pas reconnecté après cela, vérifiez le Wi-Fi sous **Réglages → Réseau**.

**Toujours pas de solution ?** Voir [L’écran d’accueil de Cora Max](/help/max-tour), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Renommer un Cora Max depuis le téléphone ne change pas ce que la tablette affiche

**Ce que cela signifie :** Le nom que vous réglez depuis le téléphone est une étiquette au niveau du compte pour cet appareil. Le nom affiché sur la tablette elle-même pendant l’appairage peut être une chose différente.

**Que faire :**
1. Vérifiez quel « nom » vous regardez : celui de votre liste d’appareils sur le téléphone, ou celui de l’écran d’appairage propre à la tablette.
2. Renommez depuis la liste d’appareils du téléphone si c’est l’étiquette du compte que vous voulez changer.

**Toujours pas de solution ?** Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)** avec le nom de l’appareil.

## Je ne trouve pas où désactiver le mot d’activation sur Cora Max

**Ce que cela signifie :** Le commutateur du mot d’activation se trouve sous **Audio**, pas sous le groupe de réglages Cora Assistant, ce qui surprend la plupart des gens.

**Que faire :**
1. Allez dans **Réglages → Audio → Écoute du mot d’activation**.
2. Désactivez-le ; vous pouvez toujours toucher l’icône Cora pour démarrer une session vocale.

**Toujours pas de solution ?** Voir [Réglages sur Cora Max](/help/max-settings), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Le verrouillage enfant empêche tout le monde d’accéder à Réglages

**Ce que cela signifie :** C’est le fonctionnement prévu. Le verrouillage enfant verrouille l’écran tactile et les commandes vocales après une durée définie sans contact ; les mesures continuent de se mettre à jour en dessous.

**Que faire :**
1. Appuyez sur **Volume haut** ou **Volume bas** trois fois en deux secondes, ou
2. Maintenez cinq doigts dans le coin supérieur droit de l’écran pendant dix secondes.

**Toujours pas de solution ?** Voir [La voix sur Cora Max](/help/max-voice), ou écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**.

## Toujours bloqué

Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**. Dites-nous quel aquarium, quel écran, et ce que vous attendiez de voir ; cela vous permet d’obtenir une réponse utile plus vite.
