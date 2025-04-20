extends Node2D

# Variables de tableau
export (int) var nb_item_ligne
export (int) var nb_item_max
export (int) var x_initial
export (int) var y_initial
export (int) var taille_cadre
export (int) var taille_objet
export (int) var x_initial_cadre
export (int) var y_initial_cadre
export (int) var distance_objet

var cadres = [
	preload("res://Scenes/Cadre_null.tscn"),
	preload("res://Scenes/Cadre_nv_1.tscn"),
	preload("res://Scenes/Cadre_nv_2.tscn"),
	preload("res://Scenes/Cadre_nv_3.tscn")
]

var generateur = preload("res://Scenes/générateur.tscn")
var objets = [
	preload("res://Scenes/arme distance.tscn"),
	preload("res://Scenes/arme mêlée.tscn")
]

var liste_objets = []

var objet1 = {
	"coordonnees": Vector2(0, 0),
	"position_liste": 0,
	"position_case": Vector2(0, 0),
	"objet": null
}

var objet2 = {
	"coordonnees": Vector2(0, 0),
	"position_liste": 0,
	"position_case": Vector2(0, 0),
	"objet": null
}

# Called when the node enters the scene tree for the first time.
func _ready():
	randomize()
	#x_initial_cadre = x_initial - ((taille_cadre - taille_objet)/2)
	#y_initial_cadre = y_initial - ((taille_cadre - taille_objet)/2)
	for i in nb_item_max:
		liste_objets.append(null)
	ajout_cadres()
	ajout_generateur()

func ajout_cadres():
	var x = x_initial_cadre
	var y = y_initial_cadre
	var cadre = null
	for i in liste_objets.size():
		if liste_objets[i] == null:
			cadre = cadres[0].instance()
		else:
			var niveau = liste_objets[i].niveau
			cadre = cadres[niveau].instance()
		add_child(cadre)
		cadre.position = Vector2(x, y)
		x += distance_objet
		if (i+1) % nb_item_ligne == 0:
			x = x_initial_cadre
			y += distance_objet
			
func ajout_generateur():
	var bouton = generateur.instance()
	add_child(bouton)
	bouton.position = Vector2(x_initial, y_initial)
	liste_objets[0] = bouton
	
	
func pixels_vers_case(pixel_x, pixel_y):
	var x = round((pixel_x - x_initial) / distance_objet)
	var y = round((pixel_y - y_initial) / distance_objet)
	return Vector2(x, y)
	
func toucher_item():
	if Input.is_action_just_pressed("ui_interaction"):
		objet1.coordonnees = get_global_mouse_position()
		objet1.position_case = pixels_vers_case(objet1.coordonnees.x, objet1.coordonnees.y)
		objet1.position_liste = objet1.position_case.x + (6 * objet1.position_case.y)
		objet1.objet = liste_objets[objet1.position_liste]
		if liste_objets[objet1.position_liste] == null:
			return 0
		elif liste_objets[objet1.position_liste].type == "générateur":
			var emplacement = premiere_case_vide()
			if emplacement == -1:
				print("Plus de place")
				return 1
			var nouvel_objet = liste_objets[objet1.position_liste].generation(self, objets, emplacement)
			liste_objets[emplacement] = nouvel_objet
			return 0
	if Input.is_action_just_released("ui_interaction"):
		objet2.coordonnees = get_global_mouse_position()
		objet2.position_case = pixels_vers_case(objet2.coordonnees.x, objet2.coordonnees.y)
		objet2.position_liste = objet2.position_case.x + (6 * objet2.position_case.y)
		objet2.objet = liste_objets[objet2.position_liste]
		if (objet1.objet != null) and (objet2.objet != null):
			objet2.objet.fusion(liste_objets, objet1)
		else:
			print("Fusion impossible")
		
func premiere_case_vide():
	for i in range(nb_item_max):
		if liste_objets[i] == null:
			return i
	return -1

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	toucher_item()
	ajout_cadres()
#	pass
