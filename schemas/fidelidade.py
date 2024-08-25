from pydantic import BaseModel

from model.fidelidade import Fidelidade

class FidelidadeSchema(BaseModel):
    """ 
    Define como um novo novo cliente no 
    Programa Fidelidade a ser inserido 
    deve ser representado
    """     
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"    
       

class FidelidadeViewSchema(BaseModel):
    """ 
    Define como um novo cliente no 
    Programa Fidelidade será retornado na listagem 
    do Programa de Fidelidade
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"    


class FidelidadeAddSchema(BaseModel):
    """ 
    Define como um novo cliente no 
    Programa Fidelidade a ser inserido 
    deve ser representado
    """
    nome: str = "Maria da Silva"
    email: str = "maria@gmail.com"
    telefone: str = "(21) 9999-9999 / 9999-9999"              


def apresenta_novo_fidelidade(item: Fidelidade):
    """ 
    Retorna uma representação do novo cliente 
    no Programa Fidelidade
    """
    return {
        "id": item.id,
        "nome": item.nome,
        "email": item.email, 
        "telefone": item.telefone,                         
    }