# -*- coding: utf-8 -*-
__author__ = 'Juan Jose López Martínez'

import time

def timer (sec = 10):
    def decorator(func):
        def wrapper(*args):
            while True:
                try:
                    func(*args)
                except Exception as ex:
                    print(ex)
                    print("Ocurrió un error inesperado durante la ejecución")
                time.sleep(sec)
        return wrapper
    return decorator
