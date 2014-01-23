# -*- encoding: utf-8 -*-
##############################################################################
#
#    cbk_technical_sheet: Product Information Tab
#    Copyright (c) 2014 Codeback Software S.L. (http://codeback.es)    
#    @author: Miguel García <miguel@codeback.es>
#    @author: Javier Fuentes <javier@codeback.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from osv import fields, osv
from datetime import datetime, timedelta
from openerp.tools.translate import _

class product_product(osv.osv):
    """añadimos los nuevos campos"""
    name = "product.product"
    _inherit = "product.product"   
    
    _columns = {        
        'product_technical_specifications_ids' : fields.one2many('product.technical.specifications', 'product_id', string="Technical Specifications"),        
        'dimensions': fields.char('Dimensions'),
        'weight': fields.char('Weight'),
    }
    
class product_technical_specifications (osv.osv):
    
    _name = "product.technical.specifications"  
    _columns = {        
        'product_id': fields.many2one("product.product", string="Product", ondelete="CASCADE"), 
        'specification': fields.char('Note', required=True),       
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: