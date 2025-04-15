from setuptools import setup, find_packages

setup(
    name='Vortex',
    version='1.2',
    include_package_data=True,
    install_requires=["click", "pyperclip", "pyautogui", "setuptools", "google.generativeai", "dotenv"],
    packages=find_packages(),
    py_modules=["main"],
    author='Kephas Tetteh',
    author_email='tettehkephas@gmail.com',
    description='A simple tool that brings ai into your terminal',
    url=' https://github.com/ichigo-k/Vortex',
    entry_points={
        "console_scripts": [
            "vortex=main:solve"
        ],
    },
)