import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    files_with_suffix = []
    dir_content = os.listdir(path)
    for p in dir_content:
        path_joined = os.path.join(path, p)
        if os.path.isfile(path_joined):
            if p[-2:] == suffix:
                files_with_suffix.append(path_joined)
        elif os.path.isdir(path_joined):
            files_with_suffix = files_with_suffix + find_files(suffix, path_joined)

    return files_with_suffix


def test():
    print(find_files(".c", "./testdir"))


test()
