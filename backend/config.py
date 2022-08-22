class FyersParameters:

    base_url = ''
    #SymbolParameters
    symbol_base_uri = 'https://public.fyers.in/sym_details'
    symbol_nse_currency_url = f'{symbol_base_uri}/NSE_CD.csv'
    symbol_nse_equity_url = f'{symbol_base_uri}/NSE_FO.csv'
    symbol_nse_capital_url = f'{symbol_base_uri}/NSE_CM.csv'
    symbol_bse_capital_url = f'{symbol_base_uri}/BSE_CM.csv'
    symbol_commodity_url = f'{symbol_base_uri}/MCX_COM.csv'

    #Fyers App Config
    app_id = 'DAO4Z8KZT9-100'
    secret_id = 'TER1KWX8U6'
    #app_base_url = 'https://tradealertapp.herokuapp.com'
    app_base_url = 'http://127.0.0.1:8000'
    login = '/'
    rediect_url = f'{app_base_url}/api/Fyers/PostLogin'


    def __init__(self) -> None:
        pass

class FrontEnd:
    base_url = 'https://tradealertapp.herokuapp.com/'
    #post_login_url = 'https://tradealertapp.herokuapp.com/'
    post_login_url = 'http://127.0.0.1:8000/'