from django.apps import apps

def get_all_custom_models():
    custom_models = set()
    all_models = set()
    # Default models from Django installation. If a new model will be added it should be added to this list.
    # YOu can add "User" model to this list to prevent from importing user data to DB.
    default_models = {"LogEntry", "Permission", "Group", "ContentType", "Session"}

    for model in apps.get_models():
        all_models.add(model.__name__)

    custom_models = all_models - default_models
    custom_models = list(custom_models)

    return sorted(custom_models)