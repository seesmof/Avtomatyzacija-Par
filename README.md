# Class Schedule Notifier

This Python script displays the current class schedule for the week and opens the links for the Zoom classes in your default browser.

## Installation

This script requires Python 3 to run. You can download Python 3 [here](https://www.python.org/downloads/).

Clone the repository:

```bash
git clone https://github.com/seesmof/gcalendar-automation.git
```

## Usage

1.  Open the terminal or command prompt and navigate to the directory where the script is located.
2.  Run the following command to install the required libraries:

`pip install -r requirements.txt`

3.  Run the script:

`python main.py`

## Schedule Information

The script displays the class schedule for the current week, based on the current date. The schedule is displayed as follows:

```arduino
- <class name> - <class time>
```

The following class times are used:

- `time_one` - 8:30
- `time_two` - 10:05
- `time_three` - 11:55
- `time_four` - 13:25

The links for the Zoom classes are opened automatically in your default browser.

## Note

This script was created for a specific class schedule and may not work correctly for other schedules. Please modify the script as needed for your own class schedule.

## License

This project is licensed under the [MIT License](LICENSE).
