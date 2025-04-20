import ollama
import argparse
import os
import datetime

def log_message(message):
    """
    Logs a message with a timestamp to the optimization log file.
    """
    log_folder = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "optimizer_log.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def read_code_from_file(file_path):
    """
    Reads the content of the given file.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
        log_message(f"Successfully read code from: {file_path}")
        if not code.strip():
            log_message("Warning: The file is empty.")
            return None
        else:
            log_message("Code successfully read.")
        return code
    except Exception as e:
        log_message(f"Failed to read file: {e}")
        return None

def optimize_code(code_content):
    """
    Sends the code to Ollama for optimization.
    """
    client = ollama.Client()
    model = 'qwen2.5-coder:0.5b'
    system_prompt = (
        "You are a code optimization agent. Your task is to improve the given code by adding missing checks, "
        "exception handling, try-catch blocks, validating inputs, handling edge cases,value errors, and make it more robust against runtime errors. "
        "You must not remove essential logic. Return only the updated and optimized code."
    )

    prompt = f"Please optimize the following code with all the necessary safety and error handling improvements:\n\n```{code_content}```"

    log_message("Sending code for optimization to supergit optimizer...")

    try:
        response = client.generate(
            model=model,
            prompt=prompt,
            system=system_prompt,
            stream=False
        )
        log_message("Optimization received successfully.")
        return response.response.strip()
    except Exception as e:
        log_message(f"Failed to get optimized code from supergit optimizer: {e}")
        return None

def save_optimized_code(code_text, original_file):
    """
    Saves the optimized code to a file in the 'optim' folder.
    """
    optim_folder = os.path.join(os.getcwd(), "optim")
    os.makedirs(optim_folder, exist_ok=True)

    base_name = os.path.basename(original_file)
    optimized_file_path = os.path.join(optim_folder, base_name)

    try:
        with open(optimized_file_path, "w", encoding="utf-8") as f:
            f.write(code_text)
        log_message(f"Optimized code saved at: {optimized_file_path}")
        return optimized_file_path
    except Exception as e:
        log_message(f"Failed to save optimized code: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Code Optimizer using supergit optimizer.")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the code file to optimize')

    args = parser.parse_args()
    file_path = args.file 

    log_message("Starting code optimization job.")
    code = read_code_from_file(file_path)

    if code:
        optimized_code = optimize_code(code)
        if optimized_code:
            save_optimized_code(optimized_code, file_path)
        else:
            log_message("Optimization failed or returned empty.")
    else:
        log_message("No code content to optimize.")

    log_message("Code optimization job completed.")

if __name__ == "__main__":
    main()
#python optimizer.py --file coder_folder/test.py
