# Beispiel für ein eigenes Modul - das irgendwo importiert werden kann

# gibt True zurück wenn die E-Mail korrekt ist, ansonsten False
def validate_email(email):
    # E-Mail muss min 5 Zeichen bestehen --> a@b.c
    if len(email) < 5:
        return False 
    # check ob ein @-Zeichen enthalten ist
    if '@' not in email:
        return False 
    return True 


def validate_password(password):
    if len(password) < 6:
        return False
    return True 