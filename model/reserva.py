from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer

from model.base import Base

class Reserva(Base):
    __tablename__ = 'reserva'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Identificador da Reserva")
    nome = Column(String(100), comment="Nome do Cliente", nullable=False)
    email = Column(String(100), unique=True, comment="Email do Cliente", nullable=False)
    telefone = Column(String(50), comment="Telefone do Cliente", nullable=False)
    dataReserva = Column(DateTime, comment="DataHora da Reserva", nullable=False)  
    qtdPessoas = Column(Integer, comment="DataHora da Reserva", nullable=False)    
    
    def __init__(self, nome:str, email:str, telefone:str, dataReserva: datetime, qtdPessoas: int):
        """
        Adiciona um nova Reserva
        
        Arguments:
            nome: nome do cliente. 
            email: email do cliente.
            telefone: telefone do cliente.
            dataReserva: dataHora da reserva.
            qtdPessoas: quantidade de pessoas.
        """
        self.nome = nome       
        self.email = email
        self.telefone = telefone
        self.dataReserva = dataReserva
        self.qtdPessoas = qtdPessoas