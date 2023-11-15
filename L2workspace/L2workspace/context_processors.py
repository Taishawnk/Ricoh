from django.conf import settings



def vue_js_files(request):
    STATICFILES_BASE_DIR = settings.STATICFILES_BASE_DIR
    return {
        "vue_js_paths" : ["vue-dev/assets/index-04bcf2a9.js"],
    }