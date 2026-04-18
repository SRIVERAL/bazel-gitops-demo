load("@rules_python//python:pip.bzl", "compile_pip_requirements")

# Esta es la regla que Bazel no encontraba
compile_pip_requirements(
    name = "requirements",
    src = "requirements.txt",
    requirements_txt = "requirements_lock.txt", # Este será el nombre del archivo lock
)