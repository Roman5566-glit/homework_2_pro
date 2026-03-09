def create_user_settings():
    """Creates settings manager"""
    settings = {}

    def manage_settings(key=None, value=None):
        """Allows to set or get settings"""
        if value:
            settings[key] = value
        return settings

    return manage_settings


user_settings = create_user_settings()

user_settings("theme", "dark")
user_settings("language", "ua")

print(user_settings())
