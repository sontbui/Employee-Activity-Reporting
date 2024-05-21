from odoo import fields, models, tools

class EmployeeActivity(models.Model):
    _name = 'employee.activity'
    _auto = False
    _description = 'Employee Activity Report'

    employee_id = fields.Many2one('hr.employee', string='Nhân viên')
    sale_order_count = fields.Integer(string='Đơn bán hàng (SO)')
    purchase_order_count = fields.Integer(string='Đơn mua hàng (PO)')
    crm_count = fields.Integer(string='CRM')
    meeting_count = fields.Integer(string='Lịch hẹn gặp khách hàng')
    expense_count = fields.Integer(string='Chi phí đã đề xuất')

    def init(self):
        tools.drop_view_if_exists(self._cr, 'employee_activity')
        self._cr.execute("""
            CREATE OR REPLACE VIEW employee_activity AS (
                SELECT
                    e.id as id,
                    e.id as employee_id,
                    (SELECT COUNT(*) FROM sale_order s WHERE s.user_id = e.user_id) as sale_order_count,
                    (SELECT COUNT(*) FROM purchase_order p WHERE p.user_id = e.user_id) as purchase_order_count,
                    (SELECT COUNT(*) FROM crm_lead c WHERE c.user_id = e.user_id) as crm_count,
                    (SELECT COUNT(*) FROM calendar_event m WHERE m.user_id = e.user_id) as meeting_count,
                    (SELECT COUNT(*) FROM hr_expense h WHERE h.employee_id = e.id) as expense_count
                FROM
                    hr_employee e
            )
        """)
