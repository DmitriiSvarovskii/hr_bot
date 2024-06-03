from aiogram import Router

from .fsm_test_myers_briggs import router as router_test_meyers
from .start_handlers import router as router_start
from .result_handlers import router as router_result
from .result_admin_handlers import router as router_result_admin

router = Router(name=__name__)

router.include_router(router_test_meyers)
router.include_router(router_start)
router.include_router(router_result)
router.include_router(router_result_admin)
