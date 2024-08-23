from sqlalchemy import Column, String, Integer

from model.base import Base

class Loja(Base):
    __tablename__ = 'loja'
    
    id = Column(Integer, primary_key=True, autoincrement=True, comment="Identificador da Loja")
    nome = Column(String(100), comment="Nome da Loja", nullable=False)
    endereco = Column(String(100), comment="Endereco da Loja", nullable=False)
    numero = Column(String(10), comment="Numero do Endereco da Loja", nullable=False)
    complemento = Column(String(100), comment="Complemento do Endereco da Loja", nullable=False)
    bairro = Column(String(30), comment="Bairro do Endereco da Loja", nullable=False)
    cidade = Column(String(30), comment="Cidade do Endereco da Loja", nullable=False)
    uf = Column(String(2), comment="UF do Endereco da Loja", nullable=False)
    cep = Column(String(9), comment="CEP do Endereco da Loja", nullable=False)
    horario_seg_sab = Column(String(30), comment="Horario Funcionamento da Loja de Segunda a Sabado", nullable=False)
    horario_dom_feriado = Column(String(30), comment="Horario Funcionamento da Loja de Domingo e Feriados", nullable=False)
    telefone = Column(String(50), comment="Telefone da Loja", nullable=False)
    foto = Column(String(50), comment="Foto da Loja", nullable=False)
            
    def __init__(self, nome:str, endereco:str, numero:str, complemento:str, 
                 bairro:str, cidade:str, uf:str, cep:str, telefone:str,
                 horario_seg_sab:str, horario_dom_feriado:str, foto:str):
        """
        Cria uma nova loja
        
        Arguments:
            nome: nome da loja. 
            endereco: endereco da loja. 
            numero: numero do endereco da loja
            complemento: complemento do endereco da loja
            bairro: bairro do endereco da loja  
            cidade: cidade do Endereco da loja
            uf: UF do endereco da loja
            cep: CEP do endereco da loja
            telefone: telefone da loja
            horario_seg_sab: Horario Funcionamento da Loja de Segunda a Sabado
            horario_dom_feriado: Horario Funcionamento da Loja de Domingo e Feriados            
            foto: foto da loja
        """
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep
        self.telefone = telefone
        self.horario_seg_sab = horario_seg_sab
        self.horario_dom_feriado = horario_dom_feriado
        self.foto = foto