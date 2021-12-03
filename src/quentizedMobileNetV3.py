from torch import nn
from src.utils.mobilenetv3 import mobilenet_v3_large


class TacoMobileNetV3(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        base = mobilenet_v3_large(pretrained=True)
        base.classifier[3] = nn.Linear(1280, num_classes)
        self.model = base

    def forward(self, x):
        x = self.model(x)
        return x
