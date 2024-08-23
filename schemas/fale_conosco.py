from pydantic import BaseModel

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
    dos Itens do Cardapio
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    mensagem: str = "mensagem"


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