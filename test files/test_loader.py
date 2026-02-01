print("TEST LOADER STARTED")

from ingestion.loader import extract_text

class DummyFile:
    def __init__(self, path):
        self.name = path
        self.path = path

    def read(self):
        with open(self.path, "rb") as f:
            return f.read()


def test_file(path):
    print("\n==============================")
    print("TESTING FILE:", path)
    print("==============================")

    file = DummyFile(path)
    text = extract_text(file)

    print("\n--- EXTRACTED TEXT ---\n")
    print(text)
    print("\n--- END ---\n")


if __name__ == "__main__":
    test_file("data/samples/sample.txt")
    test_file("data/samples/sample.docx")
    test_file("data/samples/sample.pdf")
