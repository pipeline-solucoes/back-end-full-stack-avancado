from pydantic import BaseModel
from typing import List

from model.fale_conosco import FaleConosco

class FaleConoscoSchema(BaseModel):
    """ 
    Define como um novo fale conosco a ser inserido 
    deve ser representado
    """     
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    mensagem: str = "mensagem"
       

class FaleConoscoViewSchema(BaseModel):
    """ 
    Define como o fale conosco será retornado na listagem 
    de Fale Conosco
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    mensagem: str = "mensagem"

class ListagemFaleConosco(BaseModel):
    """ 
    Define a representacao das
    mensagens do Fale Conosco
    """
    lojas: List[FaleConoscoSchema] 

def apresenta_faleconosco(lista: List[FaleConosco]):
    """ Retorna uma representação da listagem das lojas
    """
    result = []
    for item in lista:
        result.append({
            "id": item.id,
            "nome": item.nome,
            "email": item.email, 
            "telefone": item.telefone, 
            "mensagem": item.mensagem 
        })        

    return {"mensagens": result}


class FaleConoscoAddSchema(BaseModel):
    """ 
    Define como um novo fale conosco a ser inserido 
    deve ser representado
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    mensagem: str = "mensagem"            


def apresenta_novo_fale_conosco(item: FaleConosco):
    """ Retorna uma representação do novo fale conosco
    """
    return {
        "id": item.id,
        "nome": item.nome,
        "email": item.email, 
        "telefone": item.telefone, 
        "mensagem": item.mensagem                   
    }  