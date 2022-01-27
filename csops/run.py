import argparse
import pathlib
import subprocess

from csops import CONFIG
from csops._version import __version__


def encrypt(args):
    encrypted_filename = f"{args.file.stem}.enc{args.file.suffix}"
    encrypted_contents = subprocess.run(
        ["sops", "--encrypt", "--gcp-kms", CONFIG.gcp_kms_key, args.file],
        check=True,
        text=True,
        shell=False,
        capture_output=True,
    )
    with pathlib.Path(encrypted_filename).open("w", encoding="utf-8") as file:
        file.write(encrypted_contents.stdout)
    print(encrypted_filename)
    raise SystemExit(0)


def decrypt(args):
    decrypted_filename = f"{args.file.stem.split('.')[0]}{args.file.suffix}"
    decrypted_contents = subprocess.run(
        ["sops", "--decrypt", args.file],
        check=True,
        text=True,
        shell=False,
        capture_output=True,
    )
    with pathlib.Path(decrypted_filename).open("w", encoding="utf-8") as file:
        file.write(decrypted_contents.stdout)
    print(decrypted_filename)
    raise SystemExit(0)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("flag", type=str, nargs=1)
    parser.add_argument("file", type=pathlib.Path)
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + __version__)
    args = parser.parse_args()

    try:
        if args.flag == ["e"]:
            encrypt(args)
        elif args.flag == ["d"]:
            decrypt(args)
    except subprocess.CalledProcessError as error:
        print(f"Error: {error}")
        raise SystemExit(1)
