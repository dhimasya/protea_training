from odoo import api, fields, models

import requests


class BookReview(models.Model):
    _name = "book.review"
    _description = "book review"
    _rec_name = "content"

    book_id = fields.Many2one('book')
    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)
    external_id = fields.Char()
    external_source = fields.Char()
    content = fields.Text()


    @api.model
    def pull_from_website(self):
        source = 'website1'
        res = requests.get("http://localhost/product_website/api/product_review.php").json()
        # insert data to book review
        review_list = []
        if res.get('success'):
            reviews = res.get('reviews')
            for review in reviews:
                review_id = str(review.get('id', ''))
                if review_id != '':
                    check_review = self.env['book.review'].search([
                        ('external_id', '=', review_id),
                        ('external_source', '=', source)
                    ], limit=1)
                    if not check_review:
                        book = self.env['book'].search([
                            ('isbn', '=', review.get('isbn'))
                        ], limit=1)
                        if book:
                            review_list.append({
                                'book_id': book.id,
                                'content': review.get('content'),
                                'external_id': review_id,
                                'external_source': source
                            })
        if review_list:
            self.env['book.review'].create(review_list)
        return True