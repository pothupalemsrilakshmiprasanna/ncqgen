from setuptools import find_packages,setup

setup(
         name='mcqgenerator',
         version='0.0.1',
         author='prasanna',
         author_email='prasannaprasanna14200@gmail.com',
         install_requires=("openai","langchain","streamlit","python-dotenv","pyPDF2"),
         packages=find_packages()
)