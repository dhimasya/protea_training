import json

from odoo import http
from odoo.http import request, route, Response


class Library(http.Controller):

    @route("/library/book", type="http", auth="none", methods=['GET'])
    def library_book(self, **args):
        data = []
        books = request.env['book'].sudo().search([])
        for book in books:
            data.append({
                "id": book.id,
                "name": book.name,
                "page_count": book.page_count,
                "author": book.author_id.name,
            })
        return Response(template="library.library_book_index", qcontext={
            "books": data
        })
