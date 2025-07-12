from abc import ABC, abstractmethod

class Usuario:
    def __init__(self, id, nombre, apellido, correo, clave,  rol):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__clave = clave
        self._rol = rol
        
    #aplicar getters
    def get_id(self):
        return self.__id
        
    def get_nombre(self):
        return self.__nombre
        
    def get_apellido(self):
        return self.__apellido
        
    def get_correo(self):
        return self.__correo
        
    def get_rol(self):
        return self._rol
        
    #setters
    def set_clave(self, nueva_clave):
        self.__clave = nueva_clave
        
    def login(self, correo, clave):
        return self.__correo == correo and self.__clave == clave
        
    @abstractmethod
    def menu(self):
        pass
    
        