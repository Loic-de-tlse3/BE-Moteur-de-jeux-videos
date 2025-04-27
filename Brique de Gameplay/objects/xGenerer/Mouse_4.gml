var Arme_aleatoire = irandom(1);

if (compteur != nbCadre){
	if (Arme_aleatoire == 0){
		instance_create_depth(114 + (224 * (compteur % 5)), 180 + (192 * colonne), 0, xDistance1);
	} else {
		instance_create_depth(114 + (224 * (compteur % 5)), 180 + (192 * colonne), 0, xMelee1);
	}
	compteur++;
	if ((compteur % 5) == 0){
		colonne++;
	}
}
