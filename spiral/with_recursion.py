import turtle

LENGTH =   int(input("Enter length: "))
GAP_SIZE = int(input("Enter gap: "))

turtle.hideturtle()
turtle.width(5)

def draw_spiral(length, gap_size):
    #if not (length > gap_size >= 0): takhle podmínka nefungovala, nevykreslilo to poslední l a pak to hodilo chybu
    #if not (length >= gap_size >= 0 and length > 0 and gap_size > 0): tady je to ošetřený a navíc je přidaná podmínka, aby length i gap_size byly větší jak 0
    if not (length > 0 and 0 < gap_size <= length): #stejná podmínka jako ta řádek nad tím (11) akorát mi chatgpt řeklo, že to je přehlednější :d
       raise ValueError("Invalid parameters :(")

    if length == LENGTH:
        turtle.forward(length)

    for i in range(2):
        turtle.right(90)
        turtle.forward(length)

    if length - gap_size >= gap_size:
        draw_spiral(length - gap_size, gap_size)

draw_spiral(LENGTH, GAP_SIZE)

turtle.done()