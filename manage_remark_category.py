from openerp.osv import fields, osv

class Manage_remark_category(osv.osv):

	_name = 'remarks.category'
	
	_columns = {
		'description':fields.char("Remark Category ID"),
		'name':fields.char('Remark Description'),
	}

	def create(self, cr, uid, vals, context=None):
   		vals['description']= self.pool.get('ir.sequence').get(cr, uid, 'remark.cat')
   		return super(Manage_remark_category, self).create(cr, uid, vals, context=context)

Manage_remark_category()