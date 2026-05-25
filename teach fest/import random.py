import flet as ft
import flet_audio as fta
def main(page: ft.Page):

#function
    def animate(e):
        e.control.scale = 1.1 if e.data else 1.0

    def animate_end(e):
        e.control.scale = 1.0 if e.data else 1.1

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
        page.window.resizable = False
        page.add(free_deaf ,the_sun_basic,sunnie,The_solarito,solarito,the_planetaro,exio,nutro,neutronian,lowie,going)

    def go_to_info_cinco(e):
        page.controls.clear()
        page.scroll = ft.ScrollMode.AUTO
        page.window.resizable = False
        page.add(diez_deaf,the_sun_cinco,sunnie,The_solaritos,solarito,the_planetarios,exio,neutro,neutronian,blacky,blacks,Superito,supervio,lowie,going)

    
    def go_to_info_seis_siete(e):
        page.controls.clear()
        page.scroll = ft.ScrollMode.AUTO
        page.window.resizable = False
        page.add(sechi_deaf,the_sun_tweny,sunnie,The_solarilos,solarito,the_planetarioss,exio,neutron,neutronian,blacker,blacks,Superilo,supervio,expansion,universe,timmy,timta,beginning,biggie,ending,death,lowie,going)
    
    
    def go_home(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.controls.clear()
            page.scroll = False
            page.add(tiele, every_botton_light,lower) 
        
        else:
            page.controls.clear()
            page.scroll = False
            page.add(tiele, every_botton,lower) 

#audio funtions 

    async def play(e):
        await audio.play()
    
    async def pause(e):
        await audio.pause()

    async def resume(e):
        await audio.resume()

    async def next_song(e):
    
        freeer[0] = (freeer[0] + 1) % len(free)
        audio.src = free[freeer[0]]
        await audio.play()

    async def prev_song(e):
        freeer[0] = (freeer[0] - 1) % len(free)
        audio.src = free[freeer[0]]
        await audio.play()

#10 dollar one
    async def play_10(e):
        await dies.play()
    
    async def pause_10(e):
        await dies.pause()

    async def resume_10(e):
        await dies.resume()

    async def next_song_10(e):
            sir[0] = (sir[0] + 1) % len(diez)
            dies.src = diez[sir[0]]
            await dies.play()

    async def prev_song_10(e):
        sir[0] = (sir[0] - 1) % len(diez)
        dies.src = diez[sir[0]]
        await dies.play()


#20 dollar one
    async def play_20(e):
        await sies.play()
    
    async def pause_20(e):
        await sies.pause()

    async def resume_20(e):
        await sies.resume()

    async def next_song_20(e):
            veinte[0] = (veinte[0] + 1) % len(vinti)
            sies.src = vinti[veinte[0]]
            await sies.play()

    async def prev_song_20(e):
        veinte[0] = (veinte[0] - 1) % len(vinti)
        sies.src = vinti[veinte[0]]
        await sies.play()




#audios
    free = [
        "audio/sun.mp3",
        "audio/solarsss.mp3",
        "audio/exoss.mp3",
        "audio/netro.mp3",
      
    ]

    freeer = [0]

    audio = fta.Audio(src = free[freeer[0]])


    diez = [
        "audio/sun5.mp3",
        "audio/solar5.mp3",
        "audio/exo5.mp3",
        "audio/netro5.mp3",
        "audio/super5.mp3",
        "audio/black.mp3"]

    sir = [0]

    dies = fta.Audio(src = diez[sir[0]])

    vinti = [
        "audio/sun20.mp3",
        "audio/solar20.mp3",
        "audio/exo20.mp3",
        "audio/neutron20.mp3",
        "audio/black20.mp3",
        "audio/sup20.mp3",
        "audio/expansion20.mp3",
        "audio/timpo20.mp3",
        "audio/beggining.mp3",
        "audio/death.mp3",


]
    
    veinte = [0]
    sies = fta.Audio(src = diez[sir[0]])

    page.services.append(audio)
    page.services.append(dies)
    page.services.append(sies)








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
    


    #5$ textss
    the_sun_cinco = ft.Text(value ="☀️ The Sun"
                "The Sun is the star at the center of our Solar System. "
                "It is a giant ball of hot plasma held together by gravity. "
                "Its core reaches 15 million °C, where hydrogen atoms fuse into "
                "helium and release enormous amounts of energy — the same energy "
                "that warms our planet and makes life on Earth possible. "
                "The Sun makes up 99.86% of all the mass in the Solar System. "
                "It also produces solar winds that travel across space and can affect planets. "
                "Without the Suns energy, Earth would be a frozen and lifeless world.", 
                size = 15, font_family = "Comic Sans Ms", color = "orange" )

    The_solaritos = ft.Text(value ="🪐 The Solar System"
                "The Solar System is everything that orbits our Sun. "
                "It includes 8 planets, dozens of moons, and countless asteroids and comets. "
                "The four inner planets (Mercury, Venus, Earth, Mars) are rocky. "
                "The four outer planets (Jupiter, Saturn, Uranus, Neptune) are huge balls of gas or ice. "
                "It formed about 4.6 billion years ago from a giant cloud of dust and gas. "
                "Gravity keeps all these objects moving in predictable paths called orbits. "
                "Scientists study the Solar System to understand how planets and life can form.", 
                size = 15, font_family = "Comic Sans Ms", color = "blue" )

    the_planetarios = ft.Text(value ="🌍 Exoplanets"
                "Exoplanets are planets that orbit stars other than our Sun. "
                "Over 5,600 have been confirmed so far! "
                "Some are giant gas planets bigger than Jupiter. "
                "Others are small rocky worlds that might have liquid water. ", 
                size = 15, font_family = "Comic Sans Ms",color= ft.Colors.GREEN,
                spans = [ft.TextSpan(text = 
                "Scientists are especially excited about planets in the 'habitable zone"
                "the right distance from their star where life could possibly exist. "
                "New telescopes allow scientists to study the atmospheres of some exoplanets. "
                "This helps researchers search for signs of life beyond our Solar System.",style = ft.TextStyle(color = ft.Colors.BLUE))] )


    neutro = ft.Text(value ="🌠 A neutron star"
                "                        is the incredibly dense core left behind afte" 
                        " a massive star explodes in a supernova." 
                        " It is made mostly of tightly packed neutrons, so dense that a teaspoon" 
                        " would weigh billions of tons on Earth. Neutron stars often spin rapidly and can emit beams of" 
                        " radiation, which we observe as pulsars. "
                        "Some neutron stars have extremely strong magnetic fields called magnetars. "
                        "They are among the most extreme and fascinating objects in the universe.", 
                size = 15, font_family = "Comic Sans Ms", color = "cyan" )
    
    
    blacky = ft.Text(value ="🕳️A black hole is a region in space where gravity is so strong that nothing, not even light, can escape."
      "It forms when a massive star collapses at the end of its life, compressing its core into an extremely dense point called a singularity."
      "Around this center is the event horizon, which marks the boundary beyond which anything that enters cannot return."
      "Black holes can bend light and distort space and time due to their intense gravity.",
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.WHITE,
                 spans= [ft.TextSpan(text =  "They are often surrounded by glowing material called an accretion disk, formed by gas and dust falling inward."
                            "Despite their power, black holes do not pull in everything around them—objects must get very close to be affected."
                "Scientists study black holes to better understand gravity, the structure of the universe, and the laws of physics.",style = ft.TextStyle(color=ft.Colors.ORANGE_300))])
    
    
    Superito = ft.Text(value ="💥A supernova is a powerful and dramatic explosion that occurs at the end of a stars life cycle."
                        "It can happen when a massive star runs out of fuel and collapses, or when a white dwarf gains too much mass from a nearby star.",
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.BLUE_ACCENT,
                 spans = [ft.TextSpan(text = "This explosion releases an enormous amount of energy and light, sometimes outshining an entire galaxy for a short time."
                        "Supernovas create shock waves that spread elements like iron, gold, and oxygen into space.",style = ft.TextStyle(color=ft.Colors.RED_900)),
                         ft.TextSpan(text = "These elements are essential for forming new stars, planets, and even life."
                        "The explosion can leave behind a neutron star or even form a black hole.",style = ft.TextStyle(color=ft.Colors.YELLOW_900)),
                         ft.TextSpan(text = "Scientists study supernovas to learn more about how stars evolve and how the universe is constantly changing.",style = ft.TextStyle(color=ft.Colors.PURPLE_900))])
    

#Vip
    the_sun_tweny = ft.Text(value ="☀️ The Sun "
                "The Sun is the star at the center of our Solar System. "
                "It is a giant ball of hot plasma held together by gravity. "
                "Its core reaches 15 million °C, where hydrogen atoms fuse into "
                "helium and release enormous amounts of energy — the same energy "
                "that warms our planet and makes life on Earth possible. "
                "The Sun makes up 99.86% of all the mass in the Solar System. "
                "It also produces solar winds that travel across space and can affect planets. "
                "Without the Sun's energy, Earth would be a frozen and lifeless world. "
                "The Sun is about 4.6 billion years old and is considered a middle-aged star. "
                "It will continue shining for about 5 billion more years before changing dramatically. "
                "The outer layer of the Sun, called the corona, is hotter than its surface. "
                "Scientists study the Sun to better understand space weather and its effects on Earth.", 
                size = 15, font_family = "Comic Sans Ms", color = "orange" )


    The_solarilos = ft.Text(value ="🪐 The Solar System "
                "The Solar System is everything that orbits our Sun. "
                "It includes 8 planets, dozens of moons, and countless asteroids and comets. "
                "The four inner planets (Mercury, Venus, Earth, Mars) are rocky. "
                "The four outer planets (Jupiter, Saturn, Uranus, Neptune) are huge balls of gas or ice. "
                "It formed about 4.6 billion years ago from a giant cloud of dust and gas. "
                "Gravity keeps all these objects moving in predictable paths called orbits. "
                "Scientists study the Solar System to understand how planets and life can form."
                "The Solar System also contains dwarf planets like Pluto and Eris. "
                "Asteroid belts and the Kuiper Belt are regions filled with rocky and icy objects. "
                "Beyond the Kuiper Belt lies the Oort Cloud, a distant region of icy bodies. "
                "Space missions help scientists explore planets and gather valuable data.", 
                size = 15, font_family = "Comic Sans Ms", color = "blue" )


    the_planetarioss = ft.Text(value ="🌍 Exoplanets "
                "Exoplanets are planets that orbit stars other than our Sun. "
                "Over 5,600 have been confirmed so far! "
                "Some are giant gas planets bigger than Jupiter. "
                "Others are small rocky worlds that might have liquid water. "
                "Some exoplanets orbit very close to their stars and are extremely hot. "
                "Others are located far away and are covered in ice. "
                "A few exoplanets have atmospheres that scientists can study for gases. "
                "Discoveries of exoplanets help scientists understand how unique our Solar System is. ", 
                size = 15, font_family = "Comic Sans Ms",color= ft.Colors.GREEN,
                spans = [ft.TextSpan(text = 
                "Scientists are especially excited about planets in the 'habitable zone' "
                "the right distance from their star where life could possibly exist. "
                "New telescopes allow scientists to study the atmospheres of some exoplanets. "
                "This helps researchers search for signs of life beyond our Solar System. "
                "Future missions may even capture direct images of Earth-like exoplanets. "
                "These discoveries could answer one of humanity’s biggest questions: are we alone?",style = ft.TextStyle(color = ft.Colors.BLUE))] )


    neutron = ft.Text(value ="🌠 A neutron star "
                "is the incredibly dense core left behind after a massive star explodes in a supernova. "
                "It is made mostly of tightly packed neutrons, so dense that a teaspoon "
                "would weigh billions of tons on Earth. "
                "Neutron stars often spin rapidly and can emit beams of radiation, which we observe as pulsars. "
                "Some neutron stars have extremely strong magnetic fields called magnetars. "
                "They are among the most extreme and fascinating objects in the universe. "
                "Neutron stars can rotate hundreds of times per second. "
                "Their gravity is so strong that it significantly bends nearby light. "
                "Collisions between neutron stars can create gravitational waves. "
                "These collisions also produce heavy elements like gold and platinum.", 
                size = 15, font_family = "Comic Sans Ms", color = "cyan" )


    blacker = ft.Text(value ="🕳️ A black hole is a region in space where gravity is so strong that nothing, not even light, can escape. "
      "It forms when a massive star collapses at the end of its life, compressing its core into an extremely dense point called a singularity. "
      "Around this center is the event horizon, which marks the boundary beyond which anything that enters cannot return. "
      "Black holes can bend light and distort space and time due to their intense gravity. "
      "Some black holes are millions or even billions of times more massive than the Sun. "
      "These supermassive black holes are found at the centers of most galaxies. "
      "Black holes can merge and release powerful bursts of gravitational waves. "
      "They play an important role in shaping galaxies over time. ",
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.WHITE,
                 spans= [ft.TextSpan(text =  "They are often surrounded by glowing material called an accretion disk, formed by gas and dust falling inward. "
                            "Despite their power, black holes do not pull in everything around them—objects must get very close to be affected. "
                "Scientists study black holes to better understand gravity, the structure of the universe, and the laws of physics. "
                "Some black holes emit powerful jets of energy from their poles. "
                "These jets can extend for thousands of light-years into space.",style = ft.TextStyle(color=ft.Colors.ORANGE_300))])


    Superilo = ft.Text(value ="💥 A supernova is a powerful and dramatic explosion that occurs at the end of a star's life cycle. "
                        "It can happen when a massive star runs out of fuel and collapses, or when a white dwarf gains too much mass from a nearby star. "
                        "Supernovas can briefly outshine entire galaxies. "
                        "They release shockwaves that spread material through space. ",
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.BLUE_ACCENT,
                 spans = [ft.TextSpan(text = "This explosion releases an enormous amount of energy and light, sometimes outshining an entire galaxy for a short time. "
                        "Supernovas create shock waves that spread elements like iron, gold, and oxygen into space. "
                        "These explosions help trigger the formation of new stars. "
                        "They also enrich space with the building blocks of planets. ",style = ft.TextStyle(color=ft.Colors.RED_900)),
                         ft.TextSpan(text = "These elements are essential for forming new stars, planets, and even life. "
                        "The explosion can leave behind a neutron star or even form a black hole. "
                        "Supernovas can influence the structure of entire galaxies. "
                        "They are key to the recycling of cosmic material. ",style = ft.TextStyle(color=ft.Colors.YELLOW_900)),
                         ft.TextSpan(text = "Scientists study supernovas to learn more about how stars evolve and how the universe is constantly changing. "
                        "Observing supernovas helps measure distances in space. "
                        "They also provide clues about dark energy. "
                        "Each supernova tells a unique story about the star that created it.",style = ft.TextStyle(color=ft.Colors.PURPLE_900))])


    expansion = ft.Text(value ="🌌 Expansion of the Universe "
                "The universe has been expanding ever since it began. "
                "Galaxies are moving away from each other, and the farther they are, the faster they move. "
                "This discovery was first observed by Edwin Hubble. "
                "The expansion means that space itself is stretching over time. "
                "Scientists believe this expansion is accelerating due to a mysterious force called dark energy. "
                "As space expands, light from distant galaxies becomes redshifted. "
                "This allows astronomers to measure how fast objects are moving away. "
                "In the far future, galaxies may become so distant that they are no longer visible from Earth.", 
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.DEEP_PURPLE_300)


    timmy = ft.Text(value ="⏳ Time Dilation "
                "Time dilation is a concept from Einsteins theory of relativity. "
                "It means that time can pass at different speeds depending on gravity and motion. "
                "The stronger the gravity, the slower time moves. "
                "This effect becomes very noticeable near massive objects like black holes. "
                "Time also slows down when an object moves close to the speed of light. "
                "Astronauts traveling at high speeds experience slightly slower time than people on Earth. "
                "This has been proven using precise atomic clocks. "
                "Time dilation shows that time is not absolute, but flexible and affected by the universe.", 
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.AMBER_300)


    beginning = ft.Text(value ="💥 The Beginning of the Universe "
                "The universe began with an event known as the Big Bang around 13.8 billion years ago. "
                "At that moment, all space, time, and energy started expanding from a single point. "
                "In the first seconds, the universe was extremely hot and dense. "
                "As it expanded, it cooled and allowed particles to form atoms. "
                "Eventually, gravity pulled matter together to form stars and galaxies. "
                "The leftover radiation from this event can still be detected today. "
                "This is called the cosmic microwave background. "
                "Scientists study it to understand the early universe and how everything began.", 
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.RED_ACCENT)


    ending = ft.Text(value ="🧊 The End of the Universe Theories "
                "Scientists are not sure how the universe will end, but there are several theories. "
                "One idea is the Big Freeze, where expansion continues until stars burn out and everything becomes cold and dark. "
                "Another theory is the Big Crunch, where gravity stops expansion and pulls everything back together. "
                "There is also the Big Rip, where expansion speeds up so much that galaxies, stars, and even atoms are torn apart. "
                "Each theory depends on how strong dark energy is over time. "
                "Observations suggest the universe may keep expanding forever. "
                "If that happens, galaxies will drift apart and space will grow increasingly empty. "
                "Understanding the universes fate helps scientists learn more about its nature and laws.", 
                size = 15, font_family = "Comic Sans Ms", color = ft.Colors.BLUE_GREY_200)
                

    title = ft.Text(value = "The Museum", size = 80, font_family = "Charter",color = "purple",weight = ft.FontWeight.BOLD,)
    

#page
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(image=ft.DecorationImage(src="images/stars.png",fit="cover"))
    page.window.resizable = False
   



#buttons


    sixie = ft.Button("Go back", on_click=go_home)

    btn = ft.Button(on_animation_end=animate_end ,on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/red.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("0$",font_family = "Comic Sans MS",color="purple")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),
    )

    six = ft.Button(on_animation_end=animate_end,on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info_cinco,

        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0,),
        

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/supernova.png",width=175,height=175,fit="cover"),border_radius=10,),ft.Text("10$",font_family = "Comic Sans MS",color="purple")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    eightnin = ft.Button(on_animation_end=animate_end,on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info_seis_siete,
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
    btn_light = ft.Button(on_animation_end=animate_end, on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/whit.png",width=175,height=167,fit="cover"),border_radius=10,),ft.Text("0$",font_family = "Comic Sans MS",color = "black")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)


    six_light = ft.Button(on_animation_end=animate_end, on_hover = animate,scale=1,animate_scale=200,on_click=go_to_info_cinco,

        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),padding=0,),
        

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/whitnova.png",width=175,height=167,fit="cover"),border_radius=10,),ft.Text("10$",font_family = "Comic Sans MS",color = "black")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)
    

    eightnin_light = ft.Button(on_animation_end=animate_end, on_hover = animate,scale=1,animate_scale=200,on_click = go_to_info_seis_siete,
        style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),padding=0),

        content=ft.Column(
            [
                ft.Container(content=ft.Image(src="images/whitgala.png",width=500,height=175,fit="cover"),border_radius=20,),ft.Text("Vip 20$",font_family = "Comic Sans MS",color = "black")]
                ,alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=5,),)

    every_botton_light = ft.Column(
            [ft.Row([btn_light,six_light,],alignment=ft.MainAxisAlignment.CENTER,spacing=25,expand = True),
            eightnin_light],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15, expand=True)
    

#buttons pt 2
    player = ft.Button("play", on_click = play)
    pausing = ft.Button("pause", on_click = pause)
    resumin = ft.Button("resume", on_click = resume)
    nexxie = ft.Button("next text", on_click = next_song)
    prev = ft.Button("previous tex", on_click = prev_song)

    free_deaf =ft.Row([player,pausing,resumin,nexxie,prev])

    player10 = ft.Button("play", on_click = play_10)
    pausing10 = ft.Button("pause", on_click = pause_10)
    resumin10 = ft.Button("resume", on_click = resume_10)
    nexxie10 = ft.Button("next text", on_click = next_song_10)
    prev10 = ft.Button("previous tex", on_click = prev_song_10)

    diez_deaf =ft.Row([player10,pausing10,resumin10,nexxie10,prev10])

    player20 = ft.Button("play", on_click = play_20)
    pausing20 = ft.Button("pause", on_click = pause_20)
    resumin20 = ft.Button("resume", on_click = resume_20)
    nexxie20 = ft.Button("next text", on_click = next_song_20)
    prev20 = ft.Button("previous tex", on_click = prev_song_20)

    sechi_deaf =ft.Row([player20,pausing20,resumin20,nexxie20,prev20])






    
    #images
    sunnie = ft.Container(content=ft.Image(src="images/sunnie.png", width=450, height=450),alignment=ft.Alignment.CENTER,
    expand=True,)    
    solarito = ft.Container(content=ft.Image(src="images/thesolarito.png", width=550, height=450),alignment=ft.Alignment.CENTER,
    expand=True,)

    exio = ft.Container(content=ft.Image(src="images/exio.png", width=650, height=650),alignment=ft.Alignment.CENTER,
    expand=True,)

    neutronian = ft.Container(content=ft.Image(src="images/neutronia.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    blacks = ft.Container(content=ft.Image(src="images/blacky.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    supervio = ft.Container(content=ft.Image(src="images/superito.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    universe = ft.Container(content=ft.Image(src="images/universe.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    timta = ft.Container(content=ft.Image(src="images/timtam.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    biggie = ft.Container(content=ft.Image(src="images/biggie.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    death = ft.Container(content=ft.Image(src="images/death.png", width=900, height=900),alignment=ft.Alignment.CENTER,
    expand=True,)

    #icons

    theme_icon = ft.IconButton(icon=ft.Icons.LIGHT_MODE,
    on_click=updateTheme)

    theme_ico = ft.IconButton(icon=ft.Icons.LIGHT_MODE,
    on_click=updateTheme2)


    #rows/columns
    going = ft.Row(controls=[sixie],alignment=ft.MainAxisAlignment.END)
    lower = ft.Row(controls=[theme_icon],alignment=ft.MainAxisAlignment.END)
    lowie = ft.Row(controls=[theme_ico],alignment=ft.MainAxisAlignment.END)
    tiele = ft.Row(controls = [title], alignment = ft.MainAxisAlignment.CENTER)

    page.add(tiele,every_botton,lower)

ft.run(main, assets_dir = "assets")