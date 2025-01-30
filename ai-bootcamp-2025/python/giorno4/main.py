#Complessità costante (O(1))
class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, phone={self.phone})"


class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Business(name={self.name}, phone={self.phone})"


class Directory:
    def __init__(self):
        self.contacts = []
        self.name_index = {}
        self.surname_index = {}
        self.phone_index = {}

    def add(self, contact):
        self.contacts.append(contact)

        if contact.name not in self.name_index:
            self.name_index[contact.name] = []
        self.name_index[contact.name].append(contact)

        if isinstance(contact, Person):
            if contact.surname not in self.surname_index:
                self.surname_index[contact.surname] = []
            self.surname_index[contact.surname].append(contact)

        if contact.phone:
            if contact.phone not in self.phone_index:
                self.phone_index[contact.phone] = []
            self.phone_index[contact.phone].append(contact)

    def __len__(self):
        return len(self.contacts)

    def query(self, name=None, surname=None):
        results = []
        if name:
            results.extend(self.name_index.get(name, []))
        if surname:
            results.extend(self.surname_index.get(surname, []))
        return results

    def find(self, search_term):
        results = []
        results.extend(self.name_index.get(search_term, []))
        results.extend(self.surname_index.get(search_term, []))
        results.extend(self.phone_index.get(search_term, []))
        for phone, contacts in self.phone_index.items():
            if search_term in phone:
                results.extend(contacts)
        return results

directory = Directory()

assert len(directory) == 0

directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))

assert len(directory) == 3

assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]
assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
assert [el.name for el in directory.find("333")] == ["Vedrai"]

#Complessità lineare (O(n))
class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, phone={self.phone})"


class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Business(name={self.name}, phone={self.phone})"


class Directory:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def __len__(self):
        return len(self.contacts)

    def query(self, name=None, surname=None, phone=None):
        results = []
        for contact in self.contacts:
            if isinstance(contact, Person):
                if name and contact.name == name:
                    results.append(contact)
                if surname and contact.surname == surname:
                    results.append(contact)
            elif isinstance(contact, Business):
                if name and contact.name == name:
                    results.append(contact)
        return results

    def find(self, search_term):
        results = []
        for contact in self.contacts:
            if isinstance(contact, Person):
                if (search_term in contact.name or
                        search_term in contact.surname or
                        search_term in (contact.phone or "")):
                    results.append(contact)
            elif isinstance(contact, Business):
                if (search_term in contact.name or
                        search_term in (contact.phone or "")):
                    results.append(contact)
        return results

directory = Directory()

assert len(directory) == 0

directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))

assert len(directory) == 3

assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]
assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
assert [el.name for el in directory.find("333")] == ["Vedrai"]