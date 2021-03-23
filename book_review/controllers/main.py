import json

from odoo import http
from odoo.http import request, route



class BookReview(http.Controller):
    
    @route('/book/review/create', type="http", auth="none", csrf=False)
    def book_review_create(self, **args):
        data = {
            "success": False,
            "message": ""
        }
        # print(request.httprequest.headers)
        id = args.get('id')
        source = args.get('source')
        isbn = args.get('isbn')
        content = args.get('content')
        if id and source and isbn and content:
            check_review = request.env['book.review'].sudo().search([
                ('external_id', '=', id),
                ('external_source', '=', source),
            ], limit=1)
            if not check_review:
                book = request.env['book'].sudo().search([
                    ('isbn', '=', isbn),
                ], limit=1)
                if book:
                    request.env['book.review'].sudo().create({
                        'book_id': book.id,
                        'content': content,
                        'external_id': id,
                        'external_source': source,
                    })
                    data['success'] = True
                else:
                    data['message'] = "the book with this isbn %s not exist" % (isbn)
            else:
                data['message'] = "the review already exist"
        else:
            data['message'] = "required parameter is missing (id/source/isbn/content)"

        return json.dumps(data)