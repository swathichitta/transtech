from openerp.osv import fields, osv


class Survey_prints(osv.TransientModel):

	_name = "print.survey"

	_columns = {
	'customer_id':fields.many2one('customer.info','Customer/Bank'),
	'month':fields.selection([('jan','January'),
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

	'bfr_img_front':fields.binary('Front View'),
	'bfr_img_side':fields.binary('Side View'),
	'bfr_img_back':fields.binary('Back View'),
	'after_img_front':fields.binary('Front View After'),
	'after_img_side':fields.binary('Side View After'),
	'after_img_back':fields.binary('Back View After'),

	'bfr_img_front2':fields.binary('Front View 2'),
	'bfr_img_side2':fields.binary('Side View 2'),
	'bfr_img_back2':fields.binary('Back View 2'),
	'after_img_front2':fields.binary('Front View After 2'),
	'after_img_side2':fields.binary('Side View After 2'),
	'after_img_back2':fields.binary('Back View After 2'),


	'bfr_img_front3':fields.binary('Front View 3'),
	'bfr_img_side3':fields.binary('Front View Side 3'),
	'after_img_front3':fields.binary('Front View After 3'),
	'after_img_side3':fields.binary('Side View After 3'),

	}

	def action_upload(self, cr, uid, ids, context=None):
		# for i in range(0,5):
		data = self.read(cr, uid, ids)[0]


		vals = {}

		if data['bfr_img_front']:
			vals['bfr_img_front'] = data['bfr_img_front']

		if data['bfr_img_side']:
			vals['bfr_img_side'] = data['bfr_img_side']

		if data['bfr_img_back']:
			vals['bfr_img_back'] = data['bfr_img_back']

		if data['after_img_front']:
			vals['after_img_front'] = data['after_img_front']

		if data['after_img_side']:
			vals['after_img_side'] = data['after_img_side']

		if data['after_img_back']:
			vals['after_img_back'] = data['after_img_back']


		if data['bfr_img_front2']:
			vals['bfr_img_front2'] = data['bfr_img_front2']

		if data['bfr_img_side2']:
			vals['bfr_img_side'] = data['bfr_img_side2']

		if data['bfr_img_back2']:
			vals['bfr_img_back2'] = data['bfr_img_back2']

		if data['after_img_front2']:
			vals['after_img_front2'] = data['after_img_front2']

		if data['after_img_side2']:
			vals['after_img_side2'] = data['after_img_side2']

		if data['after_img_back2']:
			vals['after_img_back2'] = data['after_img_back2']


		if data['bfr_img_front3']:
			vals['bfr_img_front3'] = data['bfr_img_front3']

		if data['bfr_img_side3']:
			vals['bfr_img_side3'] = data['bfr_img_side3']

		if data['after_img_front3']:
			vals['after_img_front3'] = data['after_img_front3']
			
		if data['after_img_side3']:
			vals['after_img_side3'] = data['after_img_side3']

		survey_ids = self.pool.get('survey.details').write(cr,uid,context['active_id'],vals)
		return {
				'type': 'ir.actions.client',
				'tag': 'reload',  }


Survey_prints()