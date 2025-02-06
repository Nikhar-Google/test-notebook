# Test Notebook

## Prerequisites

Before you begin, make sure you have the following installed:

*   **Python 3:** This project requires Python 3 (version 3.7 or higher is recommended).  You can check your Python version by running `python3 --version` in your terminal.
*   **pip:** The package installer for Python. It's usually included with Python 3 installations. You can check if it's installed by running `pip3 --version`.
*   **venv:** The standard Python module for creating virtual environments. It's also typically included with Python 3.

## Installation (from a Specific Release via Git - Recommended)

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Nikhar-Google/test-notebook.git
    cd test-notebook
    ```

2.  **List Available Tags (Releases):**

    ```bash
    git tag -l
    ```

3.  **Checkout the Latest Release:**


    ```bash
    git checkout tags/v1.0.2 -b release-1.0.2
    ```

4.  **Run the Setup Script and launch the notebook:**

    *   **Linux/macOS:**
        ```bash
        bash setup.sh
        ```
