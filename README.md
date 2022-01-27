# CSOPS

Wrapper around [mozilla/sops](https://github.com/mozilla/sops).

## Installation

`pipx install git+https://github.com/dtomlinson91/csops`

## Configuration

Either use a `config.yml` or use environment variables.

If using a `config.yml` create this file in either `~/.config/csops/` or a custom directory. If using a custom directory set the environment variable `CSOPS_CONFIG` equal to this directory.

### GCP KMS Key

If using a `config.yml` set the `gcp_mks_key` under the `csops` header:

```yml
csops:
    gcp_kms_key: projects/plex-mozilla-sops/locations/global/keyRings/sops/cryptoKeys/sops-key
```

Or set the environment variable
```bash
CSOPS_GCP_KMS_KEY="projects/plex-mozilla-sops/locations/global/keyRings/sops/cryptoKeys/sops-keys"
```

## Usage

Encrypt: `csops e test.log`

Decrypt: `csops d test.enc.log`
