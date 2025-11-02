# Convertisseur Audio/Video (GitHub-ready)


Ce dépôt contient un convertisseur simple basé sur **ffmpeg**, exécutable localement (Docker) ou via **GitHub Actions**.


## Structure


- `converter/` : script principal (Python)
- `docker/` : Dockerfile + entrypoint
- `.github/workflows/convert.yml` : workflow CI qui convertit les fichiers déposés dans `inputs/`
- `inputs/` : dossier où déposer les fichiers à convertir
- `outputs/` : généré par le workflow (artefacts)


## Utilisation rapide


- Local (Docker) :


```bash
docker build -t media-converter -f docker/Dockerfile .
# convertir
docker run --rm -v $(pwd):/data media-converter /data/inputs/example.mp4 /data/outputs/example.mp3 --audio-bitrate 192k
