from odoo import models, api


class AddFollowers(models.Model):
    _inherit = 'res.partner'

    @api.model
    def add_followers_to_contacts(self):
        partner_ids = self.search([])
        user_ids = self.env['res.users'].search([('active', '=', True)])
        followers = self.search([('user_ids', 'in', user_ids.ids)])
        for partner in partner_ids:
            partner.sudo().message_subscribe(partner_ids=followers.ids)
