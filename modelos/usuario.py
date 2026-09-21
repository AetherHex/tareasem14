class Usuario:
    def __init__(self, id_usuario, username, password, rol):
        self.id = id_usuario
        self.username = username
        self.password = password
        self.rol = rol

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "rol": self.rol,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["username"], data["password"], data["rol"])
