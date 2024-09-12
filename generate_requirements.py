import subprocess

def generate_requirements():
    subprocess.run(["pip-compile", "--output-file=requirements.txt", "pyproject.toml"])

if __name__ == "__main__":
    generate_requirements()
