from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, nome, email, password):
        if not email:
            raise ValueError('O usuário precisa de email!')
        usuario = self.model(
            nome = nome,
            email = self.normalize_email(email),
            password = password
        )
        usuario.set_password(password)
        usuario.save()
        return usuario