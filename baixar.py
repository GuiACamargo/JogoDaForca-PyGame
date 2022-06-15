import cx_Freeze

executables = [cx_Freeze.Executable(script="jogo.py", icon="favicon.ico")]

cx_Freeze.setup(
    name="jogo",
    options={"build_exe": {"packages": ["pygame", "pygame_widgets"],
                           "include_files": ["assets", "registros", "favicon.ico"]
                            }},
    executables = executables
)