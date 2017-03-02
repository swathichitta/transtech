from openerp.osv import fields, osv
from openerp import api
from openerp.tools.translate import _
from openerp import  tools


class Customer_alerts(osv.osv):

	_name="customer.alerts"
	_inherit = 'alerts.dashboard'

	_columns = {
	'name_id':fields.char('ID'),
	'submitted_by':fields.many2one('res.users','Submitted By'),
	'image':fields.binary('Image'),
	'image_2':fields.binary('Image'),
	'image_3':fields.binary('Image'),

	
	}
	
	_defaults = {
		'submitted_by': lambda obj, cr, uid, context: uid,
	}
	
	def send_attachments(self,cr,uid,ids,context=None):
		# sending attachments through mail
		return True
Customer_alerts()