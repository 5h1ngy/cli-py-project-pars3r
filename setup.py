from setuptools import setup, find_packages

setup(
    name="cli-py-project-pars3r",             # Nome del pacchetto
    version="0.1.0",             # Versione del pacchetto
    packages=find_packages(),    # Cerca automaticamente i pacchetti nella directory
    install_requires=[],         # Elenca le dipendenze qui
    entry_points={
        'console_scripts': [
            'pars3r=bin.main:app',  # Nome comando=modulo:funzione
        ],
    },
    description="Un esempio di script Python installabile globalmente.",
    long_description=open("README.md").read(),  # Opzionale, per descrizioni lunghe
    long_description_content_type="text/markdown",
    author="5h1ngy",
    author_email="sig.scarano@outlook.it",
    url="https://github.com/5h1ngy/cli-py-project-pars3r",  # (Opzionale) URL del progetto
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versione minima di Python richiesta
)