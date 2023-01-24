from bs4.element import Tag


def parse_fighter_span_intro_dict(span: Tag) -> dict:
    return {"href": span.parent["href"], "name": span.text}
