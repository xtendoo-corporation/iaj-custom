# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    fecha_nacimiento = fields.Date(
        string='Fecha Nacimiento')

    formacion_academica = fields.Char(
        string='Formación Académica')

    situacion_familiar = fields.Char(
        string='Situación familiar')

    contactado = fields.Boolean(
        string='Contactado')

    anio_fuera = fields.Char(
        string='Año Fuera')

    fecha_alta = fields.Date(
        string='Fecha Alta')

    disponibilidad = fields.Char(
        string='Disponibilidad')

    puesto_interes = fields.Char(
        string='Puesto de Interés')

    salario_deseado = fields.Char(
        string='Salario Deseado')
