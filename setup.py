import os
import subprocess
from pathlib import Path

import tomli
from setuptools import find_packages, setup
from setuptools.command.build_ext import build_ext
from setuptools.extension import Extension


class CMakeExtension(Extension):
    """CMakeExtension for building the ha_hello."""

    def __init__(self, name: str, sourcedir: str = "") -> None:
        """Initialize the CMakeExtension."""
        super().__init__(name, sources=[])
        self.sourcedir = os.fspath(Path(sourcedir).resolve())


class CMakeBuild(build_ext):
    """CMake build for bertha-simulator."""

    def run(self) -> None:
        """Run the CMake build."""
        try:
            subprocess.check_output(["cmake", "--version"])
        except OSError as err:
            raise RuntimeError(
                "CMake must be installed to build the following extensions: "
                + ", ".join(e.name for e in self.extensions)
            ) from err

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext: Extension) -> None:
        """Build the extension.

        Args:
            ext (Extension): The extension to build.
        """
        cmake_args = [
            "-DBUILD_TESTS=OFF",
            "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON",
        ]

        build_temp = self.build_temp
        if not os.path.exists(build_temp):
            os.makedirs(build_temp)

        subprocess.check_call(["cmake", ext.sourcedir] + cmake_args, cwd=build_temp)
        subprocess.check_call(["cmake", "--build", ".", "--"], cwd=build_temp)


# Read dependencies from pyproject.toml
with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)

setup(
    name=pyproject["project"]["name"],
    version=pyproject["project"]["version"],
    description=pyproject["project"]["description"],
    author=pyproject["project"]["authors"][0]["name"],
    author_email=pyproject["project"]["authors"][0]["email"],
    packages=find_packages(include=["ha_hello", "ha_hello.*"]),
    ext_modules=[CMakeExtension("lib", sourcedir=".")],
    cmdclass={"build_ext": CMakeBuild},
    zip_safe=False,
    install_requires=pyproject["project"]["dependencies"],
    package_data={
        "ha_hello": [
            "lib/*.so",
        ]
    },
    include_package_data=True,
    python_requires=">=3.10",
)
