# Configuration du frontend
API_BASE_URL = "https://cimetiere-municipal-pn-production.up.railway.app/api/v1"

# Couleurs de l'application — Thème Violet Élégant Sombre
COULEURS = {
    "primaire":     "#800080",   # Purple pur classique
    "secondaire":   "#9C27B0",   # Violet profond et riche
    "accent":       "#E040FB",   # Violet rose lumineux
    "success":      "#00C896",   # Vert émeraude
    "danger":       "#FF4D6D",   # Rose rouge
    "warning":      "#FFB703",   # Or ambré
    "gris":         "#8892A4",   # Gris bleuté
    "fond":         "#0F0A1E",   # Fond très sombre violet-noir
    "blanc":        "#FFFFFF",   # Blanc pur pour les cartes
    "texte":        "#1A1A2E",   # Texte SOMBRE pour les cartes blanches
    "texte_clair":  "#555577",   # Gris foncé pour sous-titres dans cartes
    "titre":        "#FFFFFF",   # Blanc pur pour titres sur fond sombre
}

# Statuts caveaux
STATUTS_CAVEAUX = {
    "DISPONIBLE":      {"label": "Disponible",      "couleur": "#00C896"},
    "RESERVE":         {"label": "Réservé",          "couleur": "#FFB703"},
    "OCCUPE":          {"label": "Occupé",           "couleur": "#FF4D6D"},
    "NON_EXPLOITABLE": {"label": "Non exploitable",  "couleur": "#8892A4"},
    "MAINTENANCE":     {"label": "Maintenance",      "couleur": "#E040FB"},
}

# Nom de l'application
APP_NOM = "Cimetière Municipal de Pointe-Noire"
APP_VERSION = "1.0.0"