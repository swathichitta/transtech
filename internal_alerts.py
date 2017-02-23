from openerp.osv import fields, osv

class Internal_alerts(osv.osv):

	_name = 'internal.alerts'
	_inherit="alerts.dashboard"

	_columns = {
		'customer':fields.many2one('customer.info','Customer', required=True),
		'user':fields.many2one('res.users','Created By', readonly=True),
		'assign_to':fields.many2one('res.users','Assign To', domain="[('name_tl','!=',False)]"),
	}

	_defaults = {
		'user': lambda obj, cr, uid, context: uid,
	}

	def create(self, cr, uid, vals, context=None):
   		vals['name']= self.pool.get('ir.sequence').get(cr, uid, 'alert_u')
   		return super(Internal_alerts, self).create(cr, uid, vals, context=context)

Internal_alerts()