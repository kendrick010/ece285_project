import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms

class WikiArtistDataset(Dataset):

    def __init__(self, dataset_path, transforms_=None, mode='train'):
        self.dataset_path = os.path.join(dataset_path, mode)
        self.images = os.listdir(self.dataset_path)

        self.transforms_ = transforms_

    def __getitem__(self, index):
        image_path = os.path.join(self.color_path, self.color[index])    
        image = Image.open(image_path).convert('RGB')

        if self.transforms_:
            image = self.transforms_(image)

        return image

    def __len__(self):
        return len(self.images)