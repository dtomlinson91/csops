import argparse
import pathlib
import subprocess


def encrypt(args):
    encrypted_filename = f"{args.file.stem}.enc{args.file.suffix}"
    subprocess.run(
        "sops --encrypt --gcp-kms"
        f" projects/plex-mozilla-sops/locations/global/keyRings/sops/cryptoKeys/sops-key {args.file} >  {encrypted_filename}",
        check=True,
        text=True,
        shell=True,
    )
    print(encrypted_filename)
    raise SystemExit(0)


def decrypt(args):
    decrypted_filename = f"{args.file.stem.split('.')[0]}{args.file.suffix}"
    subprocess.run(
        f"sops --decrypt {args.file} >  {decrypted_filename}",
        check=True,
        text=True,
        shell=True,
    )
    print(decrypted_filename)
    raise SystemExit(0)


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("flag", type=str, nargs=1)
    parser.add_argument("file", type=pathlib.Path)
    args = parser.parse_args()

    try:
        if args.flag == ["e"]:
            encrypt(args)
        elif args.flag == ["d"]:
            decrypt(args)
    except subprocess.CalledProcessError as error:
        print(f"Error: {error}")
        raise SystemExit(1)
