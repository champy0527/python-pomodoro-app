# Python Pomodoro App

A simple Pomodoro timer app built using Python and Tkinter. The Pomodoro technique is used to improve productivity by dividing work into intervals separated by short breaks.

## Features

- **Work and Break Cycles**: Automatically alternate between work and break intervals.
- **Pause and Resume**: Pause the timer at any point and resume when needed.
- **Reset**: Reset the timer to start over.
- **Progress Tracking**: Display tick marks to show completed work sessions.
  
## Technologies Used

- **Python**: Main programming language for implementing the app.
- **Tkinter**: Used to build the graphical user interface (GUI).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/champy0527/python-pomodoro-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-pomodoro-app
    ```

3. Install the required dependencies (only `tkinter` is required, which is usually included with Python installations).

4. Run the script:

    ```bash
    python main.py
    ```

## Usage

- **Start**: Click the "Start" button to begin a Pomodoro session.
- **Pause**: Click the "Pause" button to pause the timer, and click again to resume.
- **Reset**: Click the "Reset" button to reset the timer to 00:00.
- **Session Tracking**: The app displays a ✔ symbol after each completed work session.

## Pomodoro Cycle

The app follows the Pomodoro technique cycle:

1. **Work Interval**: 25 minutes of focused work (can be customized in the code).
2. **Short Break**: 5 minutes break after each work session.
3. **Long Break**: 20 minutes break after four work sessions.

## Code Overview

- **Constants**: Define the colors, fonts, and time durations for work, short break, and long break intervals.
- **`start_timer()`**: Starts the countdown based on the current session type (work or break).
- **`count_down(count)`**: Handles the countdown mechanism, updating the timer display every second.
- **Pause and Resume Feature**: Allows the user to pause and resume the countdown at any point.
- **Reset Feature**: Resets the timer and all progress, allowing the user to start fresh.

## Lessons Learned

- Practiced using the Tkinter library for building GUI applications in Python.
- Improved understanding of Python's `after()` function for creating time-based events.
- Implemented basic state management for pausing and resuming the timer.

## Future Improvements

- Add a settings menu to customize work, short break, and long break durations.
- Implement sound notifications to indicate the start and end of each session.
- Add a log feature to track productivity over time.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## Acknowledgements

- [The Odin Project](https://www.theodinproject.com) for providing learning inspiration.
- Various online resources and communities for guidance and support in building the project.
