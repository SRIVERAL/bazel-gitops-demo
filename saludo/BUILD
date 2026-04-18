# saludo/BUILD
load("@rules_python//python:py_binary.bzl", "py_binary")

py_binary(
    name = "app_saludo",
    srcs = ["main.py"],
    main = "main.py",
    deps = [
        "@pypi//requests",
        "@pypi//urllib3",
        "@pypi//idna",
        "@pypi//charset_normalizer",
        "@pypi//certifi",
        "@pypi//prometheus_client",
        "@pypi////jaraco_context",
        "@pypi////wheel",
    ],
)