---
tags:
  - Python
  - Installation
icon: simple/python
---
# Python

In this guide, you will find step-by-step instructions for installing Python (version 3.7 or higher) and configuring the Python PATH on different operating systems.

## Python Installation

### Download and Install Python

1. **Download Python**: Visit the official Python website at [python.org](https://www.python.org/downloads/). We recommend avoiding the latest release and selecting a version of Python 3.7 or higher.

2. **Installation for Windows**:
    1. Run the downloaded Python installer.
    2. During installation, make sure to check the box that says "Add Python to PATH."

3. **Installation for macOS**:
    1. Run the downloaded Python installer.
    2. Follow the on-screen instructions, ensuring that Python is installed.

4. **Installation for Linux**:
    1. Python is often pre-installed on Linux distributions. You can check the version by running `python3 --version` in the terminal. If Python is not installed, use your distribution's package manager to install it.

## Python PATH Configuration

### macOS and Linux

Please refer to video tutorials or documentation specific to your distribution for setting up the Python PATH. The process can vary based on your system's configuration. 

???+ tip
    :simple-youtube: [Python Tutorial: How to Set the Path and Switch Between Different Versions/Executables (Mac & Linux)](https://youtu.be/PUIE7CPANfo)

### Windows

On Windows, the Python installer can add Python to the PATH for you. However, if it's not added during installation or if you need to do it manually, follow these steps:

1. **Search for "Environment Variables"**: In the Windows search bar, type "Environment Variables" and select "Edit the system environment variables."

2. **System Properties**: Click the "Environment Variables" button in the "System Properties" window.

3. **Edit User Variables**: In the "User variables" section, select "Path" and click the "Edit" button.

4. **Add Python to Path**: Click "New" and add the path to your Python installation. By default, it's something like `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3x` (replace `<YourUsername>` with your actual username and `Python3x` with the Python version).

5. **Confirm Configuration**: Close all windows and open a new Command Prompt. You should be able to run Python by typing `python` or `python3` in the command prompt.

???+ tip
    :simple-youtube: [Python Tutorial: How to Set the Path and Switch Between Different Versions/Executables (Windows)](https://youtu.be/OdIHeg4jj2c)


## Conclusion

By following these installation and Python PATH configuration steps, you will have Python (version 3.7 or higher) installed on your system. Make sure to use the appropriate instructions for your specific operating system.

Happy coding with Python!
