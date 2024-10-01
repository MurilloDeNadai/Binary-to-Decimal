import flet as ft

def main(page: ft.Page):
    page.tittle = "Binary"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.height = 400
    page.window.width = 300
    page.window.center()
    tittle = "Binary to Decimal"
    

    def click(e):
        num = inputText.value
        numSeparete = list()
        cont = 0
        resultado = 0

        for n in range(len(num)):
            numSeparete.append(num[n])

        numSeparete = numSeparete[::-1]

        for n in numSeparete:

            if n in '1':
                resul = 2**cont * 1
                resultado += resul
            
            cont += 1
        
        resultView = ft.Container(
                ft.Text(resultado), 
                bgcolor=ft.colors.GREY_300,
                padding=15,
                border_radius=10,
                )

        page.add(
            resultView,
        )
        
        page.update()
        


    inputText = ft.TextField(label="Binary number", width=300, max_length=8,)
    button = ft.TextButton("Submit", on_click=click)

    page.add(
        ft.Text(tittle, size=20, weight=ft.FontWeight.W_900), 
        inputText,
        button
    )

ft.app(main)