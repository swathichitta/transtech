from openerp.osv import fields, osv
from openerp.tools.translate import _

class Alerts_for_you(osv.osv):

	_name = 'alerts.dashboard'

	_columns = {
		'name':fields.char('Alert ID'),
		'customer':fields.many2one('customer.info','Customer'),
		'created_by':fields.many2one('res.users','Created By'),
		'atm_id':fields.many2one('atm.info','ATM'),
		'category':fields.selection([('complaint','Complaint'),
									 ('issue','Issue')],'Category'),
		'priority':fields.selection([('low','Low'),
									 ('medium','Medium'), 
									 ('high','High'),
									 ('critical','Critical')],'Priority'),
		'country_id':fields.many2one('res.country','Country',domain="[('code','=','AE')]"),
		'state_id':fields.many2one('res.country.state','State'),
		'assign_to':fields.many2one('res.users','Assign To'),
		'status':fields.selection([('assigned','Assigned'),
								   ('resolved','Resolved'), 
								   ('closed','Closed')],'Status'),
		'summary':fields.char('Summary', size=100),
		'description':fields.text('Description'),
		'reason_id':fields.many2one('reason.code','Reason Code'),
		'reason_disc':fields.text('Reason Descriptions'),
	

	}

	# def create(self,cr,uid,vals,context=None):
	# 	vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'alert.you')
	# 	user_id= super(Alerts_for_you, self).create(cr, uid, vals, context=context)
	# 	if user_id != False:
	# 		self.send_alert_invitation(cr,uid,[user_id],context=None)
	# 		return user_id

	# def send_alert_invitation(self,cr,uid,ids,context=None):
	# 	alert_obj = self.browse(cr,uid,ids,context=None)[0]
	# 	print alert_obj
	# 	customer_id =  self.pool.get('customer.info').browse(cr,uid,alert_obj.customer.id)
	# 	customer_name = customer_id.name
	# 	atm_id1 =self.pool.get('atm.info').browse(cr,uid,alert_obj.atm_id.id)
	# 	atm_name = atm_id1.name
	# 	user_ids = self.pool.get('res.users').browse(cr,uid,alert_obj.assign_to.id)
	# 	print user_ids.name_tl
	# 	teamleader_find = self.pool.get('res.users').browse(cr,uid,user_ids.name_tl.id)
	# 	print teamleader_find
	# 	temail_id = teamleader_find.email
	# 	print temail_id
	# 	if not temail_id:
	# 		raise osv.except_osv(_('No Email Provided for this Teamleader'),_("Please give a Valid email address !") )
	# 		return False
	# 	tname= teamleader_find.name
	# 	mail_ids = self.pool.get('ir.mail_server').search(cr,uid,[('active','=','True')])
	# 	mail_obj = self.pool.get('ir.mail_server').browse(cr,uid,mail_ids)[0]
	# 	username = mail_obj.smtp_user
	# 	pwd = mail_obj.smtp_pass
	# 	host = mail_obj.smtp_host
	# 	port = mail_obj.smtp_port
	# 	fromaddr = username
	# 	server = smtplib.SMTP(host+':'+'587')
	# 	server.ehlo()
	# 	server.starttls()
	# 	server.ehlo()
	# 	server.login(username, pwd)
	# 	msg = MIMEMultipart()
	# 	msg['From'] = fromaddr
	# 	msg['Subject'] = 'New Internal Alert in Transtech Portal'
	# 	toaddr = teamleader_find.email
	# 	msg['To'] = toaddr
	# 	text = ('<p><h2>Hello, %s</h2> One internal alert is generate in Transtech Portal</p><p><b>Details of generate alerts is given below:-</b></p><p><b>Genrated By </b>: %s</p><p><b>Alert ID</b> :  %s</p><p><b>Customer</b> :  %s</p><p><b>Alert Category </b> : %s</p><p><b>Priority </b>:%s</p><p><b>ATM </b>:%s,%s</p>')%(tname,user_ids.name,alert_obj.name,customer_id.name,alert_obj.category,alert_obj.priority,atm_name,atm_id1.atm_id)
	# 	body = MIMEText(text, _subtype='html')
	# 	msg.attach(body)
	# 	res = server.sendmail(fromaddr, toaddr, msg.as_string())
	# 	server.quit()

	# 	return True


		
	def _default_country(self, cr, uid, context=None):
		cid = self.pool.get('res.country').search(cr, uid, [('code', '=', 'AE')], context=context)
		return cid[0]
		
	_defaults = {
		'status':'assigned',
		'country_id':_default_country,    
		'created_by': lambda obj, cr, uid, context: uid,
	
	}

	def status_resolve(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'status':'resolved'},context=context)
		return True

	def status_close(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'status':'closed'},context=context)
		return True

	def unlink(self, cr, uid, ids, context=None):
		alert_obj = self.pool.get('customer.alerts').browse(cr,uid,ids[0])
		if alert_obj.status in ('resolved','closed'):
			raise osv.except_osv(_('Invalid Action!'), _("You can't delete an Alert which is either in 'Resolved state' or in 'Closed state' "))
			return super(Alerts_for_you, self).unlink(cr, uid, ids, context=context)

Alerts_for_you()


