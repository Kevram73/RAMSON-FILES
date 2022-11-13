# RAMSON-FILES 😎

## Composants:
Ce projet vise à simuler un ramsonware.

### Listes des fonctionnalités
+ compress.py:
    - De recueillir toutes les fichiers d'un répertoire (get_all_file_paths)
    - De zipper un répertoire et de le protéger avec un mot de passe (zip_directory)

+ main.py :
    - De générer une clé de cryptage(generate_key)
    - De la lire bien évidemment (read_key)
    - De crypter un fichier ou un dossier(crypt_file_or_dir)
        + Créer une copie cryptée du fichier cible
        + Créer un dossier de destination du fichier
        + Envoyer le fichier cible vers le répertoire
        + Compresser ce dossier et la vérouiller

        + Créer un copie du dossier, la zipper puis la protéger avec pour mot de passe la clé de chiffrement
        + Cryper le contenu des fichier du dossier

### A venir
+ Interaction avec serveur
+ Intégration d'une récursivité pour les dossiers contenant des dossiers

        