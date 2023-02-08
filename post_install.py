from odoo import api

import base64


def set_background_image(cr, version):
    with api.Environment.manage():
        env = api.Environment(cr, 1, {})
        companies = env['res.company'].search([])
        img_path = 'extra-addons/ax4b_theme/muk_web_theme/static/src/img/background.png'
        with open(img_path, 'rb') as f:
            img = f.read()
            for company in companies:
                company.background_image = base64.b64encode(img).decode('utf-8')