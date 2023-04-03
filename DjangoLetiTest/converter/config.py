import os
from django.conf import settings

tag_mapping_form = os.path.join(settings.BASE_DIR, "converter",
                           "schemas", "tag_mapping_form.json")

json_to_xml_form = os.path.join(settings.BASE_DIR, "converter",
                                "schemas", "json_to_xml_form.json")
xml_to_json_form = os.path.join(settings.BASE_DIR, "converter",
                                "schemas", "xml_to_json_form.json")
