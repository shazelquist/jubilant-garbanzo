#!../python/env/bin/python
"""
Checks and grades files according to requests
"""

from inspect import currentframe
from os import environ
from os.path import isfile, isdir
import pytest
import json

func_status = {}


def test_empty_file():
    """
    Create an empty file named "empty_file"

    Use the `touch` command
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "empty_file"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" is empty')
        assert len(f_handle.read()) == 0
    func_status[currentframe().f_code.co_name] = True


def test_fox_file():
    """
    Create a file `fox.txt`

    fill this file with the following text
        `the quick brown fox jumps over the lazy dog`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "fox.txt"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert "the quick brown fox jumps over the lazy dog" in f_handle.read().lower()
    func_status[currentframe().f_code.co_name] = True


def test_cpy_file():
    """
    Copy the `spread_me` file from `one_dir` to `two_dir`

    Use the `cp` command
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "spread_me"
    print(f'Checking existence of "one_dir/{f_path}"')
    assert isfile("one_dir/" + f_path)
    print(f'Checking existence of "two_dir/{f_path}"')
    assert isfile("two_dir/" + f_path)
    with open("two_dir/" + f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert "42" in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_move_file():
    """
    Move `yourself.txt` from `lost_dir` to `found_dir`

    Use the `mv` command
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "yourself.txt"
    print(f'Checking existence of "lost_dir/{f_path}"')
    assert not isfile("lost_dir/" + f_path)
    print(f'Checking existence of "found_dir/{f_path}"')
    assert isfile("found_dir/" + f_path)
    with open("found_dir/" + f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert "awesome" in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_make_camel():
    """
    Rename the snake_case file `do_not_step` in `one_dir` so that it follow camelCase

    Use either the `mv` or `rename` command
    """
    func_status[currentframe().f_code.co_name] = False
    old_f_path = "one_dir/do_not_step"
    f_path = "one_dir/doNotStep"
    print(f'Checking existence of "{old_f_path}"')
    assert not isfile(old_f_path)
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    func_status[currentframe().f_code.co_name] = True


def test_rename_spaces_file_names_are_annoying():
    """
    Rename `spaces file names are annoying` in `one_dir` to `less_annoying`

    Use either the `mv` or `rename` command

    Note:
        How do you reference filenames with spaces?
        You can use an escape character before the space `\\`
        or surround it with quotations.
        Sometimes you can get lucky with `tab` completion too.
    """
    func_status[currentframe().f_code.co_name] = False
    old_f_path = "one_dir/spaces file names are annoying"
    f_path = "one_dir/less_annoying"
    print(f'Checking existence of "{old_f_path}"')
    assert not isfile(old_f_path)
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert "abc" in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_update_gitignore():
    """
    Update `../.gitignore` so that git ignores the `func_status.json` file

    Use `git status` to see if has correctly ignored this json file.

    Hint:
        While you could use any method you wish to update this file,
        we can use a special redirect `>>` to append this file without affecting
        the previous contents.
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "../.gitignore"
    print(f'Checking existence of "{f_path}"')
    ignore_file = "func_status.json"
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" contains {ignore_file}')
        assert ignore_file in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_file_perms_r():
    """
    Change the permissions of the `my_diary` file in `two_dir`
    so that it can not be read.

    Check file permissions of a file with `ls -o`
    Use the `chmod` command to complete this task.

    Hint:
        chmod can change the permissions for several groups.
        In general the parameters look like this
        `chmod {group_if_any, u,g,o,blank}{+ to add, - to remove}{read/write/execute}`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "two_dir/my_diary"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    print(f'Checking that "{f_path}" has correct read permissions')
    with pytest.raises(PermissionError):
        with open(f_path, "r") as f_handle:
            print(f_handle.read())
    func_status[currentframe().f_code.co_name] = True


def test_file_perms_w():
    """
    Change the permissions of the `cookie_jar` file in `two_dir`
    so that it can not be written to.

    Check file permissions of a file with `ls -o`
    Use the `chmod` command to complete this task.

    Hint:
        chmod can change the permissions for several groups.
        In general the parameters look like this
        `chmod {group_if_any, u,g,o,blank}{+ to add, - to remove}{read/write/execute}`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "two_dir/cookie_jar"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    print(f'Checking that "{f_path}" has correct read permissions')
    with pytest.raises(PermissionError):
        with open(f_path, "a") as f_handle:
            f_handle.write("- 1 cookie\n")
    func_status[currentframe().f_code.co_name] = True


def test_three_dir():
    """
    Create a directory `three_dir` in the `bash` directory

    Use the `mkdir` command
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "three_dir"
    print(f'Checking existence of "{f_path}"')
    assert isdir(f_path)
    func_status[currentframe().f_code.co_name] = True


def test_rm_me_file():
    """
    Remove the directory `rm_me_dir`

    Use the `rm` command

    IMPORTANT:
        There is no undo!
        Practice any command removals with `ls`
        or use the `-i` parameter
        example:
            `rm -i {target_file}`
            `ls {target_file}`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "rm_me_file"
    print(f'Checking existence of "{f_path}"')
    assert not isfile(f_path)
    func_status[currentframe().f_code.co_name] = True


def test_rm_me_dir():
    """
    Remove the directory `rm_me_dir`

    use either a recursive `rm` command
        or a `rm` command and the `rmdir` command

    IMPORTANT:
        There is no undo!
        Practice any command removals with `ls`
        or use the `-i` parameter
        example:
            `rm -i {target_file}`
            `ls {target_file}`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "rm_me_dir"
    print(f'Checking existence of "{f_path}"')
    assert not isdir(f_path)
    func_status[currentframe().f_code.co_name] = True


def test_basic_grep():
    """
    Create a file called `crazy_dice.txt`

    fill this file with the text from using `grep`
        to find the line in `lost_dir/search.txt` containing `crazy dice`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "crazy_dice.txt"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert "red a crazy dice jupyter" in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_pipe_grep():
    """
    Create a file called `special_code.txt`

    fill this file with the text from using `grep`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "special_code.txt"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert "red a crazy dice jupyter" in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_pipe_grep_wc():
    """
    Create a file called oo_words

    fill this file with the number of times `oo` appears in the file

    Use `grep -o` and `wc -w` to get your answer
    You will need to use a pipe in your command `|` to link them together
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "oo_words"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert str(int("11001", base=2)) in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_sha_sum():
    """
    Create a file called `sha_search`

    Fill this file with the sha256 sum of the `search.txt` file
        using the `sha256sum` command with the `-b` parameter

    Context:
        Why would we do this?
        Let's say we're downloading a firefox from some third-party website.
        We want to check if the file has been modified by the third-party website.
        We can use use a hash like a sha256 to partially validate the sketchy version
        of firefox to see if it's been changed from the one offically hosted by mozilla.
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "sha_search"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    check = "15a230b15dc5c178e92cf9f235be4c7c34e8edeb6008d3b563f91a614f70614e"
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert check in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_wildcards_q():
    """
    Create a file called `_j_.txt`

    Fill this file with the the concatenation of files in `two_dir/wildcards`
        that have `j` in the third position.

    Use either the `?` wildcard or `*`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "_j_.txt"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    check = int("11101001111001011101010001001011101011000000110100110", base=2)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert str(check) in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_wildcards_star():
    """
    Create a file called `e.txt`

    Fill this file with the the concatenation of files in `two_dir/wildcards`
        that have `e` in them.

    Use the wildcard `*`
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "e.txt"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    chk_str = (
        "10010000011110101000011000111001001000011000011110100101111011000110010010011010011"
        + "000001111111011010111001001011111101010000001111101101100101011101000011100100100110010110"
    )
    check = int(chk_str, base=2)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert str(check) in f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_find_dot_files():
    """
    Create a file called `sec_code.txt`

    Fill this file with the secret code found in a hidden file.

    You may find `ls` helpful some combination of the `-R` `-a` arguments.
    """
    func_status[currentframe().f_code.co_name] = False
    f_path = "sec_code.txt"
    print(f'Checking existence of "{f_path}"')
    assert isfile(f_path)
    chk_str = "100000"
    check = int(chk_str, base=2)
    with open(f_path, "r") as f_handle:
        print(f'Checking that "{f_path}" has correct contents')
        assert str(check) == f_handle.read()
    func_status[currentframe().f_code.co_name] = True


def test_environment_variables():
    """
    Create an environment variable named `ENV_VAR_ARE_USEFUL`

    Set its value to `very true`

    Note:
        Use the `export`
        You can view environment variables with `printenv`

    Context:
        Environment variables are a great way to store information.
        They provide crucial information for the location of executables, formats & states.
        It's a good place to put information that you don't want to commit publicly.
    """
    assert "ENV_VAR_ARE_USEFUL" in environ
    if "ENV_VAR_ARE_USEFUL" in environ:
        assert environ.get("ENV_VAR_ARE_USEFUL", "very true")


def test_but_actually_just_write_status():
    with open("tests/func_status.json", "w") as dest:
        json.dump(func_status, dest)
