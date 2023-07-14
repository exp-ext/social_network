# from datetime import datetime

# from sqlalchemy import (DATE, JSON, TIMESTAMP, Boolean, Column, ForeignKey,
#                         Integer, String, Table)

# from .db import metadata


# roles = Table(
#     "roles",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String, nullable=False),
#     Column("permissions", JSON),
# )

# users = Table(
#     "users",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
#     Column("hashed_password", String, nullable=False),
#     Column("registered_at", TIMESTAMP, default=datetime.utcnow),
#     Column("role_id", Integer, ForeignKey(roles.c.id)),
#     Column("is_active", Boolean, default=True, nullable=False),
#     Column("is_superuser", Boolean, default=False, nullable=False),
#     Column("is_verified", Boolean, default=False, nullable=False),
#     Column("first_name", String, nullable=True),
#     Column("last_name", String, nullable=True),
#     Column("birthdate", DATE),
# )

# posts = Table(
#     "posts",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("title", String),
#     Column("text", String),
#     Column("author_id", Integer, ForeignKey(users.c.id)),
#     Column("date", TIMESTAMP),
#     Column("image", String),
# )
