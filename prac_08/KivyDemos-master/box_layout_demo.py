from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root


    def handle_greet(self): #button  (Step 2), (Step 1 in kv file to call here)
        print('greet') #print in console when press, extra

        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"#output_label,input_name are the id in the .kv file
        #when greet button is pressed, the TextInput text will be retieved and put to the label

    def handle_clear(self): #button
        #reset to ""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
