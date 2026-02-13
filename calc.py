#!/usr/bin/env python3
from decimal import Decimal

CREDITO = Decimal("3.54")

DEBITO = Decimal("1.39")


def real_credito() -> float:
    resultado = CREDITO - DEBITO
    print(f"{resultado:.2f}")
    return resultado


real_credito()
