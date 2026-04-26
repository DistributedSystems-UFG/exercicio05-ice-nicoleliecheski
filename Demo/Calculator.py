# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Demo.Calculator_forward import _Demo_CalculatorPrx_t

from Ice.Object import Object

from Ice.ObjectPrx import ObjectPrx
from Ice.ObjectPrx import checkedCast
from Ice.ObjectPrx import checkedCastAsync
from Ice.ObjectPrx import uncheckedCast

from Ice.OperationMode import OperationMode

from abc import ABC
from abc import abstractmethod

from typing import TYPE_CHECKING
from typing import overload

if TYPE_CHECKING:
    from Ice.Current import Current
    from collections.abc import Awaitable
    from collections.abc import Sequence


class CalculatorPrx(ObjectPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::Demo::Calculator``.
    """

    def add(self, a: int, b: int, context: dict[str, str] | None = None) -> int:
        return Calculator._op_add.invoke(self, ((a, b), context))

    def addAsync(self, a: int, b: int, context: dict[str, str] | None = None) -> Awaitable[int]:
        return Calculator._op_add.invokeAsync(self, ((a, b), context))

    def subtract(self, a: int, b: int, context: dict[str, str] | None = None) -> int:
        return Calculator._op_subtract.invoke(self, ((a, b), context))

    def subtractAsync(self, a: int, b: int, context: dict[str, str] | None = None) -> Awaitable[int]:
        return Calculator._op_subtract.invokeAsync(self, ((a, b), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> CalculatorPrx | None:
        return checkedCast(CalculatorPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[CalculatorPrx | None ]:
        return checkedCastAsync(CalculatorPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> CalculatorPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> CalculatorPrx | None:
        return uncheckedCast(CalculatorPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::Demo::Calculator"

IcePy.defineProxy("::Demo::Calculator", CalculatorPrx)

class Calculator(Object, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::Demo::Calculator``.
    """

    _ice_ids: Sequence[str] = ("::Demo::Calculator", "::Ice::Object", )
    _op_add: IcePy.Operation
    _op_subtract: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::Demo::Calculator"

    @abstractmethod
    def add(self, a: int, b: int, current: Current) -> int | Awaitable[int]:
        pass

    @abstractmethod
    def subtract(self, a: int, b: int, current: Current) -> int | Awaitable[int]:
        pass

Calculator._op_add = IcePy.Operation(
    "add",
    "add",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    ())

Calculator._op_subtract = IcePy.Operation(
    "subtract",
    "subtract",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0), ((), IcePy._t_int, False, 0)),
    (),
    ((), IcePy._t_int, False, 0),
    ())

__all__ = ["Calculator", "CalculatorPrx", "_Demo_CalculatorPrx_t"]
