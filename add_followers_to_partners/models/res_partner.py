from odoo import models, api


class AddFollowers(models.Model):
    _inherit = 'res.partner'

    @api.model
    def add_followers_to_contacts(self):
        partner_ids = self.search([])
        user_ids = self.env['res.users'].search([('id', 'in', (29, 34, 27, 31, 21, 33, 35))])
        followers = self.search([('user_ids', 'in', user_ids.ids)])
        for partner in partner_ids:
            partner.sudo().message_subscribe(partner_ids=followers.ids)
            partner.sudo().message_subscribe(partner_ids=partner.ids)

    def delete_followers_to_contacts(self):
        partner_ids = self.search([])
        for partner in partner_ids:
            partner.sudo().message_unsubscribe(partner_ids=partner_ids.ids)
