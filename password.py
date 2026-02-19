import re

def verify_password(pwd: str, result: bool = False) -> bool:
    """
    Vérifie si le mot de passe est robuste.
    Critères :
    - Au moins 8 caractères
    - Contient au moins une majuscule
    - Contient au moins une minuscule
    - Contient au moins un chiffre
    - Contient au moins un caractère spécial
    """
    if len(pwd) < 8:
        return result
    if not re.search(r"[A-Z]", pwd):
        return result
    if not re.search(r"[a-z]", pwd):
        return result
    if not re.search(r"\d", pwd):
        return result
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        return result

    return True  # Si tous les critères sont respectés, le mot de passe est robuste

# Exemple d'utilisation
password = input("Entrez votre mot de passe : ")

if verify_password(password):
    print("✅ Mot de passe robuste !")
else:
    print("❌ Mot de passe trop faible.")
