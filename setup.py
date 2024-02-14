from setuptools import setup, Extension
from Cython.Build import cythonize

# Define the extension module
extensions = [
    Extension(
        "crosscat.src.cython_code.State",  # Name of the module to generate
        sources=["crosscat/cpp_code/src/State.cpp"],  # Path to the .cpp source file
        include_dirs=["crosscat/cpp_code/include"],  # Include directory for header files
        language="c++",  # Specify the language for compilation
        extra_compile_args=["-std=c++11"],  # Use C++11 standard
    )
]

# Setup function to specify details
setup(
    name="State",
    ext_modules=cythonize(extensions, language_level="3"),  # Specify Python 3 language level
)
