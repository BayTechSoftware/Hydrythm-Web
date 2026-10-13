---
title: Résolution de problèmes
description: Réparez une mesure périmée, un appareil hors ligne, une commande qui n’est pas passée, un Cora Max qui ne s’associe pas ou une alerte qui ne disparaît pas.
section: Help
reviewed: 2026-10-13
order: 1
---

Trouvez la famille à laquelle appartient votre problème, puis le message ou le symptôme que vous voyez. Les titres entre guillemets sont les mots exacts que Cora vous affiche.

- [Mesures et widgets](#readings-and-widgets)
- [Un appareil ne remonte plus de mesures ou est injoignable](#device-not-reporting)
- [Une commande n’est pas passée](#command-did-not-go-through)
- [Cora Max](#cora-max)
- [Alertes, notifications et briefing quotidien](#alerts-and-notifications)
- [Caméras et surveillance de l’écumeur](#cameras-and-skimmer-watch)
- [Cora Assistant et voix](#cora-assistant-and-voice)
- [Résultats de laboratoire et rapports de santé](#lab-results-and-health-reports)
- [Langue, unités et connexion](#language-units-and-signing-in)

:::note Intégrations Beta
Certaines entrées ci-dessous concernent des intégrations Beta : Maxspect, GHL, HYDROS, Focustronic, EcoTech, Inkbird et les caméras. **Beta.** Ces intégrations sont en Beta et ne sont ouvertes qu’aux utilisateurs Beta. Si vous n’êtes pas un utilisateur Beta, vous ne les verrez pas dans **Ajouter un appareil**. Pour demander l’accès Beta, contactez le support. Plus de détails dans [Fonctions Beta](/help/mobile-beta).
:::

## Mesures et widgets {#readings-and-widgets}

### Un widget n’affiche aucune valeur {#a-widget-shows-no-value}

Vérifiez ces points dans l’ordre.

1. Regardez l’âge sur les widgets voisins. S’ils sont tous anciens aussi, c’est la connexion, pas le paramètre.
2. Ouvrez l’onglet **Appareils**. Si un appareil est injoignable, sa ligne a un point rouge ou l’indique.
3. Vérifiez sur quel aquarium se trouve l’appareil. Un appareil qui transmet au mauvais aquarium ressemble en tout point à un appareil qui ne transmet pas. Ouvrez l’appareil et vérifiez son aquarium.
4. Vérifiez que quelque chose mesure ce paramètre. Rien ne signale les phosphates sauf si vous avez un équipement qui les mesure ou que vous les notez à la main.

### Un widget est grisé {#a-widget-is-grey}

Le gris veut dire que Cora n’évalue pas cette mesure. Il y a trois raisons habituelles.

1. Son alerte est désactivée. Réactivez-la dans l’onglet **Règles** du Centre d’alertes.
2. Elle n’a pas de plage pour la juger. Faites un appui long sur le widget et réglez une plage.
3. La mesure est trop ancienne. Vérifiez l’âge sur le widget, puis notez une nouvelle mesure ou vérifiez l’appareil.

La signification de chaque couleur est dans [Lire votre tableau de bord](/help/mobile-dashboard#colours).

### Une mesure est périmée {#a-reading-is-stale}

L’âge affiché sur le widget est juste. Rien de nouveau n’est arrivé.

- Les paramètres notés à la main deviennent périmés quand personne n’a noté de mesure. Notez-en une.
- Les mesures d’équipement deviennent périmées quand l’appareil cesse de transmettre. Vérifiez sa ligne dans **Appareils**.
- Certains équipements ne transmettent que de temps en temps. Un titrateur qui mesure toutes les heures affiche en général `1 h`. C’est normal.

### Deux sources ne sont pas d’accord {#two-sources-disagree}

Rien n’est cassé. Quand votre sonde et votre kit de test ne sont pas d’accord, cela vous apprend quelque chose de réel sur votre système.

En général, la sonde a besoin d’être étalonnée. Parfois, le kit de test est vieux. Étalonnez la sonde, refaites le test avec du réactif neuf, et comparez les deux dans les mêmes conditions. Si une mesure était clairement fausse, vous pouvez l’exclure. Voir [Examiner un paramètre](/help/mobile-metric-detail).

Un [résultat ICP](/help/mobile-icp-health) vous donne un troisième chiffre à comparer, mais il ne tranche pas la question à lui seul. Les laboratoires diffèrent entre eux, et la façon dont un échantillon est manipulé et expédié change le résultat.

### Un widget affiche les mauvaises unités {#a-widget-shows-the-wrong-units}

Ce sont les unités d’affichage de l’aquarium. Vos données sont intactes, et les valeurs sont stockées de la même façon quel que soit leur affichage.

1. Ouvrez **Réglages**, ouvrez cet aquarium et choisissez **Unités**.
2. Changez-les là. Chaque téléphone et chaque Cora Max qui affiche cet aquarium se met à jour en conséquence.

### Une jauge ou un seuil a changé d’aspect après un changement d’unités {#a-gauge-or-threshold-looks-different-after-changing-display-}

C’est normal. Les jauges, les tuiles et l’historique se redessinent dans l’unité choisie. Les valeurs en dessous n’ont pas changé.

### Mon tableau de bord semble faux après une modification {#my-dashboard-looks-wrong-after-editing}

Vos mesures, votre historique et votre journal sont stockés à part de la disposition, vous n’avez donc rien perdu.

- **Sur votre téléphone**, l’éditeur n’a ni annulation ni designs enregistrés. Ouvrez **Modifier le tableau de bord** et remettez les widgets en place. Plus de détails dans [Modifier votre tableau de bord](/help/mobile-dashboard-editing).
- **Sur Cora Max**, chargez un design enregistré : ouvrez **Disposition du tableau de bord**, touchez **Mes tableaux de bord** et choisissez-en un. Si vous n’en avez pas enregistré, refaites la disposition et touchez **Enregistrer ce design**, pour que la prochaine fois il suffise d’un appui. Plus de détails dans [Modifier le tableau de bord Cora Max](/help/max-dashboard-editing#saving-layouts).

### Établir pourquoi quelque chose a changé {#establishing-why-something-changed}

**Réglages → Activité** liste chaque commande de prise, nourrissage et dosage, et ce qui l’a demandé : Cora Mobile, un Cora Max, la voix, l’Assistant, une automatisation ou votre compte. Plus de détails dans [Activité et chronologie](/help/mobile-activity).

## Un appareil ne remonte plus de mesures ou est injoignable {#device-not-reporting}

### "[Appareil] : ne remonte plus de mesures" {#device-stopped-reporting}

Cora envoie ce message quand un appareil devient silencieux. Cela ne veut pas dire que l’appareil est en panne, seulement que Cora n’en a pas eu de nouvelles depuis un moment. Le temps d’attente de Cora pour chaque marque est dans [Alertes et seuils](/help/mobile-alerts#stopped-reporting).

1. Vérifiez l’alimentation de l’appareil, et sa portée Wi-Fi ou Bluetooth.
2. Vérifiez que le Cora Max qui le lit est allumé et en ligne. Sans Cora Max, votre téléphone ne lit un appareil Neptune Apex, Red Sea ou Jecod que tant que Cora Mobile est ouvert sur le même Wi-Fi.
3. Attendez la mesure suivante. Vous recevez une deuxième notification dès qu’il transmet de nouveau.

GHL et HYDROS ont leurs propres messages, plus bas sur cette page.

### "L’appareil est hors ligne. Affichage du dernier état connu." {#device-is-offline-showing-last-known-state}

L’appareil a cessé de transmettre, et Cora affiche les dernières valeurs qu’il avait. Elles ne sont pas actuelles.

1. Vérifiez la connexion réseau de l’appareil lui-même.
2. Ne considérez pas les valeurs comme en direct tant que la ligne indique hors ligne.

### Un appareil est injoignable {#a-device-cannot-be-reached}

C’est en général le réseau.

1. L’équipement est-il allumé et fonctionne-t-il dans sa propre application ?
2. Est-il sur le même réseau que celui sur lequel vous l’avez ajouté ?
3. Quelque chose a-t-il changé sur votre routeur (nouveau matériel, nouveau nom de réseau, isolation du réseau invité) ?

Un équipement sur votre réseau local doit être joignable sur ce réseau. Un équipement qui se connecte par un compte de fabricant n’en a pas besoin, mais ce compte doit rester valide. Si l’adresse de l’appareil a changé, ouvrez-le dans l’onglet **Appareils** et touchez **Modifier la connexion** sous **Connexion**.

### Un appareil indique que la connexion a été refusée {#a-device-says-the-sign-in-was-refused}

Le fabricant a rejeté les identifiants enregistrés. Presque toujours, c’est parce que vous avez changé votre mot de passe chez lui. Ouvrez la ligne de l’appareil et reconnectez-vous.

### "Les relevés Red Sea ne se mettent plus à jour" {#red-sea-readings-have-stopped-updating}

Rien sur cet aquarium ne lit votre équipement Red Sea en ce moment, donc les mesures à l’écran ne sont pas rafraîchies.

1. Ouvrez **Réglages**, ouvrez l’aquarium, puis **Cora Max principal**. Vérifiez qu’un Cora Max est défini, ou que **Tout appareil actif (automatique)** est choisi.
2. Si vous n’avez pas de Cora Max, ouvrez l’aquarium dans Cora Mobile pendant que votre téléphone est sur le même Wi-Fi que l’équipement Red Sea.
3. Vérifiez que l’équipement Red Sea est allumé et en ligne dans sa propre application.

### Certains réglages ReefBeat sont grisés ou manquants {#some-reefbeat-settings-are-greyed-out-or-missing}

C’est normal. Les réglages propres d’un appareil Red Sea ne s’ouvrent que lorsque votre téléphone est sur le même réseau que l’appareil. Loin de ce réseau, vous ne voyez que les mesures.

1. Rejoignez le Wi-Fi de l’aquarium pour changer ces réglages.
2. Les mesures et l’historique continuent de fonctionner pendant votre absence.

### "API GHL désactivée" {#ghl-api-is-off}

GHL (Beta) désactive son API officielle après chaque mise à jour du micrologiciel, c’est donc normal après une mise à jour. Réactivez-la depuis **System → GHL API** dans GHL Control Center ou GHL Connect, sur le contrôleur lui-même. Cora continue de vérifier et se reconnecte dès qu’elle est réactivée.

### "Contrôleur GHL inaccessible" {#ghl-controller-unreachable}

Cora Max ne peut pas joindre l’adresse du contrôleur GHL (Beta) sur votre réseau.

1. Vérifiez que le contrôleur est allumé et connecté à votre réseau.
2. Vérifiez que son adresse IP n’a pas changé. Si c’est le cas, ouvrez-le sur votre téléphone (**Appareils**) et mettez-la à jour sous **Connexion**.
3. Vérifiez que le Cora Max qui lit cet aquarium est sur le même réseau que le contrôleur.

### Un contrôleur HYDROS apparaît hors ligne ou ne transmet plus {#a-hydros-controller-shows-as-offline-or-not-reporting}

HYDROS (Beta) transmet par son propre cloud, donc cela veut en général dire que le contrôleur a perdu son alimentation ou sa propre connexion. Vérifiez-le dans l’application HYDROS. Les mesures rattrapent leur retard dès qu’il est de nouveau en ligne. Une commande envoyée alors qu’il semble hors ligne n’est pas envoyée du tout.

Si un appareil HYDROS affiche **Clé révoquée**, sa clé d’appareil a été supprimée ou remplacée dans l’application HYDROS. Créez une nouvelle clé et reliez-le à nouveau sur votre téléphone depuis **Appareils → Ajouter un appareil → HYDROS**.

## Une commande n’est pas passée {#command-did-not-go-through}

Chaque commande se termine en **Confirmé**, **Non confirmé**, **Refusé** ou **Aucun changement**. La signification de chacun est dans [Contrôler votre équipement](/help/mobile-device-control).

### "Impossible de joindre cette pompe : rien n’a été envoyé" {#could-not-reach-this-pump-nothing-was-sent}

Une commande vers votre pompe Jecod ou Jebao n’a jamais quitté Cora. Sur votre téléphone, le message indique *« Impossible de joindre cette pompe. Elle doit être sur le même Wi-Fi que votre téléphone. »* En général, la pompe est éteinte ou n’est pas sur son réseau.

1. Vérifiez que la pompe est allumée.
2. Vérifiez qu’elle est sur le même réseau que celui sur lequel vous l’avez ajoutée, et que votre téléphone ou votre Cora Max est aussi sur ce réseau.
3. Touchez **Réessayer**.

### "Impossible de joindre cette pompe via Bluetooth. Approchez-vous et réessayez." {#could-not-reach-this-pump-over-bluetooth-stand-near-it-and-t}

Votre téléphone est hors de portée d’une pompe Jecod uniquement Bluetooth. Rapprochez-vous de la pompe et touchez **Réessayer**.

### "Impossible de joindre ce Gyre. Son programme n’a pas été modifié." {#could-not-reach-that-gyre-its-program-was-not-changed}

Cora n’a pas pu transmettre un nouveau programme à une Gyre Maxspect (Beta). Vérifiez que la Gyre est allumée et que votre téléphone ou votre Cora Max est sur son réseau, puis touchez **Réessayer** sur l’écran du programme.

### "Impossible de joindre l’Apex : rien n’a changé" / "rien n’a été dosé" {#could-not-reach-the-apex-nothing-changed-nothing-was-dosed}

Un Neptune Apex, un Trident ou une tête DŌS n’a pas répondu à une commande ou à une demande de dose.

1. Ouvrez l’application de l’Apex et vérifiez qu’il est en ligne.
2. Vérifiez la connexion réseau du téléphone ou du Cora Max que vous utilisez. Modifier une tête DŌS depuis votre téléphone demande que le téléphone soit sur le même réseau que l’Apex.
3. Touchez **Réessayer**.

### "… n’a pas pu être envoyé : ce Cora Max n’a pas les identifiants Apex" {#this-could-not-be-sent-no-device-on-this-tank-can-send-it}

Cora Max affiche ce message quand il n’a aucun moyen de joindre votre Apex et qu’aucun autre appareil de l’aquarium ne peut envoyer la commande à sa place. Le message dit d’ajouter les informations Apex dans les Paramètres, mais elles se règlent maintenant sur votre téléphone.

1. Sur votre téléphone, ouvrez **Appareils**, puis votre Apex, et vérifiez son adresse et ses identifiants sous **Connexion**. Corrigez-les avec **Modifier la connexion**.
2. Ou faites d’un Cora Max qui fonctionne le **Cora Max principal** de cet aquarium : **Réglages**, ouvrez l’aquarium, puis **Cora Max principal**.

### Le nourrissage ne démarre pas depuis le téléphone {#feed-does-not-start}

Sur votre téléphone, **Nourrir** n’apparaît que sur un aquarium équipé d’un Neptune Apex, et lance l’un des cycles de nourrissage programmés sur l’Apex.

- *« Aucun Cora de cet aquarium ne peut joindre l’Apex, et vous n’êtes pas sur son réseau. »* Rejoignez le Wi-Fi de l’Apex, ou associez un Cora Max à l’aquarium.
- *« L’Apex n’a pas répondu, mais il se peut qu’il soit déjà en train de nourrir. »* Vérifiez le contrôleur avant de réessayer.

### Un dosage s’est arrêté en cours de route et une alerte de "restauration" est apparue {#a-dose-stopped-partway-through-and-a-restore-alert-appeared}

La tête DŌS a perdu le contact pendant le dosage. Cora vous le dit pour ne pas avoir à supposer que la dose complète est passée.

1. Ouvrez l’alerte et vérifiez combien a été dosé avant l’arrêt.
2. Servez-vous de cette quantité pour décider de reprendre ou d’ajuster la dose.

## Cora Max {#cora-max}

### Mon Cora Max est hors ligne {#my-cora-max-is-offline}

Sur votre téléphone, sa ligne dans l’onglet **Appareils** a un point rouge. Tant qu’il est hors ligne, l’équipement qu’il lit ne se met plus à jour, vous pouvez recevoir des alertes "ne remonte plus de mesures" pour cet équipement, et les commandes envoyées à distance peuvent revenir avec *« Rien n’a été envoyé »*.

1. Vérifiez que Cora Max est alimenté et que l’écran est allumé.
2. Sur Cora Max, vérifiez **Réglages → Réglages Cora Max → Wi-Fi**, et que votre routeur fonctionne.
3. Si un autre Cora Max est sur l’aquarium, réglez le **Cora Max principal** sur **Tout appareil actif (automatique)** pour qu’il puisse prendre le relais. Voir [Plus d’un appareil Cora](/help/mobile-multi-device#primary-cora-max).
4. S’il ne démarre pas correctement, voir [Mises à jour et récupération](/help/max-updates).

:::tip Soyez prévenu la prochaine fois
Dans Cora Mobile, ouvrez **Réglages → Automatisations** et créez une règle avec le déclencheur **Quand un appareil passe hors ligne**, choisissez votre Cora Max, et ajoutez l’action **Me notifier**. Plus de détails dans [Automatisations et scènes](/help/mobile-automation).
:::

### L’association d’un Cora Max échoue {#pairing-a-cora-max-fails}

Cora Mobile trouve un nouveau Cora Max en Bluetooth, puis lui donne votre Wi-Fi. Avant de commencer, ayez au moins un aquarium dans Cora Mobile, le Bluetooth activé, et votre téléphone près de l’écran. Si l’association s’arrête en cours de route, Cora Mobile vous dit pourquoi, avec **Annuler** et **Réessayer** en dessous.

- *« Le Bluetooth est désactivé. Activez-le, puis appuyez à nouveau sur Rechercher. »* Activez le Bluetooth et relancez la recherche.
- *« L’autorisation Bluetooth est désactivée pour Cora. Activez-la dans les Réglages, puis appuyez à nouveau sur Rechercher. »* Autorisez le Bluetooth pour Cora dans les réglages de votre téléphone. **Réglages → Accès aux appareils** dans Cora Mobile vous y mène.
- *« Aucun appareil de configuration Cora à proximité n’a été trouvé via Bluetooth. »* Placez-vous à côté de Cora Max, vérifiez qu’il affiche son écran de configuration, et relancez la recherche.
- **Aucun aquarium trouvé** : créez d’abord un aquarium dans Cora Mobile, puis associez.
- *« Votre téléphone n’a pas pu joindre le Cora Max sur votre Wi-Fi. »* Mettez votre téléphone et Cora Max sur le même réseau Wi-Fi. Sur iPhone, vérifiez aussi que Cora a l’accès au réseau local (**Réglages → Accès aux appareils**). Puis touchez **Réessayer**.
- *« Le Cora Max n’a pas accepté cette session d’appairage. »* Réessayer n’aidera pas. Fermez l’écran et recommencez depuis **Appareils → Ajouter un appareil → Cora**.

Pour tout autre message, touchez **Réessayer**. Toute la configuration est dans [Configurer Cora Max](/help/max-setup).

### Cora Max affiche des données anciennes {#cora-max-shows-old-data}

Regardez l’étiquette d’état dans la barre du haut. **En ligne** et **Cloud** sont tous deux normaux. Si vous avez plusieurs Cora Max, celui qui ne collecte pas les données affiche **Cloud**, et ses mesures sont tout aussi à jour. **Obsolète** ou **Hors ligne** veut dire que Cora Max a perdu sa source et affiche les dernières données qu’il a reçues.

- Vérifiez le Wi-Fi sous **Réglages → Réglages Cora Max → Wi-Fi**.
- Vérifiez que votre réseau lui-même fonctionne.
- Si l’étiquette indique **En ligne** ou **Cloud** et que les données sont toujours anciennes, le problème est en amont de Cora Max. Vérifiez le même aquarium sur votre téléphone.

### Cora Max affiche "Mot de passe Apex" {#cora-max-shows-apex-password}

Votre Apex a refusé les identifiants que Cora a enregistrés, en général parce que le mot de passe de l’Apex a été changé. Sur votre téléphone, ouvrez **Appareils**, puis votre Apex, et touchez **Modifier la connexion** sous **Connexion** pour saisir le nouveau.

### Cora Max affiche "Enregistrement cloud refusé" {#cora-max-shows-cloud-save-refused}

Cora Cloud refuse d’enregistrer une partie des données de cet écran. Rien ne va mal avec votre aquarium ni avec Cora Max, et rien n’est à changer sur l’écran. La solution est une mise à jour de Cora Cloud.

1. Ouvrez **Réglages → Réglages Cora Max** et faites défiler jusqu’à **ÉTAT**. La ligne **Enregistrement cloud** indique quelles données sont refusées, par exemple les mesures ou les prises d’un appareil.
2. [Contactez l’assistance](/support.html) et dites-nous ce qu’indique cette ligne.

Vos mesures continuent de s’afficher sur Cora Max en attendant. Elles ne sont simplement pas enregistrées sur votre compte tant que la correction n’est pas en place.

### Un deuxième Cora Max affiche "Cora principal hors ligne" {#a-secondary-cora-max-shows-main-cora-offline}

Le Cora Max principal de cet aquarium s’est déconnecté. Cet écran affiche les dernières données qu’il a reçues, elles ne sont donc pas en direct.

1. Vérifiez l’alimentation et le Wi-Fi du Cora Max principal.
2. Attendez qu’il se reconnecte, ou changez le **Cora Max principal** pour un appareil en ligne.

### Cora Max ne se reconnecte pas tout de suite après une coupure Wi-Fi {#cora-max-wont-reconnect-right-away-after-a-wi-fi-outage}

Après avoir perdu sa connexion, Cora Max attend un peu plus longtemps avant chaque nouvelle tentative, pour ne pas inonder votre réseau. L’attente monte jusqu’à environ une minute.

1. Laissez-lui environ une minute après le retour de votre réseau.
2. S’il ne s’est toujours pas reconnecté, vérifiez **Réglages → Réglages Cora Max → Wi-Fi**.

### Renommer un Cora Max sur le téléphone ne change pas ce qu’il affiche {#renaming-a-cora-max-on-the-phone-doesnt-change-what-the-tabl}

Le nom que vous réglez sur votre téléphone est l’étiquette de cet appareil dans le compte. Le nom que Cora Max affiche sur son propre écran d’association peut être différent.

1. Vérifiez de quel nom il s’agit : celui de la liste des appareils de votre téléphone, ou celui de l’écran d’association de Cora Max.
2. Pour changer l’étiquette du compte, renommez-le depuis la liste des appareils de votre téléphone.

### Je ne trouve pas où désactiver le mot d’activation {#i-cant-find-where-to-turn-off-the-wake-word-on-cora-max}

Les commandes du mot d’activation sont avec les réglages du son, pas avec ceux de Cora Assistant.

1. Sur Cora Max, allez dans **Réglages → Réglages Cora Max**, et trouvez **Mot d’activation** sous **SON ET VOIX**.
2. Désactivez-le. Vous pouvez toujours toucher l’icône **Cora Assistant** pour commencer à parler.

Plus de détails dans [Parler à Cora](/help/max-voice).

### Le verrouillage enfant n’autorise personne à entrer dans les réglages {#child-lock-wont-let-anyone-into-settings}

C’est le rôle du verrouillage enfant. Après un certain temps sans contact, il empêche quiconque de commander l’équipement depuis cet écran, au toucher comme à la voix. Les mesures continuent de se mettre à jour, et vous pouvez toujours poser des questions à Cora. Pour déverrouiller :

1. Appuyez trois fois sur **Volume +** ou **Volume -** en moins de deux secondes, ou
2. Posez cinq doigts en haut à droite de l’écran pendant dix secondes.

Plus de détails dans [Réglages de Cora Max](/help/max-settings#child-lock).

### Une scène créée sur le téléphone n’est pas modifiable sur Cora Max {#a-scene-made-on-the-phone-doesnt-show-up-as-editable-on-cora}

Seules les versions récentes de Cora Max peuvent modifier des scènes à l’écran. Les anciennes versions lancent toujours les scènes créées sur votre téléphone, mais ne peuvent pas les modifier.

1. Mettez Cora Max à jour ([Mises à jour et récupération](/help/max-updates)), ou
2. Continuez à modifier cette scène sur votre téléphone. Elle se lance sur Cora Max dans les deux cas.

## Alertes, notifications et briefing quotidien {#alerts-and-notifications}

### Une alerte ne disparaît pas {#an-alert-is-not-clearing}

Une alerte disparaît quand la mesure revient dans la plage. Si elle ne disparaît pas, il y a trois raisons probables.

- La mesure est vraiment hors plage. Regardez l’historique du widget.
- La plage ne convient pas à votre aquarium. Voir [Alertes et seuils](/help/mobile-alerts).
- La source est faussée. Une sonde qui a besoin d’être étalonnée signale un chiffre qui est réellement hors plage. Réparez la sonde et ne touchez pas à la plage.

### Une alerte continue de prévenir alors que je l’ai prise en compte {#an-alert-wont-stop-notifying-even-after-ive-acknowledged-it}

**Reporter** et **Ignorer** sur Cora Max ne font taire que ce Cora Max. Votre téléphone continue de recevoir des notifications tant que la mesure est hors plage.

1. Pour en entendre parler moins souvent, ouvrez la règle d’alerte dans Cora Mobile et réglez un **Délai entre les alertes** plus long (jusqu’à 1 semaine).
2. Si la plage ne convient pas à votre aquarium, changez la plage elle-même.

### Je ne reçois pas de notifications {#im-not-getting-notifications}

1. Dans **Réglages → Notifications**, vérifiez que la catégorie est autorisée à envoyer des notifications.
2. Vérifiez l’autorisation de notification de votre téléphone pour Cora.
3. Le briefing quotidien reste silencieux les jours où rien n’a changé. S’il s’est complètement arrêté, voir l’entrée suivante.

Plus de détails dans [Notifications](/help/mobile-notifications).

### Mon briefing quotidien s’est arrêté {#my-daily-briefing-stopped}

- Votre essai est terminé. Reef Buddy fait partie des forfaits payants. Après l’essai de 30 jours, un compte gratuit ne reçoit plus le briefing quotidien. Voir [Forfaits et abonnements](/help/mobile-plans).
- L’aquarium n’est pas couvert par votre forfait. Chaque forfait couvre un nombre fixe d’aquariums, comptés dans l’ordre de **Réglages → Réorganiser les aquariums**. Remontez un aquarium pour l’inclure.
- Rien n’a changé aujourd’hui. Le briefing reste silencieux un jour calme.

Plus de détails dans [Reef Buddy](/help/mobile-reef-buddy).

### Des alertes continuent d’arriver d’un aquarium retiré {#alerts-from-a-removed-tank}

Retirer un aquarium ne fait que le masquer. Ses appareils lui restent liés, et un Cora Max peut encore le lire, donc son équipement peut continuer de transmettre et d’alerter.

1. Restaurez-le depuis **Réglages → Aquariums supprimés** pour le voir à nouveau.
2. Retirez ou déplacez ses appareils dans l’onglet **Appareils**.
3. Retirez-le de votre Cora Max : sur votre téléphone, ouvrez **Appareils**, puis votre Cora Max, et sous **Aquariums** touchez **Retirer l’aquarium** à côté de lui.

Retirez ensuite l’aquarium à nouveau. Plus de détails dans [Gérer vos aquariums](/help/mobile-tanks).

## Caméras et surveillance de l’écumeur {#cameras-and-skimmer-watch}

Les caméras et la surveillance de l’écumeur sont en Beta. Leur configuration est dans [Caméras et surveillance de l’écumeur](/help/mobile-cameras).

### La surveillance de l’écumeur affiche un message au lieu d’un niveau de godet {#skimmer-watch-messages}

- **Marquez d'abord le godet** : la surveillance de l’écumeur ne sait pas encore où est le godet. Touchez **Marquer le godet** et faites glisser le cadre dessus.
- **Non calibré : videz le godet et touchez Le godet est vide maintenant** : faites exactement cela, avec le godet vide.
- **Cadre déplacé : calibrez à nouveau** : vous avez déplacé le cadre, calibrez donc à nouveau avec un godet vide.
- **Pas sûr (faible confiance)** : l’image n’était pas assez nette. Lisez les **Conseils pour la caméra** sur l’écran de la surveillance de l’écumeur, puis attendez la vérification suivante ou touchez **Vérifier maintenant**.
- **Lumière trop forte derrière le godet** : éteignez la lumière derrière le godet, ou réglez la vision nocturne de la caméra sur toujours activée.
- **Cora Max n'a pas pu obtenir d'image de la caméra.** : vérifiez que la caméra est alimentée et en ligne, et que le Cora Max qui la lit est allumé.
- **La dernière vérification a échoué.** : touchez **Vérifier maintenant**. Si cela échoue encore, vérifiez la caméra et Cora Max.
- **Pas encore de mesure. Cora Max vérifie toutes les 15 minutes.** : attendez la première vérification.
- **La surveillance de l'écumeur nécessite un forfait payant.** : la surveillance de l’écumeur fait partie des forfaits payants.

## Cora Assistant et voix {#cora-assistant-and-voice}

### Cora Assistant répond sur le mauvais aquarium {#cora-assistant-answers-about-the-wrong-tank}

Vous n’avez pas choisi d’aquarium avant de poser la question, ou le mauvais est sélectionné. Choisissez l’aquarium voulu, puis posez à nouveau la question. Plus de détails dans [Interroger Cora](/help/mobile-assistant).

### Cora Assistant refuse de répondre, ou affiche à nouveau un écran de consentement {#cora-assistant-refuses-to-answer-or-shows-a-consent-screen-a}

**Autoriser Cora Assistant à utiliser les données d’aquarium enregistrées** est désactivé, il n’a donc rien à partir de quoi répondre. Touchez **Accepter et continuer** sur l’écran de consentement, ou activez l’interrupteur dans **Réglages → Cora Assistant**.

### Cora Max indique "La voix a besoin de votre accord" {#voice-needs-your-ok}

La voix sur Cora Max utilise le même choix de partage de données que Cora Assistant sur votre téléphone. Dans Cora Mobile, ouvrez **Réglages → Cora Assistant** et activez **Autoriser Cora Assistant à utiliser les données d’aquarium enregistrées**, puis réessayez. Plus de détails dans [Parler à Cora](/help/max-voice).

## Résultats de laboratoire et rapports de santé {#lab-results-and-health-reports}

### Un résultat ICP de laboratoire ou envoyé par e-mail n’est jamais arrivé {#a-lab-or-emailed-icp-result-never-showed-up}

Un résultat ne s’attache qu’une fois qu’il a un aquarium, Cora doit parfois aussi reconnaître l’expéditeur, et Cora a besoin de votre accord pour le lire.

1. Si vous voyez *« Cora Assistant a besoin de votre accord pour le lire. »*, ouvrez **Réglages → Cora Assistant** et activez **Autoriser Cora Assistant à utiliser les données d’aquarium enregistrées**. Le résultat arrive dès que vous acceptez.
2. Vérifiez l’indication que Cora affiche la première fois que vous lui envoyez un résultat.
3. Quand Cora le demande, confirmez à quel aquarium appartient le résultat.
4. Si vous avez déjà envoyé un résultat, envoyez celui-ci depuis la même adresse e-mail.

Plus de détails dans [Rapports ICP et de santé](/help/mobile-icp-health).

### Mon fichier ICP ne s’importe pas {#my-icp-file-wont-upload}

Cora lit le rapport PDF que votre laboratoire envoie. Les photos et les captures d’écran ne peuvent pas être lues. Téléchargez d’abord le PDF auprès de votre laboratoire, puis touchez à nouveau **Téléverser un ICP**.

### L’écran devient noir après un rapport de santé ou un import ICP {#black-screen-after-a-report}

Cela pouvait arriver dans Cora Mobile 1.2 et versions antérieures, et Cora Mobile 1.3 le corrige : mettez Cora Mobile à jour depuis l’App Store ou Google Play. Si cela vous arrive avant la mise à jour, fermez Cora Mobile et rouvrez-le. Le rapport a été enregistré, et vous le trouverez sous **Intelligence**.

## Langue, unités et connexion {#language-units-and-signing-in}

### Tout est soudain dans la mauvaise langue {#everything-is-suddenly-in-the-wrong-language}

Quelqu’un a changé la langue du compte sur l’un de vos appareils. C’est un seul réglage pour tout le compte.

1. Ouvrez **Réglages → Langue** dans Cora Mobile ou sur Cora Max.
2. Remettez-la. Le changement s’applique partout.

### Une ancienne alerte ou un ancien rapport est dans une autre langue après le changement {#an-old-alert-or-report-is-still-in-a-different-language-afte}

C’est normal. Cora ne retraduit rien de ce qu’il a déjà écrit. Les nouvelles alertes, les nouveaux rapports et les nouveaux briefings utilisent la nouvelle langue.

### "Impossible de contacter Cora. Vérifiez votre Wi-Fi ou vos données mobiles, puis réessayez." {#could-not-reach-cora-check-your-wi-fi-or-mobile-data-then-tr}

Votre téléphone ne peut pas joindre Cora Cloud pour se connecter. Cela concerne la connexion de votre téléphone, pas l’équipement de votre aquarium.

1. Vérifiez que votre téléphone a un Wi-Fi ou des données mobiles qui fonctionnent.
2. Essayez un autre réseau si vous en avez un.
3. Touchez **Réessayer**.

Les autres problèmes de connexion sont dans [Connexion et récupération de compte](/help/mobile-account).

## Toujours bloqué {#still-stuck}

Écrivez à **[cora@coraiq.tech](mailto:cora@coraiq.tech)**, ou signalez-le depuis Cora Mobile comme décrit dans [Signaler un problème](/help/mobile-support). Dites-nous quel aquarium, quel appareil, quel écran, et ce que vous vous attendiez à voir.
