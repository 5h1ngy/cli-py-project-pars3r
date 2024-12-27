### Guida: Creare un Pacchetto Python Installabile con `pip`

Questa guida ti guiderà attraverso i passaggi necessari per trasformare uno script Python in un pacchetto installabile globalmente utilizzando `pip`.

---

#### **1. Prepara l'Ambiente**
Assicurati di avere Python e `pip` installati sul tuo sistema. Puoi verificare con i seguenti comandi:
```bash
python3 --version
pip --version
```

Se non sono installati, segui la guida ufficiale di Python per la tua piattaforma.

---

#### **2. Organizza i File del Progetto**
Crea una struttura base per il tuo pacchetto. Supponiamo che il pacchetto si chiami `myscript`:
```
myscript/
├── myscript/
│   ├── __init__.py   # Può essere vuoto, ma necessario per il pacchetto
│   └── cli.py        # Contiene il tuo script principale
├── setup.py          # File per configurare l'installazione
└── README.md         # (Opzionale) Informazioni sul tuo pacchetto
```

- **`cli.py`**: Questo sarà il cuore del tuo script. Definisci una funzione `main()` che verrà utilizzata come punto di ingresso.

Esempio di `cli.py`:
```python
def main():
    print("Ciao! Questo è il mio script Python eseguibile globalmente.")
```

---

#### **3. Configura il File `setup.py`**
Il file `setup.py` è necessario per configurare il pacchetto e definire i suoi dettagli. Crealo nella directory principale del progetto.

Esempio di `setup.py`:
```python
from setuptools import setup, find_packages

setup(
    name="myscript",             # Nome del pacchetto
    version="1.0.0",             # Versione del pacchetto
    packages=find_packages(),    # Cerca automaticamente i pacchetti nella directory
    install_requires=[],         # Elenca le dipendenze qui
    entry_points={
        'console_scripts': [
            'myscript=bin.cli:main',  # Nome comando=modulo:funzione
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
```

---

#### **4. Aggiungi il File `README.md`**
Un file `README.md` è utile per descrivere il tuo progetto. Non è obbligatorio, ma è una buona pratica.

Esempio:
```markdown
# MyScript
Questo è un esempio di pacchetto Python che può essere installato globalmente con `pip`.

## Installazione
```bash
pip install .
```

## Uso
```bash
myscript
```
```

---

#### **5. Installa il Pacchetto Localmente**
Esegui il seguente comando nella directory principale del tuo progetto:
```bash
pip install .
```

Ora puoi eseguire il comando `myscript` da qualsiasi directory.

---

#### **6. Testa l'Esecuzione**
Esegui il comando:
```bash
myscript
```
Dovresti vedere l'output definito nella funzione `main()` di `cli.py`.

---

#### **7. Condividi il Pacchetto (Opzionale)**
Se vuoi distribuire il tuo pacchetto, puoi caricarlo su [PyPI](https://pypi.org/). Segui questi passaggi:

1. Installa gli strumenti necessari:
   ```bash
   pip install twine setuptools wheel
   ```

2. Crea i file di distribuzione:
   ```bash
   python3 setup.py sdist bdist_wheel
   ```

3. Carica il pacchetto su PyPI:
   ```bash
   twine upload dist/*
   ```

Ora il tuo pacchetto sarà disponibile per l'installazione con:
```bash
pip install myscript
```