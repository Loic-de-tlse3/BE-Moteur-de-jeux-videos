extends Node2D

enum Type {
	DISTANCE,
	MELE
}

# Chargement du sprite afin de changer son image plus tard
onready var sprite = $Sprite

# Variable d'objet initialisé en dehors du code
export (String) var type
export (int) var niveau

# Chargement des images utilisées dans la fonction de fusion
var textures_distance = [
	load("res://Projet BE images/gun.png"),
	load("res://Projet BE images/rifle.png"),
	load("res://Projet BE images/space-gun.png")
]

var textures_melee = [
	load("res://Projet BE images/knife.png"),
	load("res://Projet BE images/sword.png"),
	load("res://Projet BE images/spears.png")
]


# Appelé lorsque le noeud entre l'arbre de scène la première fois, ne fait rien dans ce programme
func _ready():
	pass
	
func generation(tableau, objets_possibles, emplacement):
	var nouvel_objet = null
	if randi()%2 == Type.DISTANCE: # Génère une arme distance ou mêlée en fonction du résultat aléatoire obtenu
		nouvel_objet = objets_possibles[0].instance()
	else:
		nouvel_objet = objets_possibles[1].instance()
	add_child(nouvel_objet)
	nouvel_objet.position = case_vers_pixels(tableau, emplacement)
	nouvel_objet.niveau = 1
	return nouvel_objet # Renvoie l'instance du nouvel objet créé
	
func get_sprite_texture():
	return sprite.texture
	
func fusion(liste_objets, second_objet):
	if (niveau < 3) and (self.type == second_objet.objet.type) and (self != second_objet.objet) and (self.niveau == second_objet.objet.niveau): 
		niveau += 1
		liste_objets[second_objet.position_liste] = null # Vide la case contenant l'autre objet (le premier sélectionné)
		changement_image()
		second_objet.objet.queue_free() # Détruit le premier objet sélectionné
		
		# Renvoie des points obtenus en fonction du niveau de la fusion
		if niveau == 3:
			return 100
		elif niveau == 2:
			return 50
	else:
		return 0
	
func case_vers_pixels(tableau, case:int):
	var x = tableau.distance_objet*(case%tableau.nb_item_ligne)
	var y = tableau.distance_objet*(case/tableau.nb_item_ligne)
	return Vector2(x, y)
	
# Change l'image du sprite en fonction de son nouveau niveau après fusion
func changement_image():
	if niveau >= 0 and niveau <= textures_distance.size():
		if type == "distance":
			sprite.texture = textures_distance[niveau-1]
		elif type == "mêlée":
			sprite.texture = textures_melee[niveau-1]
	else:
		print("niveau imprévu")
