import flet as ft
def main(page: ft.Page):

#function
    def animate(e):
        e.control.scale = 1.1 if e.data else 1.0

    def updateTheme(e):

        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.controls.clear()
            page.add(tiele,every_botton,lower)
            page.bgcolor = ft.Colors.TRANSPARENT
            title.color = ft.Colors.PURPLE
            page.theme_mode = ft.ThemeMode.DARK
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="images/stars.png",fit="cover"))
            theme_icon.icon = ft.Icons.LIGHT_MODE

        
        else:
            ft.DecorationImage(src="images/stars.png", fit="cover")
            page.controls.clear()
            page.add(tiele,every_botton_light,lower)
            page.bgcolor = ft.Colors.TRANSPARENT
            title.color = ft.Colors.WHITE_60
            theme_icon.icon = ft.Icons.DARK_MODE
            page.theme_mode = ft.ThemeMode.LIGHT
            page.decoration = ft.BoxDecoration(
            image=ft.DecorationImage(src="images/white.png", fit="cover"))

    def updateTheme2(e):

        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.bgcolor = ft.Colors.TRANSPARENT
            title.color = ft.Colors.PURPLE
            page.theme_mode = ft.ThemeMode.DARK
            page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="images/stars.png",fit="cover"))
            theme_ico.icon = ft.Icons.LIGHT_MODE

        
        else:
            ft.DecorationImage(src="images/stars.png", fit="cover")
            page.bgcolor = ft.Colors.TRANSPARENT
            title.color = ft.Colors.WHITE_60
            theme_ico.icon = ft.Icons.DARK_MODE
            page.theme_mode = ft.ThemeMode.LIGHT
            page.decoration = ft.BoxDecoration(
            image=ft.DecorationImage(src="images/white.png", fit="cover"))
            
            


    
    def go_to_info(e):
        page.controls.clear()
        page.scroll = ft.ScrollMode.AUTO
        page.add(the_sun_basic,sunnie,The_solarito,solarito,the_planetaro,exio,nutro,neutronian,lowie,going)
    
    def go_home(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.controls.clear()
            page.scroll = False
            page.add(tiele, every_botton_light,lower) 
        
        else:
            page.controls.clear()
            page.scroll = False
            page.add(tiele, every_botton,lower) 


#textss
    title = ft.Text(value = "The Museum", size = 80, font_family = "Charter",color = "purple",weight = ft.FontWeight.BOLD,)
    
    the_sun_basic = ft.Text(value ="☀️ The Sun"
                    "The Sun is the star at the center of our Solar System. "
                    "It is a giant ball of hot plasma held together by gravity. "
                    "Its core reaches 15 million °C, where hydrogen atoms fuse into "
                    "helium and release enormous amounts of energy — the same energy "
                    "that warms our planet and makes life on Earth possible. "
                    "The Sun makes up 99.86% of all the mass in the Solar System.", size = 15, font_family = "Comic Sans Ms", color = "orange" )
    
    The_solarito = ft.Text(value ="🪐 The Solar System"
                    "The Solar System is everything that orbits our Sun. "
                    "It includes 8 planets, dozens of moons, and countless asteroids and comets. "
                    "The four inner planets (Mercury, Venus, Earth, Mars) are rocky. "
                    "The four outer planets (Jupiter, Saturn, Uranus, Neptune) are huge balls of gas or ice. "
                    "It formed about 4.6 billion years ago from a giant cloud of dust and gas.",size = 15, font_family = "Comic Sans Ms", color = "blue" )

    the_planetaro = ft.Text(value ="🌍 Exoplanets"
                    "Exoplanets are planets that orbit stars other than our Sun. "
                    "Over 5,600 have been confirmed so far! "
                    "Some are giant gas planets bigger than Jupiter. "
                    "Others are small rocky worlds that might have liquid water. "
                    "Scientists are especially excited about planets in the 'habitable zone"
                    "the right distance from their star where life could possibly exist.",size = 15, font_family = "Comic Sans Ms", color = "green" )
    
    nutro = ft.Text(value ="🌠 A neutron star"
    "                        is the incredibly dense core left behind afte" 
                            " a massive star explodes in a supernova." 
                            " It is made mostly of tightly packed neutrons, so dense that a teaspoon" 
                            " would weigh billions of tons on Earth. Neutron stars often spin rapidly and can emit beams of" 
                            " radiation, which we observe as pulsars.",size = 15, font_family = "Comic Sans Ms", color = "cyan" )

#page
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="images/stars.png",fit="cover"))



#buttons


    sixie = ft.Button("Go back", on_click=go_home)

    btn = ft.Button(on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/red.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("0$",font_family = "Comic Sans MS",color="purple")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),
    )

    six = ft.Button(on_hover = animate,scale=1,animate_scale=200,

        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0,),
        

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/supernova.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("10$",font_family = "Comic Sans MS",color="purple")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    eightnin = ft.Button(on_hover = animate,scale=1,animate_scale=200,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/galazy.png",width=500,height=175,fit="cover"),border_radius=20,),ft.Text("Vip 20$",font_family = "Comic Sans MS",color = "purple")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    every_botton = ft.Column(
            [ft.Row([btn,six,],alignment=ft.MainAxisAlignment.CENTER,spacing=30,),
            eightnin],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,)
    
    #buttons light
    btn_light = ft.Button(on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/whit.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("0$",font_family = "Comic Sans MS",color = "black")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)


    six_light = ft.Button(on_hover = animate,scale=1,animate_scale=200,

        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0,),
        

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/whitnova.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("10$",font_family = "Comic Sans MS",color = "black")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)
    

    eightnin_light = ft.Button(on_hover = animate,scale=1,animate_scale=200,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/whitgala.png",width=500,height=175,fit="cover"),border_radius=20,),ft.Text("Vip 20$",font_family = "Comic Sans MS",color = "black")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    every_botton_light = ft.Column(
            [ft.Row([btn_light,six_light,],alignment=ft.MainAxisAlignment.CENTER,spacing=25,expand = True),
            eightnin_light],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15, expand=True)
    



    
    #images
    sunnie = ft.Container(content=ft.Image(src="images/sunnie.png", width=450, height=450),alignment=ft.Alignment.CENTER,
    expand=True,)    
    solarito = ft.Container(content=ft.Image(src="images/thesolarito.png", width=550, height=450),alignment=ft.Alignment.CENTER,
    expand=True,)

    exio = ft.Container(content=ft.Image(src="images/exio.png", width=650, height=650),alignment=ft.Alignment.CENTER,
    expand=True,)

    neutronian = ft.Container(content=ft.Image(src="images/neutronia.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    theme_icon = ft.IconButton(icon=ft.Icons.LIGHT_MODE,
    on_click=updateTheme)

    theme_ico = ft.IconButton(icon=ft.Icons.LIGHT_MODE,
    on_click=updateTheme2)
    #Search Bar


    #rows/columns
    going = ft.Row(controls=[sixie],alignment=ft.MainAxisAlignment.END)
    lower = ft.Row(controls=[theme_icon],alignment=ft.MainAxisAlignment.END)
    lowie = ft.Row(controls=[theme_ico],alignment=ft.MainAxisAlignment.END)
    tiele = ft.Row(controls = [title], alignment = ft.MainAxisAlignment.CENTER)

    page.add(tiele,every_botton,lower)

ft.run(main, assets_dir = "assets")
#honestly im going to wait for the teacher to do anything else