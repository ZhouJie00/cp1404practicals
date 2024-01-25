from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):



        self.names = ["Alice", "Bob", "Charlie", "Diana"]
        layout = BoxLayout(orientation='vertical') #Frame
        self.create_labels(layout) # put frame function
        return layout

        #input into UI evertime, e.g. add new label each time
        # name in self.names:
            # label = Label(text=name)
            # layout.add_widget(label)

    def create_labels(self, layout):
        for name in self.names:
            label = Label(text=name) #label and add text to label
            layout.add_widget(label) #add label into frame
DynamicLabelsApp().run()
