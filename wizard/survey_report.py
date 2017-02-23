from openerp.osv import fields, osv

class Survey_report(osv.TransientModel):

	_name = 'survey.report'

	_columns = {

	'from_date':fields.date('From Date'),
	'to_date':fields.date('To Date'),
	'customer_info':fields.many2one('customer.info','Bank/Customer'),

	}

	def view_report(self,cr,uid,ids,context=None):
		for val in self.browse(cr, uid, ids, context=context):
			from_date = val.from_date
			to_date = val.to_date
			# print "valsssssssssssssssssssss",self.pool.get('survey.details').search(cr,uid,[('visit_tm', '>=', from_date), ('visit_tm', '<=', to_date)],context=context)
		domain=[('visit_tm', '>=', from_date), ('visit_tm', '<=', to_date)]
		return { 
			'name': 'Survey Reports', 
			'view_type': 'tree', 
			'view_mode': 'tree', 
			'res_model': 'survey.details', 
			'type': 'ir.actions.act_window', 
			'domain': domain,
		}
Survey_report()