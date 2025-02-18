# Mouse Idle Clicker

This script monitors mouse movement and clicks at the bottom-right corner of the screen when the mouse has been idle for a specified duration.

## Features
- Detects mouse movement
- Resets the idle timer on movement
- Moves the mouse to the bottom-right corner and clicks if idle for a set time
- Runs continuously in the background

## Requirements
Ensure you have Python installed along with the required dependencies:

```bash
pip install pynput
```

if not installed then try this command

```bash
pip install --break-system-packages pynput
```

## Usage
1. Clone or download this script.
2. Adjust `screen_width` and `screen_height` if needed to match your screen resolution.
3. Modify `idle_time` to set the duration (in seconds) before the script performs a click.
4. Run the script:

```bash
python script.py
```

## Configuration
- `idle_time`: Time in seconds before the script clicks when idle.
- `screen_width`, `screen_height`: Screen resolution settings.
- `bottom_right_x`, `bottom_right_y`: Position for the click (default: bottom-right corner).

## Stopping the Script
- Press `CTRL + C` in the terminal to stop execution.

## Troubleshooting
- If the script does not work as expected, ensure `pynput` is installed and accessible.
- Run the script with administrator privileges if necessary.

## License
This script is open-source and free to use.

