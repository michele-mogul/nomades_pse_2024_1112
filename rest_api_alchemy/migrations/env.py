import importlib
import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.db.base import Base  # Import your application's Base
from app.config import MYSQL_CONFIG  # Import MySQL URI

# Configure logging
fileConfig(context.config.config_file_name)

# Set the target metadata to your SQLAlchemy models
target_metadata = Base.metadata

# Set the database URL dynamically
context.config.set_main_option("sqlalchemy.url", MYSQL_CONFIG['host'])


def import_all_models():
    models_dir = os.path.join(os.path.dirname(__file__), "../app/models")
    for filename in os.listdir(models_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            importlib.import_module(f"app.models.{filename[:-3]}")


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


import_all_models()
run_migrations_online()
