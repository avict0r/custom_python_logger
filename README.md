
# Custom Python Logger

This project involves developing a custom Python logger designed to fulfill the logging requirements using an object-oriented approach.


## Project Goal :

The goal of this project is to create a custom Python logger that provides a flexible and efficient solution for logging based on an object-oriented approach. The logger will be capable of handling various log levels, formats, and destinations, allowing developers to easily integrate it into their projects for comprehensive and organized logging.
## Approach :

The approach for building the custom Python logger will involve creating a CustomLogger class that encapsulates the logger functionality. The class will utilize the logging module from the Python standard library to handle log records and provide essential logging features.

Key steps in the approach include:

1. Designing the CustomLogger class with configurable options for log levels, formats, and handlers.
2. Implementing methods for logging messages with different log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).
3. Integrating various handlers like console, file, and email, allowing developers to choose desired log destinations.
4. Providing the option to customize log message formats based on the use case.
5. Ensuring compatibility with existing logging configurations for easy integration with existing projects.
## Benefits :

The custom Python logger will offer several benefits:

1. Customization: Developers can easily customize the logger's behavior to meet specific project requirements, enhancing code readability and maintainability.
2. Scalability: The object-oriented design allows seamless addition of new features and handlers, making the logger adaptable to evolving project needs.
3. Modularity: The logger will be designed as a separate module, promoting reusability across multiple projects without code duplication.
4. Centralized Logging: The logger's centralized approach will improve the consistency and organization of log messages throughout the application.
5. Ease of Use: The logger's intuitive interface and documentation will simplify integration and usage for developers with varying levels of expertise.
## Prerequisites

Before running this project, ensure that the following items are installed on your system:

Prerequisites:

Before running this project, ensure that the following items are installed on your system:

1. **Python**: Make sure you have Python installed on your machine. You can download the latest version from the official Python website (https://www.python.org/downloads/). The project is compatible with Python 3.x.

2. **pip**: Verify that `pip`, the package manager for Python, is installed. It usually comes bundled with Python installations of version 3.4 and above. You can check its version by running the following command in your terminal or command prompt:

```bash
  pip --version
```

3. **Virtual Environment (venv)**: While not mandatory, it is highly recommended to work in a virtual environment to isolate project dependencies. To create a virtual environment, you can use the built-in `venv` module (Python 3.3+) or the `virtualenv` package. If you're using Python 3.3 or later, the `venv` module is already available. To create a virtual environment named "myenv", run the following command:

```bash
  python -m venv myenv
```

***To Activate Virtual Environment**: After creating the virtual environment, you need to activate it to work within the isolated environment.* 

On Windows, run:

```bash
  myenv\Scripts\activate
```

On macOS or Linux, run:

```bash
  myenv\Scripts\activate
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/avict0r/custom_python_logger
```

Go to the project directory

```bash
  cd custom_python_logger
```
* *Remember to `activate your virtual environement`* before continuing

Install the required packages

```bash
  pip install -r requirements.txt
```

Test the logger by launching `main.py`

```bash
  python main.py
```


## Authors

- [@avict0r](https://www.github.com/avict0r)
