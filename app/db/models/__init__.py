try:
    from app.db.models.user import User
    from app.db.models.role import Role
except ModuleNotFoundError:
    from user import User
    from role import Role