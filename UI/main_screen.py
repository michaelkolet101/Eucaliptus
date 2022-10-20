from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder

input_text = '''
BoxLayout:
    padding: "10dp"

    MDTextField:
        id: insert_spring_name
        hint_text: "Insert a spring name"
        pos_hint: {"center_y": 0.7}
        color_mode: 'custom'
        helper_text_mode: "on_focus"
        size_hint: 1, None
        width: "30px"
        
        
'''

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"
'''

class Demo(MDApp):

    def build(self):
        # defining screen
        screen = Screen()

        # defining 1st label
        l = MDLabel(text="Welcome to Eucalyptus", pos_hint={'center_x': 0.6,
                                               'center_y': 0.9},
                    theme_text_color="Custom",
                    text_color=(0.2, 0, 0.2, 1),
                    font_style='H2')

        spring_search = Builder.load_string(input_text)
        tool = Builder.load_string(KV)


        screen.add_widget(l)
        screen.add_widget(spring_search)
 #       screen.add_widget(tool)

        return screen


if __name__ == "__main__":
    Demo().run()
