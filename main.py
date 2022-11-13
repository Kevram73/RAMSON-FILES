from cryptography.fernet import Fernet
import os
import compress
import shutil


class CryptFile:
    
    def __init__(self, file="my-key.key", goal=""):
        self.file = file
        self.key = Fernet.generate_key()
        self.goal = goal
        
    # Générer une clé de chiffrement
    def generate_key(self):
        with open(self.file, 'wb') as mykey:
            mykey.write(self.key)
        
    # Lire la clé de chiffrement
    def read_key(self):
        with open(self.file, 'rb') as mykey:
            self.key = mykey.read()
        return self.key

    
    # Encrypter un fichier
    def crypt_file_or_dir(self):
        
        
        f = Fernet(self.key)
        if os.path.isfile(self.goal):
            self.destination = "compress"
            os.makedirs(self.destination)
            shutil.copy(self.goal, self.destination)
            
            compress.zip_directory(self.destination, str(self.read_key()))
            
            with open(self.goal, 'rb') as original_file:
                original = original_file.read()
            encrypted = f.encrypt(original)

            with open(f"{self.goal}-1", 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            
            # Supprimer le dossier et le fichier après compression et cryptage
            os.remove(self.goal)
            shutil.rmtree(self.destination)

        elif os.path.isdir(self.goal):
            compress.zip_directory(self.goal, str(self.read_key()))
            parent_dir = "./"

            
            
            for i in os.listdir(self.goal):
                with open(f"{self.goal}/{i}", 'rb') as original_file:
                    original = original_file.read()
                encrypted = f.encrypt(original)

                with open(f"{self.goal}/{i}-1", 'wb') as encrypted_file:
                    encrypted_file.write(encrypted)
                os.remove(f"{self.goal}/{i}")
            
    def main(self, dir_or_file):
        syst = CryptFile(self, dir_or_file)
        syst.generate_key()
        syst.crypt_file_or_dir()

    
    
        
