from cx_Freeze import setup, Executable

setup(
    name = "IHM_students",
    version = "1",
    description = "M2I & MQL - IHM Students",
    executables = [Executable("main.py")],
)
