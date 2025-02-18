import time
from pynput import mouse, keyboard
from pynput.mouse import Controller
import threading

# Create an instance of Controller to control the mouse
mouse_controller = Controller()

# Last time the mouse was moved or a key was pressed
last_activity_time = time.time()

# Define the screen coordinates for bottom right (you may need to adjust this based on your screen resolution)
screen_width = 1920  # Adjust based on your screen resolution
screen_height = 1080  # Adjust based on your screen resolution
bottom_right_x = screen_width - 1  # Rightmost x coordinate
bottom_right_y = screen_height - 1  # Bottommost y coordinate

# Time to wait before clicking (in seconds)
idle_time = 30

# Function to move the mouse to the bottom right and click
def click_bottom_right():
    mouse_controller.position = (bottom_right_x, bottom_right_y)
    mouse_controller.click(mouse.Button.left)
    print(f"Clicked at: ({bottom_right_x}, {bottom_right_y})")

# Function to detect mouse movement
def on_move(x, y):
    global last_activity_time
    last_activity_time = time.time()  # Reset the last activity time when mouse is moved

# Function to detect key press
def on_press(key):
    global last_activity_time
    last_activity_time = time.time()  # Reset the last activity time when any key is pressed

# Function to monitor mouse idle time and click if necessary
def monitor_idle_time():
    while True:
        time.sleep(1)  # Check every second
        if time.time() - last_activity_time >= idle_time:
            click_bottom_right()
            time.sleep(idle_time)  # Wait for the next cycle of checking

# Set up the listener for mouse movement
mouse_listener = mouse.Listener(on_move=on_move)
mouse_listener.start()

# Set up the listener for keyboard activity
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the thread to monitor idle time and click if necessary
monitor_thread = threading.Thread(target=monitor_idle_time)
monitor_thread.daemon = True
monitor_thread.start()

# Keep the main program running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated.")
