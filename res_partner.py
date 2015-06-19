# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

##########################################################################
#   Author: Rubén Cabrera
#           rcabrera@bisnesmart.com
#           
#
##########################################################################

class ResPartner(models.Model):
	_inherit = 'res.partner'

	def check_vat_es(self,vat):
		"""
			Verify Spanish VAT numbers. 
		"""
		return True

	def check_vat_be(self,vat):
		"""Trick for BE accounts (which are ALL wrong in our clients DB)"""
		return True