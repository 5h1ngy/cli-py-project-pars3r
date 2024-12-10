# **CLI-Py-Project-Pars3r**

<p align="center">
  <img src="./assets/logo.png" alt="logo" width="512">
</p>

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-blue)](#)
![Python](https://img.shields.io/badge/python-%3E%3D3.6-green)

A Python CLI tool for parsing project structures into prompts and restoring them into a directory scaffolding.


<p align="center">
  <img src="./assets/preview_1.png" alt="logo" width="512">
  <img src="./assets/preview_2.png" alt="logo" width="512">
</p>

## **Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Changelog](#changelog)
- [Contributing](#contributing)
- [License](#license)

## **Introduction**

`CLI-Py-Project-Pars3r` is a Python-based CLI tool designed for:

1. **Packing**: Parsing a project directory into a `.prompt` file that summarizes its contents.
2. **Unpacking**: Restoring the directory scaffolding and files from a `.prompt` file.

This tool is simple to use, globally installable, and ideal for automation.

## **Features**

- ✅ Parse project directories into a summarized `.prompt` file.
- ✅ Restore directories and files from `.prompt` files.
- ✅ Interactive CLI for selecting folders or `.prompt` files.
- ✅ Configurable and extendable.
- ✅ Compatible with Python `>= 3.6`.

## **Requirements**

Ensure the following are installed:

- **Python**: `>= 3.6`
- **pip**: Python package manager

## **Installation**

### Steps:

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd cli-py-project-pars3r
   ```

2. Install the package:
   ```bash
   pip install .
   ```

3. Test the command:
   ```bash
   pars3r
   ```

## **Usage**

Run the main script using:
```bash
pars3r
```

### Core Functionalities:

1. **Packing**: 
   - Select a folder to analyze.
   - Generate a `.prompt` file summarizing its contents.
   - The `.prompt` file will include metadata, file paths, and contents.

   Example:
   ```bash
   pars3r
   ```

2. **Unpacking**:
   - Select a `.prompt` file from the list.
   - Restore the directory scaffolding and files from the `.prompt`.

   Example:
   ```bash
   pars3r
   ```

   Follow the interactive prompts to choose the `.prompt` file to unpack.

## **Project Structure**

```plaintext
cli-py-project-pars3r/
├── cli-py-project-pars3r/
│   ├── __init__.py        # Package initialization
│   ├── cli.py             # Main script
├── setup.py               # Configuration for pip
├── README.md              # Documentation
├── assets/                # Images and assets for the README
└── tests/                 # (Optional) Automated tests
```

## **Testing**

Run automated tests using:
```bash
pytest tests/
```

## **Changelog**

### **v1.1.0**
- Added **interactive file selection** for unpacking `.prompt` files.
- Improved CLI interactivity and error handling.
- Updated README to reflect new features.

### **v1.0.0**
- Initial release:
  - Added project parsing and `.prompt` file generation.
  - Added directory scaffolding restoration from `.prompt`.

## **License**

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.