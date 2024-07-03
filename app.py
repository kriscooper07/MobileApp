from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.scrollview import MDScrollView

KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: "Title"
                halign: 'center'
                font_style: "H5"
            MDLabel:
                text: "Subtitle"
                halign: 'center'
                font_style: "Subtitle1"
            MDFlatButton:
                text: "Options"
                pos_hint: {'center_y': 0.5}

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            Image:
                source: 'headshot.jpg'
                size_hint: None, None
                size: dp(80), dp(80)
            MDLabel:
                text: "Sandy Wilder Cheng"
                valign: 'center'
                halign: 'center'

        MDGridLayout:
            cols: 2
            row_default_height: dp(48)
            row_force_default: True
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: 'Student Name'
            MDTextField:
                id: s_name
                hint_text: 'Enter student name'

            MDLabel:
                text: 'Student Marks'
            MDTextField:
                id: s_marks
                hint_text: 'Enter student marks'

            MDLabel:
                text: 'Student Gender'
            MDTextField:
                id: s_gender
                hint_text: 'Enter student gender'

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            MDRaisedButton:
                text: 'Create'
                on_release: app.create_record()

            MDRaisedButton:
                text: 'Read'
                on_release: app.read_records()

            MDRaisedButton:
                text: 'Update'
                on_release: app.update_record()

            MDRaisedButton:
                text: 'Delete'
                on_release: app.delete_record()

        MDScrollView:
            MDGridLayout:
                id: output_layout
                cols: 1
                adaptive_height: True
'''

class Student:
    def __init__(self, name, marks, gender):
        self.name = name
        self.marks = marks
        self.gender = gender

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        self.students = []
        self.current_index = None
        return Builder.load_string(KV)

    def display_message(self, message):
        self.root.ids.output_layout.clear_widgets()
        self.root.ids.output_layout.add_widget(MDLabel(text=message))

    def create_record(self):
        name = self.root.ids.s_name.text
        marks = self.root.ids.s_marks.text
        gender = self.root.ids.s_gender.text
        self.students.append(Student(name, marks, gender))
        self.display_message(f'Student {name} created.')

    def read_records(self):
        self.root.ids.output_layout.clear_widgets()
        for i, student in enumerate(self.students):
            self.root.ids.output_layout.add_widget(
                MDLabel(text=f'{i+1}: {student.name}, {student.marks}, {student.gender}')
            )

    def update_record(self):
        if self.current_index is not None and 0 <= self.current_index < len(self.students):
            self.students[self.current_index].name = self.root.ids.s_name.text
            self.students[self.current_index].marks = self.root.ids.s_marks.text
            self.students[self.current_index].gender = self.root.ids.s_gender.text
            self.display_message(f'Student {self.current_index+1} updated.')
        else:
            self.display_message('No student selected or invalid index.')

    def delete_record(self):
        if self.current_index is not None and 0 <= self.current_index < len(self.students):
            del self.students[self.current_index]
            self.display_message(f'Student {self.current_index+1} deleted.')
        else:
            self.display_message('No student selected or invalid index.')

if __name__ == "__main__":
    MainApp().run()