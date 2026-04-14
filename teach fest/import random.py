import flet as ft

def main(page: ft.Page):

#function
    def animate(e):
        e.control.scale = 1.1 if e.data else 1.0

    def updateTheme(e):
        if themeSwitch.value == True:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK



    title = ft.Text(value = "The Museum", size = 80, font_family = "Comic Sans MS",color = "purple",weight = ft.FontWeight.BOLD,)

#page
    page.bgcolor = ft.Colors.BLUE_100

#buttons
    btn = ft.Button(on_hover = animate,scale=1,animate_scale=200,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/red.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("0$",font_family = "Comic Sans MS")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),
    )

    six = ft.Button(on_hover = animate,scale=1,animate_scale=200,

        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0,),
        

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/supernova.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("10$",font_family = "Comic Sans MS")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    eightnin = ft.Button(on_hover = animate,scale=1,animate_scale=200,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/galazy.png",width=500,height=175,fit="cover"),border_radius=20,),ft.Text("Vip 20$",font_family = "Comic Sans MS")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    every_botton = ft.Column(
            [ft.Row([btn,six,],alignment=ft.MainAxisAlignment.CENTER,spacing=85,),
            eightnin],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,)

    themeSwitch = ft.Switch(value=False, label="Change theme (LIGHT/DARK)",on_change = updateTheme)

    lower = ft.Row(controls=[themeSwitch],alignment=ft.MainAxisAlignment.END)
    tiele = ft.Row(controls = [title], alignment = ft.MainAxisAlignment.CENTER)

    page.add(tiele,every_botton,lower)

ft.run(main, assets_dir = "assets")