from django.conf import settings


def vue_js_files(request):
    #the reson we have built this out is because we want this to be dynamic
    static_base_dir = settings.STATICFILES_BASE_DIR
    vue_name =  'vue-dev' #brings in vue-dev folder can change this to prod when ready to deploy 'vue_prod' if settings.VUE_PROD else
    vue_dir = static_base_dir / vue_name #brings in vue-dev/assets folder 
    js_files = [x.relative_to(static_base_dir) for x in vue_dir.glob('**/*.js') ]#brings in vue-dev/ assets js files * all js files
    css_files = [ x.relative_to (static_base_dir) for x in vue_dir.glob('**/*.css')] #brings in vue-dev/ css files * all css files
    
    return {
        "vue_js_paths" : list(js_files),
        "vue_css_paths" : list(css_files),
    }