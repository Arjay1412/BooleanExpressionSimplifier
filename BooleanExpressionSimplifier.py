import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
import BooleanProcess as bp


def main(page: ft.Page):
    page.title = 'Boolean Expression Simplifier'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'light'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    def nightmode(e: ControlEvent):
        page.theme_mode = 'Dark'
        night_mode.disabled = True
        light_mode.disabled = False
        page.update()

    def lightmode(e: ControlEvent):
        page.theme_mode = 'Light'
        night_mode.disabled = False
        light_mode.disabled = True
        page.update()

    def validate(e: ControlEvent) -> None:
        if all([text_expression.value]):
            button_simplify.disabled = False
        else:
            button_simplify.disabled = True
        page.update()

    def submit(e: ControlEvent):
        if " " in text_expression.value:
            text_simplified.visible = True
            text_simplified.color = 'Red'
            text_simplified.value = 'Invalid Input!!'
            page.update()
        else:
            text_simplified.visible = True
            text_simplified.color = 'system'
            text_simplified.value = f'Simplified: {bp.evaluate(bp.tokenize(text_expression.value))}'
            page.update()


    # Fields
    text_expression: TextField = TextField(label='Boolean Expression',text_align=ft.TextAlign.LEFT,
                                         width=210)
    text_simplified: Text = Text(size=20, visible=False, text_align=ft.TextAlign.LEFT)
    button_simplify: ElevatedButton = ElevatedButton(text='Simplify', width=200, disabled=True)
    night_mode = ft.IconButton(ft.icons.MODE_NIGHT, on_click=nightmode, disabled=False)
    light_mode = ft.IconButton(ft.icons.LIGHT_MODE, on_click=lightmode, disabled=True)

    # Linking Functions
    text_expression.on_change = validate
    button_simplify.on_click = submit

    # Render Window
    page.add(
        Row(controls=[
            Column(
                [text_expression,
                 button_simplify])],
            alignment=ft.MainAxisAlignment.CENTER),
        Row(controls=[night_mode, light_mode],
        alignment=ft.MainAxisAlignment.CENTER),
        Row(controls=[text_simplified],
            alignment=ft.MainAxisAlignment.CENTER)
            )



if __name__ == '__main__':
    ft.app(target=main)