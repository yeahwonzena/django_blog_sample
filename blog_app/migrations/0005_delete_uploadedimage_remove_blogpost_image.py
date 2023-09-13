from django.db import migrations

def remove_uploadedimage_and_image(apps, schema_editor):
    # Remove the UploadedImage model and image field
    UploadedImage = apps.get_model('blog_app', 'UploadedImage')
    UploadedImage.objects.all().delete()
    BlogPost = apps.get_model('blog_app', 'BlogPost')
    BlogPost.objects.all().update(image=None)

class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_blogpost_publish'),  # Update with your actual previous migration
    ]

    operations = [
        migrations.RunPython(remove_uploadedimage_and_image),
        migrations.DeleteModel(
            name='UploadedImage',  # Update with your actual model name
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
    ]
