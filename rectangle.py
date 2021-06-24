import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

def main():
    window = turtle.Screen() # Set up the window and its attributes
    
    window.bgcolor("lightgreen")
    
    tess = turtle.Turtle() # Create tess and set some attributes

    draw_square(tess, 50)

    window.mainloop()

if __name__ == "__main__":
    main()
