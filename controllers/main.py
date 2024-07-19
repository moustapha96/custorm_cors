# custom_cors/controllers/main.py
from odoo import http
from odoo.http import Response
import json


class CustomCors(http.Controller):

    @http.route('/', type='http', auth='public', methods=['OPTIONS'], csrf=False)
    def options(self, **kwargs):
        headers = {
            'Access-Control-Allow-Origin': '*',  # Autoriser uniquement votre origine
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, Origin , X-Requested-With, Accept , Authorization, Access-Token ',
            'Access-Control-Allow-Credentials': 'true'
        }
        return Response(status=200, headers=headers)

   
