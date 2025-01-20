file_path = r"C:\Users\giuli\OneDrive\Desktop\README.md"

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        contenuto = file.read()
        print(contenuto)
except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")

