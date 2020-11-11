from django.contrib import admin
from members.models import Member, MemberProfile


class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'member_type')
    list_filter = ('member_type',)
    search_fields = ['user__email']

    def user_email(self, member):
        return member.user.email


class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('member', 'company')
    search_fields = ('member__user__email', 'company', 'phone_number', 'notes')


admin.site.register(Member, MemberAdmin)
admin.site.register(MemberProfile, MemberProfileAdmin)
