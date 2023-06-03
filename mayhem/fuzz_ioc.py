#!/usr/bin/env python3
import atheris
import sys


import fuzz_helpers


with atheris.instrument_imports(include=['extruct']):
    import extruct

from lxml.etree import ParserError, XMLSyntaxError
from bs4 import MarkupResemblesLocatorWarning

errors = ['log', 'ignore', 'strict']

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        extruct.extract(fdp.ConsumeRandomString(), base_url=fdp.ConsumeRandomString(), errors=fdp.PickValueInList(errors), uniform=fdp.ConsumeBool(), return_html_node=fdp.ConsumeBool(), schema_context=fdp.ConsumeRandomString(), with_og_array=fdp.ConsumeBool())
    except (ParserError, MarkupResemblesLocatorWarning, XMLSyntaxError, LookupError):
        return -1

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
