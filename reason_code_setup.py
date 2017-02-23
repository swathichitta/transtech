from openerp.osv import fields, osv

class Reason_code_setup(osv.osv):

	_name = 'reason.code'

	_columns = {
		'reason_code':fields.char("Code"),
		'name':fields.char('Reason Code'),
		
	}
Reason_code_setup()