from modeltranslation.translator import register, TranslationOptions    # noqa

from apps.blogs.models import Blog


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "description", "content")