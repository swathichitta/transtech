from openerp.osv import fields, osv
import datetime
import time
from dateutil.relativedelta import relativedelta

class Tasks_in_queue(osv.osv):

	_name = 'tasks.queue'

	_columns = {
		'name':fields.char('Task ID'),
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
									   ('dec', 'December')], 'Month'),
		'customer':fields.many2one('customer.info','Customer'),
		'state':fields.many2one('res.country.state','State'),
		'atm':fields.many2one('atm.info','ATM'),
		'country':fields.many2one('res.country','Country', domain="[('code','=','AE')]"),
		'surveyor':fields.many2one('res.users','Surveyor'),
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
										('16', '16 times')], 'Visit Type'),
		'next_visit':fields.datetime('Next Visit'),
		'visit_shift':fields.selection([('day','Day'),
										('night','Night')] ,'Visit Shift'),
	}


	# code to get default country name
	def _default_country(self, cr, uid, context=None):
		cid = self.pool.get('res.country').search(cr, uid, [('code', '=', 'AE')], context=context)
		return cid[0]

	_defaults = {
		'status':'assigned',
		'visit_shift':'day',
		'country':_default_country,
	}
	def create(self, cr, uid, vals, context=None):
   		vals['name']= self.pool.get('ir.sequence').get(cr, uid, 'tasks.queue')
   		return super(Tasks_in_queue, self).create(cr, uid, vals, context=context)	

	def status_done(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'status':'done'},context=context)
		return True

	def status_cancel(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'status':'cancel'},context=context)
		return True



	def create_task(self,cr,uid,context=None):
		today = datetime.datetime.now().date()
		ids1 = self.search(cr,uid,[('next_visit','!=',False),('status','in',('done','assigned','progress','pending','waitnig_approve'))])
		task_list = self.browse(cr,uid,ids1,context=None)
		vals = {}
		for i in task_list:
				vals = {'customer':i.customer.id, 'atm':i.atm.id, 'country':i.country.id, 'state':i.state.id, 'surveyor':i.surveyor.id,'visit_time':i.next_visit,'additional_info':i.additional_info,'bulk_insert':i.bulk_insert, 'visit_type':i.visit_type,'act_visit_time':i.act_visit_time,'nos':i.nos-1}
				
				if i.visit_type == 'daily':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit']  = visit_date + datetime.timedelta(days=1)

				if i.visit_type == 'weekly':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit']  = visit_date + datetime.timedelta(days=7)

				if i.visit_type == 'monthly':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(months=1)

				if i.visit_type == '2':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=15)

				if i.visit_type == '3':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=9)

				if i.visit_type == '4':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=7.5)


				if i.visit_type == '5':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=6)

				if i.visit_type == '6':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=5)

				if i.visit_type == '7':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=4)

				if i.visit_type == '8':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=3.75)

				if i.visit_type == '9':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=3.333)

				if i.visit_type == '10':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=3)

				if i.visit_type == '12':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=2.5)


				if i.visit_type == '13':
					visit_date = datetime.datetime.strptime(i.visit_time, "%Y-%m-%d %H:%M:%S")
					vals['next_visit'] = visit_date+ relativedelta(days=2.30)


				if visit_date.month == 1:
						vals['task_month'] = 'jan'
				if visit_date.month == 2:
						vals['task_month'] = 'feb'
				if visit_date.month == 3:
						vals['task_month'] = 'mar'
				if visit_date.month == 4:
						vals['task_month'] = 'apr'
				if visit_date.month == 5:
						vals['task_month'] = 'may'
				if visit_date.month == 6:
						vals['task_month'] = 'june'
				if visit_date.month == 7:
						vals['task_month'] = 'jul'
				if visit_date.month == 8:
						vals['task_month'] = 'aug'
				if visit_date.month == 9:
						vals['task_month'] = 'sep'
				if visit_date.month == 10:
						vals['task_month'] = 'oct'
				if visit_date.month == 11:
						vals['task_month'] = 'nov'
				if visit_date.month == 12:
						vals['task_month'] = 'dec'
				print self.pool.get('tasks.queue').create(cr,uid,vals,context=None)
				self.pool.get('tasks.queue').write(cr,uid,i.id,{'nos':i.nos-1},context=None)
		return True


	def change_task_status(self,cr,uid,context=None):
		today =  str(datetime.datetime.now()).split()[0]
		all_tasks = self.search(cr,uid,[('visit_time','!=',False),('status','in',('assigned','progress'))])
		task_list1 = self.browse(cr,uid,all_tasks,context=None)
		for obj in task_list1:
			if obj.visit_time.split()[0] == today:
				self.pool.get('tasks.queue').write(cr,uid,obj.id,{'status':'progress'},context=None)
			if obj.visit_time.split()[0] < today:
				self.pool.get('tasks.queue').write(cr,uid,obj.id,{'status':'pending'},context=None)

		return True
Tasks_in_queue()