import numpy as np
import datetime

class ManagerDates:
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    """receba uma data no formato dd/mm/YYYY e determine se a mesma é válida. 
        A data será válida apenas se estiver no formato dd/mm/YYYY."""
    def date_is_valid(self, date, mask='%d/%m/%Y'):
        rv = True
        # Inclusão do parâmetro mask para validar dinâmicamente ao formato desejado
        try:
            datetime.datetime.strptime(date, mask)
        except ValueError as InvalidDate:
            rv = False
        return rv

    """receba uma data e retorne o dia da semana correspondente. Ex: “Saturday”"""
    def date_weekday(self, date):
        weekday = "NotValid"
        if type(date) == datetime.datetime:
            weekday = self.weekdays.get(date.weekday())
            
        elif self.date_is_valid(date, '%Y/%m/%d'):
            year, month, day = date.split("/")
            weekday = self.weekdays.get(datetime.datetime(int(year), int(month), int(day)).weekday())
        
        return weekday
    """receba uma data em formato string e retorne em formato datetime. 
    Formatos válidos: “dd/mm/YYYY”, “dd-mm-YYYY” , “ddmmYYYY”, 
    retorna False se a data não esta em um desses formatos.
    """
    def convert_string_to_date(self, date_str):
        rv = False
        mask_2 = '%d-%m-%Y'
        mask_3 = '%d%m%Y'
        
        if self.date_is_valid(date_str):
            day, month, year  = date_str.split("/")
            rv = datetime.datetime(int(year), int(month), int(day))
        elif self.date_is_valid(date_str, mask_2):
            day, month, year  = date_str.split("-")
            rv = datetime.datetime(int(year), int(month), int(day))
        elif self.date_is_valid(date_str, mask_3):
            if len(date_str) == 7:
                day, month, year = date_str[:1], date_str[1:2], date_str[3:]
            elif len(date_str) == 8:
                day, month, year = date_str[:2], date_str[2:4], date_str[4:]
                
            rv = datetime.datetime(int(year), int(month), int(day))
             
        return rv

    """recebe o ano e o mês e retorne todas as datas do mês. Obs: utilize o Numpy (arange)"""
    def get_all_dates(self, month, year):
        yearmonth = year + "-" + month
        final_year = year
        if month == '12':
            final_month = '001'
            final_year = str(int(year)+1)
        elif month != '09':
            final_month = '0' + str(int(month)+1)
        else:
            final_month = str(int(month)+1)
        
        final_yearmonth = final_year + "-" + final_month
        dates = np.arange(yearmonth, final_yearmonth, dtype='datetime64[D]')
        return dates
    """
    recebe o ano e o mês e retorne a quantidade de dias úteis que ele possui. 
    Obs: Utilize o Numpy.
    """
    def count_days_mounth(self, month, year):
        yearmonth = year + "-" + month
        final_year = year
        if month == '12':
            final_month = '01'
            final_year = str(int(year)+1)
        elif month != '09':
            final_month = '0' + str(int(month)+1)
        else:
            final_month = str(int(month)+1)
        
        final_yearmonth = final_year + "-" + final_month
        busdays = np.busday_count(yearmonth, final_yearmonth)
        return busdays
    
    """
    recebe o ano e encontre a primeira segunda-feira de maio. 
    O retorno deve ser uma string no formato “dd/mm/YYYY”. Obs: Utilize NumPy.
    """
    def get_first_monday(self, year):
        start = year + "-05-01"
        end = year + "-05-08"
        dates = np.arange(start, end, dtype='datetime64[D]')
        for date in dates:
            str_date = np.datetime_as_string(date).replace("-", "/")    
            if 'Monday' == self.date_weekday(str_date):
                year, month, day = str_date.split("/")
                
                return day + "/" + month + "/" + year