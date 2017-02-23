from openerp.osv import fields, osv
import datetime
import time
import urllib
import random



class ATM_details(osv.osv):

	_name = 'atm.info'

	def CurrentMonth(self,cr,uid,context=None):

		visit_date = datetime.datetime.now().date()

		if visit_date.month == 1:
				month = 'dec'
		if visit_date.month == 2:
				month = 'jan'
		if visit_date.month == 3:
				month = 'feb'
		if visit_date.month == 4:
				month = 'mar'
		if visit_date.month == 5:
				month = 'apr'
		if visit_date.month == 6:
				month = 'may'
		if visit_date.month == 7:
				month = 'june'
		if visit_date.month == 8:
				month = 'jul'
		if visit_date.month == 9:
				month = 'aug'
		if visit_date.month == 10:
				month = 'sep'
		if visit_date.month == 11:
				month = 'oct'
		if visit_date.month == 12:
				month = 'nov'

		return month

	# def __count_visits1(self, cr, uid, ids, name, arg, context=None):

	# 	result = {}
	# 	mnth = self.CurrentMonth(cr,uid,context=None)

	# 	for obj in self.browse(cr, uid, ids, context=context):
	# 		survey_ids = self.pool.get('survey.info').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])
	# 		result[obj.id] = len(survey_ids)

	# 	return result

	# def __count_visits2(self, cr, uid, ids, name, arg, context=None):

	# 	result = {}
	# 	mnth = self.CurrentMonth(cr,uid,context=None)
	# 	for obj in self.browse(cr, uid, ids, context=context):
	# 		survey_ids = self.pool.get('survey.info').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])

	# 		sct_ids = self.pool.get('schedule.task').search(cr,uid,[('atm','=',obj.id),('status','!=','cancel')])
	# 		if sct_ids:
	# 			sct_obj = self.pool.get('schedule.task').browse(cr,uid,sct_ids[0])

	# 			if sct_obj.visit_type == 'monthly':
	# 				total = 1
	# 			else:
	# 				total = int(sct_obj.visit_type)
	# 			survey_ids = self.pool.get('survey.info').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])
	# 			result[obj.id] = total - len(survey_ids)
	# 			if result[obj.id] < 0:
	# 				result[obj.id] = 0
	# 		else:

	# 			result[obj.id] = 0

	# 	return result

	# def __count_visits3(self, cr, uid, ids, name, arg, context=None):

	# 	result = {}
	# 	mnth = self.CurrentMonth(cr,uid,context=None)
	# 	for obj in self.browse(cr, uid, ids, context=context):
	# 		survey_ids = self.pool.get('survey.info').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])

	# 		sct_ids = self.pool.get('schedule.task').search(cr,uid,[('atm','=',obj.id),('status','!=','cancel')])
	# 		if sct_ids:
	# 			sct_obj = self.pool.get('schedule.task').browse(cr,uid,sct_ids[0])

	# 			if sct_obj.visit_type == 'monthly':
	# 				result[obj.id] = 1
	# 			else:
	# 				result[obj.id] = sct_obj.visit_type
	# 		else:

	# 			survey_ids = self.pool.get('survey.info').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])
	# 			result[obj.id] = len(survey_ids)

	# 	return result
	


	_columns = {
		
		'atm_code':fields.char('ATM Code'),
		'name':fields.char("ATM Branch Details"),
		'atm_id':fields.char('Bank ATM ID(provided by Bank)'),
		'atm_type':fields.selection([('atm_only','ATM only'),
									('atm_cash_deposit','ATM and Cash Deposit'), 
									('drive_through','Drive Through'), 
									('walk_through','Walk Through'), 
									('lobby','Lobby'), 
									('ttw','TTW')],'ATM Type'),
				
		'customer':fields.many2one('customer.info','Customer'),
		'country':fields.many2one('res.country','Country', domain="[('code','=','AE')]"),
		'state_id':fields.many2one('res.country.state','State'),
		'sla_start':fields.datetime('SLA Start Date'),
		'sla_end':fields.datetime('SLA End Date'),
		'no_of_visits':fields.integer('Number of Visits'),
		'comments':fields.text('Special Instructions/Conditions'),
		'longitude':fields.char('Longitude'),
		'latitude':fields.char('Latitude'),
		'child_ids': fields.one2many('atm.old','parent_id',string='Moves'),
		'date':fields.date('Date'),
		'no_tasks':fields.integer('No. of Tasks'),
		'total_visits':fields.integer('Required Visits'),
		
#        New Inventory Fields

		'atm_model' : fields.char('ATM Model'), 
		'atm_make' : fields.char('ATM Make'), 
		'atm_functionality' : fields.char('ATM Functionality'), 
		'base_height' : fields.char('Base Height'),

		'location_cat':fields.selection([('offsite','Offsite'),
										('onsite','Onsite')],'Location Category'),

		'offsite_cat':fields.selection([('shopping_mall','Shopping Mall'), 
										('other','Other'), 
										('govt_institution','Govt. Institution'), 
										('fuel_station','Fuel Station')],'Offsite Category'),

		'onsite_cat':fields.selection([('branch','Branch'), 
									('csu','CSU'), 
									('mall_branch','Mall Branch')],'Onsite Category'),
		
		'kiosk_type' : fields.char('Kiosk Type'),
		'branding_details' : fields.text('Branding Details'),
		'installation_date' : fields.date('Installation Date'),
		'removed_from' : fields.char('Removed From'),
		'device1':fields.char('Device 1'),
		'device2':fields.char('Device 2'),
		'device3':fields.char('Device 3'),
		'device4':fields.char('Device 4'),
		'device5':fields.char('Device 5'),


		'make':fields.char('Make'),
		'model':fields.char('Model'),
		'capacity':fields.char('Capacity'),
		'detail1':fields.char('Detail 1'),
		'detail2':fields.char('Detail 2'),
				
		
		'atm_image':fields.binary('ATM Image'), 
		'escorting_comp' : fields.char('Escorting Company'), 
		'ded_num' : fields.char('DED Number'),
		'atm_id2':fields.char('ATM ID'),
		'serial_no':fields.char('ATM Serial No.'),
		# 'visits_done':fields.function(__count_visits1,type='integer',string="Visits Done",method=True, store = False, multi=False),
		# 'visits_left':fields.function(__count_visits2,type='integer',string="Visits Left",method=True, store=False, multi=False),
		# 'visits_total':fields.function(__count_visits3,type='integer',string="Required Visits",method=True, store=False, multi=False),
		
	
		}

	# code to get default country name
	def _default_country(self, cr, uid, context=None):
		cid = self.pool.get('res.country').search(cr, uid, [('code', '=', 'AE')], context=context)
		return cid[0]

	_defaults = {
		'date': lambda *a: time.strftime('%Y-%m-%d'),
		'country':_default_country,
	}

	def create(self, cr, uid, vals, context=None):
   		vals['atm_code']= self.pool.get('ir.sequence').get(cr, uid, 'atm.det')
   		return super(ATM_details, self).create(cr, uid, vals, context=context)

	def onchange_customer(self,cr,uid,ids,customer,context=None):
		res={'value':{}}
		cust_obj = self.pool.get('customer.info').browse(cr,uid,customer)
		res['value'].update({'sla_start':cust_obj.sla_start,
			'sla_end':cust_obj.sla_end,
			'country':cust_obj.country_id.id})

		return res

	def open_map(self, cr, uid, ids, context=None):
		address_obj= self.pool.get('atm.info')
		partner = address_obj.browse(cr, uid, ids, context=context)[0]
		url="http://maps.google.com/maps?oi=map&q="
		if partner.longitude:
			url+=partner.longitude.replace(' ','+')
		if partner.latitude:
			url+= ',' + partner.latitude.replace(' ','+')
		return {
			'type': 'ir.actions.act_url','url':url,'target': 'new'}

	def geo_localize(self, cr, uid, ids, context=None):

		partner = self.browse(cr,uid,ids)
		latitude = partner[0].latitude
		longitude = partner[0].longitude
		geo = {}
		if latitude or longitude:
			geo['lat'] = latitude
			geo['lng'] = longitude
			return float(geo['lat']), float(geo['lng'])
		return True

	def name_get(self,cr,uid,ids,context=None):
		if context is None:
			context ={}
		res=[]
		record_name=self.browse(cr,uid,ids,context)
		for object in record_name:

			# if object.name:
			if object.latitude and object.longitude:
				  # name for contact_address_id field
				res.append((object.id,object.name+', '+object.atm_id+', '+'%%'+object.latitude+'%%'+object.longitude))
			else:
			   # //name for contact_id field                     
				res.append((object.id,object.name+', '+object.atm_id))
		return res

ATM_details()



class Atm_old(osv.osv):
	_name = 'atm.old'    
	_columns = { 
				'parent_id':fields.many2one('atm.info','ATM'),
				'longitude':fields.char('Longitude'),
				'latitude':fields.char('Latitude'),
				'date':fields.date('Date'),
				'name':fields.char("ATM Branch Details"),  
				}
Atm_old()



class Atm_survey_management(osv.osv):
	_name="atm.surverys.management"
	_columns={
		'name':fields.char('Task ID', readonly=True),
		'task_month':fields.selection([('jan','January'),
									   ('feb', 'February'),
									   ('mar', 'March'),
									   ('apr', 'April'),
									   ('may', 'May'),
									   ('june','June'),
									   ('jul', 'July'),
									   ('aug', 'August'),
									   ('sep', 'September'),
									   ('oct', 'October'),
									   ('nov', 'November'),
									   ('dec', 'December'),], 'Month'),
		'customer':fields.many2one('customer.info','Customer'),
		'state':fields.many2one('res.country.state','State',domain="[('country_id','=',country)]"),
		'atm':fields.many2one('atm.info','ATM',domain="[('customer','=',customer),('state_id','=',state)]"),
		'country':fields.many2one('res.country','Country', domain="[('code','=','AE')]"),
		'surveyor':fields.many2one('res.users','Surveyor', domain="[('name_tl','!=',False)]"),
		'visit_time':fields.datetime('Visit Date And Time'),
		'additional_info':fields.text('Additional instructions'),
		'status': fields.selection([('assigned','Assigned'),
									('pending', 'Pending'),
									('cancel', 'Cancelled'),
									('progress', 'Progress'),
									('waitnig_approve','Waiting for Approval'),
									('done', 'Done'),], 'Status'),
		'bulk_insert':fields.boolean('Bulk Insert'),
		'nos':fields.integer('Number of records for Bulk Insert '),
		'remarks_id':fields.many2one('remarks.category', 'Remarks Category'),
		'remarks':fields.text('Remarks'),
		'act_visit_time':fields.datetime('Actual Date Time'),
		'assigned_by':fields.many2one('res.users','Assigned By'),
		'visit_type': fields.selection([('daily','Daily'),
										('weekly', 'Weekly'),
										('monthly', 'Monthly'),
										('2', 'Twice'),
										('3', '3 times'),
										('4', '4 times'),
										('5', '5 times'),
										('6', '6 times'),
										('7', '7 times'),
										('8', '8 times'),
										('9', '9 times'),
										('10', '10 times'),
										('12', '12 times'),
										('13', '13 times'),
										('16', '16 times'),], 'Visit Type'),
		'next_visit':fields.datetime('Next Visit'),
		'visit_shift':fields.selection([('day','Day'),
										('night','Night')] ,'Visit Shift'),
	}