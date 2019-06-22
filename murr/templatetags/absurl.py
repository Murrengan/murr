from urllib import parse
from django import template
from django.template.defaulttags import URLNode, url

register = template.Library()


class AbsoluteURLNode(URLNode):
    def render(self, context):
        path = super(AbsoluteURLNode, self).render(context)
        domain = "http://127.0.0.1:8000"
        return parse.urljoin(domain, path)


@register.tag
def absurl(parser, token, node_cls=AbsoluteURLNode):
    """Just like {% url %} but ads the domain of the current site."""
    node = url(parser, token)
    return node_cls(node.view_name, node.args, node.kwargs, node.asvar)

