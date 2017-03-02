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
	# 		survey_ids = self.pool.get('survey.details').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])
	# 		result[obj.id] = len(survey_ids)

	# 	return result

	# def __count_visits2(self, cr, uid, ids, name, arg, context=None):

	# 	result = {}
	# 	mnth = self.CurrentMonth(cr,uid,context=None)
	# 	for obj in self.browse(cr, uid, ids, context=context):
	# 		survey_ids = self.pool.get('survey.details').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])

	# 		sct_ids = self.pool.get('schedule.tasks').search(cr,uid,[('atm','=',obj.id),('status','!=','cancel')])
	# 		if sct_ids:
	# 			sct_obj = self.pool.get('schedule.tasks').browse(cr,uid,sct_ids[0])

	# 			if sct_obj.visit_type == 'monthly':
	# 				total = 1
	# 			else:
	# 				total = int(sct_obj.visit_type)
	# 			survey_ids = self.pool.get('survey.details').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])
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
	# 		survey_ids = self.pool.get('survey.details').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])

	# 		sct_ids = self.pool.get('schedule.tasks').search(cr,uid,[('atm','=',obj.id),('status','!=','cancel')])
	# 		if sct_ids:
	# 			sct_obj = self.pool.get('schedule.tasks').browse(cr,uid,sct_ids[0])

	# 			if sct_obj.visit_type == 'monthly':
	# 				result[obj.id] = 1
	# 			else:
	# 				result[obj.id] = sct_obj.visit_type
	# 		else:

	# 			survey_ids = self.pool.get('survey.details').search(cr,uid,[('month','=',mnth),('atm_surv','=',obj.id),('status','=','approved')])
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
				# print "oooooooooooooooooo",object.name
				# print "o11111111111111111o",object.atm_id
				# print "o22222222222222222o",object.latitude
				# print "o33333333333333333o",object.longitude
				# x=(object.name+', '+object.atm_id+', '+'%%'+object.latitude+'%%'+object.longitude)
				# print "999999999999999",type(str(x))
				# print "o55555555555555555o",type(object.id )
				# print "o66666666666666666o",object.name
				# print "o777777777777777777o",object.name
				  # name for contact_address_id field
				res.append((str(object.id),str(object.name+', '+object.atm_id+', '+'%%'+object.latitude+'%%'+object.longitude)))
			else:
			   # //name for contact_id field                     
				res.append((object.id,object.name+', '+object.atm_id))
		return res


	def count_tasks(self,cr,uid,context=None):
		vals = {}
		if datetime.datetime.now().month == 1:
				cur_month = 'jan'
		if datetime.datetime.now().month == 2:
				cur_month = 'feb'
		if datetime.datetime.now().month == 3:
				cur_month = 'mar'
		if datetime.datetime.now().month == 4:
				cur_month = 'apr'
		if datetime.datetime.now().month == 5:
				cur_month = 'may'
		if datetime.datetime.now().month == 6:
				cur_month = 'june'
		if datetime.datetime.now().month == 7:
				cur_month = 'jul'
		if datetime.datetime.now().month == 8:
				cur_month = 'aug'
		if datetime.datetime.now().month == 9:
				cur_month = 'sep'
		if datetime.datetime.now().month == 10:
				cur_month = 'oct'
		if datetime.datetime.now().month == 11:
				cur_month = 'nov'
		if datetime.datetime.now().month == 12:
				cur_month = 'dec'

		tsk_ids = self.pool.get('tasks.queue').search(cr,uid,[('status','=','done'),('task_month','=','aug')])
		t_obj = self.pool.get('tasks.queue').browse(cr,uid,tsk_ids)
		atm_list = []
		
		for i in t_obj:
			# if i.status=='done':
			atm_list.append(i.atm.id)
			tsk_ids1 = self.pool.get('schedule.tasks').search(cr,uid,[('atm','=',i.atm.id)])
			survey_ids = self.pool.get('survey.details').search(cr,uid,[('month','=','aug'),('atm_surv','=',i.atm.id),('status','=','approved')])
			
			if survey_ids:
				vals.update({'no_tasks':len(survey_ids)})
			else:
				vals.update({'no_tasks':0})

			if tsk_ids1:
				sct_obj = self.pool.get('schedule.tasks').read(cr,uid,tsk_ids1[0],['visit_type'])

				if sct_obj['visit_type'] == 'monthly':
					sct_obj['visit_type'] = '1'
				
				if sct_obj['visit_type'] == 'daily':
					sct_obj['visit_type'] = '30'

				if sct_obj['visit_type'] == 'weekly':
					sct_obj['visit_type'] = '4'
				# print sct_obj
				done = self.pool.get('tasks.queue').search(cr,uid,[('status','=','done'),('task_month','=','aug'),('atm','=',i.atm.id)])
				vals.update({'total_visits':int(sct_obj['visit_type'])})
				vals.update({'no_of_visits':vals['total_visits']-vals['no_tasks']})
				if vals['no_of_visits'] < 0:
						vals.update({'no_of_visits':0})
				# print vals
			else:
				# done = self.pool.get('tasks.queue').search(cr,uid,[('status','=','done'),('task_month','=','jul'),('atm','=',i.atm.id)])
				vals.update({'total_visits':len(survey_ids)})
				vals.update({'no_of_visits':vals['total_visits']-vals['no_tasks']})
				if vals['no_of_visits'] < 0:
						vals.update({'no_of_visits':0})

			self.pool.get('atm.info').write(cr,uid,i.atm.id,vals)
		untouched_atms =  self.search(cr,uid,[('id','not in',atm_list)])
		values = {}

		if untouched_atms:
			for j in untouched_atms:

				tsk_ids1 = self.pool.get('schedule.tasks').search(cr,uid,[('atm','=',j)])
				if tsk_ids1:
					sct_obj = self.pool.get('schedule.tasks').read(cr,uid,tsk_ids1,['visit_type','atm'])
					for i in sct_obj:
						if i['visit_type'] == 'monthly':
							i['visit_type'] = '1'
						
						if i['visit_type'] == 'daily':
							i['visit_type'] = '30'

						if i['visit_type'] == 'weekly':
							i['visit_type'] = '4'
						values.update({'total_visits':int(i['visit_type'])})
				else:
					values.update({'total_visits':0})
				values.update({'no_tasks':0})
				values.update({'no_of_visits':0})
				self.pool.get('atm.info').write(cr,uid,j,values)
		return True

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


