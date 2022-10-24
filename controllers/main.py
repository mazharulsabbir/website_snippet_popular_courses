from odoo import http
from odoo.http import request


class Course(http.Controller):
    @http.route(['/popular_courses'], type="json", auth="public")
    def course_attendees(self):
        dynamic_course = request.env['slide.channel'].sudo().search([], order='members_count desc', limit=6)
        dataset = {'data_list': dynamic_course}
        template = 'website_snippet_popular_courses.website_popular_course_snippet'

        return request.env['ir.ui.view']._render_template(template, dataset)
