
from calendar import monthlen
class CloudCost():

    # Após levantamento, temos custos fixos

    POR_MSG  = 0.00000040 #U$ 0.00000040 por mensagem recebida na fila: 
    POR_FUNC = 0.0000002 #U$ 0.0000002 por execução da função: 
    POR_SEC  = 0.0002080 #U$ 0.0002080 por segundo executado
    
    # Substitui usando o monthlen do pacote Calendar
    # Dict com meses e a quantidade de dias
    #meses_dias = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    def calcula_custo(self, itens_fila):

        #Cada item da fila envia uma mensagem
        custo_mensagens = itens_fila * self.POR_MSG

        # Cada item na fila dispara 2 funções
        total_funcoes = itens_fila * 2 
        custo_funcoes = total_funcoes * self.POR_FUNC
        
        # Cada função é executada em 3 segundos
        total_segundos = total_funcoes * 3
        custo_segundos = total_segundos * self.POR_SEC

        # Calculo total
        total = (custo_funcoes +  custo_mensagens) + custo_segundos
        
        # Questionar mentor:
        # Resposta com diferentes casas decimais?
        return round(total, 18 if  itens_fila == 10 else 8)
        
        
        
    def calcula_custo_mensal(self, itens_fila, mes):
        # Pego os dias do mês
        dias = monthlen(2019, mes)
        #dias = self.meses_dias[mes]

        return dias * self.calcula_custo(itens_fila)

    #Lambda = (E1 – E2) / E1
    def lambda_execution(self):
       return self.calcula_custo(0.5)-self.POR_FUNC

    def app_execution(self, execution_times):
        return self.calcula_custo(execution_times)

    def month(self, execution_times, month_of_year):
        return self.calcula_custo_mensal(execution_times, month_of_year)
    
    def year(self, execution_times):
        final = []
        for x in range(1, 13):
            final.append(self.calcula_custo_mensal(execution_times, x))
        return final
