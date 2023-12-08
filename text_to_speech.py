# Текст унших сангуудыг дуудаж байна
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
# файлын зам олох санг дуудаж байна
import site

# Клаас үүсгэж байна
class TextToSpeech:
    # Constructor Байгуулагч  функц
    def __init__(self):
        # байршилыг ашиглажх файлын замыг олох гэж байна
        location = site.getsitepackages()[0]
        # Ашиглах файлын зам дээр ашилах моделийн замыг зааж байна. 
        path = location + "/TTS/.models.json"

        # Цаанаас өгсөн бичих ёстой кодыг бичиж байна
        # Ингэхдээ ModelManager класс үүсгэж байна
        model_manager = ModelManager(path)

        # Текст унших модел буюу загварыг татаж авч байна
        model_path, config_path, model_item = model_manager.download_model("tts_models/en/jenny/jenny")

        # Текст унших классийг үүсгэж байна. 
        # Ингэхдээ хэрэгтэй параметрүүдийг дамжуулж байна.
        # Мөн, классын syn нэртэй хувьсагчид хадгалж байна. 
        # Ингэснээр дараачийн удаа generate_audio функцийг 
        # дуудахад шинээр клаас үүсгэлгүй, шууд syn нэртэй 
        # хувьсагч ашиглаж боломжтой болжээ
        self.syn = Synthesizer(
            tts_checkpoint=model_path,
            tts_config_path=config_path,
        )

    # Энэ функц бол текстийг аудио болгох функц. 
    # Энэ функцийг дуудахдаа уншуулах текстээ дамжуулахад л 
    # аудио файл үүсгэж өгөх нь ээ.
    def generate_audio(self, text):
        # Өмнө байгуулагч функцэд хадгалсан хувсагчаа 
        # ашиглаад уншуулах текстээ дамжуулж өгч байна.
        outputs = self.syn.tts(text)

        # Текстээс аудио файл үүсгээд, audio_output.wav файлд 
        # хадгалах гэж байна. Үүний тулд syn доторх save_wav() 
        # функцийг дуудаж байна.
        self.syn.save_wav(outputs, "audio_output.wav")
