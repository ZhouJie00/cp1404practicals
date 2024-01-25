from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty
STATE_TO_NAME = {'QLD': "Queensland", 'NSW': "New South Wales", 'VIC': "Victoria", 'WA': "Western Australia",
                 'TAS': "Tasmania", 'NT': "Northern Territory", 'SA': "South Australia", 'ACT': "Canberra",
                 'NQ': "Cowboys!", 'NZ': "New Zealand"}
class BoxLayoutDemo(App):
    output_text = StringProperty()
    state_codes = ListProperty()
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('Assignment2_Test.kv')
        self.state_codes = sorted(STATE_TO_NAME.keys())
        return self.root

    def change_state(self, state_code):
        """Handle change of spinner selection, output result to string property for label."""
        self.output_text = STATE_TO_NAME[state_code]
        print("Changed to", state_code)

    def handle_greet(self): #button  (Step 2), (Step 1 in kv file to call here)
        print('greet') #print in console when press, extra

        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"#output_label,input_name are the id in the .kv file
        #when greet button is pressed, the TextInput text will be retieved and put to the label

    def handle_clear(self): #button
        #reset to ""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
