from albumentations import *
import cv2

def train_augment(job_config, image_size):
    box_scale = min(image_size)
    rescale_percentage = job_config["RESCALE_PERCENTAGE"]
    return Compose([
        HorizontalFlip(p=0.5),
        VerticalFlip(p=0.5),
        RandomResizedCrop(image_size[0], image_size[1], scale=(1, 1 + rescale_percentage), ratio=(image_size[1]/image_size[0], image_size[1]/image_size[0]), interpolation=cv2.INTER_LINEAR, p=1),
        # ElasticTransform(p=job_config["ELASTIC_TRANSFORM_PR"], alpha=box_scale, sigma=box_scale * 0.05, alpha_affine=box_scale * 0.03)
    ], p=1)

def val_augment(job_config, image_size):
    return Compose([
        HorizontalFlip(p=0.5),
        VerticalFlip(p=0.5),
    ], p=1)
