#!/usr/bin/env python3

import os as os

pessoa = {
    "nome": "Gabriel",
    "idade": 23,
    "localidade": "Brasília",
    "area": "cybersecurity",
}


def input_data():
    name = str(input("digite seu nome -> "))
    idade = int(input("digite sua idade -> "))
    localidade = str(input("digite sua localidade -> "))
    area = str(input("digite sua area -> "))

    return name, idade, localidade, area


input_data()
