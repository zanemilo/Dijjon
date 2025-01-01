import os
import re
import json
import pprint
import glob

def convert_task_file(file_path):
    """
    Converts a .py file assigning a JSON string to 'task' into a Python dictionary.

    Parameters:
    - file_path (str): Path to the .py file to convert.

    Returns:
    - dict: The converted task dictionary, or None if conversion failed.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Regex to match: task = '...'
        pattern = r'^task\s*=\s*[\'"](.+?)[\'"]\s*$'
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

        if not match:
            print(f"No matching 'task' assignment found in {file_path}. Skipping.")
            return None

        json_str = match.group(1)

        # Decode escaped characters like \n
        json_str = bytes(json_str, "utf-8").decode("unicode_escape")

        # Parse JSON string into Python dict
        task_dict = json.loads(json_str)

        return task_dict

    except json.JSONDecodeError as jde:
        print(f"JSON decode error in {file_path}: {jde}")
        return None
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def build_tasks_dict(task_dicts):
    """
    Builds the final 'tasks' dictionary from a list of task dictionaries.

    Parameters:
    - task_dicts (list): List of task dictionaries.

    Returns:
    - dict: The final 'tasks' dictionary.
    """
    tasks = {}
    for idx, task in enumerate(task_dicts, start=1):
        # Map fields to the desired structure
        tasks[idx] = {
            "name": task.get("name", f"Task {idx}"),
            "type": task.get("type", "unknown"),
            "complete": task.get("complete", False),
            "narrative": {},
            "answers": {},
            "scripts": {},
            "data": task.get("data", {})
        }

        # Populate narrative
        narrative = task.get("narrative", {})
        for step_id, narrative_text in narrative.items():
            try:
                step_int = int(step_id)
                tasks[idx]["narrative"][step_int] = narrative_text
            except ValueError:
                print(f"Invalid narrative step ID '{step_id}' in Task {idx}. Skipping.")

        # Populate answers
        answers = task.get("answers", {})
        for step_id, options in answers.items():
            try:
                step_int = int(step_id)
                tasks[idx]["answers"][step_int] = options
            except ValueError:
                print(f"Invalid answers step ID '{step_id}' in Task {idx}. Skipping.")

        # Populate scripts
        scripts = task.get("scripts", {})
        for step_id, script_call in scripts.items():
            try:
                step_int = int(step_id)
                if script_call:
                    # Assume script_call is a string like "Quest.method_call1"
                    # We need to reference it without quotes
                    tasks[idx]["scripts"][step_int] = script_call
                else:
                    tasks[idx]["scripts"][step_int] = None
            except ValueError:
                print(f"Invalid scripts step ID '{step_id}' in Task {idx}. Skipping.")

    return tasks

def serialize_tasks(tasks):
    """
    Serializes the 'tasks' dictionary into a Python-formatted string,
    ensuring that 'scripts' are actual method calls.

    Parameters:
    - tasks (dict): The 'tasks' dictionary.

    Returns:
    - str: The serialized 'tasks' dictionary as a string.
    """
    serialized_tasks = "tasks = {\n"
    for task_id, task in tasks.items():
        serialized_tasks += f"    {task_id}: {{\n"
        for key, value in task.items():
            if key == "scripts":
                serialized_tasks += f"        \"{key}\": {{\n"
                for script_id, script_call in value.items():
                    if script_call:
                        serialized_tasks += f"            {script_id}: {script_call},\n"
                    else:
                        serialized_tasks += f"            {script_id}: None,\n"
                serialized_tasks += f"        }},\n"
            elif key == "narrative" or key == "answers":
                serialized_tasks += f"        \"{key}\": {{\n"
                for sub_id, sub_val in value.items():
                    if isinstance(sub_val, list):
                        # For answers which are lists
                        options = ', '.join([f"\"{option}\"" for option in sub_val])
                        serialized_tasks += f"            {sub_id}: [{options}],\n"
                    else:
                        # For narrative which are strings
                        serialized_tasks += f"            {sub_id}: \"{sub_val}\",\n"
                serialized_tasks += f"        }},\n"
            elif key == "complete":
                serialized_tasks += f"        \"{key}\": {value},\n"
            elif key == "data":
                serialized_tasks += f"        \"{key}\": {pprint.pformat(value, indent=12)},\n"
            else:
                serialized_tasks += f"        \"{key}\": \"{value}\",\n"
        serialized_tasks += f"    }},\n"
    serialized_tasks += "}\n"
    return serialized_tasks

def save_tasks_py(serialized_tasks, output_path):
    """
    Saves the serialized 'tasks' dictionary to a .py file.

    Parameters:
    - serialized_tasks (str): The serialized 'tasks' dictionary.
    - output_path (str): Path to the output .py file.

    Returns:
    - None
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(serialized_tasks)
        print(f"'tasks' dictionary successfully saved to {output_path}")
    except Exception as e:
        print(f"Error saving 'tasks' dictionary to {output_path}: {e}")

def main():
    # Define directories
    input_directory = 'C:/Users/zanem/DijjonAlphaDevelopment/assets/resources/act3'  # Update this path as needed
    output_file = 'C:/Users/zanem/DijjonAlphaDevelopment/assets/resources/a_tasks.py'  # Desired output path

    # Find all .py files matching the pattern act_*_s_*.py
    search_pattern = os.path.join(input_directory, 'act_*_s_*.py')
    task_files = glob.glob(search_pattern)

    if not task_files:
        print(f"No task files found in {input_directory} matching pattern 'act_*_s_*.py'.")
        return

    print(f"Found {len(task_files)} task file(s) to process.")

    # Extract task dictionaries from each file
    task_dicts = []
    for file_path in task_files:
        print(f"Processing file: {file_path}")
        task = convert_task_file(file_path)
        if task:
            task_dicts.append(task)
        else:
            print(f"Failed to extract task from {file_path}.")

    if not task_dicts:
        print("No valid tasks extracted. Exiting.")
        return

    # Build the final 'tasks' dictionary
    tasks = build_tasks_dict(task_dicts)

    # Serialize the 'tasks' dictionary
    serialized_tasks = serialize_tasks(tasks)

    # Save the 'tasks' dictionary to the output .py file
    save_tasks_py(serialized_tasks, output_file)

if __name__ == "__main__":
    main()
