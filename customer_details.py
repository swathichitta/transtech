from openerp.osv import fields, osv
from openerp.tools.translate import _


class Customer_Details(osv.osv):

	_name = 'customer.info'

	 		
	def _show_tasks(self, cr, uid, ids, name, args, context=None):
		res = {}
		c_ids = self.pool.get('atm.surverys.management').search(cr,uid,[('customer','=',ids[0])])
		for t_id in self.browse(cr,uid,ids):
			res[t_id.id] = c_ids
		return res
	

	_columns = {

		'customer_code':fields.char('Customer Code'),
		'name':fields.char('Customer name'),
		'image': fields.binary("Image",help="This field holds the image used as avatar for this contact, limited to 1024x1024px"),
	
        'country_id':fields.many2one('res.country','Country',domain="[('code','=','AE')]"),
		'address':fields.text('Address'),
		'contact_person':fields.char('Contact Person'),
		'contact_email':fields.char('Contact Person Email'),
		'contact_email2':fields.char('Contact Person Email 2'),
		'contact_email3':fields.char('Contact Person Email 3'),
		'mobile_no':fields.char('Contact Number'),
		'active':fields.boolean('Active??'),
		'display_mapping':fields.boolean('Dispaly Mapping'),
		'account_manager':fields.many2one('res.users','Account Manager'),
		'other_1':fields.many2one('res.users','Other1'),
		'other_2':fields.many2one('res.users','Other2'),
		'task_ids': fields.function(_show_tasks, relation='atm.surverys.management', type="many2many", string='My Tasks'),
		'sla_start':fields.datetime('SLA Start Date'),
		'sla_end':fields.datetime('SLA End Date'),
		'is_customer':fields.boolean('Is Customer'),
	}

	def create(self, cr, uid, vals, context=None):
		vals['customer_code'] = self.pool.get('ir.sequence').get(cr, uid, 'customer.info') or '/'
		return super(Customer_Details, self).create(cr, uid, vals, context=context)

	# code to get default country name
	def _default_country(self, cr, uid, context=None):
		cid = self.pool.get('res.country').search(cr, uid, [('code', '=', 'AE')], context=context)
		return cid[0]

	_defaults = {
		'country_id':_default_country,
		'active':1,
	}
  

	def send_invitation(self,cr,uid,ids,context=None):
		cust_obj = self.browse(cr,uid,ids,context=None)[0]
		if not cust_obj.contact_email:
			raise osv.except_osv(_('No Email Provided for this customer'),_("Please give a Valid email address !") )
			return False
		name=cust_obj.name
		if re.search(r'\s',cust_obj.name):
			name=cust_obj.name.replace(" ", "_")
		chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
		password = ''.join(random.choice(chars) for i in xrange(6))
		c_id = self.pool.get('res.users').search(cr,uid,[('name','=',cust_obj.name)])
		gr_id = self.pool.get('res.groups').search(cr,uid,[('name','=','Customer')])
		del_id = self.pool.get('res.groups').search(cr,uid,[('name','=','Employee')])
		if c_id:
			raise osv.except_osv(_('You are already created a User for this customer'),_("Please recheck your users list via Users Menu.") )
			return False
		val={'name':cust_obj.name,'login':name,'password':str(password),'role':'Customer'}
		new_id = self.pool.get('res.users').create(cr,uid,val,context=None)
		cr.execute('insert into  res_groups_users_rel (uid, gid) values(%s,%s)', (new_id, gr_id[0]))
		cr.execute('DELETE from  res_groups_users_rel where uid = %s and gid = %s', (new_id, del_id[0]))
		mail_ids = self.pool.get('ir.mail_server').search(cr,uid,[('active','=','True')])
		mail_obj = self.pool.get('ir.mail_server').browse(cr,uid,mail_ids)[0]
		username = mail_obj.smtp_user
		pwd = mail_obj.smtp_pass
		host = mail_obj.smtp_host
		port = mail_obj.smtp_port
		fromaddr = username
		server = smtplib.SMTP(host+':'+'587')
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(username, pwd)
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['Subject'] = 'Regarding Account Details For TransTechERP'
		toaddr = cust_obj.contact_email
		msg['To'] = toaddr
		text = ('<p><h2>Hello, %s</h2> Your account has been created in Transtech ERP as User</p><p><b>Your login credentials are given below:-</b></p><p>Username: %s</p><p>Password: %s</p><p>To login click on below link</p><p><a href="http://162.243.21.15:8069/">Click Here</a></p>')%(cust_obj.name,name,password)
		body = MIMEText(text, _subtype='html')
		msg.attach(body)
		res = server.sendmail(fromaddr, toaddr, msg.as_string())
		server.quit()

		return True

Customer_Details()