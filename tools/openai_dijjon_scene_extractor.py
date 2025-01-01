import os
import re
import openai
from openai import OpenAI, OpenAIError
import json

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

# Set your OpenAI API key
client = OpenAI(api_key=openai_api_key)

def find_scene_files(directory):
    """
    Finds all scene files in the given directory matching the pattern act_<act_number>_s_<scene_number>.txt
    """
    pattern = re.compile(r'act_(\d+)_s_(\d+)\.txt$')
    files = {}
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            act_num = int(match.group(1))
            scene_num = int(match.group(2))
            if act_num not in files:
                files[act_num] = {}
            files[act_num][scene_num] = os.path.join(directory, filename)
    return files

def get_user_scene_counts():
    """
    Prompts the user to input the number of acts and the number of scenes per act.
    Returns a dictionary with act numbers as keys and number of scenes as values.
    """
    scene_counts = {}
    while True:
        try:
            num_acts = int(input("Enter the number of acts: "))
            if num_acts <= 0:
                print("Number of acts must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    for act in range(1, num_acts + 1):
        while True:
            try:
                num_scenes = int(input(f"Enter the number of scenes in Act {act}: "))
                if num_scenes <= 0:
                    print("Number of scenes must be positive.")
                    continue
                scene_counts[act] = num_scenes
                break
            except ValueError:
                print("Please enter a valid integer.")
    return scene_counts

def read_scene_content(file_path):
    """
    Reads and returns the content of the given scene file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_scene_with_openai(scene_content, debug_file="debug_response_dijjon.txt"):
    """
    Sends the scene content to OpenAI API with instructions to extract and format it into the tasks dictionary structure.
    Returns the processed JSON response.
    """
    prompt = f"""
    You are an assistant helping to build a dynamic quest system for a game. Given the following scene content, extract the necessary information and format it into a Python dictionary structure as shown below. Ensure the response is strictly in valid JSON format without any additional text. Use double quotes for all property names and string values.

    Scene Content:
    \"\"\"
    {scene_content}
    \"\"\"

    Desired Format:
    {{
        "name": "<Task Name>",
        "type": "<Task Type>",
        "complete": false,
        "narrative": {{
            1: "<Narrative step 1>",
            2: "<Narrative step 2>",
            3: "<Narrative step 3>"
        }},
        "answers": {{
            1: ["<Option 1>", "<Option 2>", ...],
            2: ["<Option 1>", "<Option 2>", ...],
            3: ["<Option 1>", "<Option 2>", ...]
        }},
        "scripts": {{
            1": Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3
        }},
        "data": {{
            "<key1>": "<value1>",
            "<key2>": "<value2>"
        }}
    }}
    """


    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for structuring game quest tasks."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,  # Ensures deterministic output
            max_tokens=3500,
            n=1,
            stop=None
        )

        # Save raw response for debugging
        raw_response = str(response)
        with open(debug_file, "w") as file:
            file.write(raw_response)
            print(f"Raw API response saved to {debug_file}")

        content = response.choices[0].message.content
        print("API Response Content:")
        print(content)

        # Find all code blocks and filter for Python
        code_blocks = re.findall(r"```(.*?)```", content, re.DOTALL)
        for block in code_blocks:
            if block.startswith("json"):
                script_content = block.replace("json", "", 1).strip()
                return script_content

    except Exception as e:
        print(f"Error processing scene with OpenAI: {e}")
        return None

def save_task_dict(act_num, scene_num, task_dict, output_directory):
    """
    Saves the task dictionary into a Python file named act_<act_num>_s_<scene_num>.py
    """
    filename = f'act_{act_num}_s_{scene_num}.py'
    file_path = os.path.join(output_directory, filename)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"task = {repr(task_dict)}\n")
        print(f"Saved: {file_path}")
    except Exception as e:
        print(f"Error saving task dictionary: {e}")

def main():
    # Define directories
    input_directory = 'C:/Users/zanem/DijjonAlphaDevelopment/assets/resources/act1'  # Directory containing scene files
    output_directory = input_directory  # Directory to save processed task files

    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get scene counts from user
    scene_counts = get_user_scene_counts()

    # Find scene files
    scene_files = find_scene_files(input_directory)

    # Iterate through acts and scenes
    for act_num, num_scenes in scene_counts.items():
        for scene_num in range(1, num_scenes + 1):
            # Check if the file exists
            if act_num in scene_files and scene_num in scene_files[act_num]:
                file_path = scene_files[act_num][scene_num]
                print(f"Processing Act {act_num}, Scene {scene_num}: {file_path}")
                scene_content = read_scene_content(file_path)
                task_dict = process_scene_with_openai(scene_content)
                if task_dict:
                    save_task_dict(act_num, scene_num, task_dict, output_directory)
                else:
                    print(f"Failed to process Act {act_num}, Scene {scene_num}")
            else:
                print(f"Scene file for Act {act_num}, Scene {scene_num} not found in {input_directory}.")

if __name__ == "__main__":
    main()
