from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

def set_group_perms():
    group, was_created = Group.objects.get_or_create(
        name='News Writer (Advanced)'
    )

    group.permissions.add( Permission.objects.get(name='Can add bootstrap4 blockquote') )
    group.permissions.add( Permission.objects.get(name='Can change bootstrap4 blockquote') )
    group.permissions.add( Permission.objects.get(name='Can delete bootstrap4 blockquote') )
    group.permissions.add( Permission.objects.get(name='Can view bootstrap4 blockquote') )
    group.permissions.add( Permission.objects.get(name='Can add bootstrap4 picture') )
    group.permissions.add( Permission.objects.get(name='Can change bootstrap4 picture') )
    group.permissions.add( Permission.objects.get(name='Can delete bootstrap4 picture') )
    group.permissions.add( Permission.objects.get(name='Can view bootstrap4 picture') )
    group.permissions.add( Permission.objects.get(name='Can change cms plugin') )
    group.permissions.add( Permission.objects.get(name='Can view cms plugin') )
    group.permissions.add( Permission.objects.get(name='Can add cms plugin') )
    group.permissions.add( Permission.objects.get(name='Can delete cms plugin') )
    group.permissions.add( Permission.objects.get(name='Can change page') )
    group.permissions.add( Permission.objects.get(name='Can view page') )
    group.permissions.add( Permission.objects.get(name='Can use Structure mode') )
    group.permissions.add( Permission.objects.get(name='Can add blog category') )
    group.permissions.add( Permission.objects.get(name='Can change blog category') )
    group.permissions.add( Permission.objects.get(name='Can delete blog category') )
    group.permissions.add( Permission.objects.get(name='Can view blog category') )
    group.permissions.add( Permission.objects.get(name='Can add blog article') )
    group.permissions.add( Permission.objects.get(name='Can change blog article') )
    group.permissions.add( Permission.objects.get(name='Can view blog article') )
    group.permissions.add( Permission.objects.get(name='Can add link') )
    group.permissions.add( Permission.objects.get(name='Can change link') )
    group.permissions.add( Permission.objects.get(name='Can delete link') )
    group.permissions.add( Permission.objects.get(name='Can view link') )
    group.permissions.add( Permission.objects.get(name='Can add text') )
    group.permissions.add( Permission.objects.get(name='Can change text') )
    group.permissions.add( Permission.objects.get(name='Can delete text') )
    group.permissions.add( Permission.objects.get(name='Can view text') )
    group.permissions.add( Permission.objects.get(name='Can add video player') )
    group.permissions.add( Permission.objects.get(name='Can change video player') )
    group.permissions.add( Permission.objects.get(name='Can delete video player') )
    group.permissions.add( Permission.objects.get(name='Can view video player') )
    group.permissions.add( Permission.objects.get(name='Can change image') )
    group.permissions.add( Permission.objects.get(name='Can view image') )
    group.permissions.add( Permission.objects.get(name='Can add Tag') )
    group.permissions.add( Permission.objects.get(name='Can change Tag') )
    group.permissions.add( Permission.objects.get(name='Can delete Tag') )
    group.permissions.add( Permission.objects.get(name='Can view Tag') )
    group.permissions.add( Permission.objects.get(name='Can add Tagged Item') )
    group.permissions.add( Permission.objects.get(name='Can change Tagged Item') )
    group.permissions.add( Permission.objects.get(name='Can delete Tagged Item') )
    group.permissions.add( Permission.objects.get(name='Can view Tagged Item') )
