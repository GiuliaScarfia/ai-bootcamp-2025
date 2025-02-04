import json

class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __repr__(self):
        return f'Person(name="{self.name}", surname="{self.surname}", phone="{self.phone}")'

    def to_dict(self):
        return {"type": "person", "name": self.name, "surname": self.surname, "phone": self.phone}

    @staticmethod
    def from_dict(data):
        return Person(data["name"], data["surname"], data.get("phone"))

class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f'Business(name="{self.name}", phone="{self.phone}")'

    def to_dict(self):
        return {"type": "business", "name": self.name, "phone": self.phone}

    @staticmethod
    def from_dict(data):
        return Business(data["name"], data.get("phone"))

class Directory:
    def __init__(self):
        self.contacts = []
        self.name_index = {}
        self.surname_index = {}
        self.phone_index = {}

    def add(self, contact):
        self.contacts.append(contact)
        name_key = contact.name.lower()
        if name_key not in self.name_index:
            self.name_index[name_key] = []
        self.name_index[name_key].append(contact)
        if isinstance(contact, Person):
            surname_key = contact.surname.lower()
            if surname_key not in self.surname_index:
                self.surname_index[surname_key] = []
            self.surname_index[surname_key].append(contact)
        if contact.phone:
            phone_key = contact.phone.lower()
            if phone_key not in self.phone_index:
                self.phone_index[phone_key] = []
            self.phone_index[phone_key].append(contact)

    def find(self, search_term):
        search_term = search_term.lower()
        results = []
        results.extend(self.name_index.get(search_term, []))
        results.extend(self.surname_index.get(search_term, []))
        results.extend(self.phone_index.get(search_term, []))
        for phone, contacts in self.phone_index.items():
            if search_term in phone:
                results.extend(contacts)
        return results

    def save_to_file(self, path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, indent=4)

    def load_from_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = []
                self.name_index = {}
                self.surname_index = {}
                self.phone_index = {}
                for entry in data:
                    if entry["type"] == "person":
                        contact = Person.from_dict(entry)
                    else:
                        contact = Business.from_dict(entry)
                    self.add(contact)
        except FileNotFoundError:
            print("File non trovato.")

def main():
    directory = Directory()
    while True:
        command = input("> ").strip().lower()
        if command == "h":
            print("""
Comandi:
    a (person|business)   Aggiungi contatto
    f <text>              Cerca contatto
    s <path>              Salva su file JSON
    l <path>              Carica da file JSON
    q                     Esci
""")
        elif command.startswith("a "):
            _, type_ = command.split(maxsplit=1)
            if type_ == "person":
                name = input("? Name: ").strip()
                surname = input("? Surname: ").strip()
                phone = input("? Phone: ").strip() or None
                directory.add(Person(name, surname, phone))
            elif type_ == "business":
                name = input("? Name: ").strip()
                phone = input("? Phone: ").strip() or None
                directory.add(Business(name, phone))
        elif command.startswith("f "):
            _, search_term = command.split(maxsplit=1)
            results = directory.find(search_term)
            if results:
                for r in results:
                    print(r)
            else:
                print("! not found")
        elif command.startswith("s "):
            _, path = command.split(maxsplit=1)
            directory.save_to_file(path)
            print(f"Rubrica salvata in {path}")
        elif command.startswith("l "):
            _, path = command.split(maxsplit=1)
            directory.load_from_file(path)
            print(f"Rubrica caricata da {path}")
        elif command == "q":
            break
if __name__ == "__main__":
    main()
