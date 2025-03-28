from base64 import b64encode
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python b64.py <filename>")
        raise SystemExit(1)
    filename = argv[1]
    match filename:
        case filename if filename.endswith((".jpg", ".jpeg")):
            mime_type = "image/jpeg"
        case filename if filename.endswith(".png"):
            mime_type = "image/png"
        case filename if filename.endswith(".svg"):
            mime_type = "image/svg+xml"
        case filename if filename.endswith(".txt"):
            mime_type = "text/plain"
        case _:
            mime_type = input("Mime type: ")
    with open(filename, "rb") as file:
        print(f"data:{mime_type};base64,{b64encode(file.read()).decode('utf-8')}")
