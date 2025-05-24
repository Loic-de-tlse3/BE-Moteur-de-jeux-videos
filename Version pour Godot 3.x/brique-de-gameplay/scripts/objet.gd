extends Node2D

enum Type {
	DISTANCE,
	MELE
}

onready var sprite = $Sprite

export (String) var type
export (int) var niveau

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

#var tableau_instance = preload("res://Scenes/FenêtreDeJeu.tscn").instance()

# Called when the node enters the scene tree for the first time.
func _ready():
	#changement_image()
	pass # Replace with function body.
	
func generation(tableau, objets_possibles, emplacement):
	var nouvel_objet = null
	if randi()%2 == Type.DISTANCE:
		nouvel_objet = objets_possibles[0].instance()
	else:
		nouvel_objet = objets_possibles[1].instance()
	add_child(nouvel_objet)
	nouvel_objet.position = case_vers_pixels(tableau, emplacement)
	nouvel_objet.niveau = 1
	return nouvel_objet
	
func fusion(liste_objets, second_objet):
	if (niveau < 3) and (self.type == second_objet.objet.type) and (self != second_objet.objet) and (self.niveau == second_objet.objet.niveau): 
		niveau += 1
		liste_objets[second_objet.position_liste] = null
		changement_image()
		second_objet.objet.queue_free()
		if niveau == 3:
			return 100
		elif niveau == 2:
			return 50
	else:
		print("Fusion impossible")
		return 0
	
func case_vers_pixels(tableau, case:int):
	var x = tableau.distance_objet*(case%tableau.nb_item_ligne)
	var y = tableau.distance_objet*(case/tableau.nb_item_ligne)
	return Vector2(x, y)
	
func changement_image():
	if niveau >= 0 and niveau <= textures_distance.size():
		if type == "distance":
			sprite.texture = textures_distance[niveau-1]
		elif type == "mêlée":
			sprite.texture = textures_melee[niveau-1]
	else:
		print("niveau imprévu")

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
