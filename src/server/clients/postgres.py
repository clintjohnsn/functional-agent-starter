"""Postgres Connection."""
import logging

from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from psycopg_pool import AsyncConnectionPool

from server.config.settings import settings

logger = logging.getLogger(__name__)

class PostgresConnection:
    _checkpointer: AsyncPostgresSaver
    _pool: AsyncConnectionPool = None

    async def setup(self) -> None:
        if not self._pool:
            logger.debug("Creating connection pool")
            connection_kwargs = {
                "autocommit": True,
                "prepare_threshold": 0,
            }
            self._pool =  AsyncConnectionPool(
                conninfo=settings().POSTGRES_CONNECTION_STRING,
                min_size=1,
                max_size=10,
                kwargs=connection_kwargs,
            )
            logger.debug("Connection Pool created")
            self._checkpointer = AsyncPostgresSaver(self._pool)
            logger.debug("Setting up checkpointer")
            await self._checkpointer.setup()
            logger.debug("Checkpointer setup complete")

    def get(self) -> AsyncPostgresSaver:
        return self._checkpointer
    
    def close(self) -> None:
        if self._pool:
            self._pool.close()
