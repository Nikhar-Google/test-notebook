# Test Notebook

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python 3:** This project requires Python 3 (version 3.9 or higher is recommended). You can check your Python version by running:
    ```bash
    python3 --version
    ```
*   **pip:** The package installer for Python (version 23.0 or higher is required). It's usually included with Python 3 installations. Check with:
    ```bash
    pip3 --version
    ```
*   **venv:** The standard Python module for creating virtual environments. It's typically included with Python 3.
*   **Git:**  For cloning the repository and managing versions.


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
    git checkout tags/v1.0.3 -b release-1.0.3
    ```

4.  **Create a Virtual Environment:**

    ```bash
    python3 -m venv .venv
    ```

5.  **Activate the Virtual Environment:**

    ```bash
    source .venv/bin/activate
    ```

6.  **Install Dependencies:**

    ```bash
    pip install .
    ```
    This command installs the project and its dependencies (as defined in `pyproject.toml`) into the virtual environment.

7.  **Launch Jupyter Lab:**

    ```bash
    jupyter lab test_notebook.ipynb
    ```
    This will start Jupyter Lab and open the `notebook.ipynb` file in your web browser.


