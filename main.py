from flet import *

def main(page: Page):
    page.title = 'Mohammed'
    page.scroll = 'auto'
    page.window.width = 300
    page.window.height = 450
    page.window.top = 5
    page.window.left = 200
    page.bgcolor = "white"
    page.theme_mode = ThemeMode.LIGHT

    flashlight=Flashlight()
    page.overlay.append(flashlight)
    ph=PermissionHandler()
    page.overlay.append(ph)
    def open_app(e):
        ph.open_app_settings()

    # إضافة واجهة المستخدم
    page.add(#add
        AppBar(
            title=Text("Flash Light [ak]"),
            color="white",
            bgcolor="#D02B38",
            actions=[
                IconButton(icons.SETTINGS, on_click=open_app)
            ]
        ),
        # النص الرئيسي
        Row([
            Text("\n\nFlash Light App", size=30, color='black')
        ], alignment=MainAxisAlignment.CENTER),
        
        # الصورة
        Row([
            Image(src="flash.png", width=400)
        ], alignment=MainAxisAlignment.CENTER),
        
        # زر التشغيل
        Row([
            ElevatedButton(
                "On",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color="white",
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda e: flashlight.turn_on()
            ),
            # زر آخر (مثال)
            ElevatedButton(
                "Off",
                width=100,
                icon=icons.STOP,
                style=ButtonStyle(
                    bgcolor="#e3113e",
                    color="white",
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda e: flashlight.turn_off()
            )
        ], alignment=MainAxisAlignment.CENTER)
    )#add

    page.update()


app(main)
