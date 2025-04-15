from kivymd.app import MDApp  # Clase base de cualquier app con KivyMD (Material Design)
from kivymd.uix.label import MDLabel  # Etiqueta de texto con estilo Material Design
from kivymd.uix.button import MDRaisedButton  # Botón elevado (con sombra), típico de Material Design
from kivymd.uix.boxlayout import MDBoxLayout  # Layout que organiza widgets en filas o columnas
from kivymd.uix.screen import Screen  # Contenedor principal de widgets, representa una pantalla
from kivymd.uix.toolbar.toolbar import MDTopAppBar  # Barra superior de la app (título, botones, etc.)

class ContadorApp(MDApp):  # Clase principal de la app, hereda de MDApp
    def build(self):  # Método que se ejecuta al iniciar la app
        self.contador = 0  # Variable para contar (inicia en 0)

        layout = MDBoxLayout(orientation="vertical", padding=20)  # Layout vertical con espacio alrededor (padding)
        toolbar = MDTopAppBar(title="Contador KivyMD")  # Barra superior con título
        layout.add_widget(toolbar)  # Se añade la barra al layout principal

        self.label = MDLabel(  # Creamos una etiqueta de texto para mostrar el contador
            text=str(self.contador),  # El número del contador, convertido a texto
            halign="center",  # Centrado horizontalmente
            font_style="H3"  # Estilo grande del texto (H3 es un tamaño de encabezado)
        )
        layout.add_widget(self.label)  # Se añade la etiqueta al layout

        btn_layout = MDBoxLayout(spacing=20)  # Layout horizontal para los botones, con espacio entre ellos
        btn_mas = MDRaisedButton(text="+", on_release=self.incrementar)  # Botón para incrementar
        btn_menos = MDRaisedButton(text="-", on_release=self.decrementar)  # Botón para decrementar
        btn_layout.add_widget(btn_menos)  # Se añade el botón "-" al layout de botones
        btn_layout.add_widget(btn_mas)  # Se añade el botón "+" al layout de botones

        layout.add_widget(btn_layout)  # Se añade el layout de botones al layout principal

        screen = Screen()  # Creamos una pantalla (contenedor principal)
        screen.add_widget(layout)  # Añadimos el layout a la pantalla
        return screen  # Devolvemos la pantalla como contenido principal de la app

    def incrementar(self, instance):  # Función que se llama al presionar el botón "+"
        self.contador += 1  # Aumenta el valor del contador en 1
        self.label.text = str(self.contador)  # Actualiza el texto del label con el nuevo valor

    def decrementar(self, instance):  # Función que se llama al presionar el botón "-"
        self.contador -= 1  # Disminuye el valor del contador en 1
        self.label.text = str(self.contador)  # Actualiza el texto del label con el nuevo valor

ContadorApp().run()  # Crea una instancia de la app y la ejecuta