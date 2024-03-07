#!../python/env/bin/python
"""
Check for a config file.
Given the results, print the associated doc files in test_bash
"""
import json
import sys

sys.path.insert(1, "tests")
# import module_merger

show_all_hints = True


def main():
    functions = [foo for foo in dir(test_bash) if "test_" in foo]
    functions.remove("test_but_actually_just_write_status")
    sep = "\n\t"
    print(f"Checking for hints avaliable for {len(functions)} functions")
    print("Hints are marked with `->`\n\n")
    hint_conf = {}
    complete = True

    if test_bash.isfile("tests/func_status.json"):
        with open("tests/func_status.json", "r") as source:
            hint_conf = json.load(source)
    else:
        print(" -> Please run `pytest` first to update the hint config!\n")
        complete = False
    for foo in hint_conf:
        if hint_conf[foo] == False and foo in functions:
            print(" ->", f"{foo} is incomplete...{getattr(test_bash,foo).__doc__}")
            complete = False
            if not show_all_hints:
                break

    hints_left = [1 for foo in hint_conf if hint_conf[foo] == False]
    print(
        f"{sum(hints_left)} Hints left, complete this task and run `pytest` to update these hints"
    )

    if complete:
        print("Good job, no hints available!")
    else:
        print("Check for documentation with `man {command}`")
        print("\tor use the help parameter `{command} --help`")


if __name__ == "__main__":
    main()
