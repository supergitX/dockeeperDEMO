import ollama
import os
import argparse
import datetime

def log_message(message):
    """
    Logs a message with a timestamp to a log file.
    """
    log_folder = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_folder, exist_ok=True)
    
    log_file = os.path.join(log_folder, "codegen_log.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def generate_code_with_ollama(prompt):
    """
    Generates code using the Ollama API based on the provided prompt.
    """
    client = ollama.Client()
    model = 'qwen2.5-coder:0.5b'
    system_prompt = (
        "You are an expert code generator who generates a well-commented and documented code. "
        "You are a part of CI/CD pipeline and your outputs are sent to a code reviewer. "
        "Please ensure to give only the code with comments. Be concise and factual. "
        "If the user query is not related to code generation then state that you are a code generator only."
    )

    log_message("Generating code with prompt: " + prompt)

    if any(keyword in prompt.lower() for keyword in ["code", "script", "function", "class", "program"]):
        response = client.generate(
            model=model,
            prompt=prompt,
            system=system_prompt,
            stream=False
        )

        generated_text = response.response

        if "```" in generated_text:
            code_blocks = generated_text.split("```")
            if len(code_blocks) > 1:
                return code_blocks[1].strip()
            else:
                return generated_text.strip()
        else:
            return generated_text.strip()
    else:
        return "I am a code generator only."

def save_file(content, file_type, name=""):
    """
    Saves the given content into a file with the specified file type in the 'coder_folder' directory.
    """
    coder_folder = os.path.join(os.getcwd(), "coder_folder")
    os.makedirs(coder_folder, exist_ok=True)

    extensions = {"python": "py", "py": "py", "java": "java", "c": "c", "cpp": "cpp", "js": "js", "html": "html"}
    file_type = extensions.get(file_type.lower(), file_type)

    file_name = f"{name if name else 'generated_code'}.{file_type}"
    file_path = os.path.join(coder_folder, file_name)

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        log_message("File saved successfully at: " + file_path)
        return file_path
    except Exception as e:
        log_message("Error saving file: " + str(e))
        return None

def create(user_prompt, name=""):
    output_code = generate_code_with_ollama(user_prompt)
    log_message("Generated Code:\n" + output_code)

    # Detect file type (first line should be like 'python', 'c', etc.)
    first_line_end = output_code.find("\n")
    file_type = output_code[:first_line_end].strip()
    content = output_code[first_line_end + 1:].strip()

    log_message(f"Detected file type: {file_type}")
    log_message("Saving file...")
    save_file(content, file_type, name)

def main():
    parser = argparse.ArgumentParser(description="Generate and save code using supergit.")
    parser.add_argument('--prompt', '-p', type=str, required=True, help='Prompt to generate code')
    parser.add_argument('--filename', '-f', type=str, default="", help='Desired filename (without extension)')

    args = parser.parse_args()

    log_message("Starting code generation job")
    create(args.prompt, args.filename)
    log_message("Job completed.")

if __name__ == "__main__":
    main()


#python code_gen_cli.py --prompt "code to reverse a string in python" --filename "reverse_string"