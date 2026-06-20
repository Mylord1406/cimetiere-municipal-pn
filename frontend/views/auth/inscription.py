import flet as ft
from config import COULEURS, APP_NOM


def vue_inscription(page: ft.Page, on_success, on_login):

    prenom_input = ft.TextField(
        label="Prénom *",
        prefix_icon=ft.icons.PERSON,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    nom_input = ft.TextField(
        label="Nom *",
        prefix_icon=ft.icons.PERSON,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    email_input = ft.TextField(
        label="Adresse email *",
        prefix_icon=ft.icons.EMAIL,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
        keyboard_type=ft.KeyboardType.EMAIL,
    )
    telephone_input = ft.TextField(
        label="Téléphone *",
        prefix_icon=ft.icons.PHONE,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    adresse_input = ft.TextField(
        label="Adresse",
        prefix_icon=ft.icons.LOCATION_ON,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    password_input = ft.TextField(
        label="Mot de passe *",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.icons.LOCK,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )
    confirm_password_input = ft.TextField(
        label="Confirmer le mot de passe *",
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.icons.LOCK,
        border_radius=10,
        focused_border_color=COULEURS["primaire"],
        color="black",
        expand=True,
    )

    message = ft.Text("", color=COULEURS["danger"], size=13)
    loading = ft.ProgressRing(width=20, height=20, visible=False)

    def on_inscrire(e):
        from api_client import client

        # Validation
        if not all([prenom_input.value, nom_input.value, email_input.value,
                    telephone_input.value, password_input.value, confirm_password_input.value]):
            message.value = "Veuillez remplir tous les champs obligatoires (*)"
            page.update()
            return

        if password_input.value != confirm_password_input.value:
            message.value = "Les mots de passe ne correspondent pas."
            page.update()
            return

        if len(password_input.value) < 8:
            message.value = "Le mot de passe doit contenir au moins 8 caractères."
            page.update()
            return

        loading.visible = True
        btn_inscrire.disabled = True
        message.value = ""
        page.update()

        data = {
            "email": email_input.value,
            "password": password_input.value,
            "nom": nom_input.value,
            "prenom": prenom_input.value,
            "telephone": telephone_input.value,
            "adresse": adresse_input.value or "",
            "role_nom": "CLIENT",
        }

        result = client.inscrire(data)
        
        loading.visible = False
        btn_inscrire.disabled = False

        if "créé" in result.get("message", ""):
            on_success(email_input.value)
        else:
            message.value = result.get("message", "Erreur lors de l'inscription.")

        page.update()

    btn_inscrire = ft.ElevatedButton(
        text="Créer mon compte",
        width=400,
        height=48,
        bgcolor=COULEURS["primaire"],
        color="white",
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=on_inscrire,
    )

    return ft.Container(
        content=ft.Row(
            controls=[
                # Panneau gauche
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(ft.icons.HOME_WORK, size=70, color="white"),
                            ft.Container(height=15),
                            ft.Text(APP_NOM, size=20, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                            ft.Container(height=10),
                            ft.Text("République du Congo", size=13, color="#FFFFFFB3", text_align=ft.TextAlign.CENTER),
                            ft.Container(height=40),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(controls=[ft.Icon(ft.icons.CHECK_CIRCLE, color="#4CAF50", size=16), ft.Text("Réservez un caveau en ligne", color="white", size=13)], spacing=8),
                                        ft.Row(controls=[ft.Icon(ft.icons.CHECK_CIRCLE, color="#4CAF50", size=16), ft.Text("Suivez vos demandes", color="white", size=13)], spacing=8),
                                        ft.Row(controls=[ft.Icon(ft.icons.CHECK_CIRCLE, color="#4CAF50", size=16), ft.Text("Payez en toute sécurité", color="white", size=13)], spacing=8),
                                        ft.Row(controls=[ft.Icon(ft.icons.CHECK_CIRCLE, color="#4CAF50", size=16), ft.Text("Accédez à la carte interactive", color="white", size=13)], spacing=8),
                                    ],
                                    spacing=12,
                                ),
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    bgcolor=COULEURS["primaire"],
                    width=380,
                    padding=40,
                    expand=False,
                ),
                # Panneau droit — formulaire
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(height=20),
                            ft.Icon(ft.icons.PERSON_ADD, size=45, color=COULEURS["primaire"]),
                            ft.Container(height=8),
                            ft.Text("Créer un compte", size=24, weight=ft.FontWeight.BOLD, color=COULEURS["titre"]),
                            ft.Text("Rejoignez le portail du cimetière municipal", size=13, color=COULEURS["texte_clair"]),
                            ft.Container(height=20),
                            ft.Row(controls=[prenom_input, nom_input], spacing=10),
                            ft.Container(height=8),
                            email_input,
                            ft.Container(height=8),
                            telephone_input,
                            ft.Container(height=8),
                            adresse_input,
                            ft.Container(height=8),
                            ft.Row(controls=[password_input, confirm_password_input], spacing=10),
                            ft.Container(height=5),
                            message,
                            ft.Container(height=10),
                            btn_inscrire,
                            loading,
                            ft.Container(height=10),
                            ft.Row(
                                controls=[
                                    ft.Text("Déjà un compte ?", size=13, color=COULEURS["texte_clair"]),
                                    ft.TextButton(
                                        "Se connecter",
                                        style=ft.ButtonStyle(color=COULEURS["primaire"]),
                                        on_click=lambda e: on_login(),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Container(height=20),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO,
                        spacing=0,
                    ),
                    expand=True,
                    bgcolor="white",
                    padding=ft.padding.symmetric(horizontal=40, vertical=10),
                ),
            ],
            expand=True,
            spacing=0,
        ),
        expand=True,
    )