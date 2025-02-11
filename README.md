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
*   **venv:** The standard Python module for creating virtual environments. It's typically included with Python 3. It is usually included with Python 3, **but on some Linux distributions, it may need to be installed separately.**  See the "Checking and Installing `venv`" section below.
*   **Git:**  For cloning the repository and managing versions.

### Checking and Installing `venv`

**Important:** While `venv` is typically part of standard Python 3 installations, some operating systems (particularly certain Linux distributions) package it separately.  Before proceeding, verify that `venv` is available:

Run the following command in your terminal:

```bash
python3 -m venv -h
```

1. If you see help text for `venv`: venv is installed, and you can proceed to the "Installation" section.
2. If you see an error message like `No module named venv`: You need to install venv based on your OS.

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


