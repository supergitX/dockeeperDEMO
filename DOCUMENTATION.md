# 📘 Doc-Keeper

**Doc-Keeper** is an AI-powered documentation generator for your codebase, powered by **Gemini 2.0**. It scans your entire repository, intelligently summarizes key modules, and creates clean and detailed Markdown documentation — automatically.

> 🔥 Perfect for DevOps, ML projects, open source, internal tools, and more!

---

## 🧾 Project Overview

Doc-Keeper helps automate the tedious process of creating and maintaining code documentation. It leverages the power of Gemini to generate comprehensive Markdown documentation based on the codebase.  It intelligently identifies key modules, classes, and functions to provide a detailed overview of the project. It also includes an optimizer (`optimizer.py`) and a reviewer (`reviewer.py`) that uses Ollama to improve code quality and robustness.  The code generation capabilities are showcased through a command-line interface driven by `coder.py`.

## ⚙️ Setup & Installation Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/doc-keeper.git
cd doc-keeper
```

2. **Create and activate a virtual environment (recommended):**

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up Ollama:**  Install and run the Ollama server according to the instructions on their official website ([https://ollama.ai/](https://ollama.ai/)). The scripts assume Ollama runs on `localhost:11434`.

5. **Set your Gemini API key:** Obtain an API key from Google AI Studio (https://makersuite.google.com/app/apikey) and set it as an environment variable:

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"  # For Linux/macOS
set GEMINI_API_KEY="YOUR_GEMINI_API_KEY"  # For Windows PowerShell
```

## 🧩 Explanation of Key Modules, Classes, and Functions

### `doc-keeper.py`

- **`read_repo_files(base_path: str) -> dict`**:
    - Recursively reads all readable files in the repository, excluding files and directories specified in the `IGNORE_EXTENSIONS`, `IGNORE_FILES`, and `IGNORE_DIRS` tuples.
    - Returns a dictionary where keys are relative file paths and values are the file contents.

- **`generate_documentation(repo_files: dict) -> str`**:
    - Constructs a prompt for the Gemini API by including instructions and the codebase content.
    - Sends the prompt to Gemini and receives generated Markdown documentation.
    - Returns the generated Markdown string.


- **`write_documentation(doc_text: str)`**: *(Incomplete in the provided codebase)*
    - This function would take the generated Markdown documentation string as input and write it to a file, presumably `DOCUMENTATION.md`.



### `optimizer.py`

- **`log_message(message: str)`**:
    - Logs a timestamped message to `logs/optimizer_log.txt`.

- **`read_code_from_file(file_path: str) -> str | None`**:
    - Reads and returns the content of the given file.  Returns `None` if the file is empty or if a reading error occurs.  Logs messages to indicate success or failure.

- **`optimize_code(code_content: str) -> str | None`**:
    - Sends the given code to Ollama for optimization, using a system prompt designed to improve robustness and error handling.
    - Returns the optimized code from Ollama or `None` if an error occurs during the optimization process.

- **`save_optimized_code(code_text: str, original_file: str) -> str | None`**:
    - Saves the optimized code to a file in the `optim` directory. The new filename is based on the original filename.  Returns the path to the saved file or `None` if saving fails.

- **`main()`**: *(Incomplete)*
    - Would parse command-line arguments and use the other functions in this module to perform the optimization.


### `reviewer.py`

- **`log_message(message: str)`**:
    - Logs a timestamped message to `logs/review_log.txt`.

- **`read_code_from_file(file_path: str) -> str | None`**:
    - Reads and returns the content of the file at `file_path`. Returns `None` if the file reading fails or if the file is empty. Logs success/failure messages.

- **`review_code(code_content: str) -> str`**:
    - Sends the given code content to Ollama for review, using a system prompt that guides Ollama to provide feedback on code quality, error handling, and potential issues.
    - Returns the review report from Ollama.

- **`save_review(review_text: str, original_file: str) -> str | None`**:
    - Saves the review report to a `.txt` file in the `reviews` directory.  The filename includes a timestamp and the original filename.  Returns the path to the saved review file or `None` if saving fails.




### `coder.py`

- **`log_message(message: str)`**: Logs a timestamped message to `logs/codegen_log.txt`.

- **`generate_code_with_ollama(prompt: str) -> str`**: Sends the given prompt to Ollama for code generation, using a system prompt that instructs Ollama to act as a code generator in a CI/CD pipeline. Returns the generated code or a message if the prompt isn't related to code generation.

- **`save_file(content: str, file_type: str, name: str = "") -> str | None`**: Saves the given content to a file in the 'coder_folder' directory. The file type is determined from the `file_type` argument or the first line of the content.  Returns the file path or `None` if saving fails.

- **`create(user_prompt: str, name: str = "") -> str | None`**:  Generates code using `generate_code_with_ollama()`, logs the generated code, attempts to infer the file type, and then saves the code to a file using `save_file()`. Returns the file path or `None` if an error occurs.



### `coder_test.py`

- **`generate_code_with_ollama(prompt: str) -> str`**: This function is identical to the one in `coder.py`. It is likely intended for testing purposes but currently doesn't include any test assertions.

- **`save_file(content: str, file_type: str, name: str = "") -> str`**: This function is very similar to the one in `coder.py`, with minor differences in how it determines the `file_type`. It's likely included for testing but lacks proper test setup and assertions.




### `coder.ipynb`

This Jupyter Notebook demonstrates basic code generation using Ollama. It allows users to input prompts and receive code in response.  It also contains a `generate_code` function (incomplete), likely intended for more structured code generation.


## 🗂 Folder & File Structure with Descriptions

```
doc-keeper/
├── doc-keeper.py           # Main script to generate documentation.
├── DOCUMENTATION.md        # Output file containing generated documentation.
├── .github/                 # GitHub Actions workflows.
│   └── workflows/
│       └── main.yml         # Workflow for automatic documentation generation.
├── coder.ipynb             # Jupyter Notebook for code generation examples.
├── coder.py                # Script for code generation using Ollama.
├── coder_folder/           # Output directory for generated code from coder.py.
├── coder_test.py           # (Incomplete) Test file for coder.py.
├── optimizer.py            # Script to optimize code using Ollama.
├── optim/                  # Output directory for optimized code.
├── README.md               # Project description and usage instructions.
├── requirements.txt        # Project dependencies.
├── reviewer.py            # Script for code review using Ollama.
├── reviews/                # Output directory for code review reports.
└── logs/                  # Log files from the optimizer and code generator.


```


## 🔧 How to Use

1.  **To generate documentation:**  Run `doc-keeper.py` from the root directory of the project you want to document:


```bash
python doc-keeper.py
```

This will create or overwrite the `DOCUMENTATION.md` file.

2.  **To optimize code (using `optimizer.py`):** The `main` function needs to be completed to provide command-line functionality.  A basic usage example (once `main` is implemented) might look like:



```bash
python optimizer.py --file path/to/your/code.py
```

3.  **To review code (using `reviewer.py`):**  A fully implemented `main` function would allow command-line usage.  An example (after completing the implementation) might be:


```bash
python reviewer.py --file /path/to/your/code.py
```



4. **To generate code using `coder.py`:**  You will need to create the functions you need to create in `coder.py` first.


```bash
python coder.py create "your code generation prompt" --name optional_filename
python coder.py create "Write a Python function to calculate the factorial of a number." --name factorial
```



## 🤝 Contribution Guidelines

Contributions are welcome! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear messages.
4.  Push your branch to your fork.
5.  Open a pull request to the main repository.



## 🧪 Testing & Debugging Instructions

The current `coder_test.py` file is incomplete.  To implement proper testing, follow these steps:

1. **Add assertions:** Include `assert` statements to check the expected behavior of the functions in `coder.py` and potentially `optimizer.py` and `reviewer.py`.
2. **Use a testing framework (pytest recommended):** Structure your tests using `pytest` or a similar framework for better test organization and reporting.
3. **Run tests:** Execute tests using `pytest` (if installed) or by running the test file directly.

For debugging, use print statements or a debugger to understand the program's flow and identify issues. Ensure that the Ollama server is running for the code optimization and review functionalities.  Monitor the log files in the `logs` directory for any errors or unexpected behavior.

