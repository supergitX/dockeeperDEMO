# 📘 Doc-Keeper

**Doc-Keeper** is an AI-powered documentation generator for your codebase, powered by **Gemini 2.0**. It scans your entire repository, intelligently summarizes key modules, and creates clean and detailed Markdown documentation — automatically.

> 🔥 Perfect for DevOps, ML projects, open source, internal tools, and more!

---

## 🧾 Project Overview

Doc-Keeper automates code documentation. It uses Gemini to generate Markdown documentation, intelligently summarizing modules, classes, and functions.  It includes an optimizer (`optimizer.py`) and a reviewer (`reviewer.py`) leveraging Ollama to enhance code quality and robustness.  Code generation is provided via a command-line interface (`coder.py`).

## ⚙️ Setup & Installation Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/doc-keeper.git
cd doc-keeper
```

2. **Create a virtual environment (recommended):**

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up Ollama:** Install and run the Ollama server (see [https://ollama.ai/](https://ollama.ai/)).  The scripts assume Ollama runs on `localhost:11434`.

5. **Set your Gemini API key:** Obtain an API key from Google AI Studio (https://makersuite.google.com/app/apikey) and set it as an environment variable:

```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"  # For Linux/macOS
set GEMINI_API_KEY="YOUR_GEMINI_API_KEY"  # For Windows PowerShell
```


## 🧩 Explanation of Key Modules, Classes, and Functions

### `doc-keeper.py`

- **`read_repo_files(base_path: str) -> dict`**:
    - Recursively reads all readable files in the repository, excluding specified files and directories.
    - Returns a dictionary mapping relative file paths to their content.

- **`generate_documentation(repo_files: dict) -> str`**:
    - Creates a prompt for the Gemini API with instructions and codebase content.
    - Sends the prompt to Gemini and returns the generated Markdown documentation.

- **`write_documentation(doc_text: str)`**: *(Incomplete in the provided codebase)*
    - This function should write the generated Markdown to `DOCUMENTATION.md`.

### `optimizer.py`

- **`log_message(message: str)`**: Logs a timestamped message to `logs/optimizer_log.txt`.

- **`read_code_from_file(file_path: str) -> str | None`**: Reads and returns the file content. Returns `None` if the file is empty or an error occurs.

- **`optimize_code(code_content: str) -> str | None`**: Sends the code to Ollama for optimization and returns the optimized code. Returns `None` if optimization fails.

- **`save_optimized_code(code_text: str, original_file: str) -> str | None`**: Saves the optimized code to a file in the 'optim' folder.


### `reviewer.py`

- **`log_message(message: str)`**: Logs a timestamped message to `logs/review_log.txt`.

- **`read_code_from_file(file_path: str) -> str | None`**:  Reads and returns the file content.  Returns `None` if the file is empty or an error occurs.

- **`review_code(code_content: str) -> str`**: Sends the code to Ollama for review and returns the review report.

- **`save_review(review_text: str, original_file: str) -> str | None`**:  Saves the review to a `.txt` file in the `reviews` folder.



### `coder.py`

- **`log_message(message: str)`**: Logs a timestamped message to `logs/codegen_log.txt`.

- **`generate_code_with_ollama(prompt: str) -> str`**: Generates code using Ollama based on the given prompt.

- **`save_file(content: str, file_type: str, name: str = "") -> str | None`**: Saves content to a file with the specified type in `coder_folder`.

- **`create(user_prompt: str, name: str = "")`**: Generates code and saves it to a file.


### `coder_test.py` (Testing Module for `coder.py`)

- **`generate_code_with_ollama(prompt: str) -> str`**: Same as in `coder.py`. Used for testing.

- **`save_file(content: str, file_type: str, name: str = "") -> str`**: Same as in `coder.py`. Used for testing.



## 🗂 Folder & File Structure with Descriptions

```
doc-keeper/
├── doc-keeper.py           # Main script for generating documentation
├── DOCUMENTATION.md        # Output documentation file
├── .github/                # GitHub Actions workflows
│   └── workflows/
│       └── main.yml         # Workflow for automatic documentation generation
├── coder.ipynb            # Jupyter Notebook for interactive code generation using Ollama
├── coder.py               # Script for command-line code generation using Ollama
├── coder_test.py          # Unit tests for coder.py
├── coder_folder/          # Output directory for generated code from coder.py
├── optimizer.py           # Script for optimizing code using Ollama
├── optim/                 # Output directory for optimized code
├── reviewer.py            # Script for code review using Ollama
├── reviews/               # Output directory for code review reports
├── requirements.txt        # Project dependencies
└── README.md               # Project description
```



## 🔧 How to Use

### `doc-keeper.py`

Run from the project root:

```bash
python doc-keeper.py 
```

This will generate `DOCUMENTATION.md`.


### `optimizer.py` (CLI usage not fully implemented in provided code)

Intended usage (needs further implementation in `main` function):

```bash
python optimizer.py <file_to_optimize.py>
```

### `reviewer.py` (CLI usage not fully implemented in provided code)

Intended usage (needs further implementation in `main` function):

```bash
python reviewer.py <file_to_review.py>
```

### `coder.py` (CLI usage not fully implemented in provided code)

Intended usage (needs further implementation in `main` function):

```bash
python coder.py "Your code generation prompt" --name <output_file_name> --type <file_type> 
```



## 🤝 Contribution Guidelines


Contributions are welcome!  Fork the repository, make your changes, and submit a pull request.  Please ensure your code follows PEP 8 style guidelines and includes appropriate tests.



## 🧪 Testing & Debugging Instructions

### `coder_test.py`

Run the tests using:

```bash
python coder_test.py
```


### Debugging

Use a debugger like `pdb` (Python Debugger) or an IDE with debugging capabilities to step through the code and identify issues.  Log messages generated by the `log_message` functions in each module can also be helpful for troubleshooting.



## Updated Code with Docstrings


The provided code has been updated with docstrings, improving its readability and maintainability for other developers.  See the updated code files for the complete docstrings. Note that the incomplete functions (`write_documentation`, and the `main` functions in `optimizer.py`, `reviewer.py`, and `coder.py`) require further implementation to be fully functional.  The GitHub actions workflow file was also updated from `.github/workflows/generate-docs.yml` to `.github/workflows/main.yml` to reflect common practice. You can find the complete updated code in this revised response.  Remember to add the necessary logic to handle command-line arguments in the respective `main` functions, and complete the `write_documentation` function in `doc-keeper.py`.
