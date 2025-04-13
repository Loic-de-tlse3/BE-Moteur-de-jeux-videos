# Sphinx project documentation

# -- Configuration des chemins ---------------------------------------------------
SPHINX = sphinx-build
SOURCE_DIR = source
BUILD_DIR = build
HTML_DIR = $(BUILD_DIR)/html

# -- Règles par défaut ----------------------------------------------------------

.PHONY: help clean html

# Affiche la documentation pour `make`
help:
	@echo "Utilisation :"
	@echo "  make clean       - Nettoie les fichiers de génération."
	@echo "  make html        - Génère la documentation HTML."

# Nettoyage des fichiers générés
clean:
	rm -rf $(BUILD_DIR)

# Générer la documentation HTML
html:
	$(SPHINX) -b html $(SOURCE_DIR) $(HTML_DIR)

# Générer la documentation en format PDF (LaTeX) (optionnel)
latex:
	$(SPHINX) -b latex $(SOURCE_DIR) $(BUILD_DIR)/latex