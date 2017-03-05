from openerp.osv import fields, osv


class  Custom_res_users(osv.osv):
	
	_inherit="res.users"
	_inherits = {'mail.alias': 'alias_id'}

	def copy(self, cr, uid, id, default=None, context=None):
		if not default:
			default = {}
		default.update({
			'tuser_id': self.pool.get('ir.sequence').get(cr, uid, 'res.id'),
		})
		return super(Custom_res_users, self).copy(cr, uid, id, default, context=context)
		
	_columns ={
		'teamleader':fields.boolean('Is Team Leader??'),
		'name_tl':fields.many2one('res.users','Team Leader', domain="[('role','!=','Customer'),('role','!=','Surveyor')]"),
		# 'password': fields.char('Password',	help="Keep empty if you don't want the user to be able to connect on the system."),
		'tuser_id':fields.char('User ID' ),
		'contact_num':fields.char('Contact Number'),
		'joining_date':fields.date('Joining Date'),
		'Comments':fields.text('Comments'),
		'role':fields.char('Role'),
		'survey_limit':fields.integer('Limit of Surveys'),
		'customer_ids':fields.many2many('customer.info','res_banks_users_rel','id','cid','Allowed Customers'),
		'company_id':fields.many2one('res.company','Company'),
		'status': fields.selection([('never_connected','Never Connected'),('activated','Activated')],'Status'),
	}
	_defaults={
		'status':'never_connected'
	}
	def create(self, cr, uid, vals, context=None):
		if 'teamleader' in vals or 'name_tl' in vals:
			if vals['teamleader'] == True and vals['name_tl'] == False:
				vals.update({'role':'Teamleader'})
			if vals['name_tl'] != False and vals['teamleader'] == False:
				vals.update({'role':'Surveyor'})
			if vals['teamleader'] == False and vals['name_tl'] == False:
				vals.update({'role':'Customer'})
			if vals['teamleader'] == True and vals['name_tl'] != False:
				raise osv.except_osv(_('You cannot select both "Is Team Leader??" and "TeamLeader" fields at a time.' ),_("Please select only one of them.") )

		vals['tuser_id'] = self.pool.get('ir.sequence').get(cr, uid, 'res.id') 
		result = super(Custom_res_users, self).create(cr, uid, vals, context=context)
		del_id = self.pool.get('res.groups').search(cr,uid,[('name','=','Employee')])
		cr.execute('DELETE from  res_groups_users_rel where uid = %s and gid = %s', (result, del_id[0]))
		return result

	def write(self, cr, uid, ids, vals, context=None):
	
		if 'teamleader' in vals:
			if vals['teamleader'] == True:
				vals.update({'role':'Teamleader'})
			else:
				vals.update({'role':'Surveyor'})
		if 'name_tl' in vals:
			if vals['name_tl'] != False:
				vals.update({'role':'Surveyor'})
			else:
				vals.update({'role':'Teamleader'})
		
		if 'teamleader' in vals and 'name_tl' in vals:
			if vals['teamleader'] == True and vals['name_tl'] != False:
				raise osv.except_osv(_('You cannot select both "Is Team Leader??" and "TeamLeader" fields at a time.' ),_("Please select only one of them.") )
		return super(Custom_res_users,self).write(cr,uid,ids,vals,context=None)

Custom_res_users()