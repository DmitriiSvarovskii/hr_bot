import pytest

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import router as main_router
from .mocked_aiogram import MockedBot, MockedSession


@pytest.fixture(scope="session")
def dp() -> Dispatcher:
    dispatcher = Dispatcher(storage=MemoryStorage())
    dispatcher.include_router(main_router)
    return dispatcher


@pytest.fixture(scope="session")
def bot() -> MockedBot:
    bot = MockedBot()
    bot.session = MockedSession()
    return bot
