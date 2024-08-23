from sqlalchemy import Column, String, Integer

from model.base import Base

class FaleConosco(Base):
    __tablename__ = 'fale_conosco'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Identificador da Mensagem")
    nome = Column(String(100), comment="Nome do Cliente", nullable=False)
    email = Column(String(100), comment="Email do Cliente", nullable=False)
    telefone = Column(String(50), comment="Telefone do Cliente", nullable=False)    
    mensagem = Column(String(1000), comment="Mensagem", nullable=False)
    status = Column(Integer, comment="1 - Não Lido, 2 - Em Analise, 3 - Respondido", nullable=False)
    
    def __init__(self, nome:str, email:str, telefone:str, mensagem:str):
        """
        Cria um Fale Conosco
        
        Arguments:
            nome: nome do cliente. 
            email: email do cliente.
            telefone: telefone do cliente.
            descricao: mensagem. 
        """
        self.nome = nome       
        self.email = email
        self.telefone = telefone 
        self.mensagem = mensagem
        self.status = 1