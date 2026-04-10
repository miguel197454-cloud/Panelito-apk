from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from chatbot_logic import get_response


class ChatApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # fondo gris claro

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 🔥 Scroll para el chat
        self.scroll = ScrollView(size_hint=(1, 0.8))

        self.chat_label = Label(
            text="🤖 Panelito: ¡Hola! Estoy listo para ayudarte ☀️\n",
           size_hint_y=None,
           markup=True,
            color=(0, 0, 0, 1)  # 👈 ESTA ES LA CLAVE
        )

        # 👇 clave para saltos de línea automáticos
        self.chat_label.bind(
            width=lambda *x: self.chat_label.setter('text_size')(self.chat_label, (self.chat_label.width, None)),
            texture_size=lambda *x: self.chat_label.setter('height')(self.chat_label, self.chat_label.texture_size[1])
        )

        self.scroll.add_widget(self.chat_label)

        # 🔤 Input
        self.user_input = TextInput(
            size_hint=(1, 0.1),
            multiline=False,
            hint_text="Escribe tu mensaje..."
        )

        # 🔘 Botón
        self.send_button = Button(
            text="Enviar",
            size_hint=(1, 0.1),
            background_color=(0.2, 0.6, 0.2, 1)  # verde
        )
        self.send_button.bind(on_press=self.send_message)

        # agregar todo
        main_layout.add_widget(self.scroll)
        main_layout.add_widget(self.user_input)
        main_layout.add_widget(self.send_button)

        return main_layout

    def send_message(self, instance):
        message = self.user_input.text.strip()

        if message == "":
            return

        response = get_response(message)

        # 🧠 formateo con saltos de línea
        formatted_text = f"\n[b]Tú:[/b] {message}\n[b]Panelito:[/b] {response}\n"

        self.chat_label.text += formatted_text

        # 🔥 auto scroll hacia abajo
        self.scroll.scroll_y = 0

        self.user_input.text = ""


if __name__ == "__main__":
    ChatApp().run()