import random
import resend


# resend.api_key = "re_AjL5pazn_8CzkWBtBAoDXATs9cLbFUGMZ"
codigo_previo = None


def GenerarCodigo(i):
    global codigo_previo

    if i == 1:
        x = random.randint(100, 999)
        letras = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z",
        ]
        codigo = ""
        for _ in range(3):
            letra = letras[random.randint(0, 25)]
            codigo = codigo + letra
        codigo = codigo + str(x)

        codigo_previo = codigo

    elif i == 2 and codigo_previo:
        return codigo_previo
    else:
        return "Código no disponible"

    return codigo


resend.api_key = "re_AjL5pazn_8CzkWBtBAoDXATs9cLbFUGMZ"


def Recuperacion(email, codigo):
    params = {
        "from": "Acme <onboarding@resend.dev>",
        "to": "" + email + "",
        "subject": "Recuperar contraseña",
        "html": "<p>Tu codigo es: <strong>" + codigo + "</strong>!</p>",
    }
    email = resend.Emails.send(params)
