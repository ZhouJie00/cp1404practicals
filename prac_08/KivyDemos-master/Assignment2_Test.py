from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, ListProperty

STATE_TO_NAME = {'Title': "title", 'Artist': "artist", 'Year': "year", 'Learned': "is_learned"}

class BoxLayoutDemo(App):
    output_text = StringProperty()
    state_codes = ListProperty()

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('Assignment2_Test.kv')
        self.state_codes = sorted(STATE_TO_NAME.keys())
        self.create_buttons()
        return self.root

    # def create_buttons(self):
    #     for name in ["Alice", "Bob", "Charlie", "Diana"]:
    #         button = Button(text=name)
    #         button.bind(on_press=self.on_button_press)
    #         self.root.ids.button_container.add_widget(button)
    def create_buttons(self):
        name_to_value = {"Alice": "a", "Bob": "b", "Charlie": "c", "Diana": "d"}

        for name in name_to_value.keys():
            button = Button(text=name)
            # Pass the value associated with the name to the on_button_press callback
            button.bind(on_press=lambda instance, value=name_to_value[name]: self.on_button_press(value))
            self.root.ids.button_container.add_widget(button)

    def on_button_press(self, value):
        print(f"Button pressed: {value}")

    def change_state(self, state_code):
        self.output_text = STATE_TO_NAME[state_code]
        print("Changed to", state_code)

    def handle_new_song(self):
        title = self.root.ids.title_input.text
        artist = self.root.ids.artist_input.text
        year = self.root.ids.year_input.text
        print(f"{title} {artist} {year}")

    def handle_clear(self):
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""

    def handle_increment(self):
        # Implement the logic for what happens when the button is pressed
        print("Increment button pressed")

if __name__ == '__main__':
    BoxLayoutDemo().run()
