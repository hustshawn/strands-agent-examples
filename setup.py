from setuptools import setup, find_packages

setup(
    name="strands-agents-demo",
    version="0.1.0",
    description="Demo implementations using the Strands Agents SDK",
    author="Strands Agents",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "strands-agents==0.1.4",
        "strands-agents-tools==0.1.3",
    ],
)