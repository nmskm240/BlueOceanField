import pytest
import sqlalchemy

from blueOceanField.infra.database.database import Database
from blueOceanField.infra.database.orm.model import Base

DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="function", autouse=True)
def test_database():
    return Database(sqlalchemy.make_url(DATABASE_URL))


@pytest.mark.asyncio
async def test_create_table(test_database):
    """テーブル作成をテスト"""
    await test_database.create_async()

    async with test_database.session() as session:
        async with session.begin():
            connection = await session.connection()
            tables = await connection.run_sync(
                lambda conn: sqlalchemy.inspect(conn).get_table_names()
            )

            assert (
                "ohlcvs" in tables
                and "symbols" in tables
                and "exchange_places" in tables
            )

            foreign_keys = await connection.run_sync(
                lambda conn: {
                    table_name: [
                        fk_info["constrained_columns"]
                        for fk_info in sqlalchemy.inspect(conn).get_foreign_keys(
                            table_name
                        )
                    ]
                    for table_name in tables
                }
            )

            assert foreign_keys["ohlcvs"] == [["symbol_id"]]
            assert foreign_keys["symbols"] == [["place_id"]]

    await test_database.close_async()
