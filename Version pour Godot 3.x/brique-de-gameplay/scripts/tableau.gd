extends Node2D

# Variables de tableau initialisées en dehors du code
export (int) var nb_item_ligne
export (int) var nb_item_max
export (int) var x_initial
export (int) var y_initial
export (int) var taille_cadre
export (int) var taille_objet
export (int) var x_initial_cadre
export (int) var y_initial_cadre
export (int) var distance_objet

# Préchargement des scènes utilisées dans la suite du programme
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

# Dictionnaire (ou map) contenant quatre valeurs répertoriées par un nom, 
# servira à ranger les valeurs des objets avec lesquels l'utilisateurs interagira
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

# Contient le nombre de points marqués par le joueur
var nb_points = 0

# Liste contenant l'ensemble des objets du tableau
var liste_objets = []

# Appelé lorsque le noeud entre l'arbre de scène la première fois
func _ready():
	randomize() # Génère une "seed" différente afin de ne pas avoir le même paterne aléatoire à chaque fois (Utile pour la fonction generation dans objet.gd)
	for i in nb_item_max:
		liste_objets.append(null) # Initialisation du tableau avec des objets null
	ajout_generateur()

# Fonction mettant à jour les cadres, appelée à chaque image (frame)
func ajout_cadres():
	var x = x_initial_cadre
	var y = y_initial_cadre
	var cadre = null
	
	# Pour l'ensemble des objets, s'il est null on lui applique cadres[0], sinon le cadre correspondant à son niveau
	for i in liste_objets.size():
		if liste_objets[i] == null:
			cadre = cadres[0].instance() # Nécessaire pour créer une nouvelle instance
		else:
			var niveau = liste_objets[i].niveau
			cadre = cadres[niveau].instance() # Nécessaire pour créer une nouvelle instance
		add_child(cadre) # Nécessaire pour créer une nouvelle instance
		cadre.position = Vector2(x, y) # Donnes les coordonnées d'où se placer à la nouvelle instance
		
		# Mise à jour des coordonnées pour les instances suivantes
		x += distance_objet
		if (i+1) % nb_item_ligne == 0:
			x = x_initial_cadre
			y += distance_objet
			
func ajout_generateur():
	var bouton = generateur.instance()
	add_child(bouton)
	bouton.position = Vector2(x_initial, y_initial)
	liste_objets[0] = bouton # Range le generateur créé dans la première case du tableau (indépendant de l'affichage)
	
	
# Calcul la case qui correspond au coordonnées obtenues
func pixels_vers_case(pixel_x, pixel_y):
	if pixel_x > x_initial + distance_objet*5 + taille_objet/2:
		pixel_x = x_initial + distance_objet*5 + taille_objet/2
	if pixel_x < x_initial - taille_objet/2:
		pixel_x = x_initial - taille_objet/2
	if pixel_y > y_initial + distance_objet*5 + taille_objet/2:
		pixel_y = y_initial + distance_objet*2 + taille_objet/2
	if pixel_y < y_initial - taille_objet/2:
		pixel_y = y_initial - taille_objet/2
	var x = round((pixel_x - x_initial) / distance_objet)
	var y = round((pixel_y - y_initial) / distance_objet)
	return Vector2(x, y)
	
func toucher_item():
	if Input.is_action_just_pressed("ui_interaction"): # Condition validée lors d'un clic gauche
		objet1.coordonnees = get_global_mouse_position() # Donne les coordonnées du curseur de la souris
		if (objet1.coordonnees.x <= x_initial + distance_objet*5 + taille_objet/2) and (objet1.coordonnees.x >= x_initial - taille_objet/2) and (objet1.coordonnees.y <= y_initial + distance_objet*2 + taille_objet/2) and (objet1.coordonnees.y >= y_initial - taille_objet/2):
			objet1.position_case = pixels_vers_case(objet1.coordonnees.x, objet1.coordonnees.y)
			objet1.position_liste = objet1.position_case.x + (6 * objet1.position_case.y) # Calcul de la position dans liste_objets en fonction de la case dans laquelle se trouve l'objet
			objet1.objet = liste_objets[objet1.position_liste]
			if liste_objets[objet1.position_liste] == null:
				return 0 # Annulation de l'opération si le clic ne s'est pas fait sur un objet
			elif liste_objets[objet1.position_liste].type == "générateur":
				var emplacement = premiere_case_vide()
				if emplacement == -1:
					return 1
				# Génération d'un nouvel objet si le clic s'est fait sur le générateur et que le tableau n'est pas plein
				var nouvel_objet = liste_objets[objet1.position_liste].generation(self, objets, emplacement)
				liste_objets[emplacement] = nouvel_objet # On range le nouvel objet généré dans la première case vide
				return 0 # Stop la fonction ici si le clic s'est fait sur un générateur
			var texture = objet1.objet.get_sprite_texture()
			Input.set_custom_mouse_cursor(texture, 0, Vector2(64, 64))
			objet1.objet.sprite.scale = Vector2(1.2, 1.2) # Agrandi la taille de l'image pour donner une animation et visualiser l'objet selectionné si ce n'est pas le générateur
		
	if Input.is_action_just_released("ui_interaction"): # Condition validée lorsque le clic gauche est relâché
		objet2.coordonnees = get_global_mouse_position()
		if (objet1.coordonnees.x <= x_initial + distance_objet*5 + taille_objet/2) and (objet1.coordonnees.x >= x_initial - taille_objet/2) and (objet1.coordonnees.y <= y_initial + distance_objet*2 + taille_objet/2) and (objet1.coordonnees.y >= y_initial - taille_objet/2):
			objet2.position_case = pixels_vers_case(objet2.coordonnees.x, objet2.coordonnees.y)
			objet2.position_liste = objet2.position_case.x + (6 * objet2.position_case.y)
			objet2.objet = liste_objets[objet2.position_liste]
			#print("objet 1 : ", objet1.position_liste, " | objet 2 : ", objet2.position_liste)
			if (objet1.objet != null) and (objet2.objet != null and objet1.objet.type != "générateur" and objet2.objet.type != "générateur"):
				nb_points += objet2.objet.fusion(liste_objets, objet1) # Procède à la fusion des deux objets sélectionné si ce ne sont pas des générateurs et qu'ils ne sont pas null
				# print("nombre de points aquis : ", nb_points)
		if objet1.objet != null:
			objet1.objet.sprite.scale = Vector2(1, 1) # Remet la taille du premier objet sélectionné à la normale
		Input.set_custom_mouse_cursor(null, 0, Vector2(0, 0))
		
# Retourne la première case vide du tableau, celle contenant un élément null
func premiere_case_vide():
	for i in range(nb_item_max):
		if liste_objets[i] == null:
			return i
	return -1 # Renvoie -1 si le tableau est plein

# Appelé à chaque image. 'delta' est le temps qui s'est écoulé depuis l'image précédente
func _process(delta):
	toucher_item()
	ajout_cadres()
