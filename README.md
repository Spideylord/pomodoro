# Pomodoro Timer

A simple Pomodoro timer application built with Python using the `tkinter` library. This app helps you manage your work and break sessions using the Pomodoro technique, featuring a customizable tomato-themed interface.

## Project Structure

- **main.py**: Contains the core logic for the Pomodoro timer, including UI setup, timer mechanism, and countdown functionality.

## Prerequisites

To run the application, you need Python installed along with the following library:

- `tkinter` (standard library, included with Python)

Additionally, ensure you have a `tomato.png` image file in the project directory (as used in the code for the timer display).

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd pomodoro-timer
   ```

3. Ensure the `tomato.png` image file is present in the directory (you can replace it with your own tomato image if needed).

4. Run the application:

   ```bash
   python main.py
   ```

## Features

- **Work Sessions**: 1-minute work intervals (configurable via `WORK_MIN`).
- **Short Breaks**: 1-minute breaks after every work session (configurable via `SHORT_BREAK_MIN`).
- **Long Break**: 20-minute break after every 4 work sessions (configurable via `LONG_BREAK_MIN`).
- **Timer Display**: Shows remaining time with a tomato image background.
- **Checkmarks**: Displays "✔" for each completed work session.
- **Controls**:
  - **Start Button**: Begins or resumes the timer.
  - **Reset Button**: Resets the timer to the initial state.

## Gameplay/Usage

- Click "Start" to begin a work session (1 minute by default).
- The timer alternates between work and break sessions.
- After 4 work sessions, a long break (20 minutes) is triggered.
- Use "Reset" to stop the timer and clear all progress.
- The interface updates with color-coded labels: green for work, pink for short breaks, and red for long breaks.

## Customization

- Adjust `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` in `main.py` to set your preferred session lengths (in minutes).
- Replace `tomato.png` with a different image file if desired, ensuring it matches the canvas size (200x224 pixels).

## File Descriptions

- **main.py**: Implements the Pomodoro timer logic, including:
  - Timer reset functionality.
  - Countdown mechanism using `after` for scheduling.
  - UI setup with `tkinter`, featuring a canvas for the tomato image, labels for the timer text, and buttons for control.

## Notes

- The current settings use short durations (1 minute for work and short breaks, 20 minutes for long breaks) for testing purposes. Adjust these values for practical use (e.g., 25 minutes work, 5 minutes short break, 15-30 minutes long break).
- The application requires a graphical user interface, so run it in an environment with display support.
- The `tomato.png` file must be in the same directory as `main.py` to load correctly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.