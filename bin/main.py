import os
import fnmatch
from pathlib import Path
from datetime import datetime

class ScaffoldingGenerator:
    def __init__(self, base_path="."):
        self.base_path = os.path.abspath(base_path)

    def restore_from_prompt(self, prompt_file):
        """Legge il file di prompt e ripristina la struttura del progetto."""
        if not os.path.isfile(prompt_file):
            print(f"Errore: Il file '{prompt_file}' non esiste.")
            return

        with open(prompt_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Analizza il contenuto del file di prompt
        blocks = content.split("\n---\n")
        metadata = blocks[0]
        file_blocks = blocks[1:]

        # Estrai il nome del progetto
        project_name = None
        for line in metadata.splitlines():
            if line.startswith("Project Name:"):
                project_name = line.split(":", 1)[1].strip()
                break

        if not project_name:
            print("Errore: Nome del progetto non trovato nel file di prompt.")
            return

        project_folder = Path(self.base_path) / project_name
        project_folder.mkdir(parents=True, exist_ok=True)

        # Ripristina i file
        for block in file_blocks:
            lines = block.splitlines()
            file_path = None
            file_content = []
            inside_content = False

            for line in lines:
                if line.startswith("[FILE_PATH]:"):
                    file_path = line.split(":", 1)[1].strip()
                elif line.startswith("[FILE_CONTENT]:"):
                    inside_content = True
                elif inside_content:
                    file_content.append(line)

            if file_path:
                full_path = project_folder / file_path
                full_path.parent.mkdir(parents=True, exist_ok=True)

                with open(full_path, "w", encoding="utf-8") as f:
                    f.write("\n".join(file_content))

        print(f"Ripristino completato! Progetto ricreato nella cartella: {project_folder}")


class ProjectParser:
    SUPPORTED_EXTENSIONS = {".ts", ".js", ".jsx", ".tsx", ".py", ".json", ".tf", ".tfvars", ".conf"}
    
    def __init__(self, base_path="."):
        self.base_path = os.path.abspath(base_path)
        self.selected_folder = None
        self.ignore_patterns = []
        self.collected_data = []

    def parse_gitignore(self, file_path):
        """Parsa un file .gitignore e restituisce una lista di pattern."""
        patterns = []
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    patterns.append(line)
        return patterns

    def matches_gitignore(self, path, patterns):
        """Controlla se un percorso corrisponde a uno dei pattern nel .gitignore."""
        rel_path = os.path.relpath(path, self.selected_folder)
        for pattern in patterns:
            if pattern.endswith("/") and rel_path.startswith(pattern.rstrip("/")):
                return True
            elif fnmatch.fnmatch(rel_path, pattern):
                return True
        return False

    def list_directories(self):
        """Elenca le cartelle presenti nella directory base."""
        base_dir = Path(self.base_path)
        return [d for d in base_dir.iterdir() if d.is_dir()]

    def list_prompt_files(self):
        """Elenca i file di prompt nella directory base."""
        base_dir = Path(self.base_path)
        return [f for f in base_dir.iterdir() if f.is_file() and f.suffix == ".prompt"]

    def is_supported_file(self, file_path):
        """Controlla se il file ha una delle estensioni supportate."""
        return any(file_path.endswith(ext) for ext in self.SUPPORTED_EXTENSIONS)

    def select_folder(self):
        """Seleziona una cartella dalla lista delle directory disponibili."""
        directories = self.list_directories()
        if not directories:
            print("Nessuna cartella trovata nella directory specificata.")
            return False

        print("Seleziona una cartella da analizzare:")
        for idx, directory in enumerate(directories, start=1):
            print(f"{idx}. {directory.name}")
        
        try:
            choice = int(input("Inserisci il numero della cartella da selezionare: ").strip())
            if choice < 1 or choice > len(directories):
                print("Scelta non valida.")
                return False
        except ValueError:
            print("Inserisci un numero valido.")
            return False

        self.selected_folder = directories[choice - 1]
        return True

    def select_prompt_file(self):
        """Seleziona un file di prompt dalla lista dei file disponibili."""
        prompt_files = self.list_prompt_files()
        if not prompt_files:
            print("Nessun file di prompt trovato nella directory specificata.")
            return None

        print("Seleziona un file di prompt da analizzare:")
        for idx, prompt_file in enumerate(prompt_files, start=1):
            print(f"{idx}. {prompt_file.name}")
        
        try:
            choice = int(input("Inserisci il numero del file di prompt da selezionare: ").strip())
            if choice < 1 or choice > len(prompt_files):
                print("Scelta non valida.")
                return None
        except ValueError:
            print("Inserisci un numero valido.")
            return None

        return prompt_files[choice - 1]

    def parse_project(self):
        """Legge e processa i file di progetto ignorando i pattern definiti."""
        if not self.selected_folder:
            print("Nessuna cartella selezionata.")
            return

        gitignore_path = self.selected_folder / ".gitignore"
        self.ignore_patterns = self.parse_gitignore(gitignore_path)
        self.ignore_patterns.append(".git/")

        for root, dirs, files in os.walk(self.selected_folder):
            dirs[:] = [d for d in dirs if not self.matches_gitignore(os.path.join(root, d), self.ignore_patterns)]
            for file in files:
                file_path = os.path.join(root, file)
                if not self.is_supported_file(file_path):
                    continue
                if self.matches_gitignore(file_path, self.ignore_patterns):
                    continue

                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                relative_path = os.path.relpath(file_path, self.selected_folder)
                lines_count = len(content.splitlines())
                self.collected_data.append({
                    "path": relative_path,
                    "extension": Path(file_path).suffix,
                    "lines_count": lines_count,
                    "content": content
                })

    def write_output(self):
        """Scrive i dati raccolti in un file di output."""
        if not self.collected_data:
            print("Nessun file processato.")
            return

        output_filename = f"ai_prompt.project.{self.selected_folder.name}.prompt"
        output_path = Path(self.base_path) / output_filename

        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write("# AI Project File Summary\n")
            output_file.write(f"Project Name: {self.selected_folder.name}\n")
            output_file.write(f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            output_file.write(f"Total Files Processed: {len(self.collected_data)}\n\n")
            output_file.write("---\n\n")

            for idx, data in enumerate(self.collected_data, start=1):
                output_file.write(f"[FILE #{idx}]\n")
                output_file.write(f"[FILE_PATH]: {data['path']}\n")
                output_file.write(f"[FILE_EXTENSION]: {data['extension']}\n")
                output_file.write(f"[LINES_COUNT]: {data['lines_count']}\n\n")
                output_file.write("[FILE_CONTENT]:\n")
                output_file.write(data["content"])
                output_file.write("\n---\n\n")

        print(f"Completato! Il file è stato salvato in: {output_path}")

    def run(self):
        """Esegue il processo di packing o unpacking."""
        print(f"Directory di lavoro: {self.base_path}")
        if not os.path.isdir(self.base_path):
            print(f"Errore: La directory '{self.base_path}' non esiste.")
            return

        mode = input("Scegli una modalità (pack/unpack): ").strip().lower()
        if mode == "unpack":
            prompt_file = self.select_prompt_file()
            if prompt_file:
                generator = ScaffoldingGenerator(self.base_path)
                generator.restore_from_prompt(prompt_file)
        elif mode == "pack":
            if not self.select_folder():
                return

            print(f"Hai selezionato: {self.selected_folder.name}")
            print("Analisi in corso...")
            self.parse_project()
            self.write_output()
        else:
            print("Modalità non valida. Usa 'pack' per creare un prompt o 'unpack' per ripristinare un progetto.")


def app():
    base_path = input("Inserisci la directory da analizzare (lascia vuoto per usare la directory corrente): ").strip() or "."
    parser = ProjectParser(base_path)
    parser.run()
