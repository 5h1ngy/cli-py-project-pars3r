from setuptools import setup, find_packages

setup(
    name="myscript",             # Nome del pacchetto
    version="1.0.0",             # Versione del pacchetto
    packages=find_packages(),    # Cerca automaticamente i pacchetti nella directory
    install_requires=[],         # Elenca le dipendenze qui
    entry_points={
        'console_scripts': [
            'myscript=bin.main:app',  # Nome comando=modulo:funzione
        ],
    },
    description="Un esempio di script Python installabile globalmente.",
    long_description=open("README.md").read(),  # Opzionale, per descrizioni lunghe
    long_description_content_type="text/markdown",
    author="Il Tuo Nome",
    author_email="tuo.email@example.com",
    url="https://github.com/tuo-repo",  # (Opzionale) URL del progetto
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versione minima di Python richiesta
)