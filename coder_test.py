import ollama

def generate_code_with_ollama(prompt):
    """
    Generates code using the Ollama API based on the provided prompt.

    Args:
        prompt (str): The user's request for code.

    Returns:
        str: The generated code with comments, or a message indicating
             that the query is not related to code generation.
    """
    client = ollama.Client()
    model = 'qwen2.5-coder:0.5b'
    system_prompt = "You are an expert code generator who generates a well commented and documented code. You are a part of CI/CD pipeline and your outputs are sent to a code reviewer. Please ensure to give only the code with comments. Be concise and factual. If the user query is not related to code generation then state that you are a code generator only."

    if any(keyword in prompt.lower() for keyword in ["code", "script", "function", "class", "program"]):
        response = client.generate(
            model=model,
            prompt=prompt,
            system=system_prompt,
            stream=False
        )
        #write in log file

        generated_text = response.response

        if "```" in generated_text:
            # Extract code block if it's enclosed in triple backticks
            code_blocks = generated_text.split("```")
            if len(code_blocks) > 1:
                return code_blocks[1].strip()
            else:
                return generated_text.strip()
        else:
            return generated_text.strip()
    else:
        return "I am a code generator only."
"""
user_prompt = "code to find prime numbers in c"#input("Enter your code request: ")
output_code = generate_code_with_ollama(user_prompt)
print("ollama>> " + output_code)"""
import os

def save_file(content, file_type, name=""):
    """
    Saves the given content into a file with the specified file type in the 'coder_folder' directory.

    Args:
        content (str): The content to be written into the file.
        file_type (str): The file extension/type (e.g., 'py', 'java', 'txt').

    Returns:
        str: The path of the saved file or an error message if the operation fails.
    """
    # Define the directory where the file will be saved
    coder_folder = os.path.join(os.getcwd(), "coder_folder")
    
    # Ensure the directory exists
    os.makedirs(coder_folder, exist_ok=True)
    
    # Create a unique file name

    if file_type in ["python","py"]:
        file_type = "py"
    elif file_type in ["java"]:
        file_type = "java"
    elif file_type in ["c"]:
        file_type = "c"
    elif file_type in ["cpp"]:  
        file_type = "cpp"
    elif file_type in ["js"]:
        file_type = "js"
    elif file_type in ["html"]:
        file_type = "html"

    file_name = f"{name if name else 'generated_code'}.{file_type}"

    print("\n\ncoder>> Saving as File name" + file_name)

    file_path = os.path.join(coder_folder, file_name)

    try:
        # Write the content to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print("\n\ncoder>> File saved successfully at: " + file_path)
        return f"File saved successfully at: {file_path}"
    except Exception as e:
        print("\n\ncoder>> Error saving file: " + str(e))
        return f"Error saving file: {e}"
    
def create(user_prompt, name=""):
    #user_prompt =input("Enter your code request: ")
    output_code = generate_code_with_ollama(user_prompt)
    print("coder>> \n" + output_code)

    file_type = output_code[:output_code.find("\n")]
    print("\n\ncoder>> File type: " + file_type)

    content = output_code[output_code.find("\n")+1::]
    print("\n\ncoder>> Content\n" + content)

    print("\n\ncoder>> Saving file")
    # Save the file with the specified name
    save_file(content, file_type, )


create("code to find prime number in python","test.py") #prompt,name