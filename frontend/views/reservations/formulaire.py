import flet as ft
from config import COULEURS


def vue_formulaire_reservation(page: ft.Page, on_success, on_cancel, caveau_id_preselect=None):
    from api_client import client

    # Récupérer les caveaux disponibles
    geojson = client.get_caveaux_geojson()
    caveaux_disponibles = [
        f for f in geojson.get("features", [])
        if f["properties"]["statut"] == "DISPONIBLE"
    ]

    # Champs défunt
    nom_input = ft.TextField(
        label="Nom du défunt",
        prefix_icon=ft.icons.PERSON,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    prenom_input = ft.TextField(
        label="Prénom du défunt",
        prefix_icon=ft.icons.PERSON,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    date_deces_input = ft.TextField(
        label="Date de décès (AAAA-MM-JJ)",
        prefix_icon=ft.icons.CALENDAR_TODAY,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        hint_text="ex: 2024-01-15",
        expand=True,
    )
    numero_acte_input = ft.TextField(
        label="Numéro acte de décès",
        prefix_icon=ft.icons.ARTICLE,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    telephone_famille_input = ft.TextField(
        label="Téléphone famille",
        prefix_icon=ft.icons.PHONE,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    nom_famille_input = ft.TextField(
        label="Nom responsable famille",
        prefix_icon=ft.icons.PEOPLE,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )

    # Choix caveau
    caveau_options = [
        ft.dropdown.Option(
            key=str(f["properties"]["id"]),
            text=f"Caveau {f['properties']['reference']} — Zone {f['properties']['zone']}",
        )
        for f in caveaux_disponibles
    ]

    caveau_dropdown = ft.Dropdown(
        label="Choisir un caveau",
        options=caveau_options,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        expand=True,
    )

    type_concession_dropdown = ft.Dropdown(
        label="Type de concession",
        options=[
            ft.dropdown.Option("TEMPORAIRE", "Temporaire (5 ans)"),
            ft.dropdown.Option("TRENTENAIRE", "Trentenaire (30 ans)"),
            ft.dropdown.Option("PERPETUELLE", "Perpétuelle"),
            ft.dropdown.Option("FAMILIALE", "Familiale"),
        ],
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        expand=True,
    )

    notes_input = ft.TextField(
        label="Notes (optionnel)",
        multiline=True,
        min_lines=3,
        border_radius=8,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )

    message = ft.Text("", color=COULEURS["danger"], size=13)
    loading = ft.ProgressRing(width=20, height=20, visible=False)

    def on_soumettre(e):
        # Validation
        if not all([
            nom_input.value,
            prenom_input.value,
            date_deces_input.value,
            caveau_dropdown.value,
            type_concession_dropdown.value,
        ]):
            message.value = "Veuillez remplir tous les champs obligatoires."
            page.update()
            return

        loading.visible = True
        btn_soumettre.disabled = True
        message.value = ""
        page.update()

        data = {
            "caveau_id": int(caveau_dropdown.value),
            "type_concession": type_concession_dropdown.value,
            "notes_client": notes_input.value or "",
            "defunt": {
                "nom": nom_input.value,
                "prenom": prenom_input.value,
                "date_deces": date_deces_input.value,
                "numero_acte_deces": numero_acte_input.value or "",
                "telephone_famille": telephone_famille_input.value or "",
                "nom_famille_responsable": nom_famille_input.value or "",
                "nationalite": "Congolaise",
                "sexe": "M",
            }
        }

        result = client.creer_reservation(data)

        loading.visible = False
        btn_soumettre.disabled = False

        if result.get("numero"):
            on_success(result)
        else:
            message.value = result.get("message", "Erreur lors de la soumission.")

        page.update()

    btn_soumettre = ft.ElevatedButton(
        text="Soumettre la réservation",
        icon=ft.icons.SEND,
        bgcolor=COULEURS["primaire"],
        color="white",
        height=45,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        on_click=on_soumettre,
        expand=True,
    )

    btn_annuler = ft.OutlinedButton(
        text="Annuler",
        height=45,
        style=ft.ButtonStyle(
            color=COULEURS["danger"],
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
        on_click=lambda e: on_cancel(),
        expand=True,
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.BOOK, color=COULEURS["primaire"], size=28),
                        ft.Text(
                            "Nouvelle réservation",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color=COULEURS["titre"],
                        ),
                    ],
                    spacing=10,
                ),
                ft.Text(
                    "Remplissez le formulaire pour soumettre une demande d'inhumation.",
                    size=13,
                    color=COULEURS["texte_clair"],
                ),
                ft.Container(height=20),

                # Section caveau
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Emplacement", size=15, weight=ft.FontWeight.BOLD, color=COULEURS["titre"]),
                            ft.Container(height=10),
                            ft.Row(controls=[caveau_dropdown], spacing=10),
                            ft.Row(controls=[type_concession_dropdown], spacing=10),
                        ],
                        spacing=10,
                    ),
                    bgcolor=COULEURS["blanc"],
                    border_radius=12,
                    padding=20,
                    shadow=ft.BoxShadow(blur_radius=6, color="#1A000000", offset=ft.Offset(0, 2)),
                ),
                ft.Container(height=15),

                # Section défunt
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Informations du défunt", size=15, weight=ft.FontWeight.BOLD, color=COULEURS["titre"]),
                            ft.Container(height=10),
                            ft.Row(controls=[nom_input, prenom_input], spacing=10),
                            ft.Row(controls=[date_deces_input, numero_acte_input], spacing=10),
                            ft.Row(controls=[nom_famille_input, telephone_famille_input], spacing=10),
                        ],
                        spacing=10,
                    ),
                    bgcolor=COULEURS["blanc"],
                    border_radius=12,
                    padding=20,
                    shadow=ft.BoxShadow(blur_radius=6, color="#1A000000", offset=ft.Offset(0, 2)),
                ),
                ft.Container(height=15),

                # Notes
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("Notes", size=15, weight=ft.FontWeight.BOLD, color=COULEURS["titre"]),
                            ft.Container(height=10),
                            notes_input,
                        ],
                        spacing=10,
                    ),
                    bgcolor=COULEURS["blanc"],
                    border_radius=12,
                    padding=20,
                    shadow=ft.BoxShadow(blur_radius=6, color="#1A000000", offset=ft.Offset(0, 2)),
                ),
                ft.Container(height=15),

                message,
                loading,
                ft.Row(
                    controls=[btn_annuler, btn_soumettre],
                    spacing=15,
                ),
                ft.Container(height=20),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=0,
        ),
        padding=ft.padding.all(25),
        expand=True,
        bgcolor=COULEURS["fond"],
    )