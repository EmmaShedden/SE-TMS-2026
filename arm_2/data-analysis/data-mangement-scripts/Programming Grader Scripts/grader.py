from pathlib import Path
import shutil
import subprocess
import csv


def run():
    create_input_data()
    template_dict = {}
    templates_folder = Path("./template_files")
    template_files = templates_folder.glob("[!.]*")
    student_folder = Path("./student_files")
    for t in template_files:
        name = t.name
        components = name.split("_", 3)
        problem_name = components[0] + "_" + components[1]
        # print(t, problem_name)
        if not problem_name in template_dict:
            template_dict[problem_name] = []
        template_dict[problem_name].append(t)
    # print(template_dict)

    problems = list(template_dict.keys())
    problems.append("fr_2")
    problems.append("fr_7")

    problems.sort()
    gradebook = manual_grades

    limited_run = [
        "fitb_1",
        # "fitb_2",
        # "fitb_3",
        # "fitb_4",
        # "fitb_5",
        # "fitb_6",
        # "fitb_7",
        # "fitb_8",
        # "fitb_9",
        # "fitb_10",
        # "fitb_11",
        # "fitb_12",
        # "fitb_13",
        # "fitb_14",
        # "fitb_15",  # Checked
        # "fitb_16",  # Checked
        # "fitb_17",  # Checked
        # "fitb_18",  # Checked
        # "fitb_19",  # Checked
        # "fitb_20",  # Checked
        # "fitb_21",  # Checked
        # "fitb_22",  # Checked
        # "fitb_23",  # Checked
        #"fitb_24",
        # "fr_1",  # Checked
        # "fr_2",  # Checked
        # "fr_3",  # Checked
        # "fr_4",  # Checked
        # "fr_5",  # Checked
        # "fr_6",  # Checked
        # "fr_7",  # Checked
        # "fr_8",  # Checked
        # "fr_9",  # Checked
        # "fr_10",  # Checked
        # "fr_11",  # Checked
        # "fr_12",  # Checked
        # "fr_13",  # Checked
        # "fr_14",  # Checked
        # "fr_15",  # Checked
    ]

    for p in problems:
        if p not in limited_run:
            continue
        print(p)
        template_paths = template_dict[p]
        search_string = f"**/{p}_*.cpp"
        # print(search_string)
        student_files = list(student_folder.glob(search_string))
        # print(student_files)
        student_files.sort()
        for sf in student_files:
            student_name = sf.parent.name
            if student_name not in gradebook:
                gradebook[student_name] = {}
            for t in template_paths:
                # print(type(t), t)
                # print(type(sf), sf)
                success, output = run_file(t, sf, verbose=True)
                # print(p, student_name, success)
                if correct_answers_dict[p][0]:
                    success = check_output(output, correct_answers_dict[p][0], strip=correct_answers_dict[p][1], ignore_case=correct_answers_dict[p][2])
                if success:
                    break
            gradebook[student_name][p] = success
    students = list(gradebook.keys())
    students.sort()
    with open('gradebook.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        headers = ["id"] + problems.copy()
        spamwriter.writerow(headers)
        for s in students:
            row = [s]
            for p in problems:
                if p in gradebook[s]:
                    if gradebook[s][p]:
                        row.append("Pass")
                    else:
                        row.append("Fail")
                else:
                    row.append("None")
            spamwriter.writerow(row)




def create_input_data():
    all_results_path = Path("./student_results")
    results_paths = all_results_path.glob("[!.]*")
    student_files =  Path("./student_files")
    shutil.rmtree(student_files)
    student_files.mkdir(parents=True, exist_ok=True)
    for r in results_paths:
        create_student_files(r)


def create_student_files(results_folder_path):
    results_folder_path = Path(results_folder_path)
    student_id = results_folder_path.name[:4]
    coding_section_paths = []
    for i in [1,2,3]:
        coding_section_path = results_folder_path / f"coding_section_{i}.csv"
        coding_section_paths.append(coding_section_path)

    all_responses = []
    def read_coding_section(coding_section_path):
        responses = []

        with open(coding_section_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter='@')
            # Problem id is index 8
            # Response is index 12
            headers = next(csv_reader)
            if headers[10].strip() == "shown":
                for i, row in enumerate(csv_reader):
                    if row[10].strip() == "True":
                        responses.append((row[8], row[13]))
            else:
                for i, row in enumerate(csv_reader):
                    responses.append((row[8], row[12]))
                    # print(f"\n[{i}]: ")
                    # for j, item in enumerate(row):
                    #     print(f" {j}: {item}", end = ",")
        # for r in responses:
        #     print(r[0], r[1])
        return responses
    
    for coding_section_path in coding_section_paths:
        all_responses.extend(read_coding_section(coding_section_path))

    student_files_path =  Path("./student_files") / student_id
    student_files_path.mkdir(parents=True, exist_ok=True)

    for r in all_responses:
        text = r[1]
        text = text.replace("\\n", "\n")
        text = text.replace("\\t", "    ")
        text = text.replace("%YOUR ANSWER HERE%","")
        text = text.replace('cout << \\"*"','cout << "*"')
        'cout << \\"*"'
        student_file = student_files_path / f"{r[0]}_student.cpp"
        if student_file.is_file():
            print(f"Student file '{student_file}' has a duplicate. Ignoring the duplicate")
            continue
        with open(student_file, "w") as f:
            f.write(text)





def check_output(text, correct_answers: list, strip: bool = True, ignore_case: bool = True):
    def strip_lines(input):
        new_input = "\n".join([x.strip() for x in input.split('\n')])
        return new_input.strip()
    
    if strip:
        text = strip_lines(text)
        correct_answers = [strip_lines(x) for x in correct_answers]
    if ignore_case:
        text = text.lower()
        correct_answers = [x.lower() for x in correct_answers]
    # print(f"Text: {[text]}")
    # print(f"Correct answers: {correct_answers}")
    if text in correct_answers:
        return True
    else:
        return False


def run_file(template_file_path, student_file_path, verbose=False):
    print("Running:", student_file_path)
    template_file_path = Path(template_file_path)
    template_file_name = template_file_path.name
    template_file_stem = template_file_path.stem
    student_file_path = Path(student_file_path)
    student_file_name = student_file_path.name
    working_folder =  Path("./working")
    new_template_file_path = working_folder / template_file_name
    new_student_file_path = working_folder / student_file_name
    executable_file_path = working_folder / template_file_stem

    shutil.rmtree(working_folder)
    working_folder.mkdir(parents=True, exist_ok=True)
    shutil.copy(template_file_path, new_template_file_path)
    shutil.copy(student_file_path, new_student_file_path)

    compile_command = f"g++ {new_template_file_path} -o {executable_file_path} -std=c++11 -w"
    if verbose:
        print(f"Complile command: {compile_command}")
    try:
        result = subprocess.run(compile_command.split(), capture_output=True, text=True, timeout=5)
    except subprocess.TimeoutExpired:
        return False, ""
    if verbose:
        print(f"result.returncode: {result.returncode}")
        print(f"result.stdout: \n\t{"\n\t".join(result.stdout.split("\n"))}")
        print(f"result.stderr: \n\t{"\n\t".join(result.stderr.split("\n"))}")
    if result.returncode != 0:
        return False, ""

    run_command = f"./{executable_file_path}"
    if verbose:
        print(f"Run command: {run_command}")
    try:
        result = subprocess.run(run_command.split(), capture_output=True, text=True, timeout=5)
    except subprocess.TimeoutExpired:
        return False, ""
    if verbose:
        print(f"result.returncode: {result.returncode}")
        print(f"result.stdout: \n\t{"\n\t".join(result.stdout.split("\n"))}")
        print(f"result.stderr: \n\t{"\n\t".join(result.stderr.split("\n"))}")
    if result.returncode != 0:
        return False, ""
    else:
        return True, result.stdout




correct_answers_dict = {
    "fitb_1" : ([],False,False),
    "fitb_2" : ([],False,False),
    "fitb_3" : ([],False,False),
    "fitb_4" : ([" ".join([str(x) for x in range(11, 122, 2)])], True, True),
    "fitb_5" : ([],False,False),
    "fitb_6" : ([" ".join([str(x) for x in range(1, 41)]), "\n".join([str(x) for x in range(1, 40)])], True, True),
    "fitb_7" : ([],False,False),
    "fitb_8" : (['*'*97], True, True),
    "fitb_9" : ([],False,False),
    "fitb_10" : ([],False,False),
    "fitb_11" : ([],False,False),
    "fitb_12" : ([],False,False),
    "fitb_13" : ([],False,False),
    "fitb_14" : ([],False,False),
    "fitb_15" : ([],False,False),
    "fitb_16" : (["Moo!"], True, True),
    "fitb_17" : ([],False,False),
    "fitb_18" : ([],False,False),
    "fitb_19" : ([],False,False),
    "fitb_20" : ([],False,False),
    "fitb_21" : ([],False,False),
    "fitb_22" : ([],False,False),
    "fitb_23" : ([],False,False),
    "fitb_24" : (["***\n**\n*"], True, True),
    "fr_2" : ([],False,False),
    "fr_3" : ([],False,False),
    "fr_4" : ([],False,False),
    "fr_5" : ([],False,False),
    "fr_6" : ([],False,False),
    "fr_7" : ([],False,False),
    "fr_8" : ([],False,False),
    "fr_9" : ([],False,False),
    "fr_10" : (["5 4 3 2 1 liftoff!", "5 4 3 2 1liftoff!", "5 4 3 2 1 0 liftoff!", "5 4 3 2 1 0liftoff!"],True,True),
    "fr_11" : ([],False,False),
    "fr_12" : ([],False,False),
    "fr_13" : ([],False,False),
    "fr_14" : ([],False,False),
    "fr_15" : ([],False,False),
}


manual_grades = {
"O327": {"fr_2" : True},
"5ZCK": {},
"A23A": {"fr_2" : True},
"A3RT": {"fr_2" : False},
"ACHS": {"fr_2" : False},
"BUB4": {"fr_2" : True},
"D5ZT": {"fr_2" : True},
"DOGU": {"fr_2" : False},
"G5XR": {"fr_2" : False},
"H0VK": {"fr_2" : False},
"IOON": {"fr_2" : False},
"J21O": {"fr_2" : True},
"J3QN": {"fr_2" : True},
"L7QH": {"fr_2" : False},
"LIF8": {"fr_2" : True},
"M4QP": {"fr_2" : True},
"M6YD": {"fr_2" : False},
"NY50": {"fr_2" : False},
"P6XQ": {"fr_2" : True},
"PA20": {"fr_2" : False},
"Q7MD": {"fr_2" : False},
"RB3Z": {"fr_2" : False},
"TN3S": {"fr_2" : False},
"V7CR": {"fr_2" : False},
"X2VR": {"fr_2" : False},
"X4TN": {"fr_2" : False},
"X8LP": {"fr_2" : True},
"Y2JN": {"fr_2" : False},
}


if __name__ == "__main__":
    # success, output = run_file("./hello_template.cpp", "./hello_student.cpp")
    # if success:
    #     print("No error codes!")
    # else:
    #     print("Submission produced error codes")

    # correct_answers = ["Hello World!\nHello Moon!", "Hello World!\nhello moon!"]
    # success = check_output(output, correct_answers)
    # if success:
    #     print("Output is correct!")
    # else:
    #     print("Output is not correct")

    # create_student_files("./student_results/ACHS_20241124-143312")
    # create_input_data()

    # success, output = run_file("./template_files/fitb_3_template.cpp", "./student_files/M4QP/fitb_3_student.cpp")
    # success, output = run_file("./template_files/fitb_3_template.cpp", "./student_files/A3RT/fitb_3_student.cpp")
    # success, output = run_file("./template_files/fitb_2_template.cpp", "./student_files/M4QP/fitb_2_student.cpp")
    # success, output = run_file("./template_files/fitb_2_template.cpp", "./student_files/A3RT/fitb_2_student.cpp")
    # success, output = run_file("./template_files/fitb_2_template_alt_1.cpp", "./student_files/A3RT/fitb_2_student.cpp")
    # if success:
    #     print("No error codes!")
    # else:
    #     print("Submission produced error codes")

    run()





# TODO
# - Remove "%YOUR ANSWER HERE%" from all answers
# - allow alternate template files for problems like "void " in fitb_2