from django.contrib import admin

from notification.models import NoticeType, NoticeSetting, Notice, ObservedItem, NoticeQueueBatch


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "send"]


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id','message_header','message', 'recipient', 'sender','notice_type', 'added', 'unseen', 'archived', 'on_site')
    list_editable = ('on_site',)

    fieldsets = (
        (None, {
            'fields': ('message_header','message',  'recipient','notice_type')
        }),
        ('Advanced options',{
            'classes': ('collapse',),
            'fields': ('added', 'unseen', 'archived' , 'on_site')
        })
    )
    actions = ["send_notices"]

    def send_notices(self, request, queryset):
        import models
        models.send_notices(queryset)
        self.message_user(request, "Messages were successfully send.")
    send_notices.short_description = "Send selected Notices by email"


admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(NoticeSetting, NoticeSettingAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(ObservedItem)
