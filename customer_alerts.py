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
		ir_model_data = self.pool.get('ir.model.data')
		try:
			template_id = ir_model_data.get_object_reference(cr, uid, 'transtech', 'customer_mail_template')[1]
		except ValueError:
			template_id = False
		try:
			compose_form_id = ir_model_data.get_object_reference(cr, uid, 'mail', 'email_compose_message_wizard_form')[1]
		except ValueError:
			compose_form_id = False
		ctx = dict()
		ctx.update({
					'default_model': 'customer.alerts',
					'default_res_id': ids[0],
					'default_use_template': bool(template_id),
					'default_template_id': template_id,
					'default_composition_mode': 'comment',
					'mark_so_as_sent': True
				})		
		return {
			'type': 'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views': [(compose_form_id, 'form')],
			'view_id': compose_form_id,
			'target': 'new',
			'context': ctx,
		}


Customer_alerts()