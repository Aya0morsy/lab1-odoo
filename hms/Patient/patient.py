from odoo import models, fields
class HMSStudent(models.Model):
    _name='hms.patient'
    firstname=fields.Char()
    lastname=fields.Char()
    birthdate=fields.Date()
    history=fields.Html()
    CRradio=fields.Float()
    BloodType=fields.Selection([('A+','O-',),('O+','B-',),('B+','A-',),('AB-','AB+',),])
    #PCR=
    image=fields.Image()
    address=fields.Text()
    age=fields.Integer()

