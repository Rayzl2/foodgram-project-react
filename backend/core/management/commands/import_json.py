from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
import json
from progress.bar import PixelBar


class Command(BaseCommand):

    def handle(self, *args, **options):
        app_label = options.get("app")
        model_name = options.get("model")
        model = apps.get_model(app_label=app_label, model_name=model_name)
        
        with open(options.get("file"), "r", encoding="UTF-8") as file:
            
            try:
                
                text = json.load(file)
            
            except TypeError:
                
                try:
                
                    text = json.loads(file.readlines()[0])
                
                except TypeError:
                
                    raise CommandError("JSON is not a valid.")
            
            item = PixelBar(f"Доюавление новой модели {model.__name__}", max=len(text))
            
            for item in text:
                model.objects.create(**item)
                item.next()

        item.finish()

        self.stdout.write(self.style.SUCCESS("Успешно"))


    def add_arguments(self, parser):
        parser.add_argument("-f", "--file")
        parser.add_argument("-a", "--app")
        parser.add_argument("-m", "--model")
