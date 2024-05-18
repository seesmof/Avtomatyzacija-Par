<a name="readme-top"></a>

<div align="center">
<h1 align="center">Classes Automation</h1>
</div>

## Table of contents

- [Table of contents](#table-of-contents)
- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Schedule Information](#schedule-information)
- [Note](#note)
- [Built with](#built-with)
- [License](#license)

## About

This repository contains a simple Python script that is meant to automate online class attending. It runs classes on its own, as well as opens notes for them and a bunch more. Made with Python.

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

## Built with

![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## License

This project is [Public Domain](./LICENSE).

<p align="right"><a href="#readme-top"><strong>Back to top</strong></a></p>
