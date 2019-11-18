from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import os
class Command(BaseCommand):
    help = 'Entrela la IA'

    def handle(self, *args, **kwargs):
        chatbot = ChatBot(**settings.CHATTERBOT,storage_adapter="chatterbot.storage.DjangoStorageAdapter")
        trainer = ChatterBotCorpusTrainer(chatbot)
        print(os.path.dirname(os.path.abspath(__file__)))
        print(os.path.realpath(__file__))
        trainer.train("/app/PaginaPersonalAlexV1/PaginaPersonal/management/commands/spanish/")
        self.stdout.write("Entrenadismo")