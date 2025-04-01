from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
from pathlib import Path

# Añade la ruta de tu proyecto al PATH
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from app.models import *

# Configuración de Alembic
config = context.config
fileConfig(config.config_file_name)

# MetaData de SQLAlchemy
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()