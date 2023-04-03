import os
import json
import copy
import xmltodict

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from lxml import etree

from .config import json_to_xml_form, tag_mapping_form, xml_to_json_form


@csrf_exempt
def json_to_xml(request):
    """
    Обработка JSON-запроса
    """
    if request.method == "POST":
        try:
            json_data = json.loads(request.body)
            converted_input = convert_json_input_form(json_data)
            xml_data = xmltodict.unparse(converted_input, pretty=True)
            if getattr(settings, 'ENABLE_XML_VALIDATION', False):
                xsd_file = os.path.join(settings.BASE_DIR, "converter",
                                        "schemas", "Add_Entrant_List.xml")
                is_valid, error_message = validate_xml(xml_data, xsd_file)
                if not is_valid:
                    return JsonResponse({"error": error_message}, status=400)
            return HttpResponse(xml_data, content_type="application/xml")
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def xml_to_json(request):
    """
    Обработка XML-запроса
    """
    if request.method == "POST":
        try:
            xml_data = request.body.decode('utf-8')
            if getattr(settings, 'ENABLE_XML_VALIDATION', False):
                xsd_file = os.path.join(settings.BASE_DIR, "converter",
                                        "schemas", "Get_Entrant_List.xsd")
                is_valid, error_message = validate_xml(xml_data, xsd_file)
                if not is_valid:
                    return JsonResponse({"error": error_message}, status=400)
            json_form = convert_xml_input_form(xml_data)
            return JsonResponse(json_form)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


def convert_json_input_form(json_data):
    """
    Конвертация JSON-запроса в XML
    :param json_data: JSON-запрос в виде словаря
    :return: JSON-ответ в необходимом формате для дальнейшей конвертации в XML
    """
    with open(json_to_xml_form, encoding='utf-8') as json_file:
        json_form = json.load(json_file)
    json_form = convert_json_ident(json_form, json_data)
    json_form = convert_json_other(json_form, json_data)
    json_form = convert_json_address(json_form, json_data)
    result = {"EntrantChoice": {
        "AddEntrant": json_form}}
    return result


def convert_json_ident(json_form, json_data):
    """
    Преобразование в необходимый JSON-формат для дальнейшей конвертации в XML
    содержимого значения тега(ключа) Identification во время JSON->XML запроса
    :param json_form: Шаблон необходимого формата JSON-запроса
    :param json_data: JSON - запрос
    :return: Преобразованный JSON - запрос
    """
    json_ident_form = json_form["Identification"]
    doc_type_path = os.path.join(settings.BASE_DIR, "converter",
                                 "schemas", "dict_document_type_cls.json")
    with open(tag_mapping_form, encoding='utf-8') as json_file:
        tag_mapping = json.load(json_file)
    current_key = tag_mapping.get("IdDocumentType")
    if json_data.get(current_key) is None:
        raise AttributeError("No IdDocumentType")
    json_ident_form["IdDocumentType"] = 100000 + json_data.get(current_key)
    with open(doc_type_path, encoding='utf-8') as file:
        doc_type_dict = json.load(file)
    for doc in doc_type_dict:
        if doc["Id"] == json_ident_form["IdDocumentType"]:
            json_ident_form["DocName"] = doc["Name"]
            for field in doc["FieldsDescription"]["fields"]:
                current_key = tag_mapping.get(field["xml_name"])
                if field["not_null"] and json_data.get(current_key) is None:
                    raise AttributeError(f"No {field['xml_name']} in request")
                json_ident_form["Fields"][field["xml_name"]] = json_data.get(
                    current_key)
            break
    for data in json_ident_form:
        if json_ident_form[data] is None:
            current_key = tag_mapping.get(data)
            json_ident_form[data] = json_data.get(current_key)
    json_ident_form = {k: v for k, v in json_ident_form.items() if
                       v is not None}
    json_form["Identification"] = json_ident_form
    return json_form


def convert_json_other(json_form, json_data):
    """
    Преобразование в необходимый JSON-формат для дальнейшей конвертации в XML
    содержимого значения остальных тегов (кроме AddressList и
    Identification) во время JSON->XML запроса
    :param json_form: Шаблон необходимого формата JSON-запроса
    :param json_data: JSON - запрос
    :return: Преобразованный JSON - запрос
    """
    with open(tag_mapping_form, encoding='utf-8') as json_file:
        tag_mapping = json.load(json_file)
    for data in json_form:
        if json_form[data] is None:
            current_key = tag_mapping.get(data)
            if current_key is None:
                current_key = data.lower()
            json_form[data] = json_data.get(current_key)
    json_form = {k: v for k, v in json_form.items() if v is not None}
    return json_form


def convert_json_address(json_form, json_data):
    """
    Преобразование в необходимый JSON-формат для дальнейшей конвертации в XML
    содержимого значения тега(ключа) AddressList во время JSON->XML запроса
    :param json_form: Шаблон необходимого формата JSON-запроса
    :param json_data: JSON - запрос
    :return: Преобразованный JSON - запрос
    """

    addresses = json_form["AddressList"]["Address"]
    for num, pref in enumerate(('', 'second_')):
        for data in addresses[num]:
            addresses[num][data] = json_data.get(pref + data.lower())
        addresses[num]["FullAddr"] = ''
        for post in range(1, 5):
            current_value = json_data.get(pref + 'address_txt' + str(post))
            if current_value is not None:
                addresses[num]["FullAddr"] += current_value + ' '
        addresses[num] = {k: v for k, v in addresses[num].items() if
                          v is not None}
        if not json_data.get("has_another_living_address"):
            addresses.pop()
            break
    json_form["AddressList"]["Address"] = addresses
    return json_form


def convert_xml_input_form(xml_data):
    """
    Конвертация XML->JSON при XML-запросе
    :param xml_data: Содержимое XML - запроса
    :return: Результат конвертации в JSON
    """
    json_data = xmltodict.parse(xml_data)
    with open(xml_to_json_form, encoding='utf-8') as json_file:
        json_form = json.load(json_file)
    json_keys_enumeration(json_data, json_form)
    json_form['is_without_snils'] = True if json_form['snils'] is None \
        else False

    return json_form


def json_keys_enumeration(json_data, json_form, prefix=''):
    """
    Рекурсивное заполнение ключей JSON-ответа при конвертации из XML
    :param json_data: JSON-вид XML-запроса в первоначальном виде после
    конвертации
    :param json_form: Результат конвертации XML->JSON
    :param prefix: Префикс для ключей, связанных со вторым адресом проживания
    :return: json_form
    """
    with open(tag_mapping_form, encoding="utf-8") as json_file:
        tag_mapping = json.load(json_file)
    for data in json_data:
        if isinstance(json_data[data], dict):
            json_keys_enumeration(json_data[data], json_form)
        elif isinstance(json_data[data], list):
            json_form["has_another_living_address"] = True
            for addr, pref in zip(json_data[data], ["", "second_"]):
                json_keys_enumeration(addr, json_form, pref)
        else:
            map_key = tag_mapping.get(data)
            current_key = map_key if map_key is not None else data.lower()
            current_key = prefix + current_key
            if current_key in json_form.keys():
                json_form[current_key] = json_data[data]


def validate_xml(xml_data, xsd_file):
    """
    Валидация XML-файла в соответствии с XSD-схемой
    :param xml_data: XML-файл
    :param xsd_file: XSD-схема
    :return: Валиден ли файл xml_data
    """
    try:
        schema_doc = etree.parse(xsd_file)
        schema = etree.XMLSchema(schema_doc)
        xml_doc = etree.fromstring(xml_data.encode())
        schema.assertValid(xml_doc)
        return True, None
    except etree.DocumentInvalid as e:
        return False, str(e)
