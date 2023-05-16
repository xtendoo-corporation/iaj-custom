# Copyright 2023 Xtendoo - Manuel Calero
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models

class AddFollower(models.TransientModel):
    _name = 'add.follower'

    def add_followers(self):
        partner_model = self.env['res.partner']
        user_model = self.env['res.users']
        followers_model = self.env['mail.followers']

        partners = partner_model.search([('contactado', '=', True)])
        users = user_model.search([('active', '=', True)])  # Reemplaza 'test_user_login' con el nombre de usuario correcto

        for partner in partners:
            for user in users:
                # Este usuario es seguidor de este contacto?
                message_partner_ids = partner.message_follower_ids.mapped('partner_id')
                if user.partner_id not in message_partner_ids:
                    followers_model.create(
                        {
                            "res_model": "res.partner",
                            "res_id": partner.id,
                            "partner_id": user.partner_id.id,
                        }
                    )
