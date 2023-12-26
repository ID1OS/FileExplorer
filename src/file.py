import pygame
import os
import json

class File():
    """A class that contains the settings of a folder."""
    def __init__(self, path):
        """Initialize a folder."""
        self.path = path
        self.name = os.path.basename(path)
        self.reduced_name = self.name[:10]
        self.image = self.get_file_image()
        self.rect = self.image.get_rect()
        self.pos = None
        self.text_color = (30, 30, 30)
        self.bg_color = (230, 230, 230)
        self.font_path = "font.ttf"
        self.font = pygame.font.Font(self.font_path, 9)
        self.get_name_rect()


    def __str__(self):
        return "File"

    def get_name_rect(self):
        self.name_image = self.font.render(self.reduced_name, True, self.text_color, self.bg_color)
        self.name_rect = self.name_image.get_rect()

    def get_name_pos(self):
        self.name_rect.centerx = self.rect.centerx
        self.name_rect.top = self.rect.bottom

    def get_command(self):
        extension = self.name.split(".")[-1]
        extension = self.name.split(".")[-1]
        if "." in self.name:
            if extension == "py":
                return "code " + self.path
            if extension == "rar":
                return "start winrar " + self.path
            if extension in ["mp4","mkv","avi", "mov", "wmv", "flv", "webm", "3gp", "ogg", "ogv", "m4v", "mpg", "mpeg", "mov", "rm", "rmvb", "asf"]:
                return "start vlc " + self.path
            
    
    def get_file_type(self):
        extension = self.name.split(".")[-1]
        if "." in self.name:
            if extension == "py":
                return "python"
            if extension == "rar":
                return "winrar"
            if extension in  ["docx","doc"]:
                return "word"
            if extension == "pdf":
                return "pdf"
            if extension == "xlsx":
                return "excel"
            if extension in ["mp4","mkv","avi", "mov", "wmv", "flv", "webm", "3gp", "ogg", "ogv", "m4v", "mpg", "mpeg", "mov", "rm", "rmvb", "asf"]:
                return "video"
            if extension in ["jpg", "jpeg","png", "bmp", "tiff", "tif", "raw","svg", "webp", "heif","ico","pnm","pgm","ppm","pbm","hdr","exr","jfif","gif"]:
                return "photo"
            if extension in ["mp3","wav","aac","ogg","wma","flac","alac","aiff","dsd","pcm","mp2","m4a","m4b","m4p","m4r","mid","midi","xmf","rtttl","rtx","ota","imy","ogg","oga","spx","opus","amr","awb","3gp","mp4","m4v","mp4v","3g2","3gpp","3gpp2","avi","divx","flv","mkv","mk3d","mov","mp4","mpeg","mpg","mpe","webm","wmv","asf","ts","m2ts","m2t","mts","mxf","ogv","ogm","qt","rm","rmvb","vob","ifo"]:
                return "audio"
            if extension == "txt":
                return "txt"
            if extension == "c":
                return "c"
            if extension == "cpp":
                return "c"
            if extension == "json":
                return "json"
            if extension == "exe":
                return "exe"
            if extension in ["ppt","pptx"]:
                return "ppt"
            if extension == "ttf":
                return "font"
            if extension == "sh":
                return "sh"
            if extension == "html":
                return "html"
            if extension == "css":
                return "css"
            if extension == "js":
                return "js"
            if extension == "php":
                return "php"
            if extension == "java":
                return "java"
            if extension == "iso":
                return "iso"
            if extension == "zip":
                return "zip"
            if extension == "7z":
                return "7z"
            if extension == "gz":
                return "gz"
            if extension == "bz2":
                return "bz2"
            if extension == "xz":
                return "xz"
            if extension == "tar":
                return "tar"
            if extension == "apk":
                return "apk"
            if extension == "psd":
                return "psd"
            if extension == "ai":
                return "ai"
            if extension == "csv":
                return "csv"
            else:
                return "file"
        else:
            return "file"
    def get_file_image(self):
        type = self.get_file_type()
        if type == "photo":
            original_image = pygame.image.load(self.path)
            resized_image = pygame.transform.scale(original_image, (64, 64))
            return resized_image
        else:
            with open("system/files.json") as f:
                files = json.load(f)
            return pygame.image.load(os.path.join("images",files[type]))