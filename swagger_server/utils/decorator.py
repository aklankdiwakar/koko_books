# -*- coding: utf-8 -*-

"""
Script: decorator.py
Description: Parse yaml file for get test payload
"""
__author__ = 'aklankdiwakar@gmail.com'


import yaml
import os
from functools import wraps
from swagger_parser import SwaggerParser


def parse_swagger_yaml(function):
    """

    :param function:
    :return:
    """

    @wraps(function)
    def wrapper(self, *args, **kwargs):

        yaml_file = os.path.join(os.getcwd(), 'swagger_server/swagger/swagger.yaml')
        parsed_file = SwaggerParser(swagger_path=yaml_file)
        method_name = function.__name__.split('_', 1)[-1]
        _uri, _method, _tag = parsed_file.operation[method_name]
        if _method in ['POST', 'post']:
            for each_param in parsed_file.paths[_uri][_method]['parameters'].keys():
                if each_param == 'body':
                    definition = parsed_file.paths[_uri][_method]['parameters'][each_param]['schema']['$ref'].split('/')[-1]
                    body = parsed_file.specification['definitions'][definition]['example']
                    setattr(self, 'body', body)
                if each_param == 'story_number':
                    story_number = parsed_file.paths[_uri][_method]['parameters'][each_param]['x-example']
                    setattr(self, 'story_number', story_number)

        response = function(self, *args, **kwargs)
        return response

    return wrapper
