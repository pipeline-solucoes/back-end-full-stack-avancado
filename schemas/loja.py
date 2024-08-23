from typing import List
from model.loja import Loja
from pydantic import BaseModel

class LojaSchema(BaseModel):
    """ 
    Define como uma nova loja a ser inserido 
    deve ser representado
    """     

    nome : str = "Plaza Shopping"
    endereco : str = "Rua Quinze de Novembro"
    numero : str = "8"
    complemento : str = "loja 301"
    bairro : str = "Centro"
    cidade : str = "Niterói"
    uf : str = "RJ"
    cep: str = "24110-650"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    horario_seg_sab: str = "10:00 as 23:00"
    horario_dom_feriado: str = "10:00 as 21:00"
    foto: str = "/assets/lojaPlaza.jpeg"

class LojaViewSchema(BaseModel):
    """ 
    Define como a loja será retornado na listagem 
    das lojas
    """
    nome : str = "Plaza Shopping"
    endereco : str = "Rua Quinze de Novembro"
    numero : str = "8"
    complemento : str = "loja 301"
    bairro : str = "Centro"
    cidade : str = "Niterói"
    uf : str = "RJ"
    cep: str = "24110-650"
    telefone: str = "(21) 9999-9999 / 9999-9999"
    horario_seg_sab: str = "10:00 as 23:00"
    horario_dom_feriado: str = "10:00 as 21:00"
    foto: str = "/assets/lojaPlaza.jpeg"

class ListagemLoja(BaseModel):
    """ Define a representacao das lojas 
    """
    lojas: List[LojaSchema] 

def apresenta_lojas(lojas: List[Loja]):
    """ Retorna uma representação da listagem das lojas
    """
    result = []
    for loja in lojas:
        result.append({
            "id": loja.id,
            "nome": loja.nome,
            "endereco": loja.endereco,
            "numero": loja.numero,
            "complemento": loja.complemento,
            "bairro": loja.bairro,
            "cidade": loja.cidade,
            "uf": loja.uf,
            "cep": loja.cep,
            "telefone": loja.telefone,
            "horario_seg_sab": loja.horario_seg_sab,
            "horario_dom_feriado": loja.horario_dom_feriado,
            "foto": loja.foto
        })        

    return {"lojas": result}