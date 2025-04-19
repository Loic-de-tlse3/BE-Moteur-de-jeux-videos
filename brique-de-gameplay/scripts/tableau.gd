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

var cadre_null = preload("res://Scenes/Cadre_null.tscn")
var generateur = preload("res://Scenes/générateur.tscn")
var objets = [
	preload("res://Scenes/arme distance.tscn"),
	preload("res://Scenes/arme mêlée.tscn")
]

var liste_objets = []

var premier_item_touche = Vector2(0, 0)
var second_item_touche = Vector2(0, 0)

# Called when the node enters the scene tree for the first time.
func _ready():
	randomize()
	x_initial_cadre = x_initial - ((taille_cadre - taille_objet)/2)
	y_initial_cadre = y_initial - ((taille_cadre - taille_objet)/2)
	ajout_cadre_null()
	for i in nb_item_max:
		liste_objets.append(null)
		print(liste_objets[i])
	ajout_generateur()

func ajout_cadre_null():
	var x = x_initial_cadre
	var y = y_initial_cadre
	for i in nb_item_max:
		var cadre = cadre_null.instance()
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
		premier_item_touche = get_global_mouse_position()
		var position_case1 = pixels_vers_case(premier_item_touche.x, premier_item_touche.y)
		#TODO vérifier si l'élément touché est le générateur ou un objet
		var position_liste_elt1 = position_case1.x + (6 * position_case1.y)
		print(position_liste_elt1)
		if liste_objets[position_liste_elt1] == null:
			print("probleme")
			return 0
		elif liste_objets[position_liste_elt1].type == "générateur":
			print("réussi")
			return 0
			#liste_objets[position_liste_elt1].generation()
		elif (liste_objets[position_liste_elt1].type == "distance") || (liste_objets[position_liste_elt1].type == "mêlée"):
			print("gestion click objet")
	if Input.is_action_just_pressed("ui_interaction"):
		print("deuxième if")
		second_item_touche = get_global_mouse_position()
		var position_case2 = pixels_vers_case(second_item_touche.x, second_item_touche.y)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	toucher_item()
#	pass
