from openapprentice.models.user import User


if not User.table_exists():
    User.create_table()
