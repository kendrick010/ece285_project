import io
import zipfile
from PIL import Image, ImageFile
from torch.utils.data import Dataset

ImageFile.LOAD_TRUNCATED_IMAGES = True

class WikiArtDataset(Dataset):
    def __init__(self, zip_path, transform=None):
        self.zip_path = zip_path
        self.transform = transform
        
        # Open zip file just to get file list, then close it
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            self.file_list = []
            self.labels = []
            
            for f in zip_file.namelist():
                if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                    parts = f.split('/')
                    if len(parts) > 2 and parts[0] == 'images':
                        art_type = parts[1]
                        self.file_list.append(f)
                        self.labels.append(art_type)

    def __len__(self):
        return len(self.file_list)
    
    def __getitem__(self, idx):
        image_path, image_label = self.file_list[idx], self.labels[idx]
        
        # Open zip file fresh for each read
        with zipfile.ZipFile(self.zip_path, 'r') as zip_file:
            image = zip_file.read(image_path)
            image = Image.open(io.BytesIO(image)).convert('RGB')
            
            if self.transform:
                image = self.transform(image)
            
            return image, image_label