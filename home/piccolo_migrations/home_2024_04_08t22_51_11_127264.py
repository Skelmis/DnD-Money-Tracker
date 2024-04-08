from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Real
from piccolo.columns.column_types import Text
from piccolo.columns.indexes import IndexMethod


ID = "2024-04-08T22:51:11:127264"
VERSION = "1.5.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="home", description=DESCRIPTION
    )

    manager.add_table(
        class_name="Money", tablename="money", schema=None, columns=None
    )

    manager.add_column(
        table_class_name="Money",
        tablename="money",
        column_name="entity",
        db_column_name="entity",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Money",
        tablename="money",
        column_name="copper",
        db_column_name="copper",
        column_class_name="Real",
        column_class=Real,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Money",
        tablename="money",
        column_name="silver",
        db_column_name="silver",
        column_class_name="Real",
        column_class=Real,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Money",
        tablename="money",
        column_name="electrum",
        db_column_name="electrum",
        column_class_name="Real",
        column_class=Real,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Money",
        tablename="money",
        column_name="gold",
        db_column_name="gold",
        column_class_name="Real",
        column_class=Real,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Money",
        tablename="money",
        column_name="platinum",
        db_column_name="platinum",
        column_class_name="Real",
        column_class=Real,
        params={
            "default": 0.0,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
