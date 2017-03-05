from openerp.osv import fields, osv
from openerp.tools.translate import _
import datetime
import time
from dateutil.relativedelta import relativedelta


class Schedule_tasks(osv.osv):


	def __count_visits(self, cr, uid, ids, name, arg, context=None):
		result = {}
		for obj in self.browse(cr, uid, ids, context=context):
			if obj.visit_type == 'monthly':
				result[obj.id] = 1
			else:
				result[obj.id] = obj.visit_type
		return result

	_name = 'schedule.tasks'
	_columns = {
		'name':fields.char('Scheduled Task ID',),
		'customer':fields.many2one('customer.info','Customer',size=64),
		'state':fields.many2one('res.country.state','State',domain="[('country_id','=',country)]"),
		'atm':fields.many2one('atm.info','ATM',domain="[('customer','=',customer),('state_id','=',state)]"),
		'country':fields.many2one('res.country','Country', domain="[('code','=','AE')]"),
		'surveyor':fields.many2one('res.users','Surveyor'),
		'visit_date':fields.date('Start Date'),
		'additional_info':fields.text('Additional instructions'),
		'status': fields.selection([
									('assigned','Assigned'),
									('cancel', 'Cancelled'),
									], 'Status', track_visibility='always'),
		'bulk_insert':fields.boolean('Bulk Insert'),
		'remarks_id':fields.many2one('remarks.category', 'Remarks Category'),
		'remarks':fields.text('Remarks'),
		'assigned_by':fields.many2one('res.users','Assigned By' ),
		'visit_type': fields.selection([
										('monthly', 'Monthly/1 visit'),
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
										('16', '16 times'),
										], 'Visit Type/ No. of Visits to be done'),
		'next_exec':fields.date('Next Execution'),
		'visits_count':fields.function(__count_visits,type='integer',string="No.of visits per Month",method=True, store=True, multi=False),
		'visit_shift':fields.selection([('day','Day'),('night','Night')] ,'Visit Shift'),
	}
	
	def status_cancel(self,cr,uid,ids,context=None):
		self.write(cr,uid,ids,{'status':'cancel'},context=context)
		return True 

	def create(self,cr,uid,vals,context=None):

		lines = self.search(cr,uid, [('atm','=',vals['atm']),('visit_date','=',vals['visit_date']),('status','=','assigned'),('surveyor','=',vals['surveyor']),('customer','=',vals['customer'])])
		if lines:
			raise osv.except_osv(_('Error !'),_("One Task has been already created with this ATM & with the same visit date !") )

		today = datetime.datetime.strptime(vals['visit_date'], "%Y-%m-%d")
		if vals['visit_type'] == 'daily':
			visit_date = today
			vals['next_exec']  = visit_date + datetime.timedelta(days=1)

		if vals['visit_type'] == 'weekly':
			visit_date = today
			vals['next_exec']  = visit_date + datetime.timedelta(days=7)

		if vals['visit_type'] == 'monthly':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(months=1)

		if vals['visit_type'] == '2':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=15)

		if vals['visit_type'] == '3':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=9)

		if vals['visit_type'] == '4':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=7.5)


		if vals['visit_type'] == '5':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=6)

		if vals['visit_type'] == '6':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=5)

		if vals['visit_type'] == '7':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=4)

		if vals['visit_type'] == '8':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=3.75)

		if vals['visit_type'] == '9':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=3.333)

		if vals['visit_type'] == '10':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=3)

		if vals['visit_type'] == '12':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=2.5)

		if vals['visit_type'] == '13':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=2.30)

		if vals['visit_type'] == '16':
			visit_date = today
			vals['next_exec'] = visit_date+ relativedelta(days=1.875)

		if vals['next_exec'].weekday() == 4:
			vals['next_exec'] =  vals['next_exec'] - relativedelta(days=1)

		vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'sched.tasks')

		return super(Schedule_tasks, self).create(cr, uid, vals, context=context)

	def _default_country(self, cr, uid, context=None):
		cid = self.pool.get('res.country').search(cr, uid, [('code', '=', 'AE')], context=context)
		return cid[0]

   	_defaults={
   		'assigned_by': lambda obj, cr, uid, ctx=None: uid,
		'status':'assigned',
		'visit_shift':'day',
		'bulk_insert': True,
		'country':_default_country,
   	}

   	def write(self,cr,uid,ids,vals,context=None):
		if isinstance(ids, (int, long)):
			ids = [ids]

		wr =  super(Schedule_tasks, self).write(cr, uid, ids, vals, context=context)

		if 'next_exec' not in vals:
			t_obj = self.browse(cr,uid,ids,context=None)

			t_obj = t_obj[0]

			today = datetime.datetime.strptime(t_obj.visit_date, "%Y-%m-%d")
			if t_obj.visit_type == 'daily':
				visit_date = today
				vals['next_exec']  = visit_date + datetime.timedelta(days=1)

			if t_obj.visit_type == 'weekly':
				visit_date = today
				vals['next_exec']  = visit_date + datetime.timedelta(days=7)

			if t_obj.visit_type == 'monthly':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(months=1)

			if t_obj.visit_type == '2':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=15)

			if t_obj.visit_type == '3':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=9)

			if t_obj.visit_type == '4':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=7.5)


			if t_obj.visit_type == '5':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=6)

			if t_obj.visit_type == '6':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=5)

			if t_obj.visit_type == '8':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=3.75)

			if t_obj.visit_type == '7':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=4)

			if t_obj.visit_type == '9':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=3.333)

			if t_obj.visit_type == '10':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=3)

			if t_obj.visit_type == '12':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=2.5)

			if t_obj.visit_type == '13':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=2.30)

			if t_obj.visit_type == '16':
				visit_date = today
				vals['next_exec'] = visit_date+ relativedelta(days=1.875)

			if vals['next_exec'].weekday() == 4:
				vals['next_exec'] =  vals['next_exec'] - relativedelta(days=1)
			return super(Schedule_tasks, self).write(cr, uid, ids, vals, context=context)
		return True


	def schedule_task(self,cr,uid,context=None):
		today = datetime.datetime.now().date()
		ids1 = self.search(cr,uid,[('status','!=','cancel'),('next_exec','=',today)])
		ids2 = self.search(cr,uid,[('status','!=','cancel'),('visit_date','=',today)])
		nxt_visit1 = today + relativedelta(days=1)
		nxt_visit2 = today + relativedelta(days=2)
		nxt_visit3 = today + relativedelta(days=3)
		ids3 = self.search(cr,uid,[('status','!=','cancel'),'|','|',('next_exec','=',nxt_visit1),('next_exec','=',nxt_visit2),('next_exec','=',nxt_visit3)])
		f_ids =  ids1 + ids2 + ids3
		f_ids = list(set(f_ids))
		task_list = self.browse(cr,uid,f_ids,context=None)
		vals = {}
		if task_list:
			for i in task_list:
				vals = {'customer':i.customer.id, 'atm':i.atm.id, 'country':i.country.id, 'state':i.state.id, 'surveyor':i.surveyor.id,'additional_info':i.additional_info,'bulk_insert':False, 'visit_type':i.visit_type}
				
				if i.next_exec.split(' ')[0] == str(today):
					visit_date = datetime.datetime.strptime(i.next_exec, "%Y-%m-%d")
					vals['visit_time'] = visit_date

				elif i.visit_date.split(' ')[0] == str(today):
					visit_date = datetime.datetime.strptime(i.visit_date, "%Y-%m-%d")
					vals['visit_time'] = visit_date

				else:
					visit_date = datetime.datetime.strptime(i.next_exec, "%Y-%m-%d")
					vals['visit_time'] = today

				if i.visit_type == 'daily':
					vals['next_visit']  = visit_date + datetime.timedelta(days=1)

				if i.visit_type == 'weekly':
					vals['next_visit'] = visit_date+ relativedelta(days=7)

				if i.visit_type == 'monthly':
					vals['next_visit'] = visit_date+ relativedelta(months=1)

				if i.visit_type == '2':
					vals['next_visit'] = visit_date+ relativedelta(days=15)

				if i.visit_type == '3':
					vals['next_visit'] = visit_date+ relativedelta(days=9)

				if i.visit_type == '4':
					vals['next_visit'] = visit_date+ relativedelta(days=7.5)

				if i.visit_type == '5':
					vals['next_visit'] = visit_date+ relativedelta(days=6)

				if i.visit_type == '6':
					vals['next_visit'] = visit_date+ relativedelta(days=5)

				if i.visit_type == '7':
					vals['next_visit'] = visit_date+ relativedelta(days=4)

				if i.visit_type == '8':
					vals['next_visit'] = visit_date+ relativedelta(days=3.75)

				if i.visit_type == '9':
					vals['next_visit'] = visit_date+ relativedelta(days=3.333)

				if i.visit_type == '10':
					vals['next_visit'] = visit_date+ relativedelta(days=3)

				if i.visit_type == '12':
					vals['next_visit'] = visit_date+ relativedelta(days=2.5)


				if i.visit_type == '13':
					vals['next_visit'] = visit_date+ relativedelta(days=2.30)

				if i.visit_type == '16':
					vals['next_visit'] = visit_date+ relativedelta(days=1.875)

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

				holiday = self.pool.get('hr.holidays.public.line').search(cr,uid,[('date','=',vals['next_visit'])])
				
				if vals['next_visit'].weekday() == 4 or holiday:
					vals['next_visit'] =  vals['next_visit'] - relativedelta(days=1)

				t_ids = self.pool.get('tasks.queue').search(cr,uid,[('customer','=',vals['customer']),('atm','=',vals['atm']),('task_month','=',vals['task_month'])])

				if i.visit_type == 'monthly':
					i.visit_type = '1'
					
				if len(t_ids) < int(i.visit_type) and visit_date.month == datetime.datetime.now().month:
					self.pool.get('tasks.queue').create(cr,uid,vals,context=None)
				self.pool.get('schedule.tasks').write(cr,uid,i.id,{'next_exec':vals['next_visit']},context=None)
		return True


	def changeDateto1st(self,cr,uid,context=None):
		present = datetime.datetime.now()
		sched_tasks =  self.search(cr,uid,[('id','!=',False)])
		today = present.date()
		import calendar
		month_days =  calendar.monthrange(present.year,present.month)
		if month_days[1] == present.day:
			tomorrow = today + relativedelta(days=1)
			self.write(cr,uid,sched_tasks,{'visit_date':tomorrow})
		return True
		
Schedule_tasks()