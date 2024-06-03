from aiogram.filters.callback_data import CallbackData
from typing import Optional


class ResultTestCbData(
    CallbackData,
    prefix='result',
    sep='_'
):
    test_id: Optional[int] = None


class ResultAdminTestCbData(
    ResultTestCbData,
    prefix='result-admin',
    sep='_'
):
    user_id: int


class ResultAdminListTestCbData(
    ResultAdminTestCbData,
    prefix='result-adm',
    sep='_'
):
    pass
