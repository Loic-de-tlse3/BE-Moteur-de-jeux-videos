extends Node2D

enum TypeObjet {
	DISTANT,
	CAC
}

# Declare member variables here. Examples:
var niveauObjet = 1
var typeObjet = TypeObjet.DISTANT


# Called when the node enters the scene tree for the first time.
func _ready():
	typeObjet = TypeObjet(randi() % TypeObjet.size())
	majApparence()
	
func majApparence():
	if typeObjet == TypeObjet.DISTANT:
		#TODO
		print("TODO changer apparence en arme distance")
	else:
		#TODO
		print("TODO changer apparence en arme càc")
		
func get_typeObjet():
	return typeObjet
	
func get_niveauObjet():
	return niveauObjet
	
func destruction():
	queue_free()
	#TODO
	print("TODO Destruction de l'objet")

func fusionner(objet):
	if (typeObjet != objet.get_typeObjet()) or (niveauObjet != objet.get_niveauObjet()) or (niveauObjet == 3):
		#TODO
		print("TODO refuser la fusion")
	else:
		#TODO
		print("TODO accepter la fusion")
		niveauObjet++
objet.destruction()
		

	
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
