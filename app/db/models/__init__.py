try:
    from app.db.models.user import User
    from app.db.models.role import Role
    from app.db.models.task import Task
    from app.db.models.task_status import TaskStatus
    from app.db.models.project import Project
    from .requirement import Requirement
    from .project_member import ProjectMember
except ModuleNotFoundError:
    from user import User
    from role import Role
    from task import Task
    from task_status import TaskStatus
    from project import Project
    from requirement import Requirement
    from project_member import ProjectMember





