
import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    eraser_coords = canvas.coords(eraser)
    overlapping_objects = canvas.find_overlapping(*eraser_coords)

    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill="white")

def move_eraser(event):
    """Move the eraser with mouse"""
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    erase_objects(canvas, eraser)

def main():
    global canvas, eraser

    # Create main window
    root = tk.Tk()
    root.title("Canvas Eraser")

    # Create canvas
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()

    # Create grid of blue cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE

            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue", outline="black")

    # Wait for user click
    canvas.bind("<Button-1>", lambda event: start_eraser(event, canvas))
    
    root.mainloop()

def start_eraser(event, canvas):
    global eraser

    last_click_x, last_click_y = event.x, event.y

    # Create eraser
    eraser = canvas.create_rectangle(
        last_click_x, last_click_y,
        last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE,
        fill="pink"
    )

    # Bind motion for erasing
    canvas.bind("<Motion>", move_eraser)

if __name__ == "__main__":
    main()
