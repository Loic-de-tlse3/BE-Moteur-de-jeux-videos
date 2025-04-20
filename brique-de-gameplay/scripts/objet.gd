extends Node2D

enum Type {
	DISTANCE,
	MELE
}

export (String) var type

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.
	
func generation(objets_possibles, emplacement:int):
	var nouvel_objet = null
	if randi()%2 == Type.DISTANCE:
		nouvel_objet = objets_possibles[0].instance()
	else:
		nouvel_objet = objets_possibles[1].instance()
	add_child(nouvel_objet)
	return nouvel_objet

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
