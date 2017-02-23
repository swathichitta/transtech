from openerp.osv import fields, osv
import datetime

class Schedule_tasks(osv.osv):

	_name = 'schedule.tasks'
	_inherit="tasks.queue"

	_columns = {

		'schedule_id':fields.char('Scheduled Task ID'),
		'start_date':fields.date('Start Date'),
		
	}

	def create(self, cr, uid, vals, context=None):
   		vals['schedule_id']= self.pool.get('ir.sequence').get(cr, uid, 'sched.tasks')
   		return super(Schedule_tasks, self).create(cr, uid, vals, context=context)


   	_defaults={
   	'bulk_insert':1,
   	}
Schedule_tasks()