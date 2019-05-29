from operator import itemgetter
"""
Em todas as funções, você receberá uma lista de vendedores,
 contendo um dicionario com os dados do vendedor:
"""

class SellersRancking:
    """
    Mostrar o vendedor com maior valor em vendas.
    """
    def best_seller(self, sellers):
        if len(sellers) > 0: 
            return [sorted(sellers,key=itemgetter('value'),reverse=True)[0]['name']]
        else :
            return []
 
    #- Listar todos os vendedores ordenados pelo valor vendido, do maior para o menor.
    def rancking_list(self, sellers):
        if len(sellers) > 0: 
            sorted_sellers = sorted(sellers, key=itemgetter('value'), reverse=True)
            return [seller['name'] for seller in sorted_sellers]
        else:
            return []
    
    #- Mostrar o melhor vendedor de uma determinada loja. 
    # Você receberá a lista de vendedores e deverá fazer um filtro nesta lista pela loja e 
    # retornar o nome do vendedor com o maior valor em vendas.
    def best_seller_store(self, sellers, store):
        if len(sellers) > 0: 
            
            return [sorted(rd).pop(0)]
        else:
            return []

    """ 
    Também é estipulado uma meta para vendas de R$ 500,00. 
    Então é necessário listar os vendedores que não atigiram esta meta, 
    em ordem crescente pelo valor de venda.
    """
    def sales_goals(self, sellers):
        if len(sellers) > 0: 
            sorted_sellers = filter(lambda seller: seller['value'] < 500, sorted(sellers, key=itemgetter('value')))
            return ([seller['name'] for seller in sorted_sellers])
        else:
            return []
