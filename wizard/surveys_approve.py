from openerp.osv import fields, osv
from openerp.tools.translate import _

class surveys_approve(osv.TransientModel):
	_name="surveys.approve"

	def approve_survey(self, cr, uid, ids, context=None):
		data_inv = self.pool.get('survey.details').read(cr, uid, context['active_ids'], ['status'], context=context)

		for record in data_inv:
			if record['status'] not in ('waiting_approval'):
				raise osv.except_osv(_('Warning!'), _("Selected survey(s) cannot be approved as they are not in 'Waiting Approval' state."))
		self.pool.get('survey.details').write(cr,uid,context['active_ids'],{'status':'approved'})
		obj_list = self.pool.get('survey.details').browse(cr,uid,context['active_ids'])
		for obj in obj_list:
			self.pool.get('atm.surverys.management').write(cr, uid, obj.surv_task.id,{'status':'done'}, context)
		return {'type': 'ir.actions.act_window_close'}

surveys_approve()