import pyautogui
from PIL import Image
from pynput.mouse import Listener

threshold = 10

# Load your custom cursor image
custom_cursor_path = "/Users/kenzie/Desktop/CS3300/finalProject/static/images/Flower.png"  # Replace with the correct path
custom_cursor = Image.open(custom_cursor_path)

# Initialize previous_x and previous_y
previous_x, previous_y = 0, 0

def on_move(x, y):
    global previous_x, previous_y  # Declare these variables as global

    if abs(x - previous_x) > threshold or abs(y - previous_y) > threshold:
        print(f'Mouse moved to ({x}, {y})')

        # Move the cursor relatively
        pyautogui.move(x - previous_x, y - previous_y, duration=0.1, tween=pyautogui.easeInOutQuad)

        # Display the custom cursor image
        pyautogui.mouseInfo()
        pyautogui.mouseInfo(x=0, y=0, color=(0, 0, 0), duration=0.1, tween=pyautogui.easeInOutQuad)

        pyautogui.mouseDown(button="left")  # Optional: Simulate left mouse click to show the custom cursor
        pyautogui.mouseUp(button="left")

    previous_x, previous_y = x, y  # Update previous_x and previous_y

# Set up the listener
with Listener(on_move=on_move) as listener:
    # Keep the listener running
    listener.join()
