"""Orkestrator generator kategori `chat.jsonl` untuk Nara-Allegretto-2."""
from __future__ import annotations

from .core_v2 import CategoryCollector
from .gen_chat_core import build_chat_core
from .gen_chat_daily import build_chat_daily
from .gen_chat_dialogs import build_chat_dialogs
from .gen_chat_everyday_plus import build_chat_everyday_plus
from .gen_chat_fun import build_chat_fun
from .gen_chat_life import build_chat_life
from .gen_chat_nusantara_reflect import build_chat_nusantara_reflect
from .gen_chat_scenarios import build_chat_scenarios
from .gen_chat_social import build_chat_social
from .gen_chat_topics_extra import build_chat_topics_extra


def build_chat_v2(col: CategoryCollector, *, limit: int | None = None) -> None:
    modules = [
        build_chat_core,
        build_chat_daily,
        build_chat_social,
        build_chat_life,
        build_chat_fun,
        build_chat_scenarios,
        build_chat_everyday_plus,
        build_chat_dialogs,
        build_chat_topics_extra,
        build_chat_nusantara_reflect,
    ]
    if limit is not None:
        step = max(1, limit // len(modules))
        for idx, fn in enumerate(modules, start=1):
            cap = limit if idx == len(modules) else min(limit, step * idx)
            fn(col, limit=cap)
            if len(col.rows) >= limit:
                break
        return

    for fn in modules:
        fn(col, limit=None)
