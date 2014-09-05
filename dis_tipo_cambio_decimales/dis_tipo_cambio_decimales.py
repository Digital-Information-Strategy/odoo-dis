# -*- coding: utf-8 -*-
##############################################################################
#
#	OpenERP, Open Source Management Solution
#	Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU Affero General Public License as
#	published by the Free Software Foundation, either version 3 of the
#	License, or (at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU Affero General Public License for more details.
#
#	You should have received a copy of the GNU Affero General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
from osv import osv, fields

class res_currency_rate(osv.osv):
	_inherit = "res.currency.rate"
	_columns = {
		'rate': fields.float('Rate', digits=(12,9), help='Precision decimal 9'),
	}
res_currency_rate()
class res_currency(osv.osv):
	def _current_rate(self, cr, uid, ids, name, arg, context=None):
		return self._current_rate_computation(cr, uid, ids, name, arg, True, context=context)
	def _current_rate_silent(self, cr, uid, ids, name, arg, context=None):
		return self._current_rate_computation(cr, uid, ids, name, arg, False, context=context)
	_inherit = "res.currency"
	_columns = {
		'rate': fields.function(_current_rate, string='Current Rate', digits=(12,9), help='The rate of the currency to the currency of rate 1.'),
		'rate_silent': fields.function(_current_rate_silent, string='Current Rate', digits=(12,9),help='The rate of the currency to the currency of rate 1 (0 if no rate defined).'),
	}
res_currency()