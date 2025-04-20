import ollama
import argparse
import os
import datetime

def log_message(message):
    """
    Logs a message with a timestamp to the review log file.
    """
    log_folder = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "review_log.txt")
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
            log_message(f"Code content:\n{code}")
        return code
    except Exception as e:
        log_message(f"Failed to read file: {e}")
        return None

def review_code(code_content):
    """
    Sends the code to Ollama for review.
    """
    client = ollama.Client()
    model = 'qwen2.5-coder:0.5b'
    system_prompt = (
        "You are an expert code reviewer who reviews the code and checks for any linting errors, "
        "boundary conditions that may cause runtime errors,also state the need to establish necessary try-catch-except blocks "
        "to handle errors. You need to output a code report with review of code and feedback verbose on quality and robustness against boundary cases or wrong inputs of the code with explanation."
        "if you find promblems then mention that part of the code and give the reason why it is a problem. "
        "start the review with 'Code Review Report by supergit_reviewer:' and end with 'End of Review Report'."
    )

    prompt = f"Please review the following code and give review report:\n\n```{code_content}```"

    log_message("Sending code for review to supergit reviewer...")

    try:
        response = client.generate(
            model=model,
            prompt=prompt,
            system=system_prompt,
            stream=False
        )
        log_message("Review received successfully.")
        return response.response.strip()
    except Exception as e:
        log_message(f"Failed to get review from supergit reviewer: {e}")
        return "Error in code review process."

def save_review(review_text, original_file):
    """
    Saves the review to a .txt file in the 'reviews' folder.
    """
    reviews_folder = os.path.join(os.getcwd(), "reviews")
    os.makedirs(reviews_folder, exist_ok=True)

    base_name = os.path.basename(original_file)
    name_without_ext = os.path.splitext(base_name)[0]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    review_file_path = os.path.join(reviews_folder, f"{name_without_ext}_review_{timestamp}.txt")

    try:
        with open(review_file_path, "w", encoding="utf-8") as f:
            f.write(review_text)
        log_message(f"Review saved at: {review_file_path}")
        return review_file_path
    except Exception as e:
        log_message(f"Failed to save review: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Code Reviewer using supergit reiewer.")
    parser.add_argument('--file', '-f', type=str, required=True, help='Path to the code file to review')

    args = parser.parse_args()
    file_path = args.file 

    log_message("Starting code review job.")
    code = read_code_from_file(file_path)

    if code:
        review = review_code(code)
        save_review(review, file_path + '.txt')
    else:
        log_message("No code content to review.")

    log_message("Code review job completed.")

if __name__ == "__main__":
    main()
#python reviewer.py --file coder_folder/test.py
