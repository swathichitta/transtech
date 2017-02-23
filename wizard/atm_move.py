from openerp.osv import fields, osv
import datetime
import time

class Atm_localization(osv.osv):
    _name = 'atm.move'   
    _columns = { 
                'longitude':fields.char('Longitude'),
				'latitude':fields.char('Latitude'),
                'date':fields.date('Date'),
                'name':fields.char("ATM Branch Details"),  
                }


    _defaults = {
        'date': lambda *a: time.strftime('%Y-%m-%d')
    }

    def action_save(self,cr,uid,ids,context=None):
        atm_id = context['active_ids']
        data = self.read(cr, uid, ids)[0]
        atm_obj = self.pool.get('atm.info').browse(cr,uid,atm_id)[0]
        self.pool.get('atm.info').write(cr,uid,atm_id[0],{'child_ids':[[0, False, {'latitude': atm_obj.latitude, 'name': atm_obj.name, 'longitude': atm_obj.longitude,'date':atm_obj.date}]]},context=context)
        self.pool.get('atm.info').write(cr,uid,atm_id[0],data,context=context)
        #res = super(atm_localization,self).create(cr,uid,vals,context=None)
        return True


Atm_localization()