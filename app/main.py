import argparse
from organizer import organize_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize arquivos por extensão.")
    parser.add_argument("path", help="Caminho da pasta a ser organizada")
    args = parser.parse_args()

    organize_files(args.path)
