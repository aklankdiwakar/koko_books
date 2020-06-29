"""
Script: kbooks_controller.py
Description: To calculate the rental amount for verity of books, based on different story.
"""

__author__ = 'aklankdiwakar@gmail.com'

from tabulate import tabulate
from swagger_server import PRICE_LIST_S1, PRICE_LIST_S2, PRICE_LIST_S3


def add_artifact_line(story_number, body):  # noqa: E501
    """Do calculation and generate invoice

    This API will do calculation and generate invoice for rented books. # noqa: E501

    :param story_number: Story
    :type story_number: str
    :param body: Do calculation and generate invoice
    :type body: dict | bytes

    :rtype:
    """

    final_rental_price, index, final_rental_price_list = 0, 1, list()
    price_list = eval('PRICE_LIST_{}'.format(story_number))

    for book_type, list_of_books in body.items():

        # ['Rental charge for per day', 'Minimum days', 'Raise in rental charge after minimum days']
        rental_charge, minimum_days, raised_rental_change = price_list[book_type]
        for book_name, rental_days in list_of_books:
            rental_days = int(rental_days)
            # If no of rental days are less then minimum days. Charges should be calculated with fixed minimum days.
            if rental_days < minimum_days:
                rental_days = minimum_days
            # If rental days are more then minimum days. Charges should be applied based on raised charge.
            if rental_days > minimum_days:
                rental_charge = raised_rental_change

            charge_for_each_book = rental_charge * rental_days

            final_rental_price_list.append([index, '{} ({})'.format(book_name, book_type), rental_days,
                                            charge_for_each_book])
            final_rental_price = float(final_rental_price) + float(charge_for_each_book)
            index += 1

    final_rental_price_list.append(['', 'Total', '', final_rental_price])
    return (tabulate(final_rental_price_list, headers=['SL No.', 'Description', 'No of Days', 'Price'],
                     tablefmt='pretty'))
