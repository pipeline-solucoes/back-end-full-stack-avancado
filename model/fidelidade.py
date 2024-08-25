from sqlalchemy import Column, String, Integer

from model.base import Base

class Fidelidade(Base):
    __tablename__ = 'fidelidade'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Identificador do Programa Fidelidade")
    nome = Column(String(100), comment="Nome do Cliente", nullable=False)
    email = Column(String(100), unique=True, comment="Email do Cliente", nullable=False)
    telefone = Column(String(50), comment="Telefone do Cliente", nullable=False)        
    
    def __init__(self, nome:str, email:str, telefone:str):
        """
        Adiciona um cliente no Programa Fidelidade
        
        Arguments:
            nome: nome do cliente. 
            email: email do cliente.
            telefone: telefone do cliente.            
        """
        self.nome = nome       
        self.email = email
        self.telefone = telefone