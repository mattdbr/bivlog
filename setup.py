from cx_Freeze import setup, Executable

setup(
    name = "Biv Logger",
    version = "0.1",
    description = "I wish logging was this easy",
    executables = [Executable("biv.py")])