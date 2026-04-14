import random
import flet as ft

def main(page: ft.Page):
#functions
    def normalClick(e):
        images = [
            "images/die1.png",
            "images/die2.png",
            "images/die3.png",
            "images/die4.png",
            "images/die5.png",
            "images/die6.png"
        ]

        random_image = random.choice(images)
        dice.src = random_image

    def sigmaClick(e):
        dice.src = "images/sigma.png"
#page
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#buttons
    dicebutton = ft.Button(content=ft.Text("Touch it to make it dice",size=20,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
    font_family="Comic Sans Ms"),on_click=normalClick)


    sigmabutton = ft.Button(content=ft.Text("this will make u sigma 🤫",style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),size=20,
    font_family="Comic Sans Ms"),on_click=sigmaClick)

    buttonrow = ft.Row(controls=[dicebutton, sigmabutton],alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.END)

    dice = ft.Image(src="images/die1.png")

    page.add(dice, buttonrow)

ft.run(main=main, assets_dir="assets")
