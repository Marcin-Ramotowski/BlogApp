from django.contrib import admin
from news.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    @staticmethod
    def created_year(self):
        return self.created.year

    @admin.action(description='Clear content')
    @staticmethod
    def cleanup_content(model_admin, request, query_set):
        query_set.update(content='')

    @admin.action(description='Add footer')
    @staticmethod
    def add_footer(model_admin, request, query_set):
        footer = '\n========\nWszelkie prawa zastrzezone'
        for post in query_set:
            if not post.content.endswith(footer):
                post.content += footer
                post.save()

    @admin.action(description='Hide emails')
    @staticmethod
    def hide_emails(model_admin, request, query_set):
        import re
        for post in query_set:
            post.content = re.sub(r'[_\-a-zA-Z0-9\.]+@[_\-a-zA-Z0-9\.]+\.[A-Za-z]{1,3}', '<e-mail>', post.content)
            post.save()

    actions = ('cleanup_content', 'add_footer', 'hide_emails')
    list_display = ('author', 'title', 'category', 'created', 'created_year')
    # list_per_page = 3
    search_fields = ('title', 'content')
    ordering = ('category', 'created')
    list_filter = ('author', 'category', 'created')
    date_hierarchy = 'created'
    raw_id_fields = ('author',)
