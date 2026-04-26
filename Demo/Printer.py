# Copyright (c) ZeroC, Inc.

# slice2py version 3.8.1

from __future__ import annotations
import IcePy

from Demo.Printer_forward import _Demo_PrinterPrx_t

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


class PrinterPrx(ObjectPrx):
    """
    Notes
    -----
        The Slice compiler generated this proxy class from Slice interface ``::Demo::Printer``.
    """

    def printString(self, s: str, context: dict[str, str] | None = None) -> None:
        return Printer._op_printString.invoke(self, ((s, ), context))

    def printStringAsync(self, s: str, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Printer._op_printString.invokeAsync(self, ((s, ), context))

    def printInt(self, n: int, context: dict[str, str] | None = None) -> None:
        return Printer._op_printInt.invoke(self, ((n, ), context))

    def printIntAsync(self, n: int, context: dict[str, str] | None = None) -> Awaitable[None]:
        return Printer._op_printInt.invokeAsync(self, ((n, ), context))

    def reverseString(self, s: str, context: dict[str, str] | None = None) -> str:
        return Printer._op_reverseString.invoke(self, ((s, ), context))

    def reverseStringAsync(self, s: str, context: dict[str, str] | None = None) -> Awaitable[str]:
        return Printer._op_reverseString.invokeAsync(self, ((s, ), context))

    @staticmethod
    def checkedCast(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> PrinterPrx | None:
        return checkedCast(PrinterPrx, proxy, facet, context)

    @staticmethod
    def checkedCastAsync(
        proxy: ObjectPrx | None,
        facet: str | None = None,
        context: dict[str, str] | None = None
    ) -> Awaitable[PrinterPrx | None ]:
        return checkedCastAsync(PrinterPrx, proxy, facet, context)

    @overload
    @staticmethod
    def uncheckedCast(proxy: ObjectPrx, facet: str | None = None) -> PrinterPrx:
        ...

    @overload
    @staticmethod
    def uncheckedCast(proxy: None, facet: str | None = None) -> None:
        ...

    @staticmethod
    def uncheckedCast(proxy: ObjectPrx | None, facet: str | None = None) -> PrinterPrx | None:
        return uncheckedCast(PrinterPrx, proxy, facet)

    @staticmethod
    def ice_staticId() -> str:
        return "::Demo::Printer"

IcePy.defineProxy("::Demo::Printer", PrinterPrx)

class Printer(Object, ABC):
    """
    Notes
    -----
        The Slice compiler generated this skeleton class from Slice interface ``::Demo::Printer``.
    """

    _ice_ids: Sequence[str] = ("::Demo::Printer", "::Ice::Object", )
    _op_printString: IcePy.Operation
    _op_printInt: IcePy.Operation
    _op_reverseString: IcePy.Operation

    @staticmethod
    def ice_staticId() -> str:
        return "::Demo::Printer"

    @abstractmethod
    def printString(self, s: str, current: Current) -> None | Awaitable[None]:
        pass

    @abstractmethod
    def printInt(self, n: int, current: Current) -> None | Awaitable[None]:
        pass

    @abstractmethod
    def reverseString(self, s: str, current: Current) -> str | Awaitable[str]:
        pass

Printer._op_printString = IcePy.Operation(
    "printString",
    "printString",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    None,
    ())

Printer._op_printInt = IcePy.Operation(
    "printInt",
    "printInt",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_int, False, 0),),
    (),
    None,
    ())

Printer._op_reverseString = IcePy.Operation(
    "reverseString",
    "reverseString",
    OperationMode.Normal,
    None,
    (),
    (((), IcePy._t_string, False, 0),),
    (),
    ((), IcePy._t_string, False, 0),
    ())

__all__ = ["Printer", "PrinterPrx", "_Demo_PrinterPrx_t"]
