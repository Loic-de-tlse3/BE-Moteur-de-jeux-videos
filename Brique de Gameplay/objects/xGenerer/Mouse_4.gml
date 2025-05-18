var Arme_aleatoire;
randomize();
Arme_aleatoire = choose(0,1);

if (compteur != nbCadre){
	if (Arme_aleatoire == 0){
		tableau[compteur-1]=instance_create_depth(114 + (224 * (compteur % 5)), 180 + (192 * colonne), 0, xDistance1);
		tableau[compteur-1]=instance_create_depth(96 + (224 * (compteur % 5)), 160 + (192 * colonne),-1, xCadre1);
		tableau_objets[compteur-1]="Distance";
	} else {
		tableau[compteur-1]=instance_create_depth(114 + (224 * (compteur % 5)), 180 + (192 * colonne), 0, xMelee1);
		tableau[compteur-1]=instance_create_depth(96 + (224 * (compteur % 5)), 160 + (192 * colonne), -1, xCadre1);
		tableau_objets[compteur-1]="Melee";
	}
	compteur++;
	if ((compteur % 5) == 0){
		colonne++;
	}
}
